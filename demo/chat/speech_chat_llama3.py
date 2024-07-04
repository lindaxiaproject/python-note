import argparse
import base64
import io
import os
import queue
import random
import re
import time
import traceback
from datetime import date
from typing import Union
import requests
import jupyter_client
import websocket
from PIL import Image
import json
from pathlib import Path
import openai
from transformers import pipeline as pip
import whisper_processor
from getimages import get_mp4s, server_address, client_id, get_images_url, upload_images, get_images
from translate import translate

model_path = "Llama3-8B-Chinese-Chat-q8_0-v2_1"

# client = openai.OpenAI(
#     base_url="http://localhost:8000/v1",
#     api_key="123456"
# )
client = openai.OpenAI(
    base_url="http://192.168.8.125:28760/v1",
    api_key="123456"
)

# #加载大语言模型
# DEFAULT_MODEL_PATH = "/Users/peter/chatglm.cpp/chatglm3-ggml.bin"
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--model", default=model_path, type=Path, help="model path")
parser.add_argument("--mode", default="chat", type=str, choices=["chat", "generate"], help="inference mode")
parser.add_argument("-l", "--max_tokens", default=8192, type=int, help="max total length including prompt and output")
parser.add_argument("--tool_choice", default="auto", type=str, help="当没有工具时，none是默认值，有工具时，`auto`是默认值")
parser.add_argument("--tools", default=None, type=str, help="A list of tools the model may call. Currently, only functions are supported as atool.")
parser.add_argument("--top_p", default=0.2, type=float, help="top-p sampling")
parser.add_argument("--temp", default=0.2, type=float, help="temperature")
parser.add_argument("--repeat_penalty", default=1.0, type=float, help="penalize repeat sequence of tokens")
parser.add_argument("-t", "--threads", default=0, type=int, help="number of threads for inference")
parser.add_argument("--plain", action="store_true", help="display in plain text without markdown support")
parser.add_argument("--text_negative", default="signature, low quality,bad quality, disfigured, toy, bad anatomy, missing limbs, missing fingers,", help="text_negative")
parser.add_argument("--image_style", default="photo-hdr", help="image style:base,photo-hdr....")
args = parser.parse_args()

# ----- begin code interpreter -----
def get_kernel_client(kernel_name) -> jupyter_client.BlockingKernelClient:
    km = jupyter_client.KernelManager(kernel_name=kernel_name)
    km.start_kernel()

    kc: jupyter_client.BlockingKernelClient = km.blocking_client()
    kc.start_channels()

    return kc

def clean_ansi_codes(text: str) -> str:
    ansi_escape = re.compile(r"(\x9B|\x1B\[|\u001b\[)[0-?]*[ -/]*[@-~]")
    return ansi_escape.sub("", text)

def extract_code(text: str) -> str:
    return re.search(r"```.*?\n(.*?)```", text, re.DOTALL)[1]

def run_code(kc: jupyter_client.BlockingKernelClient, code: str) -> Union[str, Image.Image]:
    kc.execute(code)

    try:
        shell_msg = kc.get_shell_msg(timeout=30)
        io_msg_content = None
        while True:
            try:
                next_io_msg_content = kc.get_iopub_msg(timeout=30)["content"]
            except queue.Empty:
                break
            if next_io_msg_content.get("execution_state") == "idle":
                break
            io_msg_content = next_io_msg_content

        if shell_msg["metadata"]["status"] == "timeout":
            return "Execution Timeout Expired"

        if shell_msg["metadata"]["status"] == "error":
            try:
                traceback_content = clean_ansi_codes(io_msg_content["traceback"][-1])
            except Exception:
                traceback_content = "Traceback Error"
            return traceback_content

        if "text" in io_msg_content:
            return io_msg_content["text"]
        # print(f'io_msg_content={io_msg_content}')
        data_content = io_msg_content.get("data")
        if data_content is not None:
            image_content = data_content.get("image/png")
            if image_content is not None:
                return Image.open(io.BytesIO(base64.b64decode(image_content)))
            text_content = data_content.get("text/plain")
            if text_content is not None:
                return text_content

        return ""

    except Exception:
        return traceback.format_exc()
# ----- end code interpreter -----

def image_to_base64_data_uri(file_path):
    with open(file_path, "rb") as img_file:
        base64_data = base64.b64encode(img_file.read()).decode('utf-8')
        return f"data:image/png;base64,{base64_data}"

def get_weather(city_name: str) -> str:
    import requests

    key_selection = {
        "current_condition": ["temp_C", "FeelsLikeC", "humidity", "weatherDesc", "observation_time"],
    }
    resp = requests.get(f"https://wttr.in/{city_name}?format=j1")
    resp.raise_for_status()
    resp = resp.json()

    ret = {k: {_v: resp[k][0][_v] for _v in v} for k, v in key_selection.items()}
    return json.dumps(ret)

