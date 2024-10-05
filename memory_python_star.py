from memory_profiler import profile
import sys
from guppy import hpy


@profile
def print_arg_1(arg,b,c,d,e,f,g,h,i,j):
    return arg
# instantiating the decorator
@profile
# code for which memory has to
# be monitored
def my_func():
    a=[i for i in range(100)]
    # b=1

    # arg=print_arg_1(*a[0:10:1])
    # print(arg)
    arg2=print_arg_1(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9])
    # print(arg2)
    # print_arg_1(*a[0:100:1])
    # print_arg_1(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10],
    #             a[11], a[12], a[13], a[14], a[15], a[16], a[17], a[18], a[19], a[20],
    #              a[21], a[22], a[23], a[24], a[25], a[26], a[27], a[28], a[29], a[30],
    #             a[31], a[32], a[33], a[34], a[35], a[36], a[37], a[38], a[39], a[40],
    #              a[41], a[42], a[43], a[44], a[45], a[46], a[47], a[48], a[49], a[50],
    #             a[51], a[52], a[53], a[54], a[55], a[56], a[57], a[58], a[59], a[60],
    #             a[61], a[62], a[63], a[64], a[65], a[66], a[67], a[68], a[69], a[70],
    #             a[71], a[72], a[73], a[74], a[75], a[76], a[77], a[78], a[79], a[80],
    #             a[81], a[82], a[83], a[84], a[85], a[86], a[87], a[88], a[89], a[90],
    #             a[91], a[92], a[93], a[94], a[95], a[96], a[97], a[98], a[99]
    #             )

    print("xxx: ",sys.getsizeof(a[0:1]))
    print("xxxxxxx: ",sys.getsizeof(a[0])+sys.getsizeof(a[1])+sys.getsizeof(a[2])+sys.getsizeof(a[3])
          +sys.getsizeof(a[4])+sys.getsizeof(a[5])+sys.getsizeof(a[6])+sys.getsizeof(a[7])+sys.getsizeof(a[8])
          +sys.getsizeof(a[9]))
    # print(sys.getsizeof(print_arg_1(*a[0:11:1])))
    # print(sys.getsizeof(print_arg_1(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10])))

    h = hpy()

    print (h.heap().all)





if __name__ == '__main__':
    my_func()