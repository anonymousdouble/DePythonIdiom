import os
abs_path=os.getcwd()
import sys
sys.path.append(abs_path+"/")
sys.path.append(abs_path+"/extract_transform_complicate_code_new")
sys.path.append(abs_path+"/extract_idiom_code_new")
from flask import Flask,render_template,redirect,url_for,session
from flask import request,jsonify
import json
from extract_idiom_code_new import pair_idiom_nonidiom_list_compre,pair_idiom_nonidiom_set_compre,\
    pair_idiom_nonidiom_dict_compre,pair_idiom_nonidiom_chain_compare,pair_idiom_nonidiom_truth_value_test,\
    pair_idiom_nonidiom_for_else,pair_idiom_nonidiom_for_multi_tar,pair_idiom_nonidiom_multi_ass,\
    pair_idiom_nonidiom_call_star_many_cirumstances_contain_not_explain
from extract_transform_complicate_code_new.comprehension import extract_compli_for_comprehension_only_one_stmt_improve,\
    extract_compli_for_comprehension_set_only_one_stmt,extract_compli_for_comprehension_dict_only_one_stmt_new
from extract_transform_complicate_code_new import    transform_chained_comparison_compli_to_simple,\
extract_compli_var_unpack_for_target_improve,transform_for_else_compli_to_simple_improve_copy_result_csv,\
extract_compli_truth_value_test_code_remove_is_isnot,extract_compli_multiple_assign_code_improve_complete_improve,\
extract_compli_var_unpack_star_call_improve
from datetime import timedelta
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.debug=True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=1)
idioms = ['All','List Comprehension', 'Set Comprehension', 'Dict Comprehension','Chain Comparison',
          'Truth Value Test','Assign Multiple Targets','For Multiple Targets','For Else'
          ,'Star']
@app.route('/' ,methods=['POST','GET'])
def index():

    # body = request.get_data(as_text=True)
    # if body:
    #     # body = request.form.get('other')
    #     body = json.loads(body)
    #     print("main body:", body)
    # result=""
    code = '''
def f():
    for  (name, (value, source)) in build_dict['properties']:
        if source == 'Force Build Form':
             pass
    ambiguous = {k: v for (k, v) in refs[0].items() if len(v) > 1} 
    if fuzzy:
        pass
    if table_name in row is False:
        pass
    a,b=c
    data, the_hash = data[:-4], data[-4:]
    decrement_run = lambda run: [val - 1 for val in run]
    [CL.remove(m) for m in CL if m in DF_tree.nodes[node_p]['GM']] 
    for pull_file in p.files():
        if pull_file.filename == filename:
            break
    else:
        assert False, f"Could not find '{filename}'"
    pack("<2d", *p[:2])

    values = {v.lower() if isinstance(v, str) else v for v in self._values}    '''
    pythonic_code=""
    return render_template("index.html",idioms=idioms,code=code,pythonic_code=pythonic_code,idiom_one="")
    # return 'welrender_template("index.html",data=msg)come to my webpage!'

