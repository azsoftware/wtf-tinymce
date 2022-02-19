from flask import Flask, render_template, flash
from werkzeug.utils import redirect
from wtf_tinymce import wtf_tinymce

from forms import ExampleForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "dummy_secret"

# Init wtf-tinymce
wtf_tinymce.init_app(app)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/submit", methods=["GET", "POST"])
def submit():
    form = ExampleForm()
    if form.validate_on_submit():
        flash("Successfully submitted")
        return redirect("/")
    return render_template("submit.html", form=form)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
