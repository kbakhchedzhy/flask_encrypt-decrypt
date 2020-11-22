from flask import Flask, render_template, request
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)


app = Flask(__name__)


@app.route('/encrypt')
def encrypt():
    """
    Require parameter for encrypt
    :return: encrypted string
    """
    param = request.args.get('param', '')
    token = f.encrypt(param.encode()).decode()
    return render_template('index.html', param=token, text="Encrypted")


@app.route('/decrypt')
def decrypt():
    """
    Require encrypted parameter for decrypt
    :return: decrypted string
    """
    param = request.args.get('param', '')
    token = f.decrypt(param.encode()).decode()
    return render_template('index.html', param=token, text="Decrypted")


app.run(debug=True)
