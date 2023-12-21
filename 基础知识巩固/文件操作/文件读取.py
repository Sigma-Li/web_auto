# 统计文件中某个字符串出现的次数
# way1 read()
'''f=open('C:/Users/v-sigmali/PycharmProjects/aa.txt','r',encoding='utf-8')
str=f.read()
#  readline() readlines() 返回列表, read() 返回字符串
# print(type(str))
print(str.count('itheima'))
print(str.strip('\n').replace('\n',' ').split(' ').count('itheima'))'''

# way2 readlines()
count=0
ff=open('C:/Users/v-sigmali/PycharmProjects/aa.txt','r',encoding='utf-8')
details=ff.readlines()
for individual in details:
    nn=individual.strip().split(' ')
    for words in nn:
        if words =='itheima':
            count+=1
print(count)
