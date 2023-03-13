import paho.mqtt.client as mqtt
import numpy as np
import time

def Step(temp):
# Loop through each angle value, each iteration lasts 0.05 seconds
    for i in range(len(theta1)):
        start_time = time.time()
        msg = '('+ str(theta1[i]) + ',' + str(theta2[i]) + ')'
        # Send the angles in the correct format to the broker
        temp.publish(topic,msg)
        
        if i % 20 == 0:
            # Publish to the adafruit dashboard once every second to avoid throttle limits
            client.publish("abeckett/feeds/theta1", theta1[i])
            client.publish("abeckett/feeds/theta2", theta2[i])
            print(msg)

        while (time.time() - start_time < 0.05):
            #wait until 0.05 seconds have passed
            x = 'I need something in the while loop'

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("abeckett/feeds/button")

def on_message(client, userdata, msg):
    print(str(msg.payload))
    # When the button is pressed on the adafruit dashboard
    if str(msg.payload) == "b'1'":
        # Call the function to move the motors
        Step(temp)
    

address = '10.247.55.238'
# MQTT topics
topic = 'angles' 

# Set up adafruit MQTT
client = mqtt.Client()
client.username_pw_set("abeckett", "aio_cIeN07Ks3ypfJP1C1iM2UPJIUYnQ")

# Load in angles calculated in Matlab
theta1 = np.genfromtxt('/Users/aidanbeckett/Downloads/ME35_21-main/SampleCodes/Motor Carrier/angles1.csv', delimiter=',')
theta2 = np.genfromtxt('/Users/aidanbeckett/Downloads/ME35_21-main/SampleCodes/Motor Carrier/angles2.csv', delimiter=',')
theta1 = 180 * theta1 / np.pi
theta2 = 180 * theta2 / np.pi

# Initialize connection with mqtt broker
temp = mqtt.Client('Aidan')
temp.connect(address)
client.connect("io.adafruit.com", 1883, 60) # adafuit.io
client.on_connect = on_connect
client.on_message = on_message
client.connect("io.adafruit.com", 1883, 60)
client.loop_forever()
