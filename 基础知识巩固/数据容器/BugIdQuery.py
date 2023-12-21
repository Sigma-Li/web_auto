#通过bug列表query ID
bug_data=open('C:/Users/v-sigmali/PycharmProjects/bugs.txt','r',encoding='utf-8')
initial=bug_data.readline()
details=bug_data.readlines()
for work in details:
    good=work.replace('\t',' ').replace('[',' ').replace(']',' ').replace('  ',' ')
    better=good.strip('\n').split(' ')
    print(better[0])

# Task owner bug id query   暂不实现
# test_details=open('C:/Users/v-sigmali/PycharmProjects/summary.txt','r',encoding='utf-8')
# for line in range(0,8):
#     notnecessary=test_details.readline()
# # notnecessary1=test_details.readline()
# # a=test_details.readline()
# # b=test_details.readline()
# # c=test_details.readline()
# # d=test_details.readline()
# # e=test_details.readline()
# ava=test_details.readlines()
# for data in ava:
#     format=data.replace('\t',' ').strip('\n').split(' ')

