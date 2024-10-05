import pylint.lint
a=[]
for i in range(10):
    a.append(i)
a=set()
for i in range(10):
    a.add(i)
if len(a)==0:
    pass
if a==[]:
    pass
a=[]
for i in range(10):
    a.append(i)

a=0
if a==[]:
    pass
if a=={}:
    pass
b=3
if a>1 and b>2 and a<3:
    pass

if a==True and  b>1:
    pass
if a=="":
    pass
if a is []:
    pass
code='''
option={}
if option!={}:
    pass
'''
code2='''
option={}
if not option:
    pass
'''
import timeit
print(timeit.timeit(code,number=1000000))
print(timeit.timeit(code2,number=1000000))
# pylint_opts = ['--disable=line-too-long','/Users/zhangzejunzhangzejun/PycharmProjects/pythonProject/python-ast-explorer-master/python_nine_category.py']
# pylint.lint.Run(pylint_opts)