def random_number_generator(seed: int, range: tuple[int, int]) -> int:
    import random

    return random.Random(seed).randint(*range)

#Chat、Code执行、Agent调用、Image识别
def predict(message, history, *chatargs):
    # llava-llama-3-8b（多模态），Llama3-8B-Chinese-Chat-q8_0-v2_1（文本），moondream（多模态）,Llama3-70B
    CHAT_SYSTEM_PROMPT = "你是一名非常善于助人的机器人，使用中文回答问题。"
    CI_SYSTEM_PROMPT = "你是一名非常善于助人的机器人，善于写Python代码。"
    IMAGE_SYSTEM_PROMPT = "你是一个完美描述图像的助手，用中文回复."
    model_path = "Llama3-8B-Chinese-Chat-q8_0-v2_1"
    system_message = CHAT_SYSTEM_PROMPT
    messages = []
    print(f'{message=}')
    print(f'{history=}')
    print(f'{chatargs=}')

    if message["files"]:
        model_path = "moondream"
        system_message = IMAGE_SYSTEM_PROMPT
    elif chatargs[2] == "code":
        system_message = chatargs[3]
    elif chatargs[2] == "image":
        system_message = chatargs[3]
        # messages.append({'role': 'system', "name": "example_user", 'content': "画一只金毛狗在草地上玩耍。"}),
        # messages.append({'role': 'system', "name": "example_assistant", 'content': '一只狗，金色毛，草地，玩耍'}),

    for user_message, assistant_message in history:
        messages.append ( {"role": "user", "content": str(user_message)} )
        messages.append ( {"role": "assistant", "content": assistant_message} )
    messages.append({"role": "system", "content": system_message})

    generation_kwargs = dict (
        model=model_path,
        max_tokens=chatargs[0],
        temperature=chatargs[1],
        stream=True,
    )
    if chatargs[2] == "tool":
        messages.append({"role": "user", "content": message["text"]})
        tools = chatargs[3].replace("'", "\"")
        tools = json.loads(tools)
        generation_kwargs.update({"stream": False, "tools": tools, "tool_choice": "auto"})
        print(f'函数调用一次参数：{generation_kwargs}')
        message_last = [messages[-1]]
        print(f'函数调用一次message：{message_last}')
        response = client.chat.completions.create(
            messages=message_last,
            **generation_kwargs,
        )
        print(f'函数调用一次模型返回：{json.dumps(json.loads(response.model_dump_json()), indent=2)}')
        response_message = response.choices[0].message
        tool_calls = response_message.tool_calls
        if tool_calls:
            available_functions = {
                "random_number_generator": random_number_generator,
                "get_weather": get_weather,
                # "image_captioning": image_captioning
            }  # only one function in this example, but you can have multiple
            messages.append(response_message)  # extend conversation with assistant's reply
            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_to_call = available_functions[function_name]
                function_args = json.loads(tool_call.function.arguments)
                print(f'{function_name=}')
                print(f'{function_args=}')
                print(f'{function_args.keys()}')
                if function_name == "get_weather":
                    function_response = function_to_call(
                        city_name=function_args.get("city_name"),
                    )
                    messages.append (
                        {
                            "tool_call_id": tool_call.id,
                            "role": "user",
                            "name": function_name,
                            "content": function_response,
                        }
                    )
                elif function_name == "random_number_generator":
                    function_response = function_to_call(
                        range=function_args.get("range"),
                        seed=function_args.get("seed"),
                    )
                    messages.append (
                        {
                            "tool_call_id": tool_call.id,
                            "role": "user",
                            "name": function_name,
                            "content": str(function_response),
                        }
                    )
                # elif function_name == "image_captioning":
                #     function_response = function_to_call(
                #         range=function_args.get(message["files"]),
                #     )
                #     for i in range (len(function_response)):
                #         messages.append (
                #             {
                #                 "tool_call_id": tool_call.id,
                #                 "role": "user",
                #                 "content": function_response[i][-1]["generated_text"]
                #             }
                #         )
                #     # messages.append (
                #     #     {
                #     #         "tool_call_id": tool_call.id,
                #     #         "role": "user",
                #     #         "name": function_name,
                #     #         "content": function_response,
                #     #     }
                #     # )

            generation_kwargs.update({"stream": True})
            del_generation_kwargs = ['tools', 'tool_choice']
            print(f'函数调用二次参数：{generation_kwargs}')
            print (f'函数调用二次messages：{messages}' )
            for key in del_generation_kwargs:
                del generation_kwargs[key]
            response = client.chat.completions.create(
                messages=messages,
                **generation_kwargs
            )
            print(f'函数调用二次模型返回：{response}')
        else:
            print(f'{tool_calls=}')
    elif chatargs[2] == "image":
        # messages.append ( {"role": "user", "content": message["text"]} )
        # print(f'画图模型参数:{messages}')
        # generation_kwargs.update ({"stream": False} )
        # response = client.chat.completions.create(
        #     messages=messages,
        #     **generation_kwargs,
        # )
        # print(f'画图调用模型返回：{response}')

        text_positive_en = translate ( message["text"], 'zh', 'en' )
        jsonfile = 'json/sd3_t2i_api.json'
        with open ( jsonfile, 'r' ) as f:
            prompt = json.load ( f )
        # 设置新参数
        prompt["53"]["inputs"]["batch_size"] = 1
        prompt["53"]["inputs"]["width"] = 1024
        prompt["53"]["inputs"]["height"] = 1024
        prompt["3"]["inputs"]["seed"] = random.randint ( 1, 307988467008177 )
        prompt["54"]["inputs"]["text_positive"] = text_positive_en
        prompt["54"]["inputs"]["text_negative"] = args.text_negative
        prompt["54"]["inputs"]["style"] = args.image_style
        prompt["9"]["inputs"]["filename_prefix"] = 'sd3_web_api'
        for i in prompt.keys ():
            print ( str ( i ) + str ( prompt[i] ) )
        ws = websocket.WebSocket ()
        ws.connect ( "ws://{}/ws?clientId={}".format ( server_address, client_id ) )
        image_url = get_images_url( ws, prompt )

    elif message["files"]:
        print(f'image识别调用参数：{generation_kwargs}')
        for i in range ( len ( message["files"] ) ):
            messages.append (
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": message["text"]},
                        {"type": "image_url", "image_url": image_to_base64_data_uri (message["files"][i] )}
                    ]
                }
            )
        response = client.chat.completions.create(
            messages=messages,
            **generation_kwargs,
        )
        # if message["files"]:
        #     for i in range ( len ( message["files"] ) ):
        #         messages.pop()
        #     for i in range ( len ( message["files"] ) ):
        #         messages.append (
        #             {
        #                 "role": "user",
        #                 "content": [
        #                     {"type": "text", "text": message["text"]},
        #                     {"type": "image_url", "image_url":  (message["files"][i] )}
        #                 ]
        #             }
        #         )
        # print(f'image调用messages：{messages}')
        print(f'image识别调用模型返回：{response}')
    elif chatargs[2] == "code":
        messages.append ( {"role": "user", "content": message["text"]} )
        print(f'code调用参数：{generation_kwargs}')
        print(f'code调用messages：{messages}')
        response = client.chat.completions.create(
            messages=messages,
            **generation_kwargs,
        )
        print(f'code调用模型返回：{response}')
    else:
        messages.append({"role": "user", "content": message["text"]})
        print(f'非函数调用messages：{messages}')
        print(f'非函数调用参数：{generation_kwargs}')
        response = client.chat.completions.create(
            messages=messages,
            **generation_kwargs,
        )
        print(f'非函数调用模型返回：{response}')
    text = ""
    if message["files"]:
        for chunk in response:
            content = chunk.choices[0].delta.content
            if content:
                text += content
        print(f'图片识别内容：{text}')
        image_text = translate(text, "en", "zh")
        for i in range(len(image_text)):
            time.sleep(0.05)
            yield f"{image_text[: i + 1]}"
    elif chatargs[2] == "code":
        for chunk in response:
            content = chunk.choices[0].delta.content
            if content:
                text += content
                yield text
        kc = get_kernel_client ('git-test')
        code = extract_code (text)
        print ( f'代码：{code}' )
        observation = run_code ( kc, code )
        print ( f'代码执行结果：{observation}' )
        if isinstance(observation, Image.Image):
            image_path = "/private/var/folders/4h/bhhq4h3j22bd70wrmnmy0n3c0000gn/T/gradio/tmp_image.png"
            observation.save(image_path)
            yield f"{text}\n\n<img src='file={image_path}'></img>"
        else:
            yield f"{text}\n 代码执行结果：{observation}"
    elif chatargs[2] == "image":
        yield f"\n<img src='{image_url}'></img>"
    else:
        for chunk in response:
            content = chunk.choices[0].delta.content
            if content:
                text += content
                yield text
        print(f'回复内容：{text}')


