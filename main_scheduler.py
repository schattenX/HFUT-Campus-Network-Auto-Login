import json
import auto_login_can
from apscheduler.schedulers.blocking import BlockingScheduler

def run_login():
    with open('identification.json', 'r') as f:
        user_info = json.load(f)
    AutoLoginCAN = auto_login_can.AutoLoginCAN(user_info["username"], user_info["password"])
    AutoLoginCAN.login_once()

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(run_login, 'interval', minutes=1)  # 每分钟执行一次
    try:
        print('自动化脚本已启动，按Ctrl-C退出当前脚本')
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print('已相应退出操作，当前任务完成后会自动退出，请稍等...')
        pass