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
import os
import sys
import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
##############################################################

################# ADD UTILITY FUNCTIONS HERE #################


##############################################################
# initializing the pin numbers where motors are connected
L_PWM_PIN1 = 38
L_PWM_PIN2 = 40
R_PWM_PIN2 = 32
R_PWM_PIN1 = 33
ENA = 31
ENA1 =37

# declare motor pins as output pins
# motors get input from the PWM pins
def motor_pin_setup():
    global L_MOTOR1, L_MOTOR2, R_MOTOR1, R_MOTOR2,E1,E2
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(R_PWM_PIN1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(R_PWM_PIN2, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(L_PWM_PIN1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(L_PWM_PIN2, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(ENA, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(ENA1, GPIO.OUT, initial=GPIO.HIGH)

# setting initial PWM frequency for all 4 pins
    L_MOTOR1 = GPIO.PWM(L_PWM_PIN1, 100) 
    R_MOTOR1 = GPIO.PWM(R_PWM_PIN1, 100)
    L_MOTOR2 = GPIO.PWM(L_PWM_PIN2, 100)
    R_MOTOR2 = GPIO.PWM(R_PWM_PIN2, 100)
    E1 = GPIO.PWM(ENA, 100) 
    E2 = GPIO.PWM(ENA1, 100) 

    # setting initial speed (duty cycle) for each pin as 0
    L_MOTOR1.start(0)
    R_MOTOR1.start(0)
    L_MOTOR2.start(0)
    R_MOTOR2.start(0)

def left():
    L_MOTOR1.ChangeDutyCycle(100)
    R_MOTOR2.ChangeDutyCycle(100)
    print("left")

def right():
    L_MOTOR2.ChangeDutyCycle(100)
    R_MOTOR1.ChangeDutyCycle(100)
    print("right")

def straight():
    L_MOTOR1.ChangeDutyCycle(100)
    R_MOTOR1.ChangeDutyCycle(100)
    print("straight")


def wait():
    L_MOTOR1.ChangeDutyCycle(0)
    R_MOTOR1.ChangeDutyCycle(0)
    print("wait")
    motor_pause(5)
def motor_pause(secs):
    L_MOTOR1.ChangeDutyCycle(0)
    R_MOTOR1.ChangeDutyCycle(0)
    L_MOTOR2.ChangeDutyCycle(0)
    R_MOTOR2.ChangeDutyCycle(0)
    time.sleep(secs)
    print(motor_pause)


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

    ################## ADD YOUR CODE HERE	##################
    # client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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

    ################## ADD YOUR CODE HERE	##################
    message = client.recv(256).decode('utf-8')

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

    ################## ADD YOUR CODE HERE	##################
    msg = message.encode('utf-8')
    client.send(msg)

    ##########################################################

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
        # Set up new socket client and connect to a socket server
    try:
        client = setup_client(host, port)

    except socket.error as error:
        print("Error in setting up server")
        print(error)
        sys.exit()

    # Wait for START command from socket_server_rgb.pys
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
        if message == "LEFT":
            left()
            time.sleep(2)
            motor_pause(2)

        if message == "RIGHT":
            right()
            time.sleep(2)
            motor_pause(2)

        if message == "STRAIGHT":
            straight()
            time.sleep(2)
            motor_pause(2)

        if message == "WAIT_5":
            wait()
            time.sleep(2)

    print("maitrey")

