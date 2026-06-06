import os 

def RemoveFiles():
    # 获取用户输入的文件夹路径，并去除首尾空格
    # Get the folder path from user input and strip any leading/trailing whitespaces
    path = input("文件路径/path（点我这里）：").strip()
    
    # 检查输入的路径是否存在
    # Check if the entered path exists
    if os.path.exists(path):
        # 获取用户需要删除的文件后缀
        # Get the file extension that needs to be deleted from user input
        extension = input("需要删除的文件后缀/remove (点我这里)：")
        
        # 列出该路径下的所有文件和文件夹
        # List all files and directories in the specified path
        files = os.listdir(path)
        
        # 遍历文件夹中的每一个文件
        # Iterate through each file in the directory
        for i in files:
            # 检查文件是否以指定的后缀结尾
            # Check if the file ends with the specified extension
            if i.endswith(extension):
                try:
                    # 使用 os.path.join 自动处理斜杠，更稳妥
                    # Safely join the path and filename to handle slashes correctly across platforms
                    os.remove(os.path.join(path, i))
                except Exception:
                    # 遇到权限问题或找不到文件直接跳过，确保不卡死
                    # Skip if encountering permission issues or file not found, preventing the script from crashing
                    pass 
        
        # 提示用户清理完成
        # Inform the user that the cleanup is complete
        print("清理完毕！")
    else:
        # 如果路径不存在，提示错误
        # If the path does not exist, print an error message
        print("路径不存在！重新输入！")

# 执行函数
# Execute the function
RemoveFiles()