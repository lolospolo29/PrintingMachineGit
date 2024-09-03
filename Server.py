from flask import Flask, request

# rom Classes import AlertSignal, TradeSignal

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def receive_signal():
    # AlertSignal.reset_countdown()  # Countdown zurücksetzen
    json_string = request.data.decode('utf-8')

    print(json_string)

    # TradeSignal.order_signal(json_string)

    return f'Received Analyse data: {json_string}'


@app.route('/startcountdown', methods=['POST'])
def startcountdown():
    # AlertSignal.start_Alert_Thread()  # Countdown zurücksetzen
    json_string = request.data.decode('utf-8')
    return f'Received Analyse data: {json_string}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

# API Secrets
# Name : DemoApiKey
# Api Key : Ifp91Iy8fOY6x22bVG
# Secret: eagubhmZG5nY0gbycEeJNGR50GuT5YnpZA37
