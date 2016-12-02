文档说明：
1.myweb是使用django 搭建的web项目，实现查询数据库里的需求表，测试表，脚本表
2.使用的技术有django的搭建，页面使用bootstrap和bootstrap-table插件，jquery来完成
3.由于是第一次搭建，里面很多app都是练习使用
4.PyMySQL-master是连接mysql使用的，mysql貌似可以之间连接django但是我安装失败，所以就用了这种方式，大家如果连接自己的数据库需要在setting里面设置DATABASES ={}
5.static文件夹是我建立的一个存放静态资源的文件夹，存放js、css等，如果自己定义静态文件夹需要在setting里设置STATIC_URL = 'static/'，STATIC_ROOT = os.path.join(BASE_DIR, 'static') 并在urls.py里设置urlpatterns =[]+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT).
6.页面都定义在templates里面
7.fileUploadTest是实现了上传文件，并将文件保存到upload文件夹下，将路径保存数据库
8.yxtest是实现了数据库的增删改查，不过他们每个功能都是使用的统一模板，而不是分别定义的
例如：需求表，测试表，脚本表他们的增操作都是使用一个模板，通过遍历该对象的属性来生成界面。
9. yxtest2是实现了将一张数据库的表，用树的形式来展示，前提是他们有对应的关系。。
10.yxtest3是实现了需求表，测试表，脚本表在数据库提取，封装成json传到浏览器并使用bootstrao-table来展示
他们对应的增删改查都是使用特定的模板（好处就是可以展示自己想展示的信息，并且定义简单）
注意：bootstrao-table自己带ajax功能。在页面初始化的时候都是使用ajax提交请求，而不是返回模板的时候，顺便返回请求。（ps:只有需求表实现了新增功能，其余的类似。其余操作只定义了按钮和事件，还没有定义处理过程）


django3.5常使用的命令：
1.python manage.py startapp APPname 新建一个app
2.django1.9以后不支持python manage.py syncdb
所以使用python manage.py migrate 或者 python manage.py makemigrations
3.新建好model以后执行
python manage.py makemigrations 用来检测数据库变更和生成数据库迁移文件 
python manage.py sqlmigrate APPname 0001 用来把数据库迁移文件转换成数据库语言 
python manage.py migrate 用于执行迁移动作
