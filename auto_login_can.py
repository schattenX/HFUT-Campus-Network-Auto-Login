import re
import requests
from time import sleep
from plyer import notification
from datetime import datetime


def notify(title, message):
    try:
        notification.notify(
            title= title,
            message= message,
            timeout=5  # 单位：秒
        )
    except NotImplementedError:
        print(f"通知功能不可用：{title} - {message}")

    # print(response.text)


class AutoLoginCAN:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.can_url = "http://192.168.4.1/"

    """
        未登录前的登录状态标识符：< title >上网登录页< / title >
        登录后的登录状态标识符：<title>注销页</title>
        检查目前的登录状态：未登录/已登录
        若为“未登录”状态，则调用can_login_url登录，并在第一次登录时提示toast：登录成功
    """
    def login(self):
        # 校园网登录的url，直接在浏览器里输入这个字符串就可以登陆
        can_login_url = "http://192.168.4.1/drcom/login?callback=dr1003&DDDDD="+self.username+"&upass="+self.password+"&0MKKey=123456&R1=0&R2=&R3=0&R5=0&R6=0&para=00&v6ip=&terminal_type=1&lang=zh-cn&jsVersion=4.2.1&v=6705&lang=zh"
        # toaster = ToastNotifier()
        while True:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            response = requests.get(self.can_url)
            # 正则字符串寻找登录状态标识符
            pattern = re.compile("<title>(.*?)</title>", re.S)
            title   = re.findall(pattern, response.text)[0]
            # 处于未登录状态时：执行登录操作
            if title == "上网登录页":
                response_code = requests.get(can_login_url).status_code

                if response_code == 200:
                    notify("登录成功", "您已成功登录校园网！")
                    print(f"{timestamp} 登录成功...")
            else:
                # toaster.show_toast("已处于登录状态", duration=5)
                print(f"{timestamp} 已处于登录状态...")
            # 每分钟检查一次
            sleep(60)

