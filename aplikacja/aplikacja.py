from flask import Flask, render_template
app = Flask(__name__)
import ConfigParser
from flask.ext.mysql import MySQL

@app.route("/db/zapisz/<zmienna>/<wartosc>")
def zapisz(zmienna, wartosc):
    return '''
    <html>
        <head>
            <title>Home Page - Microblog</title>
        </head>
        <body>
            <h1>''' + zmienna + ': ' + wartosc + '''!</h1>
        </body>
    </html>'''

@app.route("/db/pobierz/<zmienna>")
def pobierz(zmienna):
    return '''
    <html>
        <head>
            <title>Home Page - Microblog</title>
        </head>
        <body>
            <h1>''' + zmienna + ''' db communication in development!</h1>
        </body>
    </html>'''


@app.route("/")
def main():
    #return "Dzien dobry!"
    zmienne = { 'aaa': 'kropeczka', 'kolejny_parametr': 1234567 }
    return render_template('index.html', zmienne=zmienne)


@app.route('/index')
def index():
    naszconfig = read_config()
    user = {'username': naszconfig['nazwa']}
    return '''
    <html>
        <head>
            <title>Home Page - Microblog</title>
        </head>
        <body>
            <h1>Hello, ''' + user['username'] + '''!</h1>
        </body>
    </html>'''


def read_config():
    import os
    current_file = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file)
    print (current_dir)
    naszconfig = {}
    config = ConfigParser.ConfigParser()
    try:
        config.read(os.path.join(current_dir, 'config.cfg'))
        print ('czytam konfiguracje glowna')
        port = config.get('config', 'port')
    except:
        print ('czytam konfiguracje przykladowa')
        config.read(os.path.join(current_dir, 'config.cfg.example'))
    naszconfig['port'] = config.get('config', 'port')
    naszconfig['nazwa'] = config.get('config', 'nazwa')
    return naszconfig



if __name__ == "__main__":

    naszconfig = read_config()

    mysql = MySQL()
     
    # MySQL configurations
    app.config['MYSQL_DATABASE_USER'] = 'jay'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'jay'
    app.config['MYSQL_DATABASE_DB'] = 'BucketList'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    #mysql.init_app(app)
    #conn = mysql.connect()

    #cur = mysql.connection.cursor()
    #cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
    #mysql.connection.commit()
    #cur.close()

    app.run(host='0.0.0.0', port=naszconfig['port'])
