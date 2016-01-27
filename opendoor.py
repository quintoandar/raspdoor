import wiringpi2
import time

def open():
    io = wiringpi2.GPIO(wiringpi2.GPIO.WPI_MODE_PINS)
    io.pinMode(23,io.OUTPUT)
    io.digitalWrite(23,io.HIGH)
    time.sleep (0.2)
    io.digitalWrite(23,io.LOW)
    
if __name__ == "__main__":
    open()