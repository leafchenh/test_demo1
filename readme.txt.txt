项目结构：
	1. 项目文件my_test
	2. 环境文件venv

项目文件my_test介绍：
	1. game_ranking 游戏排名应用文件
	2. static 静态文件（包括下载的bootstrap插件）
	3. templates 页面模板文件
	4. db.sqlite3 所使用的数据存储

游戏排名应用game_ranking介绍：
	1. 后台管理文件 admin.py
	2. 与存储交互文件models.py
	3. 处理用户请求，处理数据并渲染文件views
	4. 路由文件urls.py

项目测试：
	1. 执行Django项目代码
	2. 登录http://127.0.0.1:8888 查看首页
	3. 登录http://127.0.0.1:8888/admin 查看后台管理页
	4. 登录http://127.0.0.1:8888/put 查看用户信息提交页，填写信息并提交
	5. 登录http://127.0.0.1:8888/get 用户填写ID，查询范围，查询排名
	6. 展示排名信息	