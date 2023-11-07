"""
    pip是一个现代的，通用的Python包管理工具。提供了对 Python 包的查找、下载、安装、卸载的功能。

第一种方式：命令行下远程安装
    pip更换数据源(由于访问国外网站慢，建议更换)：
        家目录中，创建 pip目录，然后增加文件：pip.ini  内容拷贝下 面的即可(不要加其他字符)：

        [global]
        index-url =
        https://mirrors.aliyun.com/pypi/simple/

        [install]
        trusted-host=mirrors.aliyun.com

        inux的家目录：~ 增加目录和文件:~/.pip/pip.conf
        Windows的家目录是	c:/user/用户名  增加目录和文件	c:/user/用户名/pip/pip.ini


     其他数据源：
        阿里云 http://mirrors.aliyun.com/pypi/simple/
        豆瓣： http://pypi.douban.com/simple/
        中国科学技术大学 : https://pypi.mirrors.ustc.edu.cn/simple
        清华： https://pypi.tuna.tsinghua.edu.cn/simple
        华中理工大学 : http://pypi.hustunique.com/simple
        山东理工大学 : http://pypi.sdutlinux.org/simple
        V2EX：http://pypi.v2ex.com/simple

第二种方式：  Pycharm中直接安装到项目中
	在Pycharm中，依次点击: file-- >setting-- >Project 本项目名-- >Project Interpreter
	点击 +  ，然后输入要安装的第三方库 pymysql  ,再点击按钮Install Package,等待安装即可，几秒种后，即提示安装成功

"""