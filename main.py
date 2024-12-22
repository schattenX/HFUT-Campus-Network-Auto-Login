import json
import auto_login_can


if __name__ == '__main__':

    # 打开用户信息文件，读取用户名和密码
    with open('identification.json', 'r') as f:
        user_info = json.load(f)
    AutoLoginCAN = auto_login_can.AutoLoginCAN(user_info["username"], user_info["password"])
    AutoLoginCAN.login()