# TG-FileStreamBot-zh
## 此仓库源于EverythingSuckz/TG-FileStreamBot的python分支，我对此进行了个人汉化去掉了一些我不使用的部分。

## 电报机器人
这是一个Telegram机器人，它可以提供 Telegram 文件的流链接，可以上传BOT或从其他频道用户那里转发。
TG频道的文件可以永久保存，即使管理员销号TG频道也会一直存在。TG-FileStreamBot可以把频道里的文件生成直链。
## 创建频道并获取频道ID
新建一个频道，公开频道或者私人频道都可以。为频道添加机器人[@MarieNews](https://t.me/MissRose_bot),将它设置为管理员。
向频道随便发送一个消息，长按这条消息把它转发给@MissRose_bot机器人，然后在机器人内再回复这条消息并附上/id。
-100xxxxxxxxxx就是我们频道的ID。
```bash
The forwarded channel, has an id of -1002224102557.The forwarded channel,has an id of -1002224102557.
```
然后我们把我们自己的BOT添加入频道并设置为管理员。

## 创建TG账号APPID 与 APP HASH
**这里我们尽量要使用家宽进行注册，机房IP可能会报错无法进行注册。IP最好与你的注册升级号同一个国家。**
浏览器打开https://my.telegram.org，登录你的Telegram账号，注册获取一个app id和app hash。
登录后选择API development tools。根据提示创建并保存。
记录好APP ID 和 APP HASH。

## 创建机器人
向[BotFather](https://t.me/BotFather)发送/newbot指令来新建一个bot。
根据提示注册好电报机器人，保存好TOKEN。
```
#Alright, a new bot. How are we going to call it? Please choose a name for your bot.
输入你的bot显示名称
#Good. Now let's choose a username for your bot. It must end in `bot`. Like this, for example: TetrisBot or tetris_bot.
输入你的bot用户名，之后你会用这个用户名搜索你的bot,用户名必须以bot结尾,比如freefile_bot
```

## git项目到自己的VPS
**需要先搭建好python环境。**

```bash
git clone https://github.com/Seikoa/TG-FileStreamBot-zh.git
cd TG-FileStreamBot-zh
pip3 install virtualenv 
```
下面我们要创建一个 **.env**文件
```bash
vi .env
```
输入下面内容保存并退出
```bash
API_ID=           #这里写你的app id
API_HASH=         #这里写你的app hash
BOT_TOKEN=        #这里写你的机器人密钥
BIN_CHANNEL=      #这里写你的频道id，包括前面的-号
PORT=             #这里写你想要使用的端口号
FQDN=             #这里填你的域名，不带http
HAS_SSL=False     #这里是ssl选项，最好填默认的False
```
保存好后执行下面指令
```bash
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip3 install -r requirements.txt
python3 -m WebStreamer
```
检测程序是否运行正常，向你的BOT发送/start查看是否响应。

为了防止在退出SSH后程序自动关闭，我们要对程序进行保活。
我们可以使用screen或者tmux。
我们先将已经运行的BOT关闭,我们摁下Ctrl + C关闭我们的程序
因为现在系统主流是debian系，我在这只放出apt安装tmux的代码行

```
apt install tmux -y
tmux
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip3 install -r requirements.txt
python3 -m WebStreamer
```

现在关闭vps程序也可以正常运行，链接文件会经过vps，所以只要你的VPS没用被GFW拦截，国内也能正常使用你的链接下载文件。
