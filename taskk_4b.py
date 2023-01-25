'''
*****************************************************************************************
*
*        		===============================================
*           		Pharma Bot (PB) Theme (eYRC 2022-23)
*        		===============================================
*
*  This script is to implement Task 3D of Pharma Bot (PB) Theme (eYRC 2022-23).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''

# Team ID:			[ Team-ID ]
# Author List:		[ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:			socket_client_rgb.py
# Functions:		
# 					[ Comma separated list of functions in this file ]

####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv)                    ##
##############################################################
import socket
import time
import os, sys
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
##############################################################

################# ADD UTILITY FUNCTIONS HERE #################


##############################################################
# initializing the pin numbers where motors are connected
L_PWM_PIN1 = 13
L_PWM_PIN2 = 19
R_PWM_PIN2 = 32
R_PWM_PIN1 = 33
ENA = 31
ENA1 =37
# declare motor pins as output pins
# motors get input from the PWM pins
def motor_pin_setup():
    global L_MOTOR1, L_MOTOR2, R_MOTOR1, R_MOTOR2
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(R_PWM_PIN1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(R_PWM_PIN2, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(L_PWM_PIN1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(L_PWM_PIN2, GPIO.OUT, initial=GPIO.HIGH)
    # setting initial PWM frequency for all 4 pins
    L_MOTOR1 = GPIO.PWM(L_PWM_PIN1, 100) 
    R_MOTOR1 = GPIO.PWM(R_PWM_PIN1, 100)
    L_MOTOR2 = GPIO.PWM(L_PWM_PIN2, 100)
    R_MOTOR2 = GPIO.PWM(R_PWM_PIN2, 100) 
    
    # setting initial speed (duty cycle) for each pin as 0
    L_MOTOR1.start(0)
    R_MOTOR1.start(0)
    L_MOTOR2.start(0)
    R_MOTOR2.start(0)
    

def left():
    L_MOTOR1.ChangeDutyCycle(100)
    R_MOTOR2.ChangeDutyCycle(100)


def right():
    L_MOTOR2.ChangeDutyCycle(100)
    R_MOTOR1.ChangeDutyCycle(100)

def straight():
    L_MOTOR1.ChangeDutyCycle(100)
    R_MOTOR1.ChangeDutyCycle(100)

def wait():
    L_MOTOR1.ChangeDutyCycle(0)
    R_MOTOR1.ChangeDutyCycle(0)
    motor_pause(50)



def setup_client(host, port):

	"""
	Purpose:
	---
	This function creates a new socket client and then tries
	to connect to a socket server.

	Input Arguments:
	---
	`host` :	[ string ]
			host name or ip address for the server

	`port` : [ string ]
			integer value specifying port name
	Returns:

	`client` : [ socket object ]
			   a new client socket object
	---

	
	Example call:
	---
	client = setup_client(host, port)
	""" 

	client = None

	##################	ADD YOUR CODE HERE	##################
	#client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	print(client)
	print(host, port)
	client.connect((host, port))

	

	##########################################################

	return client

def receive_message_via_socket(client):
	"""
	Purpose:
	---
	This function listens for a message from the specified
	socket connection and returns the message when received.

	Input Arguments:
	---
	`client` :	[ socket object ]
			client socket object created by setup_client() function
	Returns:
	---
	`message` : [ string ]
			message received through socket communication
	
	Example call:
	---
	message = receive_message_via_socket(connection)
	"""

	message = None

	##################	ADD YOUR CODE HERE	##################
	message=client.recv(256).decode('utf-8')



	##########################################################

	return message

def send_message_via_socket(client, message):
	"""
	Purpose:
	---
	This function sends a message over the specified socket connection

	Input Arguments:
	---
	`client` :	[ socket object ]
			client socket object created by setup_client() function

	`message` : [ string ]
			message sent through socket communication

	Returns:
	---
	None
	
	Example call:
	---
	send_message_via_socket(connection, message)
	"""

	##################	ADD YOUR CODE HERE	##################
	msg=message.encode('utf-8')
	client.send(msg)


	##########################################################

def rgb_led_setup():
	"""
	Purpose:
	---
	This function configures pins connected to rgb led as output and
	enables PWM on the pins 

	Input Arguments:
	---
	You are free to define input arguments for this function.

	Returns:
	---
	You are free to define output parameters for this function.
	
	Example call:
	---
	rgb_led_setup()
	"""

	##################	ADD YOUR CODE HERE	##################
	redPin = 24
	greenPin = 5
	bluePin = 18

	# ENA =31
	# ENA =37
	global r,g,b
#	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(redPin,GPIO.OUT,initial=GPIO.LOW)
	GPIO.setup(greenPin,GPIO.OUT,initial=GPIO.LOW)
	GPIO.setup(bluePin,GPIO.OUT,initial=GPIO.LOW)

	# GPIO.setup(R_PWM_PIN, GPIO.OUT, initial=GPIO.HIGH)
	r=GPIO.PWM(redPin, 100)
	g=GPIO.PWM(greenPin, 100)
	b=GPIO.PWM(bluePin, 100)

#	# e=GPIO.PWM(R_PWM_PIN, 100)

	r.start(0)
	b.start(0)
	g.start(0)
    #return r,g,b
#    print("hello")
	
	##########################################################
	
def rgb_led_set_color(color):
	"""
	
	---
	This function takes the color as input and changes the color of rgb led
	connected to Raspberry Pi 

	Input Arguments:
	---

	`color` : [ string ]
			color detected in QR code communicated by server
	
	You are free to define any additional input arguments for this function.

	Returns:
	---
	You are free to define output parameters for this function.
	
	Example call:
	---
	rgb_led_set_color(color)
	"""    

	##################	ADD YOUR CODE HERE	##################
	time.sleep(1)
# 	print("------------------------------------------------")
	if color == 'Red':
		r.ChangeDutyCycle(100)
		g.ChangeDutyCycle(0)
		b.ChangeDutyCycle(0)
# 
# 		GPIO.output(redPin,GPIO.LOW)
# 		GPIO.output(greenPin,GPIO.HIGH)
# 		GPIO.output(bluePin,GPIO.HIGH)
	if color == 'Green':

		r.ChangeDutyCycle(0)
		g.ChangeDutyCycle(100)
		b.ChangeDutyCycle(0)

# 		
# 		GPIO.output(redPin,GPIO.LOW)
# 		GPIO.output(greenPin,GPIO.HIGH)
# 		GPIO.output(bluePin,GPIO.LOW)

	if color == 'Blue':
# 		print("blue")
		r.ChangeDutyCycle(0)
		g.ChangeDutyCycle(0)
		b.ChangeDutyCycle(100)
# 
# 		GPIO.output(redPin,GPIO.LOW)
# 		GPIO.output(greenPin,GPIO.LOW)
# 		GPIO.output(bluePin,GPIO.HIGH)


	if color == 'Orange':
# 		print("orange")
		r.ChangeDutyCycle(100)
		g.ChangeDutyCycle(13.7)
		b.ChangeDutyCycle(0)

# 		GPIO.output(redPin,GPIO.HIGH)
# 		GPIO.output(greenPin,GPIO.LOW)
# 		GPIO.output(bluePin,GPIO.HIGH)

  
	if color == 'Sky Blue':
# 		print("skyblue")
		r.ChangeDutyCycle(0)
		g.ChangeDutyCycle(100)
		b.ChangeDutyCycle(100)
# 
# 		GPIO.output(redPin,GPIO.HIGH)
# 		GPIO.output(greenPin,GPIO.HIGH)
# 		GPIO.output(bluePin,GPIO.HIGH)

	if color == 'Pink':
# 		print("pink")
		r.ChangeDutyCycle(100)
		g.ChangeDutyCycle(0)
		b.ChangeDutyCycle(47.84)

# 		GPIO.output(redPin,GPIO.HIGH)
# 		GPIO.output(greenPin,GPIO.HIGH)
# 		GPIO.output(bluePin,GPIO.LOW)





	
	##########################################################

if __name__ == "__main__":

		host = "10.25.2.249"
		port = 5050
# 
# 		## 
# 		redPin = 24
# 		gndPin = 23
# 		greenPin = 5
# 		bluePin = 18
# 
# 		## PWM values to be set for rgb led to display different colors
# 		pwm_values = {"Red": (255, 0, 0), "Blue": (0, 0, 255), "Green": (0, 255, 0), "Orange": (255, 35, 0), "Pink": (255, 0, 122), "Sky Blue": (0, 100, 100)}
# 
# 
# 		## Configure rgb led pins
# 		rgb_led_setup()
# 
# 
		## Set up new socket client and connect to a socket server
		try:
			client = setup_client(host, port)


		except socket.error as error:
			print("Error in setting up server")
			print(error)
			sys.exit()

		## Wait for START command from socket_server_rgb.pys
		message = receive_message_via_socket(client)
		if message == "START":
			print("\nTask 3D Part 3 execution started !!")
        motor_pin_setup()

		while True:
			## Receive message from socket_server_rgb.py
			message = receive_message_via_socket(client)

			## If received message is STOP, break out of loop
			if message == "STOP":
				print("\nTask 3D Part 3 execution stopped !!")
				break
			else:
				print("Color received: " + message)
			if message == "LEFT"
                left()
			if message == "RIGHT"
                right()
			if message == "STRAIGHT"
                straight()
			if message == "WAIT_5"
                wait()
            
# 				rgb_led_set_color(message)
		


