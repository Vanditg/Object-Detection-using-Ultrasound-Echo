import time
import RPi.GPIO as GPIO

# Use BCM GPIO references

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define GPIO to use on Pi
GPIO_TRIGGER = 38
GPIO_ECHO    = 40

print "Ultrasonic Measurement"

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  
GPIO.setup(GPIO_ECHO,GPIO.IN)     
 
# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)

time.sleep(1)


GPIO.output(GPIO_TRIGGER, True)

time.sleep(0.00001)

GPIO.output(GPIO_TRIGGER, False)

start = time.time()

while GPIO.input(GPIO_ECHO)==0:
  start = time.time()

while GPIO.input(GPIO_ECHO)==1:
  stop = time.time()

elapsed = stop-start

distance = elapsed * 34300

distance = distance / 2

print "Distance : %.1f" % distance

GPIO.cleanup()