#输出语音Chat格式处理
def postprocess(text, speech):

    if speech is None:
        return f"<pre>{text}</pre>"
    else:
        return f"{text}\n<audio controls><source src='{speech}' type='audio/wav'></audio>"

#输入语音Chat格式处理
def addspeech(chatbot, speech):

    chatbot.append([(speech,), None])
    print(f'speech----{chatbot=}')
    return chatbot

#语音问答
def spe_tex_spe(chatbot, messages, spk, style):

    generation_kwargs = dict (
        model=model_path,
        max_tokens=args.max_tokens,
        temperature=args.temp,
        stream=True,
    )

    speech_path = chatbot[-1][0][0]
    print(f'{chatbot[-1][0][0]}')
    #本地调用语音转文本
    # spe_txt = speechtotext(input_file_path=speech_path, model_type='base')
    #远程调用语音转文本
    spe_txt = get_s2t_whisper(speech_path)
    print(f'{spe_txt=}')
    system_prompt = '你是一个善于交流的人，尽量不要拒绝别人的请求,尽量使用口语化来回复。'
    messages.append({"role": "system", "content": system_prompt})
    messages.append ( {"role": "user", "content": spe_txt} )
    print(f'1*******{chatbot=}')
    print(f'1*******{messages=}')

    response = client.chat.completions.create(
        messages=messages,
        **generation_kwargs
    )

    text = ""
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content:
            text += content
    reply_message = text
    print(f'{reply_message=}')
    #本地调用文本转语音
    # speech_path = genspeech(txt=str(reply_message), gentype='固定语音')
    #远程调用文本转语音
    speech_path = get_t2s_chartts(txt=str(reply_message), spk=spk, style=style)
    print(f'{speech_path=}')

    speech_message = (speech_path,)
    print(f'{type(speech_message)=}')
    chatbot[-1][1] = speech_message
    print(f'{chatbot=}')
    messages.append ({"role": "assistant", "content": reply_message} )
    yield chatbot, messages
    print(f'2*******{chatbot=}')
    print(f'2*******{messages=}')

