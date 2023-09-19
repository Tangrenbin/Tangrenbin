import os
import codecs
import chardet

# 定义要处理的文件后缀名
file_extensions = ['.c', '.h', '.sh', '.py', '.txt', '.csv']

# 初始化为空的文件后缀名列表则处理所有文件，不进行后缀名过滤
# file_extensions = []

# 定义要处理的根文件夹路径
root_directory = './'  # 修改为你的文件夹路径

def convert_file_encoding(file_path, source_encoding, target_encoding='utf-8'):
    try:
        # 打开源文件以指定的编码方式读取内容
        with codecs.open(file_path, 'r', encoding=source_encoding, errors='strict') as source_file:
            content = source_file.read()
            # 打开目标文件以指定的编码方式写入内容
            with codecs.open(file_path, 'w', encoding=target_encoding) as target_file:
                target_file.write(content)
        print(f"已将文件 {file_path} 从 {source_encoding} 转换为 {target_encoding}")
    except Exception as e:
        print(f"处理文件 {file_path} 时出错: {str(e)}")

def detect_encoding(file_path):
    try:
        with open(file_path, 'rb') as file:
            detector = chardet.universaldetector.UniversalDetector()
            for line in file.readlines():
                detector.feed(line)
                if detector.done:
                    break
            detector.close()
            return detector.result['encoding']
    except Exception as e:
        print(f"检测文件编码时出错: {str(e)}")
        return None

def convert_files_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            # 如果file_extensions为空或文件以指定后缀名结尾，执行转换
            if not file_extensions or file.endswith(tuple(file_extensions)):
                file_path = os.path.join(root, file)
                source_encoding = detect_encoding(file_path)
                if source_encoding is not None and source_encoding != 'utf-8':
                    convert_file_encoding(file_path, source_encoding)

if __name__ == '__main__':
    convert_files_in_directory(root_directory)