# try:
#     f = open('./dom.txt','r',encoding='utf-8')
#     print(f.read())
# finally:
#     if f:
#         f.close()


f1 = open('./dom.txt','w',encoding='utf-8')
f1.write('这是测试写文件')
f1.close()

with open('./dom.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        print(line.strip())