# 文本生成动画使用sd1.5和AnimateDiffu模型
def get_t2v_AnimateDiff(text_positive, image_style):

    text_positive_en = translate(text=text_positive, src_lang='zh', tgt_lang='en')

    print(f'{text_positive_en=}')
    jsonfile = 'json/sd1.5_t2v_AnimateDiff_api.json'
    with open (jsonfile, 'r' ) as f:
        prompt = json.load (f)
    # 设置新参数
    prompt["3"]["inputs"]["seed"] = random.randint ( 1, 1045435935651534 )
    prompt["11"]["inputs"]["filename_prefix"] = 't2v_AnimateDiff_api'
    prompt["19"]["inputs"]["text_positive"] = text_positive_en
    # prompt["19"]["inputs"]["text_negative"] = text_negative
    prompt["19"]["inputs"]["style"] = image_style
    for i in prompt.keys():
        print(str(i) + str(prompt[i]))
    ws = websocket.WebSocket()
    ws.connect("ws://{}/ws?clientId={}".format(server_address, client_id))
    images = get_mp4s(ws, prompt)
    output_files = []
    for node_id in images:
        for image_data in images[node_id]:
            # 保存图片
            variadic = f'{date.today().strftime("%Y_%m_%d")}/{date.today().strftime("%Y%m%d")}_{int(time.time())}'
            output_file = Path(f'extensions/sd_api_pictures/outputs/{variadic}.mp4')
            output_file.parent.mkdir(parents=True, exist_ok=True)
            with open(output_file.as_posix(), 'wb') as f:
                f.write(image_data)
            print(f'{output_file=}')
            time.sleep(1)
            # output_files.append(output_file.as_posix())
            # print(f'{output_files=}')
            # output_files.append(Image.open(io.BytesIO(image_data)))
    return output_file.as_posix()

#文本生成动画使用SVD
def get_t2v_svd(text_positive, text_negative, image_style):

    text_positive_en = translate(text_positive, 'zh', 'en')
    seed = random.randint ( 1, 4294967294 )
    with open ( 'json/sc_t2i2v_new_api.json', 'r' ) as f:
        prompt = json.load(f)

    # 设置新参数
    prompt["3"]["inputs"]["seed"] = seed
    prompt["88"]["inputs"]["seed"] = seed
    prompt["96"]["inputs"]["seed"] = seed
    prompt["101"]["inputs"]["text_positive"] = text_positive_en
    prompt["101"]["inputs"]["text_negative"] = text_negative
    prompt["101"]["inputs"]["style"] = image_style
    prompt["134"]["inputs"]["filename_prefix"] = 't2v_svd_api'
    for i in prompt.keys():
        print(str(i) + str(prompt[i]))
    ws = websocket.WebSocket()
    ws.connect("ws://{}/ws?clientId={}".format(server_address, client_id))
    images = get_mp4s(ws, prompt)
    #初始化返回文件列表
    output_files = []
    for node_id in images:
        for image_data in images[node_id]:
            # 保存视频
            variadic = f'{date.today().strftime("%Y_%m_%d")}/{date.today().strftime("%Y%m%d")}_{int(time.time())}'
            output_file = Path(f'extensions/sd_api_pictures/outputs/{variadic}.mp4')
            output_file.parent.mkdir(parents=True, exist_ok=True)
            with open(output_file.as_posix(), 'wb') as f:
                f.write(image_data)
            print(f'{output_file=}')
            time.sleep(1)
            # output_files.append(Image.open(io.BytesIO(image_data)))
    # filepath = Path(f'extensions/sd_api_pictures/outputs/{date.today().strftime("%Y_%m_%d")}')
    # print(f'{filepath=}')
    # images_list = getfiles(filepath)
    return output_file.as_posix()

