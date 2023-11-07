"""
    os模块
        可以帮助我们直接对操作系统进行操作。我们可以直接调用操作系统的可执行文件、命令，直接操作文件、目录等等。
    os模块-调用操作系统命令
        os.system 可以帮助我们直接调用系统的命令
        os.startfile：直接调用可执行文件
"""
import  os

# 调用windows系统的记事本程序
os.system("notepad.exe")
# 调用windows系统中ping命令
os.system("ping www.baidu.com")

# 运行安装好的微信
os.startfile(r"C:\Program Files(x86)\Tencent\WeChat\WeChat.exe")