from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return('Main page')


@app.route('/procesingEndpoint', methods=['GET', 'POST'])
def webhook():
    a = 2  # Ingresar número entero
    b = 6  # Ingresar número entero
    id = request.args.get(a)
    monto = request.args.get(b)
    x = a*b/4
    return jsonify(str({'Success': 'Ok', 'total': x}))


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
