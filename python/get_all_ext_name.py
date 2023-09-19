import os

def count_file_extensions(directory):
    # 创建一个空字典用于存储扩展名及其出现次数
    extension_count = {}

    # 遍历指定路径下的所有文件
    for root, _, files in os.walk(directory):
        for file in files:
            # 使用os.path.splitext()获取文件扩展名
            _, file_extension = os.path.splitext(file)
            # 去掉扩展名中的点号，如果有的话
            file_extension = file_extension.lstrip('.')
            # 更新字典中的计数或初始化计数为1
            extension_count[file_extension] = extension_count.get(file_extension, 0) + 1

    return extension_count

if __name__ == '__main__':
    directory = './'  # 修改为你要统计的文件夹路径
    extensions_count = count_file_extensions(directory)

    # 打印结果
    print("文件扩展名统计结果:")
    for extension, count in extensions_count.items():
        print(f".{extension}: {count} 个文件")
