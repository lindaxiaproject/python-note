"""
    异常机制本质：
        当程序出现异常，程序安全的退出、处理完后继续执行的机制
        python中引进了很多用来描述和处理异常的类。异常类定义中包含了该类异常的信息和对异常进行处理的方法。

    BaseException
        keyBoardInterrupt
        Exception
            NameError、ValueError、AttributeError等
        SystemExit
        GeneratorExit


    python中一切都是对象，异常也采用对象的方式来处理。

    异常解决的关键：定位
        当发生异常时，解释器会报相关的错误信息，并会在控制台打印出相关错误信息。我们只需按照从上到下的顺序即可追溯
        （Trackback）错误发生的过程，最终定位引起错误的那一行代码。

    常见异常：
        SyntaxError ：语法错误
        NameError： 尝试访问一个没有申明的变量（变量未定义）
        ZeroDivisionError： 除数为0错误（零除错误）
        ValueError：数值错误（例如： float("林大侠")）
        TypeError：类型错误(例如：123+"abc")
        AttributeError：访问对象的不存在的属性
        IndexError： 索引越界异常
        KeyError： 字典的关键字不存在
"""