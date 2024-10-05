import util,os
path="/Users/zhangzejunzhangzejun/PycharmProjects/pythonProject/view_count/"
total_num=[]
dict_num=dict()
total_count=0
for file in os.listdir(path):
    print("file: ",file)
    file_name=path+file
    a=util.load_csv(file_name)
    for ind,(e1, e2) in enumerate(a):
        if ind==0:
            continue
        total_num+=[int(e1)]*int(e2)
        dict_num[int(e1)]=int(e2)
        total_count+=int(e2)
    # total_num+=[ for e1,e2 in a]
    # print(a)
    # break
print("len: ",len(total_num))
count=0
for key in sorted(dict_num):
    print(key, dict_num[key])
    # break
    count+=dict_num[key]
    if count>total_count*0.90:

        print(count,key,dict_num[key])
        break
elements=['body','type_ignores','argtypes','returns','name','args','decorator_list',
          'returns','type_comment','bases','keywords','decorator_list','returns','value','targets','name','bases'
          'value','type_comment','target','op','value',
          'annotation','simple','iter','type_comment','orelse','test',
          'items','subject','cases','exc','cause','body','handlers','finalbody',
          'test','msg','names','module','level','op','values','left','right',
          'operand','keys','values','generators','elt','conversion','format_spec','comparators',
          'kind','attr','id','elts','lower','upper','step','ops','func','conversion']
print("len of elements: ",len(elements),len(set(elements)))
multiple_elemments=['type_ignores','decorator_list','body','bases','keywords','targets','orelse',
              'items','cases', 'handlers','finalbody', 'orelse',  'names',  'values','keys',
                'elts','generators','ops',  'comparators', 'values','elts' ]
print("elements: ",len(multiple_elemments),len(set(multiple_elemments)))
# print(sorted(total_num)[len(total_num)//2])