import shutil
import os

# 拷贝文件内容到一个已经存在的文件中  copyfileobj()
with open("01.py","r",encoding='utf-8') as f1,\
        open("01.txt",'w+',encoding="utf-8") as f2:
    shutil.copyfileobj(f1,f2)
    f2.seek(0)
    print(f2.read())

# 拷贝文件内容到一个不存在的文件中  copyfile()
shutil.copyfile("01.py","02.txt")
print(open("02.txt",encoding="utf-8").read())

# 拷贝文件的权限 copymode
print(os.stat("01.txt")[0])       # os.stat获取文件属性
print(os.stat("02.txt")[0])

shutil.copymode("02.txt","01.txt")   # 将文件02的权限覆盖给01文件
print(os.stat("02.txt")[0])


# 拷贝文件的状态信息  copystat()
res = os.stat("01.txt")
res2 = os.stat("03.txt")
print(res[-3],res[-2])    # 取到文件的atime和mtime时间戳
print(res[-3],res[-2])

shutil.copystat("01.txt","02.txt")  #  进行文件状态信息的拷贝

# 拷贝文件内容和文件权限 copy()
shutil.copy("01.txt","03.txt")


# 拷贝目录树 copytree， 目标目录必须不存在，如果存在则会抛出FileExistsError的错误
res = os.listdir("./aaa")
print(res)
try:
    shutil.copytree("./aaa","./testdir",ignore=shutil.ignore_patterns("test1.txt","test"))  # ignore选项 排除不拷贝的文件
    print(os.listdir("./testdir"))
except FileExistsError as e:
    print(e)

# 递归删除目录下的目录和文件  rmtree
shutil.rmtree("./aaa/cccc")

# 递归移动文件，相当于mv命令 move() ,修改了文件名
print(os.listdir("./aaa"))
shutil.move("./aaa","./bbb")
print(os.listdir("./bbb"))

# 创建压缩包并返回文件路径
"""
base_name	压缩包路径及名字 (只写名字默认保存在当前目录)
format	压缩包类型 : “zip” “tar” “bztar” “gztar”
root_dir	要压缩的文件夹路径 (默认当前路径)
owner	用户 (默认是当前用户)
group	组 (默认是当前组)
logger	用于记录日志 (通常是logger.Logger对象)
"""

shutil.make_archive(base_dir="./bbb",format="tar",root_dir="./bbb")
