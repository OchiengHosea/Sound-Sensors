import RPi.GPIO as GPIO
import time

#GPIO SETUP
sound = 6
led = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(sound, GPIO.IN)
# GPIO.setup(led,GPIO.OUT)
def callback(sound):
        if GPIO.input(sound):
            print("Sound Detected!")
            # GPIO.output(led,HIGH)
        else:
            print("No sound Detected!")
		    # GPIO.output(led,LOW)
      

GPIO.add_event_detect(sound, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(sound, callback)  # assign function to GPIO PIN, Run function on change

while True:
    time.sleep(1)