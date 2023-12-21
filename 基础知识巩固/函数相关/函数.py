# 无参数无返回值
def demo():
    print('hello world')


demo()
demo()
var = demo()
var
var1 = demo
var1()


# ********************************************************************************
# 有参数 无返回值
def demo1(x, y):
    z = x + y
    m = x ** y
    print(f'{x} + {y} = {z}')
    print(f'{x} ** {y} = {m}')


demo1(4, 2)


# ********************************************************************************
def demo3(num1, num2):  # 定义函数时传递的参数是实参
    if num1 == num2:
        print('You are right!')
    else:
        print('No')


demo3(5, 6)  # 调用时的参数是实参


# ********************************************************************************
#   必须参数
# 字符串格式化   %s == string    %d == int    %f == float

def stuinfo(name, age):
    print('学生的名字是%s,年龄是%d' % (name, age))


stuinfo('sigma', 26)

'''    print('学生的名字是%s,年龄是%d'%(name,age))
TypeError: %d format: a number is required, not str
'''


# ********************************************************************************


# 关键字参数

def stuinfo1(name, age, record):
    print(f'第一种方式：该学生姓名：{name},年龄：{age},成绩：{record}')
    print('第二种方式：该学生姓名 %s, 年龄 %d,成绩 %f' % (name, age, record))


stuinfo1(age=18, record=98.5, name='sigma')


# ********************************************************************************

# 默认参数
# 实参指定某一值即默认参数，调用时如果不传入形参，则为指定值，若传入形参，则覆盖指定值。且默认参数一般放在最后。
def add(x, y, z=100):
    sum = x + y + z
    print(sum)


add(3, 6)
add(3, 7, 9)


# ********************************************************************************

# 不定长参数  *args 用来接收多个位置参数，得到元组
def unstable(*args):
    print(args)


unstable(5, 8, 25)


def unstable1(version, *args):  # 形参有多个时，不定长参数位置放最后
    print(f'版本是： {version},兼容系统：{args}')


unstable1('23.8.32', 'ios', 'android', 'windows', 'macOS')


# 不定长参数之 **kwargs  用来接收多个关键字参数，得到一个字典，传参用key value 形式

def unstable2(**kwargs):
    print(kwargs)


unstable2(name='sigma', age=26)
# ********************************************************************************

# 函数返回值  return后的代码不会输出。到 return执行完毕

def returna():
    return '一定要学会有返回值的函数'
result=returna()               #返回值哪里调用就返回到哪里，如果想要显示返回值，需要用变量接受
print(result)                 #输出变量或者
print(returna())

def returnb(x,y,z):
    sum2=x +y +z
    return sum2, '正在学习有关函数返回值'
b = returnb(4,7,6)
print(b)
    # return一次返回多个值

