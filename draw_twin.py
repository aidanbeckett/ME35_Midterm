import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import numpy as np
import time

address = '10.247.55.238'
# MQTT topics
tell = 'Aidan/angles' 
listen = 'Aidan/listen'

# Initialize connection with mqtt broker
temp = mqtt.Client('ReadAngle')
temp.connect(address)

# Set constants
L1 = 7
L2 = 13

def draw_twin(who,user,message):
    ang_str = message.payload.decode()
    #decode changes from binary to ascii string

    # Assuming the angles arrive in a '(theta1,theta2)' format, convert the string to an array of radians
    angles = np.pi * np.array(eval(ang_str)) / 180
    print(angles)
    
    # Use forward kinematics to calculate position of each leg
    leg1x = [0, L1*np.cos(angles[0])]
    leg1y =[0, L1*np.sin(angles[0])]
    leg2x = [L1*np.cos(angles[0]), L1*np.cos(angles[0]) + L2*np.cos(angles[1])]
    leg2y =[L1*np.sin(angles[0]), L1*np.sin(angles[0]) + L2*np.sin(angles[1])]

    # Plot the two legs to creat the digital twin
    plt.clf() #clear figure
    plt.plot(leg1x, leg1y)
    plt.plot(leg2x, leg2y)

    plt.show()


temp.on_message = draw_twin

temp.loop_start()
temp.subscribe(tell)

time.sleep(15)
temp.loop_stop()
temp.disconnect()
