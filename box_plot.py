
import sys, ast, os, copy
import tokenize
import sys,shutil,traceback
import matplotlib.pyplot as plt
sys.path.append("..")
sys.path.append("../../")
sys.path.append("/mnt/zejun/smp/code1/")
sys.path.append("/mnt/zejun/smp/code1/test_case")
sys.path.append("/mnt/zejun/smp/code1/transform_c_s")
import util#,rq2_performance,test_time
import numpy as np
time_record_dir=util.data_root + "time_record_dir/"
all_groups_new_time_list=[]
all_groups_old_time_list=[]
all_groups_new_time_list_min=[]
all_groups_old_time_list_min=[]
all_new_time_list = []
all_old_time_list = []
dict_map=dict()
time_record_list=[]
def is_float(element):
    try:
        a=float(element)
        return a
    except:

        return 0
#call_star
# for e in os.listdir(time_record_dir+"chain_compare/"):
#     file_name=e[:-4]
#     time_record_list.extend(util.load_pkl(time_record_dir+"chain_compare/", file_name))
# # util.save_pkl(time_record_dir, "call_star_timeit_repeat3_number_100000_new", time_record_list)
# util.save_pkl(time_record_dir, "chain_compare_timeit_repeat3_number_100000_total", time_record_list)
# if 1:
#
# # for i in range(1,26):
# #     pair_code_compare_list=util.load_pkl(time_record_dir, "list_compre_timeit_repeat3_number_100000")
#     # print(len(time_record_list))
#     # pair_code_compare_list = util.load_pkl(time_record_dir, "set_compre_own_config_timeit_repeat3_number_100000")
#     # pair_code_compare_list = util.load_pkl(time_record_dir, "dict_compre_timeit_repeat3_number_100000")
#     # pair_code_compare_list = util.load_pkl(time_record_dir, "call_star_timeit_repeat3_number_100000_new")
#     # pair_code_compare_list = util.load_pkl(time_record_dir, "call_star_timeit_repeat3_number_100000_2")
#     # pair_code_compare_list = util.load_pkl(time_record_dir, "for_target_timeit_repeat3_number_100000")
#     # pair_code_compare_list = util.load_pkl(time_record_dir, "chain_compare_timeit_repeat3_number_100000_total")
#     # pair_code_compare_list = util.load_pkl(time_record_dir, "chain_compare_timeit_repeat3_number_100000_2")
#     pair_code_compare_list = util.load_pkl(time_record_dir, "truth_value_test_timeit_repeat3_number_100000")
#
#     print(len(pair_code_compare_list))
#     # new_time_flatten_list=[[] for i in pair_code_compare_list]
#     # old_time_flatten_list=[[] for i in pair_code_compare_list]
#     all_repeat_old_time_min_list=[]
#     all_repeat_new_time_min_list=[]
#     for ind_com,one_code_pair_time in enumerate(pair_code_compare_list):
#         # for one_test_case_code_pair_time in one_code_pair_time:
#
#         new_time_list=one_code_pair_time[-1]
#         old_time_list = one_code_pair_time[-2]
#         repeat_old_time_min_list =[]
#         repeat_old_time_sum_list =[]
#         repeat_new_time_min_list = []
#         repeat_new_time_sum_list = []
#         # repeat_old_time_min_list =[np.median([float(each_time) for each_repeat in new_time_list for each_case in each_repeat for each_time in each_case])]
#         # repeat_new_time_min_list=[np.median([float(each_time) for each_old_repeat in old_time_list  for each_case in each_old_repeat for each_time in each_case])]
#         #'''
#         for ind_repet,each_repeat in enumerate(new_time_list):
#             each_old_repeat=old_time_list[ind_repet]
#             # each_repeat_new_time_list =  [np.median([float(each_time) for each_case in each_repeat for each_time in each_case])]
#             # each_repeat_old_time_list = [np.median([float(each_time) for each_case in each_old_repeat for each_time in each_case])]
#             a = [1 for each_case in each_repeat for each_time in each_case ]
#             b = [1 for each_case in each_old_repeat for each_time in each_case ]
#             if len(each_repeat)!=len(each_old_repeat):
#                 print("it is wrong, len(each_repeat), len(each_old_repeat): ",len(each_repeat),len(each_old_repeat))
#             elif len(a)!=len(b):
#                 print("it is wrong, len(a), len(b): ",len(each_repeat),len(each_old_repeat))
#
#             each_repeat_new_time_list = [np.sum([is_float(each_time) for each_time in each_case])  for each_case in each_repeat]
#             each_repeat_old_time_list = [np.sum([is_float(each_time) if is_float(each_time) else 0 for each_time in each_case]) for each_case in each_old_repeat]
#             # each_repeat_new_time_list = [float(each_time) for each_case in each_repeat for each_time in each_case]
#             # each_repeat_old_time_list=[float(each_time) for each_case in each_old_repeat for each_time in each_case]
#             # print("len: ",len(each_repeat_new_time_list),len(each_repeat_old_time_list))
#             if repeat_old_time_min_list:
#                 repeat_old_time_min_list=[min(e,repeat_old_time_min_list[ind_min]) for ind_min, e in enumerate(each_repeat_old_time_list)]
#                 repeat_new_time_min_list=[min(e,repeat_new_time_min_list[ind_min]) for ind_min, e in enumerate(each_repeat_new_time_list)]
#                 repeat_old_time_sum_list=[e+repeat_old_time_sum_list[ind_min] for ind_min, e in enumerate(each_repeat_old_time_list)]
#                 repeat_new_time_sum_list=[e+each_repeat_new_time_list[ind_min] for ind_min, e in enumerate(each_repeat_new_time_list)]
#             else:
#                 repeat_old_time_min_list=copy.deepcopy(each_repeat_old_time_list)
#                 repeat_new_time_min_list = copy.deepcopy(each_repeat_new_time_list)
#                 repeat_old_time_sum_list=copy.deepcopy(each_repeat_old_time_list)
#                 repeat_new_time_sum_list=copy.deepcopy(each_repeat_new_time_list)
#         #'''
#         beg=len(all_repeat_old_time_min_list)
#         for ind_map,e in enumerate(repeat_old_time_min_list):
#             dict_map[beg+ind_map]=one_code_pair_time
#         all_repeat_old_time_min_list.extend(repeat_old_time_sum_list)
#         all_repeat_new_time_min_list.extend(repeat_new_time_sum_list)
#
#         # all_repeat_old_time_min_list.extend(repeat_old_time_min_list)
#         # all_repeat_new_time_min_list.extend(repeat_new_time_min_list)
#         # break
#         # # for e in new_time_list:
#         # #     print(e)
#         # #https://github.com/CodeReclaimers/neat-python/blob/master/neat/graphs.py
#         # ##随机数https://github.com/CodeReclaimers/neat-python/blob/master/tests/test_graphs.py
#         # if len(new_time_list)==len(old_time_list):
#         #     for ind, e in enumerate(new_time_list):
#         #         if len(old_time_list[ind]) != len(e):
#         #             print(one_code_pair_time[:-2], len(old_time_list[ind]), len(e))
#         #             break
#         #         if old_time_list[ind]==e:
#         #             print("it is same: ",one_code_pair_time[:-2])
#         #     else:
#         #         new_time_flatten_list.extend([float(e) for e_list in new_time_list for e in e_list])
#         #         old_time_flatten_list.extend([float(e) for e_list in old_time_list for e in e_list])
#         #         # new_time_flatten_list.extend([[float(e),one_code_pair_time[:-2]] for e_list in new_time_list for e in e_list])
#         #         # old_time_flatten_list.extend([[float(e),one_code_pair_time[:-2]] for e_list in old_time_list for e in e_list])
#         #         all_new_time_list.extend([float(e) for e_list in new_time_list for e in e_list ])
#         #         all_old_time_list.extend([float(e)  for e_list in old_time_list for e in e_list ])
#         #
#         #
#         #         # if not all_groups_new_time_list_min:
#         #         #     all_groups_new_time_list_min.extend([float(e)  for e_list in new_time_list for e in e_list ])
#         #         #     all_groups_old_time_list_min.extend([float(e) for e_list in old_time_list for e in e_list])
#         #         # else:
#         #         #     for ind_min,e in enumerate(all_groups_new_time_list_min):
#         #         #         all_groups_new_time_list_min[ind_min]=min(all_groups_new_time_list_min[ind_min],e)
#         #         #         all_groups_old_time_list_min[ind_min]=min(all_old_time_list[ind_min],all_groups_old_time_list_min[ind_min])
#
#
#     # if not all_groups_new_time_list:
#     #     all_groups_new_time_list=[[] for i in range(len(new_time_flatten_list))]
#     #     all_groups_old_time_list=[[] for i in range(len(old_time_flatten_list))]
#     # print("len of all_groups_new_time_list: ",len(new_time_flatten_list),len(all_groups_new_time_list))
#     # for ind_fla,e in enumerate(new_time_flatten_list):
#     #     all_groups_new_time_list[ind_fla].append(e)
#     #     all_groups_old_time_list[ind_fla].append(old_time_flatten_list[ind_fla])
#     #
#     #
#     # print(len(all_new_time_list))
#     # print(len(all_old_time_list))
#
#
#
#
# # print(all_groups_new_time_list[0],min(all_groups_new_time_list[0]),max(all_groups_new_time_list[0]))
# # print(all_groups_old_time_list[0],min(all_groups_old_time_list[0]),max(all_groups_old_time_list[0]))
# # all_groups_new_time_list_min=[ min(e) for e in all_groups_new_time_list]
# # all_groups_old_time_list_min=[ min(e) for e in all_groups_old_time_list]
# print(len(all_repeat_old_time_min_list),all_repeat_old_time_min_list)
# print(len(all_repeat_new_time_min_list),all_repeat_new_time_min_list)
all_old_time_list=[[i*0.1 for i in range(10)] for i in range(9)]
# all_new_time_list=[[i*0.05 for i in range(10)],[(i+1)*0.05 for i in range(10)]]
# all_new_time_list=[all_repeat_old_time_min_list]
# all_old_time_list=[all_repeat_new_time_min_list]
# all_new_time_list=[all_repeat_old_time_min_list]
# all_old_time_list=[all_repeat_new_time_min_list]
# all_new_time_list=[all_new_time_list]
# all_old_time_list=[all_old_time_list]
x_position=[0.1+i*1 for i in range(9)]
x_position_fmt=["List Compre","Set Compre","Dict Compre","Call Star","For Multi Tar","Chain Compare","Truth Test","Multi Assign","For Else"]

