from flask import Flask,render_template,redirect,request

app = Flask(__name__)

TODOS=[]

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST": #take input from html form
        desc = request.form["desc"]
        date = request.form["date"]
        num=len(TODOS)+1
        todo = {"num":num,"desc":desc,"date":date}
        TODOS.append(todo)
        return redirect("/")
    else:
        return render_template('base.html',todos=TODOS)


if(__name__=="__main__"):
    app.run(debug=True)