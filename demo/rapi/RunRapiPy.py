import filecmp
import json
import os
import shutil
from datetime import datetime


from tqdm import tqdm


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

def split_lst(lst, extent=10):
    if len(lst) % extent != 0:
        mx = (len(lst) // extent + 1) * extent
    else:
        mx = len(lst)
    result_list = []
    for i in range(0, mx, extent):
        result_list.append(lst[i:i + extent])
    return result_list



if __name__ == '__main__':
    # 获取当前时间
    current_time = datetime.now()
    # 格式化时间戳，例如：2024-07-28_12-45-30
    timestamp = current_time.strftime('%Y-%m-%d_%H-%M-%S')

    app_name = 'complete'
    engine_dir = "engine"
    app_inputs = IO.load_json("SeleniumRequestData-V20240711.json")

    os.makedirs(app_name, exist_ok=True)
    os.makedirs(os.path.join(app_name, 'apis'), exist_ok=True)
    os.makedirs(os.path.join(app_name, 'temp_engine'), exist_ok=True)
    os.makedirs(os.path.join(app_name, 'tasks_jsons'), exist_ok=True)

    for i in app_inputs:
        api_name = i.pop('api_name').replace(' ', '_').lower().replace('(', '_l_').replace(')', '_r_')
        i['api_home'] = os.path.join(app_name, 'apis', api_name)
        i['url'] = i.pop('api_url')
        i['userdir'] = os.path.join(app_name, 'temp_engine', api_name)
        i.pop('save_path')
        i.pop('headless')

    # 对应生成同等api个数的用户目录
    print('>>>>>> 开始生成api对应的用户目录....')
    for i in tqdm(app_inputs):
        shutil.copytree(engine_dir, i['userdir'])
    print('>>>>>> 结束生成api对应的用户目录！')

    for t, i in tqdm(enumerate(split_lst(app_inputs, 10))):
        IO.save_json(i, os.path.join(app_name, 'tasks_jsons', f'tasks_json_{t}.json'))

    print('>>>>>> 开始运行javascript核心代码.....')
    for i in os.listdir(os.path.join(app_name, 'tasks_jsons')):
        print(i)
        os.system(f"node main.js {os.path.join(app_name, 'tasks_jsons', i)}")
    print('>>>>>> 结束运行javascript核心代码！')


    print('### 开始对api文件名进行规则反编码.....')
    for i in os.listdir(os.path.join(app_name, 'apis')):
        if i.startswith('.'):
            continue
        if '_l_' in i:
            shutil.move(os.path.join(app_name, 'apis', i),
                        os.path.join(app_name, 'apis', i.replace('_l_', '(').replace('_r_', ')')))
    print('### 结束对api文件名进行规则反编码!')

    print('------- 开始校验app下的html数据-----')
    for i in os.listdir(os.path.join(app_name, 'apis')):
        assert len(os.listdir(os.path.join(app_name, 'apis', i))) == 8
    print('------- 结束校验app下的html数据！-----')


    os.system(f"zip -r {app_name}.zip {os.path.join(app_name, 'apis')}")
    print('！！！成功打包app文件-----')

