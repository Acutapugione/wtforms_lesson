from .. application import app
from .. forms import MyForm
from flask import render_template


@app.route("/", methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        print("Form validated and submitted")
    return render_template("index.html", form=form)