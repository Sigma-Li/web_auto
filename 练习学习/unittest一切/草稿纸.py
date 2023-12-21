# sum=0
# for i in range(1, 101):
#     if i % 2 == 0:
#         sum+=i
# print(sum)
import yaml

# i=0
# sum = 0
# while i<=100:
#     if i % 2==0:
#         sum=sum+i
#     i+=1
# print(sum)
# ytyt=list()
# c=open('data1.txt', 'r', encoding='utf-8')
# for i in c.readlines():
#     ytyt.append(i.replace('\t',' ').strip('\n').split(' '))
# print(ytyt)
#
# bug=open('data2.txt','r',encoding='utf-8')
# for i in bug.readlines():
#     print(i.replace('\t',' ').strip('\n').split(' '))

F=open('data3.yml',encoding='utf-8')
T=yaml.load(F,Loader=yaml.FullLoader)
print(T)

u=open('data4.yml',encoding='utf-8')
oo=yaml.load(u,Loader=yaml.FullLoader)
print(oo)