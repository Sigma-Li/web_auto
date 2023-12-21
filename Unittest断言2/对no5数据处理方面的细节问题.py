
def datahandle():
    list = []
    data=open('datainfo.txt','r',encoding='utf-8')
    content=data.readlines()
    for i in content:
        premeter=i.strip('\n').split(" ")
        ddd=list.append(premeter)
        return list

aa=datahandle()
print(aa)