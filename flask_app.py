from flask import Flask, render_template, redirect, url_for, request
from requests import post,get

app = Flask(__name__)

@app.route('/')
@app.route('/inicio')
def home():
    return render_template('index.html')

@app.route('/demo',methods=['POST','GET'])
def compra():
  if request.method=='POST':
    dados = post("https://api-model-simple.juanengml.repl.co/covid_mask").json()
    return dados['ibm_mode']

  return   render_template('demo.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')