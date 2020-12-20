from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/shop-details")
def shopdetais():
    return render_template("shop-details.html")


@app.route("/shop")
def Shop():
    return render_template("shop.html")


@app.route("/shopping-cart")
def shopppingcart():
    return render_template("shopping-cart.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/checkout")
def checkout():
    return render_template("checkout.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/blog-details")
def blogdetail():
    return render_template("blog-details.html")


app.run(debug=True)
