import RPi.GPIO as GPIO
import time

LED_PIN = [18, 23, 24, 25, 8]  

try:
    # 1. Configurar modo de numeración BCM
    GPIO.setmode(GPIO.BCM)
    # 2. Desactivar advertencias (opcional)
    GPIO.setwarnings(False)
    # 3. Configurar pines como salida
    for led in LED_PIN:
        GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)
    print("Control de LEDs iniciado (Modo BCM)")
    print(f"Usando GPIOs: {LED_PIN}")
    print("Presiona Ctrl+C para salir")

    # 4. Loop principal 
    while True:
        
        for led in LED_PIN:
            GPIO.output(led, GPIO.HIGH)
            print(f"LED GPIO {led} ENCENDIDO")
            time.sleep(1)
            GPIO.output(led, GPIO.LOW)
            print(f"LED GPIO {led} APAGADO")
            time.sleep(1)

        for led in reversed(LED_PIN):
            GPIO.output(led, GPIO.HIGH)
            print(f"LED GPIO {led} ENCENDIDO")
            time.sleep(1)
            GPIO.output(led, GPIO.LOW)
            print(f"LED GPIO {led} APAGADO")
            time.sleep(1)

except KeyboardInterrupt:
    print("\nPrograma interrumpido por el usuario")
finally:
    # 5. Limpieza - Restaurar pines a estado seguro
    GPIO.cleanup()
    print("GPIO limpiado. Programa finalizado.")