#语音转文本whisper（服务器调用）
def get_s2t_whisper(file_path):

    s2t_url = "http://192.168.8.125:28761/inference"

    # 设置文件和参数
    files = {'file': open (whisper_processor.check_sample_rate(file_path), 'rb' )}
    params = {
        'temperature': args.temp,
        'temperature_inc': '0.2',
        'response_format': 'json'
    }

    # 发送POST请求
    response = requests.post (url=s2t_url, files=files, params=params )
    # 检查响应状态码
    if response.status_code == 200:
        print ( "s2t_whisper Request successful!" )
        # 处理JSON响应
        json_response = response.json ()
        print (json_response["text"] )
        response_text = json_response["text"]
    else:
        print (f"s2t_whisper Request failed with status code {response.status_code}" )
        response_text = response.status_code
    return response_text

#文本转语音CharTTS（服务器调用）
def get_t2s_chartts(txt, spk, style):

    #文本转语音服务地址
    t2v_url = "http://192.168.8.125:28763/v1/tts"
    # t2v_url = "http://127.0.0.1:8000/v1/tts"

    # 设置文件和参数
    params = {
        "text": txt,
        "spk": spk,
        "style": style,
        "temperature": 0.3,
        "top_P": 0.5,
        "top_K": 20,
        "seed": 42,
        "format": "mp3",
        "bs": 8,
        "thr": 100,
        # "prompt1": "我是一个说话非常嗲的山东女孩，喜欢撸串和喝啤酒。",
        # "prompt2": "很喜欢交朋友。",
        # "prefix": "",
    }

    # 发送POST请求
    response = requests.get ( url=t2v_url, params=params )
    # 检查响应状态码
    if response.status_code == 200:
        print ( "t2s_chattts Request successful!" )

        # 保存音频
        output_file = Path ( f'/Users/peter/git-test/wavfile/output.mp3' )
        output_file.parent.mkdir ( parents=True, exist_ok=True )
        with open (output_file.as_posix(), 'wb' ) as f:
            f.write(response.content )
        print (f'{output_file=}' )

    else:
        print ( f"t2s_chattts Request failed with status code {response.status_code}" )

    return output_file.as_posix()

#获取ChartTTS信息（服务器调用）
def get_chattts_info(object_type):

    server_adds = "192.168.8.125:28763"
    # server_adds = "127.0.0.1:8000"
    # t2v_speakers_url = "192.168.8.125:28763/v1/speakers/list"
    # t2v_styles_url = "http://192.168.8.125:28763/v1/styles/list"
    object_info = "http://{}/v1/{}".format (server_adds, object_type )
    # print(f'{object_info=}')
    # 设置文件和参数
    params = {
        'response_format': 'json'
    }
    response = requests.get ( url=object_info, params=params )
    spk_list = []
    # 检查响应状态码
    if response.status_code == 200:
        print (f"Load {object_type} Request successful! Address={object_info}")
        json_response = response.json ()
        data_list = json_response["data"]
        for i in range(len(data_list)):
            data_list[i]["index"] = i
            spk_list.append ( data_list[i].get ("name" ) )
    else:
        print (f"Load {object_type} Request failed with status code {response.status_code}")
    return spk_list

#通过文本获取图片识别物、遮罩、两者合并三个图
def get_segm_mark(image, segm_prompt):

    print(f'{image=}')
    image = image["background"]
    print(f'{image=}')
    print(f'{segm_prompt=}')
    text_positive = translate(text=segm_prompt, src_lang='zh', tgt_lang='en')
    if image != None and segm_prompt!=None:
        #上传图片
        upload_path = upload_images(image)
        print(f'{upload_path=}')
        print(f'{upload_path.get("name")=}')
        jsonfile = 'json/segment_mark_api.json'
        with open (jsonfile, 'r' ) as f:
            prompt = json.load (f)
        # 设置新参数
        prompt["139"]["inputs"]["filename_prefix"] = 'mark_api'
        prompt["189"]["inputs"]["filename_prefix"] = 'segm_api'
        prompt["190"]["inputs"]["filename_prefix"] = 'join_api'
        prompt["4"]["inputs"]["prompt"] = text_positive
        prompt["5"]["inputs"]["image"] = upload_path.get("name")
    for i in prompt.keys():
        print(str(i) + str(prompt[i]))
    ws = websocket.WebSocket()
    ws.connect("ws://{}/ws?clientId={}".format(server_address, client_id))
    images = get_images(ws, prompt)
    output_files = []
    for node_id in images:
        for image_data in images[node_id]:
            # 保存图片
            variadic = f'{date.today().strftime("%Y_%m_%d")}/{date.today().strftime("%Y%m%d")}_{int(time.time())}'
            output_file = Path(f'extensions/sd_api_pictures/outputs/{variadic}.png')
            output_file.parent.mkdir(parents=True, exist_ok=True)
            with open(output_file.as_posix(), 'wb') as f:
                f.write(image_data)
            print(f'{output_file=}')
            time.sleep(1)
            output_files.append(output_file.as_posix())

    return [output_files[0], output_files[1], output_files[2]]

