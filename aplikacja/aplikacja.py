from flask import Flask, render_template
app = Flask(__name__)
import ConfigParser


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

    app.run(host='0.0.0.0', port=naszconfig['port'])
