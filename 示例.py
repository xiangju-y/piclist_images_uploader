import os
import platform


def markdown_path_config(markdown_path, level_num=None):
    # 去除文件扩展名并获取文件名
    file_path = markdown_path
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
    for i in range(0,len(levels)):
        print(f"第{i+1}级",levels[i].replace('\\', '/') + '/')
    # 输出结果，从文件名开始逐级向上
    if level_num is not None and level_num <= len(levels):

        return levels[level_num - 1].replace('\\', '/') + '/'
    return None  # 如果 level_num 无效，返回 None

# 示例路径
print('你当前的系统',platform.system())
file_path = r"C:\\Users\\Administrator\\Desktop\\blog\\xiangju_blog\\source\\_posts\\python\\da"
result = markdown_path_config(file_path,2 )  # 设置level_num
print(f"结果: {result}")