#通过文本提示，修改遮罩部分生成新图
def get_mark_img(join, prompt, image_style):

    print(f'{join=}')
    print(f'{prompt=}')
    print(f'{image_style=}')
    text_positive = translate(text=prompt, src_lang='zh', tgt_lang='en')
    if join != None and prompt!=None:
        #上传图片
        upload_path = upload_images(join)
        print(f'{upload_path=}')
        print(f'{upload_path.get("name")=}')
        jsonfile = 'json/inpaint_sc_api.json'
        with open (jsonfile, 'r' ) as f:
            prompt = json.load (f)
        # 设置新参数
        prompt["3"]["inputs"]["seed"] = random.randint ( 1, 4294967294 )
        prompt["33"]["inputs"]["seed"] = random.randint ( 1, 4294967294 )
        prompt["9"]["inputs"]["filename_prefix"] = 'inpaint_sc_web_api'
        prompt["104"]["inputs"]["text_positive"] = text_positive
        prompt["104"]["inputs"]["style"] = image_style
        prompt["50"]["inputs"]["image"] = upload_path.get("name")
    for i in prompt.keys():
        print(str(i) + str(prompt[i]))
    ws = websocket.WebSocket()
    ws.connect("ws://{}/ws?clientId={}".format(server_address, client_id))
    images = get_images(ws, prompt)
    output_files = []
    for node_id in images:
        for image_data in images[node_id]:
            # 保存图片
            variadic = f'{date.today().strftime("%Y_%m_%d")}/{date.today().strftime("%Y%m%d")}_{int(time.time())}'
            output_file = Path(f'extensions/sd_api_pictures/outputs/{variadic}.png')
            output_file.parent.mkdir(parents=True, exist_ok=True)
            with open(output_file.as_posix(), 'wb') as f:
                f.write(image_data)
            print(f'{output_file=}')
            time.sleep(1)
            output_files.append(output_file.as_posix())
    return output_files[0]

#图片高清处理，不自动保存图片
def get_upscaleimage(image, preprocessor, height, width, subfolder):

    print(f'{image=}')
    print(f'{preprocessor=} {height=} {width=}')
    if image != None:
        #上传图片
        upload_path = upload_images(image, subfolder)
        print(f'{upload_path=}')
        jsonfile = 'json/UpscaleImage_api.json'
        with open (jsonfile, 'r' ) as f:
            prompt = json.load (f)
        # 设置新参数
        prompt["2"]["inputs"]["width"] = width
        prompt["2"]["inputs"]["height"] = height
        prompt["3"]["inputs"]["model_name"] = preprocessor
        prompt["6"]["inputs"]["directory"] = upload_path.get("subfolder")
        prompt["7"]["inputs"]["filename_prefix"] = "UpscaleImage"
    for i in prompt.keys():
        print(str(i) + str(prompt[i]))
    ws = websocket.WebSocket()
    ws.connect("ws://{}/ws?clientId={}".format(server_address, client_id))
    images = get_images(ws, prompt)
    output_files = []
    for node_id in images:
        for image_data in images[node_id]:
            # # 保存图片
            # variadic = f'{date.today().strftime("%Y_%m_%d")}/{date.today().strftime("%Y%m%d")}_{int(time.time())}'
            # output_file = Path(f'extensions/sd_api_pictures/outputs/{variadic}.png')
            # output_file.parent.mkdir(parents=True, exist_ok=True)
            # with open(output_file.as_posix(), 'wb') as f:
            #     f.write(image_data)
            # print(f'{output_file=}')
            # time.sleep(1)
            print(f'{type(image_data)=}')
            output_files.append(Image.open(io.BytesIO(image_data)))
    return output_files

