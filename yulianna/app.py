
from flask import Flask, url_for, Response, request

app = Flask(__name__)

bootstrap_css_link = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.3/css/bootstrap.min.css">'
bootstrap_js_link = '<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.3/js/bootstrap.bundle.min.js"></script>'

styles = """
<style>
    html, body {
        font-family: sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f9e8e8; 
        text-align: center; 
    }

    h1 {
        color: #333;
        font-weight: bold;
        font-size: 36px;
        margin-top: 50px;
    }

    p {
        color: #1455;
        font-size: 18px;
        margin-bottom: 20px; 
    }

    hr {
        border: 1px solid #ccc;
        width: 50%;
        margin: auto; 
        margin-bottom: 20px; 
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    ul li {
        display: inline;
        margin-right: 10px;
    }

    a {
        text-decoration: none;
        color: #007bff;
    }

    a:hover {
        color: #0056b3;
    }
</style>
"""


@app.route('/')
@app.route('/hi')
def hello_from_flask():
    return "Hello from Flask!"


@app.route('/bye')
def goodbye_from_flask():
    return "Goodbye from Flask!"


@app.route('/dynamic/<colour>')
def echo_colour_choice(colour):
    return f"you like {colour}"


@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello, {name}!'


# # @app.route('/page1/<name>')
# def simple_html_page(name):
#     return """
#     <!doctype>
#     <html>
#     <head>
#         <title>Page 1</title>
#     </head>
#     <body>
#         <h1>page 1</h1>
#         <p>hello{}!</p>
#     </body>
#     </html>
#     """.format(name)


@app.route('/page1/<name>')
def simple_html_page(name):
    home_url = url_for('hello_from_flask')
    return f"""
        ‹! doctype>
        <html>
        <head>
                ‹title>Page 1</title>
                {styles}
        </head>
        <body>
                <h1>Name Page</h1>
                ‹p>Hello {name}!</p>
                <hr>
                <a href="{home_url}">Home Page</a>
                </body>
        </html>"""


# @app.route('/page2')
# def about():
#     return """
#         <!doctype html>
#         <html>
#         <head>
#                 <title>Page 2</title>
#         </head>
#         <body>
#                 <h1>Page 2</h1>
#                 <p>This is Page 2.</p>
#                 <hr>
#                 <a href="/">Go back to Home Page</a>
#         </body>
#         </html>
#     """


@app.route('/home')
def home():
    home_url = url_for('home')
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
    {styles}
    {bootstrap_css_link}
</head>
<body>
    <h1>Welcome to Rivera Pearl!</h1>
    <p>Check out our pages:</p>
    <img src="https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.charleskeith.co.uk%2Fdw%2Fimage%2Fv2%2FBCWJ_PRD%2Fon%2Fdemandware.static%2F-%2FSites-ck-products%2Fdefault%2Fdw046eaf5a%2Fimages%2Fhi-res%2F2023-L6-CK2-50271205-J8-1.jpg%3Fsw%3D756%26sh%3D1008&tbnid=GQ4rJ5yos58cHM&vet=12ahUKEwju0P3ClpCFAxUYT6QEHef7BwQQMygaegUIARDeAw..i&imgrefurl=https%3A%2F%2Fwww.charleskeith.co.uk%2Fgb%2FCK2-50271205_NOIR.html&docid=VI--8Her8_ZvIM&w=756&h=1008&q=bag&client=safari&ved=2ahUKEwju0P3ClpCFAxUYT6QEHef7BwQQMygaegUIARDeAw" alt="Bag" style="width: 300px; height: 400px;">
    <ul class="nav">
        <li class="nav-item">
            <a class="nav-link" href="/about">About Us</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="/contact">Contact Us</a>
        </li>
        <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Products
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                <li><a class="dropdown-item" href="{url_for('product1', shop='Women', amount=10, product='Bag')}">Product 1</a></li>
                <li><a class="dropdown-item" href="{url_for('product2', shop='Women', amount=15, product='Bag')}">Product 2</a></li>
                <li><a class="dropdown-item" href="{url_for('product3', shop='Women', amount=20, product='Bag')}">Product 3</a></li>
            </ul>
            </ul>
        </li>
    </ul>
    {bootstrap_js_link}
</body>
</html>
"""


@app.route('/about')
def about():
    home_url = url_for('home')
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>About Rivera Pearl</title>
    {styles}
</head>
<body>
    <h1>About Us</h1>
    <p>We are a small team dedicated to providing the best fashion thats trending.</p>
    <a href="{home_url}">Back to Home</a>
    <a href="/contact">Contact Us</a>
</body>
</html>
"""


@app.route('/contact')
def contact():
    home_url = url_for('home')
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Contact Us</title>
    {styles}
</head>
<body>
    <h1>Contact Us</h1>
    <p>You can reach us via email at riverapearl@example.com or by phone at +123456789.</p>

    <ul class="nav">
        <li class="nav-item">
            <a class="nav-link" href="/home">Homepage</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="/about">About Us</a>
        </li>
    </ul>
</body>
</html>
"""


@app.route('/get/text')
def get_text():
    return Response("Hello from Flask using an explicit Response object", mimetype='text/plain')


@app.route('/post/text', methods=['POST'])
def post_text():
    data_sent = request.data.decode('utf-8')
    return Response("You posted this data to the Flask app: " + data_sent, mimetype='text/plain')


@app.route("/product1/<shop>/<int:amount>/<product>")
def product1(shop, amount, product):
    home_url = url_for('home')
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Product 1</title>
    {styles}
    {bootstrap_css_link}
</head>
<body>
    <h1>Product 1</h1>
    <p>Hello!</p>
    <p>You are searching for {product}, priced £{amount}.</p>
    <hr>
    <a href="{home_url}">Back to Home</a>
    <a href="{url_for('product2', shop= shop, amount=amount, product=product)}">Next</a>
</body>
</html>"""


@app.route("/product2/<shop>/<int:amount>/<product>")
def product2(shop, amount, product):
    home_url = url_for('home')
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Product 2</title>
    {styles}
    {bootstrap_css_link}
</head>
<body>
    <h1>Product 2</h1>
    <p>Hello !</p>
    <p>You are searching for {product}, priced £{amount}.</p>
    <hr>
    <a href="{home_url}">Back to Home</a>
    <a href="{url_for('product1', shop=shop, amount=amount, product=product)}">Back</a>
    <a href="{url_for('product3', shop=shop, amount=amount, product=product)}">Next</a>
</body>
</html>"""


@app.route("/product3/<shop>/<int:amount>/<product>")
def product3(shop, amount, product):
    home_url = url_for('home')
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Product 3</title>
    {styles}
    {bootstrap_css_link}
</head>
<body>
    <h1>Product 3</h1>
    <p>Hello!</p>
    <p>You are searching for {product}, priced £{amount}.</p>
    <hr>
    <ul class="list-group">
        <li class="list-group-item"><a href="{home_url}">Back to Home</a></li>
        <li class="list-group-item"><a href="{url_for('product1', shop=shop, amount=amount, product=product)}">Go to start</a></li>
        <li class="list-group-item"><a href="{url_for('product2', shop=shop, amount=amount, product=product)}">Back</a></li>
    </ul>
</body>
</html>"""


if __name__ == "__main__":
    app.run(debug=True)
