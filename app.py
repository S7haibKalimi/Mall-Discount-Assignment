from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")


@app.route("/discount", methods = ['POST'])
def operation():
    operation = request.form['operation']
    price1 = int(request.form['price1'])
    price2 = int(request.form['price2'])
    price3 = int(request.form['price3'])
    price4 = int(request.form['price4'])
    total = price1 + price2 + price3 + price4

    if total <= 1000:
        discount = (10/100)*total
        result = total - discount

    elif total > 1000 and total <= 2000:
        discount = (20/100)*total
        result = total - discount

    else:
        discount = (30/100)*total
        result = total - discount
    
    return render_template("result.html", result = result)

if __name__=="__main__":
    app.run(host="0.0.0.0", port = 5000)
