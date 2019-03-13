from flask import Flask, render_template, request
app=Flask("eat-my-diet")

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/yummy_entrees")
def ye():
    return render_template("yummy_entrees.html")
@app.route("/healthy_lunches")
def hl():
    return render_template("healthy_lunches.html")
@app.route("/delicious_deserts")
def dd():
    return render_template("delicious_deserts.html")
@app.route("/students")
def students():
    return render_template("students.html")

@app.route('/')
def hello(name=None):
    return render_template('index.html', name=name)


@app.route("/feedback", methods=["POST"])
def get_feeback():
    # request.values is a dictionary holding any
    # POST request data that's not already part of the URL
    data = request.values

    return render_template("feedback.html", form_data=data)



app.run(debug=True)