#多图片插帧转视频函数，image原图、frame_nums插帧帧数、frame_rate帧率、subfolder视频保存路径
def get_images_vfi_video(image, frame_nums, frame_rate, subfolder):

    print(f'{image=}{frame_nums=}{frame_rate=}{subfolder=}')
    if image != None :
        upload_path = upload_images(image, subfolder)
        print(f'{upload_path=}')
        print(f'{upload_path.get("subfolder")=}')
        jsonfile = 'json/images2video_api.json'
        with open (jsonfile, 'r' ) as f:
            prompt = json.load (f)
        # 设置新参数
        prompt["24"]["inputs"]["directory"] = upload_path.get("subfolder")
        prompt["30"]["inputs"]["filename_prefix"] = 'images2video_web_api'
        prompt["30"]["inputs"]["frame_rate"] = frame_rate
        prompt["26"]["inputs"]["multiplier"] = frame_nums
    for i in prompt.keys():
        print(str(i) + str(prompt[i]))
    ws = websocket.WebSocket()
    ws.connect("ws://{}/ws?clientId={}".format(server_address, client_id))
    images = get_mp4s(ws, prompt)
    for node_id in images:
        for image_data in images[node_id]:
            # 保存图片
            variadic = f'{date.today().strftime("%Y_%m_%d")}/{date.today().strftime("%Y%m%d")}_{int(time.time())}'
            output_file = Path(f'extensions/sd_api_pictures/outputs/{variadic}.mp4')
            output_file.parent.mkdir(parents=True, exist_ok=True)
            with open(output_file.as_posix(), 'wb') as f:
                f.write(image_data)
            print(f'{output_file=}')
            time.sleep(1)
            # output_files.append(output_file.as_posix())
            # print(f'{output_files=}')
    return output_file.as_posix()

#图生视频函数
def get_image2video(image_input):

    if image_input:
        upload_path = upload_images(image_input)
        print(f'{upload_path=}')
        with open ( 'json/svd_i2v_api.json', 'r' ) as f:
            prompt = json.load ( f )

        # 设置新参数
        prompt["3"]["inputs"]["seed"] = random.randint ( 1, 4294967294 )
        prompt["35"]["inputs"]["filename_prefix"] = 'svd_i2v_web_api'
        prompt["23"]["inputs"]["image"] = upload_path.get('name')
    for i in prompt.keys():
        print(str(i) + str(prompt[i]))
    ws = websocket.WebSocket()
    ws.connect("ws://{}/ws?clientId={}".format(server_address, client_id))
    images = get_mp4s(ws, prompt)
    for node_id in images:
        for image_data in images[node_id]:
            # 保存图片
            variadic = f'{date.today().strftime("%Y_%m_%d")}/{date.today().strftime("%Y%m%d")}_{int(time.time())}'
            output_file = Path(f'extensions/sd_api_pictures/outputs/{variadic}.mp4')
            output_file.parent.mkdir(parents=True, exist_ok=True)
            with open(output_file.as_posix(), 'wb') as f:
                f.write(image_data)
            print(f'{output_file=}')
            time.sleep(1)

    return output_file.as_posix()

