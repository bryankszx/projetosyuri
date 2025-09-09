from machine import Pin, time_pulse_us
import time

PIN_TRIG = 25
PIN_ECHO = 27
PIN_LED = 26

trig = Pin(PIN_TRIG, Pin.OUT)
echo = Pin(PIN_ECHO, Pin.IN)
led = Pin(PIN_LED, Pin.OUT)

def obter_distancia():
    trig.value(0)
    time.sleep_us(2)

    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    duracao = time_pulse_us(echo, 1, 30000)

    if duracao < 0:
        return None

    distancia = (duracao / 2) * 0.0343
    return distancia

while True:
    detectar = obter_distancia()

    if detectar is None:
        print("Erro na leitura do sensor.")
        led.value(0)
    else:
        print("Distância:", round(detectar, 2), "cm")

        if detectar <= 10:
            print("Objeto Detectado!")
            led.value(1)
            time.sleep(1)
        else:
            print("Nenhum Objeto Detectado.")
            led.value(0)

    time.sleep(3)