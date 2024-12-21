import os
import sys
import json
import traceback
import auto_login_can
from datetime import datetime

def get_logs_path():
    """如果logs文件夹不存在，则创建文件夹"""
    base_path = os.path.abspath(".")
    logs_path = os.path.join(base_path, "logs")
    if not os.path.exists(logs_path):
        os.makedirs(logs_path)
    return logs_path

if __name__ == '__main__':
    try:

        # 打开用户信息文件，读取用户名和密码
        with open('identification.json', 'r') as f:
            user_info = json.load(f)
        AutoLoginCAN = auto_login_can.AutoLoginCAN(user_info["username"], user_info["password"])
        AutoLoginCAN.login()
    except Exception as e:
        # 获取时间戳
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        # 构建日志文件路径
        logs_dir = get_logs_path()
        log_file_path = os.path.join(logs_dir, f"{timestamp}_error.log")

        # 将异常信息输出到文件
        with open(log_file_path, 'w') as log_file:
            log_file.write(traceback.format_exc())

        # 输出错误日志路径到控制台，方便调试
        print(f"错误日志已写入: {log_file_path}")