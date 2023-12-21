data=open('数据', 'r', encoding='utf-8')
content=data.readlines()
for i in content:
    print(i)
    ll=i.replace('\t',' ').strip('\n').split(' ')

print(ll)
