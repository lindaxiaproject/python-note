import filecmp
import json
import os
import shutil
from datetime import datetime

from tqdm import tqdm


def split_lst(lst, extent=10):
    if len(lst) % extent != 0:
        mx = (len(lst) // extent + 1) * extent
    else:
        mx = len(lst)
    result_list = []
    for i in range(0, mx, extent):
        result_list.append(lst[i:i + extent])
    return result_list


def are_files_equal(file1, file2):
    return filecmp.cmp(file1, file2, shallow=False)


def checkout(api_home='aaaa', lst=None):
    lst = lst or ['app.html', 'params.html', 'headers.html', 'body.html', 'authorizations.html',
                  'code_snippets_python.html', 'code_snippets_shell.html', 'Example_Response.html']
    same_files = []
    for i in range(len(lst) - 1):
        if are_files_equal(os.path.join(api_home, lst[i]),
                           os.path.join(api_home, lst[i + 1])):
            same_files.append(i + 1)
    print(same_files, 'same_files')
    same_files = [lst[i] for i in same_files]
    for same_file in same_files:
        with open(os.path.join(api_home, same_file), 'w') as f:
            f.write('')


class IO:
    @staticmethod
    def load_json(file_path):
        """
        从指定的文件路径加载JSON数据。

        :param file_path: JSON文件的路径
        :return: JSON文件中的数据，通常是一个字典或列表
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"文件 {file_path} 未找到。")
            return None
        except json.JSONDecodeError:
            print(f"文件 {file_path} 不是有效的JSON格式。")
            return None
        except Exception as e:
            print(f"读取文件时发生错误：{e}")
            return None

    @staticmethod
    def save_json(data, file_path):
        """
        将数据保存为JSON文件。

        :param data: 要保存的数据，通常是字典或列表
        :param file_path: 要保存的文件路径
        """
        try:
            # 确保文件目录存在
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            # 使用'w'模式打开文件，如果文件已存在则覆盖
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except TypeError:
            print(f"数据 {data} 不能被序列化为JSON。")
        except Exception as e:
            print(f"写入文件时发生错误：{e}")

if __name__ == '__main__':
    # 获取当前时间
    current_time = datetime.now()
    # 格式化时间戳，例如：2024-07-28_12-45-30
    timestamp = current_time.strftime('%Y-%m-%d_%H-%M-%S')
    # 本地打包名
    app_name = f'rapi_html_zip_{timestamp}'
    # engine_dir = "engine"
    app_inputs = IO.load_json("./SeleniumRequestData-V20240711.json")
    # 参数exist_ok = True表示如果目录已经存在，不会引发错误，而是会正常执行
    os.makedirs(app_name, exist_ok=True)
    os.makedirs(os.path.join(app_name, 'apis'), exist_ok=True)
    os.makedirs(os.path.join(app_name, 'temp_engine'), exist_ok=True)
    os.makedirs(os.path.join(app_name, 'tasks_jsons'), exist_ok=True)

    for i in app_inputs:
        api_name = i.pop('api_name').replace(' ', '_').lower().replace('(', '_l_').replace(')', '_r_')
        i['api_home'] = os.path.join(app_name, 'apis', api_name) # rapi_html_zip_2024-07-28_09-09-56/apis/search-face-in-repository
        i['url'] = i.pop('api_url') # 'https://rapidapi.com/ai-engine-ai-engine-default/api/faceanalyzer-ai/playground/apiendpoint_0d5ac829-2fe2-47ea-9d66-1c172999dcb7'
        i['userdir'] = os.path.join(app_name, 'temp_engine', api_name) # rapi_html_zip_2024-07-28_09-09-56/temp_engine/search-face-in-repository
        i.pop('save_path')
        i.pop('headless')

    # for i in tqdm(app_inputs):
    #     shutil.copytree(engine_dir, i['userdir'])

    for t, i in tqdm(enumerate(split_lst(app_inputs, 10))):
        IO.save_json(i, os.path.join(app_name, 'tasks_jsons', f'tasks_json_{t}.json'))

    for i in os.listdir(os.path.join(app_name, 'tasks_jsons')):
        print(i)
        os.system(f"node /Users/linhong/WebstormProjects/rapi-data-collect/rapi/Main.js {os.path.join(app_name, 'tasks_jsons', i)}")

    '''校验修复'''
    for i in os.listdir(os.path.join(app_name, 'apis')):
        if i.startswith('.'):
            continue
        if '_l_' in i:
            shutil.move(os.path.join(app_name, 'apis', i),
                        os.path.join(app_name, 'apis', i.replace('_l_', '(').replace('_r_', ')')))
    for i in os.listdir(os.path.join(app_name, 'apis')):
        if len(os.listdir(os.path.join(app_name, 'apis', i))) == 7:
            # 补全为空
            with open(os.path.join(app_name, 'apis', i, 'Example_Response.html'), 'w') as f:
                f.write('')
        if len(os.listdir(os.path.join(app_name, 'apis', i))) < 7:
            print(i, '缺损..')

    '''置空重复'''
    for i in os.listdir(os.path.join(app_name, 'apis')):
        if i.startswith('.'):
            continue
        try:
            checkout(os.path.join(app_name, 'apis', i))
        except FileNotFoundError as e:
            print(e)
    '''打包删除临时文件'''
    os.system(f"zip -r {app_name}.zip {os.path.join(app_name, 'apis')}")

    shutil.rmtree(app_name)
