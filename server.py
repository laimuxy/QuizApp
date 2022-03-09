from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

#Pirmā lapa, kas tiks ielādēta
@app.route('/',methods = ['POST', 'GET'])
def root():
    return render_template("index.html")

#Cels uz about
@app.route('/about',methods = ['POST', 'GET'])
def about():
    return render_template("about.html")

#cels uz test
@app.route('/test',methods = ['POST', 'GET'])
def test():
  parametri = ["IQ", "augums", "izmers"]
    return render_template("test.html", parametri=parametri)

#Pārbaudes lapa, lai saprastu, ka kods vispār strādā
@app.route('/health')
def health():
  return "OK"

if __name__ == '__main__':
  app.run(debug="true")
