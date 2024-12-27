import argparse
import os
import platform
import json
import time
import uuid
import requests

class typora_images_url:
    def __init__(self, markdown_path, data_json=None, dir_level=None, img_url=None, uploader=None, piclist_url=None,key=None):
        self.markdown_path = markdown_path
        self.dir_data(data_json)
        self.img_path = self.markdown_path_config(dir_level)
        self.img_url = [path.replace('\\\\', '\\') for path in img_url]
        self.uploader = uploader
        self.open_json()
        self.piclist_url = piclist_url
        self.key=key

    def get_plictist(self):
        path = []
        for uploader_list, uploader_can in self.data['uploader'].items():
            if uploader_list == self.uploader:
                configlist = uploader_can['configList'][0].copy()
                configlist = self.configlist_config(configlist)
                for configList_can in uploader_can['configList']:
                    path.append(configList_can['path'])
        matches = [s for s in path if s == self.img_path]
        if not matches:
            self.data['uploader'][self.uploader]['configList'].append(configlist)
            self.write_json()
        # print(self.img_url)
        restart = self.plist_url()
        return restart

    def get_config(self):
        self.uuid = uuid.uuid4()
        self._createdAt = int(time.time() * 1000)  # 获取毫秒级时间戳
        self._updatedAt = self._createdAt + 2000  # 通常在创建时，创建时间和更新时间相同

    def configlist_config(self, configlist):
        self.get_config()
        configlist['_createdAt'] = self._createdAt
        configlist['_updatedAt'] = self._updatedAt
        configlist['_id'] = str(self.uuid)
        configlist['_configName'] = self.img_path
        configlist['path'] = self.img_path
        self.customUrl = configlist['customUrl']
        return configlist

    def safe_get(self, lst, index=0, default=None):
        try:
            return lst[index] if lst else default
        except IndexError:
            return default

    def dir_data(self, data_json=None):
        # Windows: %APPDATA %\piclist\data.json
        # Linux: $XDG_CONFIG_HOME / piclist / data.json or ~ /.config / piclist / data.json
        # macOS: ~ / Library / Application\ Support / piclist / data.json
        if data_json is None:
            system = platform.system()
            if system == 'Windows':
                appdata_path = os.path.expandvars('%APPDATA%\\piclist\\data.json')
            elif system == 'Linux':
                appdata_path = os.path.expandvars('$XDG_CONFIG_HOME/piclist/data.json') or os.path.expanduser(
                    '~/.config/piclist/data.json')
            elif system == 'Darwin':
                appdata_path = os.path.expanduser('~Library/Application Support/piclist/data.json')
            self.data_json = appdata_path
        else:
            self.data_json = data_json

    def open_json(self):
        with open(self.data_json, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
            f.close()

    def write_json(self):
        with open(self.data_json, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def markdown_path_config(self, level_num=None):
        # 去除文件扩展名并获取文件名
        file_path = self.markdown_path
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        # 获取不包含文件名的目录路径并将其分解为各部分
        dir_parts = os.path.normpath(os.path.dirname(file_path)).split(os.sep)
        # 初始化当前路径为文件名
        current_path = file_name
        levels = []
        # 从文件所在目录开始，逐步向上追溯到根目录
        for part in reversed(dir_parts):
            if part:  # 如果不是空字符串或根目录
                levels.append(current_path)
                current_path = os.path.join(part, current_path)
        # 添加系统盘符作为最后一级（如果存在），并处理 Windows 系统盘符
        drive, _ = os.path.splitdrive(file_path)
        if drive:
            # 处理 Windows 系统盘符，例如 C:\ 变成 C:/
            drive = drive.replace('\\', '/') + '/'
            levels.append(os.path.join(drive, current_path))
        # print(f"Levels with Drive: {levels}")  # 调试信息
        # 输出结果，从文件名开始逐级向上
        if level_num is not None and level_num <= len(levels):
            return levels[level_num - 1].replace('\\', '/') + '/'
        return None  # 如果 level_num 无效，返回 None

    def plist_url(self):
        data = {
            "list": self.img_url
        }
        headers = {
            "Content-Type": "application/json"
        }
        url = self.piclist_url + '/upload?' + f'picbed={self.uploader}&configName={self.img_path}&key={self.key}'
        response = requests.post(url=url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()['result']
        else:
            return response.text

def main():
    parser = argparse.ArgumentParser(description="处理文件路径和相关信息")
    # 通过命令行输入文件路径、目录位置、目录级别、图片链接
    parser.add_argument('file_path', help="文件路径")
    parser.add_argument('--dir_data', help="piclist,data.json目录位置 (可选)", default=None, type=str)
    parser.add_argument('--piclist_url', help="piclist上传更新图片api(默认是http://127.0.0.1:36677)",
                        default='http://127.0.0.1:36677', type=str)
    parser.add_argument('--key', help="piclist,图片的鉴权密钥,默认为空",default=None,type=str)
    parser.add_argument('--dir_level', help="图床的目录级别,默认是2 (可选)", default=2, type=int)
    parser.add_argument('--uploader', help="选择图床(默认是github)", default='github', type=str)
    parser.add_argument('image_url', nargs='*', help="图片链接 (最后给出)")

    # 解析命令行参数
    args = parser.parse_args()
    # 调用函数处理
    print(args)
    zhi = typora_images_url(markdown_path=args.file_path, data_json=args.dir_data,
                            dir_level=args.dir_level, img_url=args.image_url,
                            uploader=args.uploader, piclist_url=args.piclist_url,
                            key=args.key)
    result = zhi.get_plictist()
    for i in result:
        print(i)


if __name__ == '__main__':
    main()
# 文件路径,目录位置 目录级别, 图片链接
