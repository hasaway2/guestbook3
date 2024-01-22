from flask import Flask, render_template, request, redirect

import dao

app = Flask(__name__)

@app.route("/")
def list():
  result = dao.findall()
  return render_template("list.html", list=result)

@app.route("/read")
def read():
  gno = request.args.get('gno', type=int)
  result = dao.findone(gno)
  print(result)
  return render_template("read.html", guest=result)

@app.route("/write", methods=['post'])
def write():
  writer = request.form.get('writer', type=str)
  content = request.form.get('content', type=str)
  dao.save(writer=writer, content=content)
  return redirect("/")

@app.route("/update", methods=['post'])
def update():
  gno = request.form.get('gno', type=int)
  content = request.form.get('content', type=str)
  dao.update(gno=gno, content=content)
  return redirect("/")

@app.route("/delete", methods=['post'])
def delete():
  gno = request.form.get('gno', type=int)
  dao.delete(gno=gno)
  return redirect("/")

app.run(debug=True)
