# 文件编码转换脚本

这个脚本用于批量将指定文件夹中的文件从不同的字符编码格式（如 ANSI、UTF-8、UTF-16 等）转换为 UTF-8 编码。它还提供了自动检测文件编码的功能。

# 代码
- [change_encoding_to_utf-8.py](./change_encoding_to_utf-8.py)

## 使用说明

### 安装依赖

在运行脚本之前，请确保已安装以下 Python 模块：

- `chardet`：用于检测文件的编码。
- `pathlib`：用于处理文件路径。

你可以使用以下命令安装这些依赖：

- pip install chardet


### 配置

在脚本中，你需要进行以下配置：

- `root_directory`：指定要处理的根文件夹路径。将其设置为你要转换文件的文件夹路径。

- `file_extensions`：定义要处理的文件后缀名列表。默认包括 ['.c', '.h', '.sh', '.py', '.txt', '.csv']。你可以根据需要添加或删除文件类型。

### 运行脚本

在终端中运行脚本，它会自动扫描指定文件夹中的文件，并尝试将它们从检测到的编码格式转换为 UTF-8 编码。

- python change_encoding_to_utf-8.py


注意事项
--------

- 如果在处理文件时发生错误，脚本将输出错误消息并继续处理其他文件。

- 如果脚本运行过程中提示检测文件编码时出错证明源文件的编码格式已经损坏，需要手动解决。 

- 请确保在运行脚本之前备份重要文件，以防发生意外情况。

- 脚本默认会将文件转换为 UTF-8 编码，但你可以根据需要修改 `target_encoding` 变量以使用其他编码。

这个脚本提供了一种方便的方式来批量转换文件的编码格式，特别适用于处理不同编码的文件。希望它对你有所帮助！