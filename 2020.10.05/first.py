username = "admin"
password = "123456"

usrname = input("请输入用户名:")
passwd  = input("请输入密码:")

if usrname == username and passwd == password:
    print("登录成功!")
if usrname != username:
    print("用户名错误")
    exit()
if passwd != password:
    print("密码错误")
