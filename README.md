# HFUT CAN AutoLogin Script

## 配置环境
```shell
pip install -r requirements.txt
```
- 环境所依赖的包中最主要的是plyer, requests和pyinstaller。
  - plyer：生成一个Toast，提示用户相关信息。
  - requests：请求校园网URL。
  - pyinstaller：将python脚本打包为windows可执行程序。
  - APScheduler：任务调度工具包，有效避免脚本“卡住”的情况。

## 打包为可执行程序
```shell
pyinstaller --onefile --hidden-import plyer.platforms.win.notification main_scheduler.py
```
执行打包程序后，会在当前目录下生成两个目录`build`和`dist`，以及一个文件`main_scheduler.spec`。

## 启动程序
进入`dist`目录下，创建文件`identification.json`，该文件的内容为：
```json
{
  "username": "<Here is your username>",
  "password": "<Here is your password>"
}
```
然后启动`main_scheduler.exe`，该程序每分钟检查一次校园网的连接状态。

## Windows上开机自动执行脚本
- 进入`dist`目录下，给当前的可执行程序`main_scheduler.exe`创建一个快捷方式，然后按下组合键`Win+R`，输入`shell:startup`，进入【启动】文件夹。
- 将`dist`目录下生成的快捷方式拷贝到【启动】文件夹下，即可实现开机自启。
