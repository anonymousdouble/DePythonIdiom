import sys,ast,os
code_dir="/".join(os.path.abspath(__file__).split("/")[:-2])+"/"
print("code_dir: ",code_dir)
sys.path.append(code_dir)
import util
print(1)
util.save_csv("~/star_call_idiom_code_many_circumstances_cannot_explain.csv",
    [[1,2,3,4]])
