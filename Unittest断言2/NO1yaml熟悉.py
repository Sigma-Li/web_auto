# 读取yaml 中的正常内容
import yaml

f=open('b.yml',encoding='utf-8')
a=yaml.load(f,Loader=yaml.FullLoader)
print(a)