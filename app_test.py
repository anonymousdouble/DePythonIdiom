from flask import Flask,render_template,redirect,url_for,session
from flask import request
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    idioms = ['List Comprehension', 'Set Comprehension', 'Dict Comprehension']
    result=""
    return render_template("myindex.html",idioms=idioms,result=result)
    # return 'welrender_template("index.html",data=msg)come to my webpage!'
def me(a):
    return a+"hello"
@app.route('/idiom_refactor', methods=['POST','GET'])
def api_parse():
    if request.method=='POST':

        body = request.get_data()
        try:
            print("body:",body.__str__())
            # out=me(body)
            session['pythonic_code'] = "redirect"
            result="redirect2"
            print("body:", session['pythonic_code'])
            return redirect(url_for('index'))
            # return {"k":"redirect"+body
            # return render_template("myindex.html",[],result=result)
        except:
            return "Nothing need to be refactored!"
    else:
        session['pythonic_code'] = "redirect_current"
        result = "redirect_current"
        print("body:", session['pythonic_code'])
        # return render_template("myindex.html", [],result=result)
        # return {"k":"redirect_current"}#"redirect"#render_template('index.html')
        return redirect(url_for('index'))
if __name__ == "__main__":
    app.run(port=2020,host="127.0.0.1",debug=True)