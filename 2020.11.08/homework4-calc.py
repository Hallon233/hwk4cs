print("====指令列表====")
print("1.加法")
print("2.减法")
print("3.除法")
print("4.乘法")
print("================")


choice=(input("请输入指令:"))
if choice=="1":                                #加法
    a=float(input("请输入第一个数字:"))
    b=float(input("请输入第二个数字:"))
    print(a+b)
elif choice=="2":
    a=float(input("请输入第一个数字:"))
    b=float(input("请输入第二个数字:"))
    print(a-b)
elif choice=="3":
    a=float(input("请输入第一个数字:"))
    b=float(input("请输入第二个数字:"))
    print(a/b)
elif choice=="4":
    a=float(input("请输入第一个数字:"))
    b=float(input("请输入第二个数字:"))
    print(a*b)
else:
    print("指令不存在")

