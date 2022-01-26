from flask import *

app = Flask(__name__)

a = 0

@app.route('/hello')
def hello():
    global a
    a += 1
    return f'''
    <html>
            <body>
                <h1>Здесь HTML разметка</h1>
                <p>Немного тектса тут и там</p>
                <p>{a}</p>
            </body>
        </html>
        '''

@app.route('/')
def main_page():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


app.run(debug=True)
