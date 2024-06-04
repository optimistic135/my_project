## **Flask项目介绍**

整个项目采用前后端分离的开发方式：

在`python_flask`文件夹下存放的是网站应用的后端api接口，具体实现了

```python
#POST请求
    /login	#实现用户登录
	/register	#实现用户注册
	/addword	#实现添加生词
	/exer	#生成练习题
	/jude 	#判断对错
    
#GET请求：
	/meg	#得到用户添加生成信息
    
#DETELE请求：
	/deteleuser	#删除用户
	/deteleword	#删除生词
```



数据库表设计如下

```python
users表：
	id(key)
   	username
    password
    jion_time
learning表:
    id(key)
    username
    english
    chinese
    join_time
word表:	#向其中导入了六级词汇6000个作为题库
    id(key)
    english
    chinese
```



在`Vue`文件夹下存放的是使用`npm bulid`指令得到的打包过的项目文件夹

`nginx`文件夹中存放的是关于网站部署在虚拟机上nginx配置文件中的内容（由于项目运行在我创建的虚拟机中，在本机处于关机状态下可能导致访问失败）