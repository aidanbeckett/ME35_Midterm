# ME35_Midterm

# legpath.py calculates and plots the possible paths of the leg

# sendangles.py waits for the press of the button at https://io.adafruit.com/abeckett/dashboards/me35-midterm 
# and then sends the angles in theta1.csv and theta2.csv to the mqqt broker.

# drawtwin.py can be run simultaneously to sendangles.py; it subscribes to the mqtt broker and plots the current
# position of each leg link

# InverseKinematics.m is pretty self explanatory in my humble opinion. The two accompanying csv files are the 
# x and y valuesof the path.
