# 保存文件并上传github流程
# 1.修改完成后按Ctrl + S 保存
# 2.在终端输入 git add 文件名
#   例如 git add hello.py 
#   添加文件夹内所有文件 git add . 
# 3.在终端输入 git commit -m "修改内容" 
#   例如 git commit -m "增加了某某功能" 
# 4.在终端输入 git push 
# 网页端按f5刷新页面

# 将你的新项目关联至github
# 1.登录github创建 New repository
# 2.在终端输入git config --global user.name  "你的github用户名" 
# 3.在终端输入git config --global user.email   "你的github邮箱" 
# 4.在终端输入git init
# 5.完成第一大块内容
# 6.在终端输入git remote add origin https://github.com/用户名/仓库名.git
# 7.在终端输入git push -u origin main
# 若显示port443 网络问题 大概率因为Watt Toolkit无法加速虚拟机里运行的Linux 可以考虑用github自带的add拖拽文件上传 
# 或者使用PS终端上传
# 注意浏览器拖转和终端指令不能混用 因为本地没有记录
# 若使用过浏览器上传 输入 git push -f origin main    -f  force 强制上传