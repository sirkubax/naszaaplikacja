from flask import Flask, render_template
app = Flask(__name__)
import ConfigParser

naszconfig = {}

@app.route("/")
def main():
    #return "Dzien dobry!"
    zmienne = { 'aaa': 'kropeczka', 'kolejny_parametr': 1234567 }
    return render_template('index.html', zmienne=zmienne)


@app.route('/index')
def index():
    global naszconfig
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
    global naszconfig
    config = ConfigParser.ConfigParser()
    try:
        config.read('config.cfg')
        print ('czytam konfiguracje glowna')
        port = config.get('config', 'port')
    except:
        print ('czytam konfiguracje przykladowa')
        config.read('config.cfg.example')
    naszconfig['port'] = config.get('config', 'port')
    naszconfig['nazwa'] = config.get('config', 'nazwa')
    print naszconfig



if __name__ == "__main__":

    read_config()

    app.run(host='0.0.0.0', port=naszconfig['port'])
