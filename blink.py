import time
try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(10,GPIO.OUT)
    p = GPIO.PWM(10,1)
    p.start(0)
    while 1:
        for dc in range(0,101,5):
            p.ChangeDutyCycle(100)
            time.sleep(0.1)
        for dc in range(100,-1,-5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
