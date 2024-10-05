import time,timeit
# start=time.time()
# code='''
# tags = []
# for i in range(10):
#     tags.append(i)
# '''
# total_time_1= min(
#     timeit.repeat(code, globals={**globals(), **locals()}, repeat=1, number=100000))
# code='''
# tags = [i for i in range(10)]
# '''
# total_time_2= min(
#     timeit.repeat(code, globals={**globals(), **locals()}, repeat=1, number=100000))
# print("time1, time2: ",total_time_1,total_time_2,(total_time_1-total_time_2)/total_time_1)

# end=time.time()
# aa=end-start
# print("time: ",aa)
# start=time.time()
# tags = [i for i in range(1000)]
# end=time.time()
# print("time: ",(end-start)/aa)

start=time.time()
tags =set()
for i in range(10):
    tags.add(i)
end=time.time()
aa=end-start
print("time: ",aa)
start=time.time()
tags = {i for i in range(10)}
end=time.time()
print("time: ",(end-start)/aa)

a=[1]

code='''
a==[]
'''
total_time_1= min(
    timeit.repeat(code, globals={**globals(), **locals()}, repeat=1, number=100000))
code='''
not a
'''
total_time_2= min(
    timeit.repeat(code, globals={**globals(), **locals()}, repeat=1, number=100000))
print("time1, time2: ",total_time_1,total_time_2,(total_time_1-total_time_2)/total_time_1)
code='''
a=1
b=1
'''
total_time_1= min(
    timeit.repeat(code, globals={**globals(), **locals()}, repeat=1, number=100000))
code='''
a,b=1,1
'''
total_time_2= min(
    timeit.repeat(code, globals={**globals(), **locals()}, repeat=1, number=100000))
print("time1, time2: ",total_time_1,total_time_2,(total_time_1-total_time_2)/total_time_1)
