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
# Filename:			socket_server_rgb.py
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
from zmqRemoteApi import RemoteAPIClient
import traceback
import zmq
import numpy as np
import cv2
from pyzbar.pyzbar import decode
##############################################################

################# ADD UTILITY FUNCTIONS HERE #################

def read_qr_code(sim):
	"""
	Purpose:
	---
	This function detects the QR code present in the CoppeliaSim vision sensor's 
	field of view and returns the message encoded into it.

	Input Arguments:
	---
	`sim`    :   [ object ]
		ZeroMQ RemoteAPI object

	Returns:
	---
	`qr_message`   :    [ string ]
		QR message retrieved from reading QR code

	Example call:
	---
	control_logic(sim)
	"""
	qr_message = None
	
	##############  ADD YOUR CODE HERE  ##############
	m=sim.getObject("/vision_sensor")
	## Retrieve the handle of the Arena_dummy scene object.
	# e=sim.getObject("/left_joint")
	# r=sim.getObject("/right_joint")
	# sim.setJointTargetVelocity(e,0)
	# sim.setJointTargetVelocity(r,0)
	arena_dummy_handle = sim.getObject("/PB_Arena") 

	## Retrieve the handle of the child script attached to the Arena_dummy scene object.
	childscript_handle = sim.getScript(sim.scripttype_childscript, arena_dummy_handle, "")

	## Call the activate_qr_code() function defined in the child script to make the QR code visible at checkpoint E
	sim.callScriptFunction("activate_qr_code", childscript_handle, "checkpoint E")

	img1, resX, resY = sim.getVisionSensorCharImage(m)
	# print(type(resX))
	# resX=resX-20
	# print(resX)
	img1 = np.frombuffer(img1, dtype=np.uint8).reshape(resY, resX, 3)
	img1 = cv2.flip(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB), 0)
	# print(img.shape)
	img1=img1[0:512,70:442]
	# cv2.imshow('maitrey',img1)
	# print("{{{{{{{{{{{{{{{{{{{{{br")
	qr_message=decode(img1)
	# qr_message=d.data.decode('utf-8')
	#print("***************************************************",qr_message)

	##################################################

	return qr_message


def setup_server(host, port):

	"""
	Purpose:
	---
	This function creates a new socket server and then binds it 
	to a host and port specified by user.

	Input Arguments:
	---
	`host` :	[ string ]
			host name or ip address for the server

	`port` : [ int ]
			integer value specifying port number
	Returns:

	`server` : [ socket object ]
	---

	
	Example call:
	---
	server = setup_server(host, port)
	""" 

	server = None

	##################	ADD YOUR CODE HERE	##################
	server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((host, port))

	##########################################################

	return server

def setup_connection(server):
	"""
	Purpose:
	---
	This function listens for an incoming socket client and
	accepts the connection request

	Input Arguments:
	---
	`server` :	[ socket object ]
			socket object created by setupServer() function
	Returns:
	---
	`connection` : [ socket object ]
	        socket connection object

	`address` : [ tuple ]
	        address of socket connection
	
	Example call:
	---
	connection, address = setup_connection(server)
	"""
	connection = None
	address = None

	##################	ADD YOUR CODE HERE	##################
	# print("jjjj")
	server.listen()
	# while True:
	connection, address = server.accept()
	

	##########################################################

	return connection, address

def receive_message_via_socket(connection):
	"""
	Purpose:
	---
	This function listens for a message from the specified
	socket connection and returns the message when received.

	Input Arguments:
	---
	`connection` :	[ connection object ]
			connection object created by setupConnection() function
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
	message=connection.recv(64).decode('utf-8')


	##########################################################

	return message

def send_message_via_socket(connection, message):
	"""
	Purpose:
	---
	This function sends a message over the specified socket connection

	Input Arguments:
	---
	`connection` :	[ connection object ]
			connection object created by setupConnection() function

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
	connection.send(msg)



	##########################################################

if __name__ == "__main__":
	
	host = ''
	port = 5050


	## Set up new socket server
	try:
		server = setup_server(host, port)

		# print(type(server))

	except socket.error as error:
		print("Error in setting up server")
		print(error)
		sys.exit()


	## Set up new connection with a socket client (PB_task3d_socket.exe)
	try:
		print("\nPlease run PB_task3d_socket.exe program and choose Part 3")
		connection_1, address_1 = setup_connection(server)
		print("Connected to: " + address_1[0] + ":" + str(address_1[1]))

	except KeyboardInterrupt:
		sys.exit()

	## Set up new connection with a socket client (socket_client_rgb.py)
	try:
		print("\nPlease run socket_client_rgb.py program")
		connection_2, address_2 = setup_connection(server)
		print("Connected to: " + address_2[0] + ":" + str(address_2[1]))

	except KeyboardInterrupt:
		sys.exit()

	
	## Send START command to both socket clients to start Task execution
	send_message_via_socket(connection_1, "START")
	send_message_via_socket(connection_2, "START")

	time.sleep(5)

	## Connect to CoppeliaSim by initialising a ZMQ CoppeliaSim client
	client = RemoteAPIClient()
	sim = client.getObject('sim')

	## Receive commands from PB_Task3d_socket.exe in a continuous while loop
	while True:
		## Receive commands from PB_Task3d_socket.exe
		message = receive_message_via_socket(connection_1)

		## If received command is "READ_QR"
		if message == "READ_QR":
			## Read the color encoded in QR code in CoppeliaSim using vision sensor
			color = read_qr_code(sim)
			## Print color read by read_qr_code() function
			print("QR details read: ", color)
			## Transmit the color read by read_qr_code() to both socket 
			## clients (PB_task3d_socket.exe and socket_client_rgb.py)
			send_message_via_socket(connection_2, color)
			send_message_via_socket(connection_1, color)
			pass

		## If received command from PB_Task3d_socket.exe is "STOP"
		elif message == "STOP":
			
			## Transmit STOP command to socket_client_rgb.py
			send_message_via_socket(connection_2, "STOP")

			## Close connections with both socket clients
			connection_1.close()
			connection_2.close()

			# Close server
			server.close()
			print("\nSocket Connections closed !!")
			print("Task 3D Part 3 execution stopped !!")
			break
		else:
			pass