#https://www.tutorialspoint.com/adjust-the-width-of-box-in-boxplot-in-python-matplotlib
plt.rcParams["figure.figsize"] = [10, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.rcParams["axes.spines.right"]=False
plt.rcParams["axes.spines.top"]=False
# plt.figsize=(cm_to_inch(800),cm_to_inch(20))
plt.boxplot(all_old_time_list,positions=x_position,widths=0.2)
plt.text(0.1,0.5,"test")
plt.text(1.1,0.5,"test")

plt.xticks([i for i in x_position] ,x_position_fmt )
plt.ylabel("time (s)")

plt.show()
def cm_to_inch(value):
    return value/2.54
# plt.savefig(fname="set_comprehension_time_diff.png")#,fontsize=[10,10]
# plt.show()

'''
count=0
count_posi=0
count_equal_0=0
diff_list=[]
diff_ratio_list=[]
base_num=300000
count_total_0=0
for ind, e in enumerate(all_repeat_new_time_min_list):
    # print(e)
    if not e:
        count_total_0+=1
        # print("why is 0: ",e)
        continue
    diff = all_repeat_old_time_min_list[ind] - e
    diff_list.append(diff/base_num)
    # print(all_repeat_old_time_min_list[ind])
    diff_ratio=diff/all_repeat_old_time_min_list[ind]
    if diff_ratio<-1:
        # print()
        continue
        print("interested infor: ",all_repeat_old_time_min_list[ind],e,diff,diff_ratio,dict_map[ind])

    diff_ratio_list.append(diff_ratio)
    # print("interested infor: ", all_repeat_old_time_min_list[ind], e, diff, diff_ratio, dict_map[ind])

    if diff < 0:
        # print(ind)
        count += 1

    elif diff==0:
        count_equal_0+=1
        # print(ind)
    elif diff >0 :
        count_posi+=1
    if diff_ratio>0.3:
        pass
            # print("diff: ",diff,e,all_groups_old_time_list_min[ind],diff/all_groups_old_time_list_min[ind])
print("all count: ",count_total_0, count,count_posi)
print("count_equal_0: ",count_equal_0)

#https://anaconda.org/afalkovskiy/comp_time_compare/notebook 折线图
#https://blog.csdn.net/weixin_44613728/article/details/115190556

a="ListComp"
plt.boxplot(diff_list)
plt.xticks(ticks=[0.1],labels=["time_diff"] )
plt.ylabel("time difference(s)")
plt.xlabel(a)
plt.savefig(fname="_time_diff.png")#,fontsize=[10,10]
plt.show()
plt.boxplot(diff_ratio_list)
plt.xticks(ticks=[0.1],labels=["time_diff_ratio"] )
plt.ylabel("ratio of time difference")
plt.xlabel(a)
plt.savefig(fname="time_diff_ratio.png")#,fontsize=[10,10]
plt.show()
'''
# from scipy.stats import ranksums,mannwhitneyu,wilcoxon
# import cliffsDelta
# print("diff: ",np.median(diff_list),np.min(diff_list),np.max(diff_list))
# print("diff: ",np.median(diff_ratio_list),np.min(diff_ratio_list),np.max(diff_ratio_list))
# stat, p = wilcoxon([e/base_num for e in all_repeat_old_time_min_list], [e/base_num for e in all_repeat_new_time_min_list])
#         # stat_wilcoxon, p1_wilcoxon =wilcoxon(s_repo_list, c_repo_list)
#
# d, res = cliffsDelta.cliffsDelta([e/base_num for e in all_repeat_old_time_min_list], [e/base_num for e in all_repeat_new_time_min_list])
# print("stat, p, d,res: ", stat, p, d, res)
# #'''
