# 文件写入： W模式，文件不存在会创建文件，存在就会将此文件内容清空并写入文本
'''file=open('c:/users/v-sigmali/PycharmProjects/write.txt','w',encoding='utf-8')
new=file.write("Hello!I'm Sigma who is  learning to write text to a file with Python" )
file.flush()'''

#文件追加 W模式,文件不存在会创建文件，存在时，内容会添加到文件

'''file1=open('c:/users/v-sigmali/PycharmProjects/write.txt','a',encoding='utf-8')
new1=file1.write('\nThis is a new line')
file1.flush()'''


#案例 将testcase1.txt 中pass,failed和其他 的case 筛选出来分别备份到名为 passed.txt,failed.txt 和other.txt 的文件中

file2=open('c:/users/v-sigmali/PycharmProjects/testcase1.txt','r',encoding='utf-8')
content=file2.readline()
content=file2.readlines()
for items in content:
    item=items.replace('\t',' ').strip().split(' ')
    if item[-1] == 'Passed':
        file3=open('c:/users/v-sigmali/PycharmProjects/passed.txt','a',encoding='utf-8')
        file3.write(items)
    elif item[-1] == 'Failed':
        file4=open('c:/users/v-sigmali/PycharmProjects/failed.txt','a',encoding='utf-8')
        file4.write(items)
    else:
        file5 = open('c:/users/v-sigmali/PycharmProjects/other.txt', 'a', encoding='utf-8')
        file5.write(items)
