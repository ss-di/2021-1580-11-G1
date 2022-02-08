from flask import Flask, render_template, escape, abort, request, make_response

app = Flask(__name__)
# //app.register_error_handler('404.html', page_not_found)

class Items:
    def __init__(self, name='item', descr='some description', price=300, img="123.png") -> None:
        self.name = name
        self.descr = descr
        self.price = price
        self.image = img

class Feedback:
    def __init__(self, login, text):
        self.login = login
        self.text = text

ITEMS = [Items('Alexei', 'Kaput', '1945'), Items(),\
    Items('Новый товар', "Описание нового товара", 800, "panther.jpg"), Items(), Items(), Items(), Items(), Items(), Items(), Items('panther', "the most beautiful panther eva", 400, "shitty_panther_ytsv-p3.png")]
FEEDBACK = []

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def index():
    print("args:", request.args)
    name = request.cookies.get('username')
    if not name:
        name = "Не задано"
    return render_template('index.html', test = name)

@app.route('/about', methods=['GET', 'POST'])
def about():
    login = ''
    if request.method == 'POST':
        login = request.form.get('login')
        text = request.form.get('text')
        if login != '' and text != '':
            f = Feedback(login, text)
            FEEDBACK.append(f)
            
    resp = make_response(render_template('about.html', feedback=FEEDBACK))
    if login:
        resp.set_cookie('username', login)
    return resp

@app.route('/catalog')
def catalog():
    min_price = int(request.args.get('min_price', 0))
    max_price = int(request.args.get('max_price', 10e9))
    items = list(filter(lambda x: min_price <= int(x.price) <= max_price, ITEMS))
    return render_template('catalog.html', items=items)

@app.route('/item/<item>')
def show_item_profile(item):
    # show the user profile for that user
    item = escape(item)
    for thing in ITEMS:
        if thing.name == item:
            return render_template('item.html', item=thing)
    return abort(404, description="not found")

if __name__ == '__main__':
    app.run(debug=True)
