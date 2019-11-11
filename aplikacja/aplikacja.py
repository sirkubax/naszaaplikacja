from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    #return "Dzien dobry!"
    zmienne = { 'aaa': 'kropeczka' }
    return render_template('index.html', zmienne=zmienne)

@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return '''
    <html>
        <head>
            <title>Home Page - Microblog</title>
        </head>
        <body>
            <h1>Hello, ''' + user['username'] + '''!</h1>
        </body>
    </html>'''


if __name__ == "__main__":
    app.run()