#文生图
def get_text2image(batch_size, text_positive, image_style, model_type, *kargs):
    print(f'{image_style=}')
    print(f'上传图片URL:{kargs[0]=}')  #上传图片URL
    print(f'lora名字:{kargs[1]=}')  #lora名字
    print(f'图片宽:{kargs[2]=}')  #图片宽
    print(f'图片高:{kargs[3]=}')  #图片高
    print(f'seed:{kargs[4]=}')  #seed
    upimage_path=kargs[0]
    lora_name=kargs[1]
    width = kargs[2]
    height = kargs[3]
    seed = kargs[4]
    text_positive_en = translate(text_positive, 'zh', 'en')

    if upimage_path:
        try:
            upload_file_name = upload_images(upimage_path)
            print(f'{upload_file_name=}')
            print(f'{upload_file_name.get("name")=}')
            jsonfile = 'json/i2i_turbo_api.json'
            with open (jsonfile, 'r' ) as f:
                prompt = json.load (f)
            # 设置新参数
            prompt["13"]["inputs"]["noise_seed"] = seed
            prompt["27"]["inputs"]["filename_prefix"] = 'i2i_turbo_web_api'
            prompt["30"]["inputs"]["text_positive"] = text_positive_en
            prompt["30"]["inputs"]["text_negative"] = args.text_negative
            prompt["30"]["inputs"]["style"] = image_style
            prompt["32"]["inputs"]["image"] = upload_file_name.get("name")
            prompt["34"]["inputs"]["amount"] = batch_size
        except:
            print('uploadfile not found')
    else:
        if model_type == 'quality':
            jsonfile = 'json/base+refiner_api.json'
            with open ( jsonfile, 'r' ) as f:
                prompt = json.load ( f )
            # 设置新参数
            prompt["5"]["inputs"]["batch_size"] = batch_size
            prompt["5"]["inputs"]["width"] = width
            prompt["5"]["inputs"]["height"] = height
            prompt["10"]["inputs"]["noise_seed"] = seed
            prompt["99"]["inputs"]["text_positive"] = text_positive_en
            prompt["99"]["inputs"]["text_negative"] = args.text_negative
            prompt["99"]["inputs"]["style"] = image_style
            prompt["19"]["inputs"]["filename_prefix"] = 'b_r_web_api'
        elif model_type == 'lora':
            loarmodel = lora_name + '.safetensors'
            jsonfile = 'json/base_refiner_loar_api.json'
            with open (jsonfile, 'r' ) as f:
                prompt = json.load ( f )
            # 设置新参数
            prompt["5"]["inputs"]["batch_size"] = batch_size
            prompt["5"]["inputs"]["width"] = width
            prompt["5"]["inputs"]["height"] = height
            prompt["10"]["inputs"]["noise_seed"] = seed
            prompt["11"]["inputs"]["noise_seed"] = seed
            prompt["19"]["inputs"]["filename_prefix"] = 'b_r_loar_web_api'
            prompt["119"]["inputs"]["lora_name"] = loarmodel
            prompt["123"]["inputs"]["text_positive"] = text_positive
            prompt["123"]["inputs"]["text_negative"] = args.text_negative
            if lora_name == 'liudehua':
                prompt["123"]["inputs"]["style"] = image_style
            else:
                prompt["123"]["inputs"]["style"] = 'base'
        elif model_type == 'sc':
            jsonfile = 'json/sc_t2i_api.json'
            with open ( jsonfile, 'r' ) as f:
                prompt = json.load ( f )
            # 设置新参数
            prompt["97"]["inputs"]["batch_size"] = batch_size
            prompt["97"]["inputs"]["width"] = width
            prompt["97"]["inputs"]["height"] = height
            prompt["88"]["inputs"]["seed"] = seed
            prompt["96"]["inputs"]["seed"] = seed
            prompt["101"]["inputs"]["text_positive"] = text_positive_en
            prompt["101"]["inputs"]["text_negative"] = args.text_negative
            prompt["101"]["inputs"]["style"] = image_style
            prompt["135"]["inputs"]["filename_prefix"] = 'sc_web_api'
        elif model_type == 'sd3':
            jsonfile = 'json/sd3_t2i_api.json'
            with open ( jsonfile, 'r' ) as f:
                prompt = json.load ( f )
            # 设置新参数
            prompt["53"]["inputs"]["batch_size"] = batch_size
            prompt["53"]["inputs"]["width"] = width
            prompt["53"]["inputs"]["height"] = height
            prompt["3"]["inputs"]["seed"] = seed
            prompt["54"]["inputs"]["text_positive"] = text_positive_en
            prompt["54"]["inputs"]["text_negative"] = args.text_negative
            prompt["54"]["inputs"]["style"] = image_style
            prompt["9"]["inputs"]["filename_prefix"] = 'sd3_web_api'
        else:
            jsonfile = 'json/sdturbo_api_new.json'
            with open (jsonfile, 'r' ) as f:
                prompt = json.load (f)
            # 设置新参数
            prompt["5"]["inputs"]["batch_size"] = batch_size
            prompt["5"]["inputs"]["width"] = width
            prompt["5"]["inputs"]["height"] = height
            prompt["13"]["inputs"]["noise_seed"] = seed
            prompt["30"]["inputs"]["text_positive"] = text_positive_en
            prompt["30"]["inputs"]["text_negative"] = args.text_negative
            prompt["30"]["inputs"]["style"] = image_style
            prompt["27"]["inputs"]["filename_prefix"] = 'sdturbo_web_api'

    for i in prompt.keys():
        print(str(i) + str(prompt[i]))
    ws = websocket.WebSocket()
    ws.connect("ws://{}/ws?clientId={}".format(server_address, client_id))
    images = get_images(ws, prompt)
    for node_id in images:
        for image_data in images[node_id]:
            # 保存图片
            variadic = f'{date.today().strftime("%Y_%m_%d")}/{date.today().strftime("%Y%m%d")}_{int(time.time())}'
            output_file = Path(f'extensions/sd_api_pictures/outputs/{variadic}.png')
            output_file.parent.mkdir(parents=True, exist_ok=True)
            with open(output_file.as_posix(), 'wb') as f:
                f.write(image_data)
            print(f'{output_file=}')
            time.sleep(1)
    filepath = Path(f'extensions/sd_api_pictures/outputs/{date.today().strftime("%Y_%m_%d")}')
    print(f'{filepath=}')
    images_list = getfiles(filepath)
    return images_list

def getfiles(folder_path):
    if folder_path==None:
        folder_path = Path(f'extensions/sd_api_pictures/outputs/{date.today().strftime("%Y_%m_%d")}')
    image_files=[]
    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 检查文件是否是图片文件（这里简单地检查文件扩展名）
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp',)):
                # 构建完整的文件路径
                file_path = os.path.join(root, file)
                image_files.append(file_path)
    return sorted(image_files, reverse=True)