@app.route('/idiom_refactor', methods=['POST','GET'])
def api_parse():
    # if request.method=='POST':

        body = request.get_data(as_text=True)
        # body = request.form.get('other')
        body = json.loads(body)
        idiom=body['idiom']
        code_frag=body['code']
        print(">>>>>>>>>code_frag: ",code_frag)
        # print(idiom,code_frag)
        if idiom=='List Comprehension':
            code_pair_list=pair_idiom_nonidiom_list_compre.get_list_compreh(code_frag)
            # code_pair_list=extract_compli_for_comprehension_only_one_stmt_improve.get_list_compreh(code_frag)
            if code_pair_list:
                pass
                print("code_list: ",code_pair_list,jsonify(code_pair_list).json[0][0])

            return jsonify(code_pair_list)
            pass
        elif idiom=='Set Comprehension':
            code_pair_list = pair_idiom_nonidiom_set_compre.get_set_compreh(code_frag)
            # code_pair_list = extract_compli_for_comprehension_set_only_one_stmt.get_set_compreh(code_frag)
            if code_pair_list:
                pass
                # print("code_list: ", code_pair_list, jsonify(code_pair_list).json[0][0])

            return jsonify(code_pair_list)
            pass
        elif idiom=='Dict Comprehension':
            code_pair_list = pair_idiom_nonidiom_dict_compre.get_dict_compreh(code_frag)
            # code_pair_list = extract_compli_for_comprehension_dict_only_one_stmt_new.get_dict_compreh(code_frag)
            return jsonify(code_pair_list)
            pass
        elif idiom=='Chain Comparison':
            code_pair_list = pair_idiom_nonidiom_chain_compare.get_chain_compare(code_frag)
            # code_pair_list = transform_chained_comparison_compli_to_simple.get_chain_compare(code_frag)
            return jsonify(code_pair_list)
            pass
        elif idiom=='Truth Value Test':
            code_pair_list = pair_idiom_nonidiom_truth_value_test.get_truth_value_test_code(code_frag)
            # code_pair_list = extract_compli_truth_value_test_code_remove_is_isnot.get_truth_value_test_code(code_frag)
            return jsonify(code_pair_list)
            pass
        elif idiom=='Assign Multiple Targets':
            code_pair_list = pair_idiom_nonidiom_multi_ass.get_multiple_assign_code(code_frag)

            # code_pair_list = extract_compli_multiple_assign_code_improve_complete_improve.transform_multiple_assign_code(code_frag)
            return jsonify(code_pair_list)
            pass
        elif idiom=='For Multiple Targets':
            code_pair_list = pair_idiom_nonidiom_for_multi_tar.get_for_multi_tar(code_frag)

            # code_pair_list = extract_compli_var_unpack_for_target_improve.transform_for_multiple_targets_code(
            #     code_frag)
            return jsonify(code_pair_list)
            pass
        elif idiom=='For Else':
            code_pair_list = pair_idiom_nonidiom_for_else.get_loop_else(
                code_frag)
            # code_pair_list = transform_for_else_compli_to_simple_improve_copy_result_csv.transform_for_else_code(
            #     code_frag)
            return jsonify(code_pair_list)
            pass
        elif idiom=='Star':
            code_pair_list = pair_idiom_nonidiom_call_star_many_cirumstances_contain_not_explain.get_star(
                code_frag)
            # code_pair_list = extract_compli_var_unpack_star_call_improve.transform_star_call_code(
            #     code_frag)
            return jsonify(code_pair_list)

            pass
        elif idiom=='All':
            #idioms = ['All','List Comprehension', 'Set Comprehension', 'Dict Comprehension','Chain Comparison',
          #'Truth Value Test','Assign Multiple Targets','For Multiple Targets','For Else'
          #,'Star in Call']
            code_pair_list=[]
            print("code_frag")
            print(code_frag)
            code_pair_list_list_compre=pair_idiom_nonidiom_list_compre.get_list_compreh(code_frag)
            print(code_pair_list_list_compre)
            for e in code_pair_list_list_compre:
                e.insert(0, "List Comprehension")
                code_pair_list.append(e)
            # code_pair_list.extend([e.insert(0,"List Comprehension") for e in code_pair_list_list_compre])
            code_pair_list_set_compre = pair_idiom_nonidiom_set_compre.get_set_compreh(code_frag)
            for e in code_pair_list_set_compre:
                e.insert(0, "Set Comprehension")
                code_pair_list.append(e)
            # code_pair_list.extend([e.insert(0,"Set Comprehension") for e in code_pair_list_set_compre])
            code_pair_list_dict_compre = pair_idiom_nonidiom_dict_compre.get_dict_compreh(code_frag)
            # code_pair_list.extend([e.insert(0,"Dict Comprehension") for e in code_pair_list_dict_compre])
            for e in code_pair_list_dict_compre:
                e.insert(0, "Dict Comprehension")
                code_pair_list.append(e)
            code_pair_list_chain_compare = pair_idiom_nonidiom_chain_compare.get_chain_compare(code_frag)
            # code_pair_list.extend([e.insert(0,"Chain Compare") for e in code_pair_list_chain_compare])
            for e in code_pair_list_chain_compare:
                e.insert(0, "Chain Compare")
                code_pair_list.append(e)
            code_pair_list_truth_value = pair_idiom_nonidiom_truth_value_test.get_truth_value_test_code(code_frag)
            # code_pair_list.extend([e.insert(0,"Truth Value Test") for e in code_pair_list_truth_value])
            for e in code_pair_list_truth_value:
                e.insert(0, "Truth Value Test")
                code_pair_list.append(e)
            code_pair_list_assign_multi_targets = pair_idiom_nonidiom_multi_ass.get_multiple_assign_code(code_frag)
            # code_pair_list.extend([e.insert(0,"Assign Multi Targets") for e in code_pair_list_assign_multi_targets])
            for e in code_pair_list_assign_multi_targets:
                e.insert(0, "Assign Multi Targets")
                code_pair_list.append(e)
            code_pair_list_for_multi_target =  pair_idiom_nonidiom_for_multi_tar.get_for_multi_tar(code_frag)
            # code_pair_list.extend([e.insert(0,"For Multi Targets") for e in code_pair_list_for_multi_target])
            for e in code_pair_list_for_multi_target:
                e.insert(0, "For Multi Targets")
                code_pair_list.append(e)
            code_pair_listfor_else = pair_idiom_nonidiom_for_else.get_loop_else(
                code_frag)
            for e in code_pair_listfor_else:
                e.insert(0, "For Else")
                code_pair_list.append(e)
            # code_pair_list.extend([e.insert(0,"For Else") for e in code_pair_listfor_else])

            code_pair_list_call_star = pair_idiom_nonidiom_call_star_many_cirumstances_contain_not_explain.get_star(
                code_frag)
            for e in code_pair_list_call_star:
                e.insert(0, "Star")
                code_pair_list.append(e)
            # code_pair_list.extend([e.insert(0,"Call Star") for e in code_pair_list_call_star])

            return jsonify(code_pair_list)
        else:
            return None,None
        # try:
        #     print("body:",body)
        #     pythonic_code=me(body)
        #     return jsonify(pythonic_code)
        #     # return render_template("myindex2.html", idioms=idioms, code=body["code"]+"csdc", pythonic_code=pythonic_code, idiom_one=body["idiom"])
        #     # return redirect(url_for('index'))
        #     # return redirect(url_for('index',idioms=idioms,code=body["code"]+"csdc",pythonic_code=pythonic_code,idiom_one=body["idiom"]))
        #     # return {"k":"redirect"+body
        #     # return render_template("myindex.html",[],result=result)
        # except:
        #     return "Nothing need to be refactored!"
    # else:
    #     session['pythonic_code'] = "redirect_current"
    #     result = "redirect_current"
    #     print("body:", request.get_data())
    #     return redirect(url_for('index', idioms=idioms, code=body["code"] + "csdc", pythonic_code=pythonic_code,
    #                             idiom_one=body["idiom"]))
    #
    #     # return render_template("myindex.html", [],result=result)
    #     # return {"k":"redirect_current"}#"redirect"#render_template('index.html')
    #     return redirect(url_for('index'))
if __name__ == "__main__":
    # app.run(host=os.getenv('IP', '0.0.0.0'),
    #         port=int(os.getenv('PORT',5000)))
    # app.run(host=os.getenv('IP', '0.0.0.0'),
    #         port=int(os.getenv('PORT', 5001)))
    # app.run(host="127.0.0.1",
    #         port=int(os.getenv('PORT', 1000)), debug = True)
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT',5000)))
    # app.run(port=5000, host="13.231.149.154", debug=False)
    # app.run(port=2029,host="127.0.0.1",debug=False)
     # app.run(port=2023,host="127.0.0.1",debug=False)
