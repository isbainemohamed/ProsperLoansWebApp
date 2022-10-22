from flask import Flask, jsonify, request, render_template
import time
import random
from predict import predict
from predict import run

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/send', methods =["GET", "POST"])
def process():
    if request.method == "POST":
       # getting input with name = fname in HTML form

       full_name = request.form.get('full_name')
       term = int(request.form.get('term'))
       # print(transcription)
       grade = request.form.get('grade')
       int_rate = request.form.get("int_rate")
       loan_amnt = request.form.get("loan_amnt")
       emp_title = request.form.get("emp_title")
       emp_length = int(request.form.get("emp_length"))
       home_ownership = request.form.get("home_ownership")
       annual_inc = float(request.form.get("annual_inc"))
       verification_status = request.form.get("verification_status")
       purpose = request.form.get("purpose")
       dti = request.form.get("dti")
       ## process request
       time.sleep(5)
       #prediction=random.choice(["able","enable"])
       prediction=run(term,grade,int_rate,loan_amnt,emp_title,emp_length,home_ownership,verification_status,annual_inc,purpose,dti)
       return {"name":full_name,"prediction":prediction}



if __name__ == '__main__':
   app.run()
