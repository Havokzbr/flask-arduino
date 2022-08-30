#from arduino import Arduino
from flask import Flask, render_template
import datetime

'''
O código fonte a seguir implementará ao servidor web, conforme requisição recebida do navegador, alterar o estado de on/off do LED.
'''

LED = 13
estado = {'led' : False}

app = Flask(__name__)

@app.route('/')
def inicio():
    return mostrar_estado()

@app.route('/led/1')
def ligar_led():
    arduino = Arduino()
    arduino.digital(LED, 1) # Arduino, escreva HIGH(1) ou ligue o LED
    estado['led'] = True
    return mostrar_estado

@app.route('/led/0')
def desl_led():
    arduino = Arduino()
    arduino.digital(LED, 0) # Arduino, escreva HIGH(0) ou desliguei o LED
    estado['led'] = False
    return mostrar_estado

def mostrar_estado():
    return render_template('control_led.html', **estado)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)