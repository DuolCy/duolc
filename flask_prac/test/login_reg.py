from flask import Flask,request
from flask import render_template
from test.common.sql_database import *
app = Flask(__name__)
@app.route('/reg',methods=['get'])
def reg():
    return render_template('reg.html')
# @app.route('/result')
# def reasult():
#     if request.method == 'GET':
#         result = request.form
#         return render_template("result.html", result=result)


app.run()