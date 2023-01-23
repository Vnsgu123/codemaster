'''
*****************************************************************************************
*
*        		     ===============================================
*           		       Pharma Bot (PB) Theme (eYRC 2022-23)
*        		     ===============================================
*
*  This script contains all the past implemented functions of Pharma Bot (PB) Theme 
*  (eYRC 2022-23).
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''

# Team ID:			[ Team-ID ]
# Author List:		[ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:			PB_theme_functions.py
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
import json
##############################################################

################# ADD UTILITY FUNCTIONS HERE #################


##############################################################


################## ADD SOCKET COMMUNICATION ##################
####################### FUNCTIONS HERE #######################
"""
Add functions written in Task 3D for setting up a Socket
Communication Server in this section
"""

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

	`port` : [ string ]
			integer value specifying port name
	Returns:

	`server` : [ socket object ]
	---

	
	Example call:
	---
	server = setupServer(host, port)
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
	`server` : [ socket object ]
	
	Example call:
	---
	connection = setupConnection(server)
	"""
	connection = None
	address = None

	##################	ADD YOUR CODE HERE	##################
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

##############################################################
##############################################################

######################### ADD TASK 2B ########################
####################### FUNCTIONS HERE #######################
"""
Add functions written in Task 2B for reading QR code from
CoppeliaSim arena in this section
"""

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
	qr_message = None
	##############  ADD YOUR CODE HERE  ##############
	## Retrieve the handle of the Arena_dummy scene object.
	# e=sim.getObject("/left_joint")
	# r=sim.getObject("/right_joint")
	# sim.setJointTargetVelocity(e,0)
	# sim.setJointTargetVelocity(r,0)
	# arena_dummy_handle = sim.getObject("/Arena_dummy") 

	## Retrieve the handle of the child script attached to the Arena_dummy scene object.
	# childscript_handle = sim.getScript(sim.scripttype_childscript, arena_dummy_handle, "")

	## Call the activate_qr_code() function defined in the child script to make the QR code visible at checkpoint E
	# sim.callScriptFunction("activate_qr_code", childscript_handle, "checkpoint E")

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


	##################################################

	return qr_message

##############################################################
##############################################################

############### ADD ARENA PARAMETER DETECTION ################
####################### FUNCTIONS HERE #######################
"""
Add functions written in Task 1A and 3A for detecting arena parameters
from configuration image in this section
"""

def detect_all_nodes(image):
	"""
	Purpose:
	---
	This function takes the image as an argument and returns a list of
	nodes in which traffic signals, start_node and end_node are present in the image

	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`traffic_signals, start_node, end_node` : [ list ], str, str
			list containing nodes in which traffic signals are present, start and end node too
	
	Example call:
	---
	traffic_signals, start_node, end_node = detect_all_nodes(maze_image)
	"""    
	traffic_signals = []
	start_node = ""
	end_node = ""

    ##############	ADD YOUR CODE HERE	##############
	traffic_signals = []
	start_node = ""
	end_node = ""

	##############	ADD YOUR CODE HERE	##############
	frame = image
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	li = []
	for i in range(0,3):
		if i == 0:
			# print("maitrey")
			mask=cv2.inRange(hsv,(0,100,20),(10,255,255))
		if i == 1:
			# print("patel")
			mask=cv2.inRange(hsv,(36,50,70),(89,255,255))
		if i == 2:
			# print("impossible")
			mask=cv2.inRange(hsv,(129,50,70),(158,255,255))

		# mask=cv2.inRange(hsv,l_b,u_b)
		# mask=cv2.inRange(hsv,(0,100,20),(10,255,255))
		res= cv2.bitwise_and(frame ,frame ,mask=mask)
		# cv2.imshow("frames", frame)
		# cv2.imshow("hsv", hsv)
		# cv2.imshow("musk", mask)
		# cv2.imshow("res", res)
		imgGrey = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
		_, thrash = cv2.threshold(imgGrey, 50, 255, cv2.THRESH_BINARY)
		# cv2.imshow('thresh image ',thrash)

		contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
		cv2.waitKey(1)
		# cv2.imshow(" new", frame)
		for contour in contours:
			approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
			# cv2.drawContours(frame, [approx], 0, (0, 255, 155), 2)
			# cv2.imshow('contour',frame)
			M = cv2.moments(contour)
			if len(approx) == 4 and len(contour) < 50:		
				# print(len(contour))
				if M['m00'] != 0:
					cx = int(M['m10']/M['m00'])
					cy = int(M['m01']/M['m00'])
				# print(cx,cy)
				cy=cy/100
				cy=int(cy)
				if cx == 100:
					w='A'
				elif cx == 200:
					w='B'
				elif cx == 300:
					w='C'
				elif cx == 400:
					w='D'
				elif cx == 500:
					w='E'
				elif cx == 600:
					w='F'
				elif cx == 700 :
					w='G'
					
				q=w+str(cy)
				li.append(q)
		if i==0:
			traffic_signals=li
			# print("'traffic signals':",end ='')
			# print(traffic_signals)

		if i==1:
			start_node=li[0]
			# print("'start node':",end ='')
			# print(start_node)

		if i==2:
			end_node=li[0]
			# print("'End node':",end ='')
			# print(end_node)


		# print("'traffic signals':",end ='')
		# print(li)
		li=[]

	
	##################################################


    ##################################################

	return traffic_signals, start_node, end_node

def detect_horizontal_roads_under_construction(image):	
	"""
	Purpose:
	---
	This function takes the image as an argument and returns a list
	containing the missing horizontal links

	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`horizontal_roads_under_construction` : [ list ]
			list containing missing horizontal links
	
	Example call:
	---
	horizontal_roads_under_construction = detect_horizontal_roads_under_construction(maze_image)
	"""    
	horizontal_roads_under_construction = []

	##############	ADD YOUR CODE HERE	##############
	q=100
	w=200
	for j in range(1,6):
		qq=96
		ww=105
			
		for i in range(1,7):
			
			crop_img=image[qq:ww ,q:w]
			# cv2.imshow('cropimge',crop_img)
			cv2.waitKey(2)
			gray = cv2.cvtColor(crop_img,cv2.COLOR_RGB2HSV)
			mask = cv2.inRange(gray ,(0,0,231),(180,18,255))
			res = cv2.bitwise_and(crop_img ,crop_img, mask=mask)
			# cv2.imshow('res image ',res)
			imgGrey = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
			_, thrash = cv2.threshold(imgGrey, 50, 255, cv2.THRESH_BINARY)
			# cv2.imshow('thresh image ',thrash)
			contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
			cv2.waitKey(1)
			# print(len(contours))
			# cv2.imshow(" new", img)
			for contour in contours:
				approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
				# cv2.drawContours(crop_img, [approx], 0, (0, 0, 255), 2)
				# cv2.imshow('contour',crop_img)
				
				
				if j==1 :    
					u='A'+str(i)
					z='B'+str(i)
					v=u+'-'+z
				elif j==2 :
					u='B'+str(i)
					z='C'+str(i)
					v=u+'-'+z
				elif j==3 :
					u='C'+str(i)
					z='D'+str(i)
					v=u+'-'+z
				elif j==4 :
					u='D'+str(i)
					z='E'+str(i)
					v=u+'-'+z
				elif j==5 :
					u='E'+str(i)
					z='F'+str(i)
					v=u+'-'+z
				elif j==6 :
					u='F'+str(i)
					z='G'+str(i)
					v=u+'-'+z
					
				# print(v)
				horizontal_roads_under_construction.append(v)
				# print(list)
			


			qq=qq+100
			ww=ww+100
		q=q+100
		w=w+100
  	
	##################################################
	cv2.waitKey(0)


	##################################################
	
	return horizontal_roads_under_construction	

def detect_vertical_roads_under_construction(image):
	"""
	Purpose:
	---
	This function takes the image as an argument and returns a list
	containing the missing vertical links

	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`vertical_roads_under_construction` : [ list ]
			list containing missing vertical links
	
	Example call:
	---
	vertical_roads_under_construction = detect_vertical_roads_under_construction(maze_image)
	"""    
	vertical_roads_under_construction = []

	##############	ADD YOUR CODE HERE	##############
	qq=95
	ww=107
	for j in range(1,7):
		q=100
		w=200
			
		for i in range(1,6):
			
			crop_img=image[q:w ,qq:ww]
			# cv2.imshow('cropimge',crop_img)
			cv2.waitKey(2)
			gray = cv2.cvtColor(crop_img ,cv2.COLOR_RGB2HSV)
			mask = cv2.inRange(gray ,(0,0,231),(180,18,255))
			res = cv2.bitwise_and(crop_img ,crop_img, mask=mask)
			# cv2.imshow('res image ',res)
			imgGrey = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
			_, thrash = cv2.threshold(imgGrey, 50, 255, cv2.THRESH_BINARY)
			# cv2.imshow('thresh image ',thrash)
			contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
			cv2.waitKey(1)
			# print(len(contours))
			# cv2.imshow(" new", img)
			for contour in contours:
				approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
				# cv2.drawContours(crop_img, [approx], 0, (0, 0, 255), 2)
				# cv2.imshow('contour',crop_img)
				k=i
				l=i+1
				
				if j==1 :    
					u='A'+str(k)
					z='A'+str(l)
					v=u+'-'+z
				elif j==2 :
					u='B'+str(k)
					z='B'+str(l)
					v=u+'-'+z
				elif j==3 :
					u='C'+str(k)
					z='C'+str(l)
					v=u+'-'+z
				elif j==4 :
					u='D'+str(k)
					z='D'+str(l)
					v=u+'-'+z
				elif j==5 :
					u='E'+str(k)
					z='E'+str(l)
					v=u+'-'+z
				elif j==6 :
					u='F'+str(k)
					z='F'+str(l)
					v=u+'-'+z
				elif j==7 :
					u='G'+str(k)
					z='G'+str(l)
					v=u+'-'+z
					
				# print(v)
				vertical_roads_under_construction.append(v)
				# print(list)
			


			q=q+100
			w=w+100
		qq=qq+100
		ww=ww+100
	# print("'vertical_road_under_construction':",end ='')
	# print(vertical_roads_under_construction)

	cv2.waitKey(0)	
	##################################################
	
	##################################################
	
	return vertical_roads_under_construction

def detect_medicine_packages(image):
	"""
	Purpose:
	---
	This function takes the image as an argument and returns a nested list of
	details of the medicine packages placed in different shops

	** Please note that the shop packages should be sorted in the ASCENDING order of shop numbers 
	   as well as in the alphabetical order of colors.
	   For example, the list should first have the packages of shop_1 listed. 
	   For the shop_1 packages, the packages should be sorted in the alphabetical order of color ie Green, Orange, Pink and Skyblue.

	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`medicine_packages` : [ list ]
			nested list containing details of the medicine packages present.
			Each element of this list will contain 
			- Shop number as Shop_n
			- Color of the package as a string
			- Shape of the package as a string
			- Centroid co-ordinates of the package
	Example call:
	---
	medicine_packages = detect_medicine_packages(maze_image)
	"""    
	medicine_packages = []

	##############	ADD YOUR CODE HERE	##############
	z=100
	q=200
	for i in range(0,6):
		# print(z,q)
		cropped_image = image[100:200 , z:q]
		# cv2.waitKey(0)
		# print(z,q)
		# cv2.imshow('corp 1',cropped_image)
		gray = cv2.cvtColor(cropped_image ,cv2.COLOR_RGB2HSV)
		# cv2.imshow('gray image ',gray)
		for p in range(0,4):
			# print(p)
			if p==3:
				l_b =(25,50,70)
				h_b =(52,255,255)
			elif p==2:
				l_b =(128,50,70)
				h_b =(160,255,255)
			elif p==1:
				l_b =(90,50,70)
				h_b =(128,255,255)

			elif p==0 :
				# print("ooooo")
				l_b =(52,50,70)
				h_b =(89,255,255)


			mask = cv2.inRange(gray ,l_b, h_b)
			res = cv2.bitwise_and(cropped_image ,cropped_image, mask=mask)
			# cv2.imshow('res image ',res)
			imgGrey = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
			_, thrash = cv2.threshold(imgGrey, 50, 255, cv2.THRESH_BINARY)
			# cv2.imshow('thresh image ',thrash)
			contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
			cv2.waitKey(1)
			# cv2.imshow(" new", img)
			for contour in contours:
				approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
				# cv2.drawContours(cropped_image, [approx], 0, (0, 0, 255), 2)
				# cv2.imshow('contour',cropped_image)
				x = approx.ravel()[0]
				y = approx.ravel()[1] - 5
				if len(approx) == 3:
					# print('triangle',p)
					li=[]
					www=str(i+1)
					vv='Shop_'+www
					li.append(vv)
					if p==0:    
						li.append('Green')
					elif p==1:
						li.append('Orange')
					elif p==2:
						li.append('Pink')
					else :
						li.append('Skyblue')
					li.append('Triangle')
					M = cv2.moments(contour)
					if M['m00'] != 0:
						cx = int(M['m10']/M['m00'])
						cy = int(M['m01']/M['m00'])
					# cv.drawContours(image, [i], -1, (0, 255, 0), 2)
					l=[]
					e=i+1
					cx=e*100+cx
					cy=100+cy
					l.append(cx)
					l.append(cy)
					li.append(l)
					# print(cx,cy)
					# print(li)
					medicine_packages.append(li)
					# cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
				elif len(approx) == 4:
					
					li=[]
					ww=str(i+1)
					v='Shop_'+ww
					li.append(v)
					if p==0:    
						li.append('Green')
					elif p==1:
						li.append('Orange')
					elif p==2:
						li.append('Pink')
					else :
						li.append('Skyblue')
					li.append('Square')
					M = cv2.moments(contour)
					if M['m00'] != 0:
						cx = int(M['m10']/M['m00'])
						cy = int(M['m01']/M['m00'])
					# cv.drawContours(image, [i], -1, (0, 255, 0), 2)
					l=[]
					t=i+1
					cx=t*100+cx
					cy=100+cy
					l.append(cx)
					l.append(cy)
					li.append(l)
					# print(cx,cy)
					# print(li)
					medicine_packages.append(li)
				else:
					li=[]
					w=str(i+1)
					f='Shop_'+w
					li.append(f)
					if p==0:    
						li.append('Green')
					elif p==1:
						li.append('Orange')
					elif p==2:
						li.append('Pink')
					else :
						li.append('Skyblue')
					li.append('Circle')
					M = cv2.moments(contour)
					if M['m00'] != 0:
						cx = int(M['m10']/M['m00'])
						cy = int(M['m01']/M['m00'])
					# cv.drawContours(image, [i], -1, (0, 255, 0), 2)
					l=[]
					g=i+1
					cx=g*100+cx
					cy=100+cy
					l.append(cx)
					l.append(cy)
					li.append(l)
					# print(cx,cy)
					# print(li)
					medicine_packages.append(li)
					# cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

		# cv2.waitKey()
		z=z+100
		q=q+100
	# print(medicine_packages_present)
	cv2.waitKey(0)
	##################################################


	##################################################

	return medicine_packages

def detect_paths_to_graph(image):
	"""
	Purpose:
	---
	This function takes the image as an argument and returns a dictionary of the
	connect path from a node to other nodes and will be used for path planning

	HINT: Check for the road besides the nodes for connectivity 

	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns: U7YHGN8765
	---
	`paths` : { dictionary }
			Every node's connection to other node and set it's value as edge value 
			Eg. : { "D3":{"C3":1, "E3":1, "D2":1, "D4":1}, 
					"D5":{"C5":1, "D2":1, "D6":1 }  }

			Why edge value 1? -->> since every road is equal

	Example call:
	---
	paths = detect_paths_to_graph(maze_image)
	"""    

	paths = {}

	##############	ADD YOUR CODE HERE	##############
	horizontal_roads_under_construction=[]
	A1,A2,A3,A4,A5,A6={},{},{},{},{},{}
	B1,B2,B3,B4,B5,B6={},{},{},{},{},{}
	C1,C2,C3,C4,C5,C6={},{},{},{},{},{}
	D1,D2,D3,D4,D5,D6={},{},{},{},{},{}
	E1,E2,E3,E4,E5,E6={},{},{},{},{},{}
	F1,F2,F3,F4,F5,F6={},{},{},{},{},{}
	G1,G2,G3,G4,G5,G6={},{},{},{},{},{}

	q=100
	w=200
	flag=0
	for j in range(1,6):
		qq=96
		ww=105
			
		for i in range(1,7):
			flag=0
			crop_img=image[qq:ww ,q:w]
			# cv2.imshow('cropimge',crop_img)
			cv2.waitKey(2)
			gray = cv2.cvtColor(crop_img,cv2.COLOR_RGB2HSV)
			mask = cv2.inRange(gray ,(0,0,231),(180,18,255))
			res = cv2.bitwise_and(crop_img ,crop_img, mask=mask)
			# cv2.imshow('res image ',res)
			imgGrey = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
			_, thrash = cv2.threshold(imgGrey, 50, 255, cv2.THRESH_BINARY)
			# cv2.imshow('thresh image ',thrash)
			contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
			cv2.waitKey(1)
			# print(len(contours))
			# cv2.imshow(" new", img)
			for contour in contours:
				approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
				# cv2.drawContours(crop_img, [approx], 0, (0, 0, 255), 2)
				# cv2.imshow('contour',crop_img)
				flag=1
				
				if j==1 :    
					u='A'+str(i)
					z='B'+str(i)
					v=u+'-'+z
				elif j==2 :
					u='B'+str(i)
					z='C'+str(i)
					v=u+'-'+z
				elif j==3 :
					u='C'+str(i)
					z='D'+str(i)
					v=u+'-'+z
				elif j==4 :
					u='D'+str(i)
					z='E'+str(i)
					v=u+'-'+z
				elif j==5 :
					u='E'+str(i)
					z='F'+str(i)
					v=u+'-'+z
				elif j==6 :
					u='F'+str(i)
					z='G'+str(i)
					v=u+'-'+z
					
				# print(v)
				horizontal_roads_under_construction.append(v)
				# print(list)
			

			if flag == 0:
				if j==1 :
					if i == 1:
						u='A'+str(i)
						z='B'+str(i)
						# q='A'+i
						# o='B'+i
						A1[z]=1
						B1[u]=1
						# print(A1,B1)
					if i == 2:
						u='A'+str(i)
						z='B'+str(i)
						# q='A'+i
						# o='B'+i
						A2[z]=1
						B2[u]=1
						# print(A2,B2)
					if i == 3:
						u='A'+str(i)
						z='B'+str(i)
						# q='A'+i
						# o='B'+i
						A3[z]=1
						B3[u]=1
						# print(A3,B3)
					if i == 4:
						u='A'+str(i)
						z='B'+str(i)
						# q='A'+i
						# o='B'+i
						A4[z]=1
						B4[u]=1
						# print(A4,B4)
					if i == 5:
						u='A'+str(i)
						z='B'+str(i)
						# q='A'+i
						# o='B'+i
						A5[z]=1
						B5[u]=1
						#print(A5,B5)
					if i == 6:
						u='A'+str(i)
						z='B'+str(i)
						# q='A'+i
						# o='B'+i
						A6[z]=1
						B6[u]=1
						# print(A6,B6)

				elif j==2 :
					if i == 1:
						u='B'+str(i)
						z='C'+str(i)
						# q='A'+i
						# o='B'+i
						B1[z]=1
						C1[u]=1
						# print(B1,C1)
					if i == 2:
						u='B'+str(i)
						z='C'+str(i)
						B2[z]=1
						C2[u]=1
						# q='A'+i
						# o='B'+i
						# print(B2,C2)
					if i == 3:
						u='B'+str(i)
						z='C'+str(i)
						B3[z]=1
						C3[u]=1
						# q='A'+i
						# o='B'+i
						# print(B3,C3)
					if i == 4:
						u='B'+str(i)
						z='C'+str(i)
						B4[z]=1
						C4[u]=1
						# q='A'+i
						# o='B'+i
						# print(B4,C4)
					if i == 5:
						u='B'+str(i)
						z='C'+str(i)
						B5[z]=1
						C5[u]=1
						# q='A'+i
						# o='B'+i
						# print(B5,C5)
					if i == 6:
						u='B'+str(i)
						z='C'+str(i)
						B6[z]=1
						C6[u]=1
						# q='A'+i
						# o='B'+i
						# print(B6,C6)

				elif j==3 :
					if i == 1:
						u='C'+str(i)
						z='D'+str(i)
						# q='A'+i
						# o='C'+i
						C1[z]=1
						D1[u]=1
						# print(C1,D1)
					if i == 2:
						u='C'+str(i)
						z='D'+str(i)
						# q='A'+i
						C2[z]=1
						D2[u]=1
						# o='C'+i
						# print(C2,D2)
					if i == 3:
						u='C'+str(i)
						z='D'+str(i)
						# q='A'+i
						C3[z]=1
						D3[u]=1
						# o='C'+i
						# print(C3,D3)
					if i == 4:
						u='C'+str(i)
						z='D'+str(i)
						# q='A'+i
						# o='C'+i
						C4[z]=1
						D4[u]=1
						# print(C4,D4)
					if i == 5:
						u='C'+str(i)
						z='D'+str(i)
						# q='A'+i
						C5[z]=1
						D5[u]=1
						# o='C'+i
						# print(C5,D5)
					if i == 6:
						u='C'+str(i)
						z='D'+str(i)
						# q='A'+i
						C6[z]=1
						D6[u]=1
						# o='C'+i
						# print(C6,D6)

				elif j==4:
					if i == 1:
						u='D'+str(i)
						z='E'+str(i)
						# q='A'+i
						# o='D'+i
						D1[z]=1
						E1[u]=1
						# print(D1,E1)
					if i == 2:
						u='D'+str(i)
						z='E'+str(i)
						# q='A'+i
						D2[z]=1
						E2[u]=1
						# o='D'+i
						# print(D2,E2)
					if i == 3:
						u='D'+str(i)
						z='E'+str(i)
						# q='A'+i
						D3[z]=1
						E3[u]=1
						# o='D'+i
						# print(D3,E3)
					if i == 4:
						u='D'+str(i)
						z='E'+str(i)
						D4[z]=1
						E4[u]=1
						# q='A'+i
						# o='D'+i
						# print(D4,E4)
					if i == 5:
						u='D'+str(i)
						z='E'+str(i)
						# q='A'+i
						D5[z]=1
						E5[u]=1
						# o='D'+i
						# print(D5,E5)
					if i == 6:
						u='D'+str(i)
						z='E'+str(i)
						D6[z]=1
						E6[u]=1
						# q='A'+i
						# o='D'+i
						# print(D6,E6)



				elif j==5 :
					if i == 1:
						u='E'+str(i)
						z='F'+str(i)
						# q='A'+i
						# o='E'+i
						E1[z]=1
						F1[u]=1
						# print(E1,F1)
					if i == 2:
						u='E'+str(i)
						z='F'+str(i)
						# q='A'+i
						E2[z]=1
						F2[u]=1
						# o='E'+i
						# print(E2,F2)
					if i == 3:
						u='E'+str(i)
						z='F'+str(i)
						# q='A'+i
						E3[z]=1
						F3[u]=1
						# o='E'+i
						# print(E3,F3)
					if i == 4:
						u='E'+str(i)
						z='F'+str(i)
						# q='A'+i
						E4[z]=1
						F4[u]=1
						# o='E'+i
						# print(E4,F4)
					if i == 5:
						u='E'+str(i)
						z='F'+str(i)
						# q='A'+i
						E5[z]=1
						F5[u]=1
						# o='E'+i
						# print(E5,F5)
					if i == 6:
						u='E'+str(i)
						z='F'+str(i)
						# q='A'+i
						E6[z]=1
						F6[u]=1
						# o='E'+i
						# print(E6,F6)

				elif j==6 :
					if i == 1:
						u='F'+str(i)
						z='G'+str(i)
						# q='A'+i
						# o='F'+i
						F1[z]=1
						G1[u]=1
						# print(F1,G1)
					if i == 2:
						u='F'+str(i)
						z='G'+str(i)
						# q='A'+i
						F2[z]=1
						G2[u]=1
						# o='F'+i
						# print(F2,G2)
					if i == 3:
						u='F'+str(i)
						z='G'+str(i)
						# q='A'+i
						F3[z]=1
						G3[u]=1
						# o='F'+i
						# print(F3,G3)
					if i == 4:
						u='F'+str(i)
						z='G'+str(i)
						# q='A'+i
						F4[z]=1
						G4[u]=1
						# o='F'+i
						# print(F4,G4)
					if i == 5:
						u='F'+str(i)
						z='G'+str(i)
						# q='A'+i
						F5[z]=1
						G5[u]=1
						# o='F'+i
						# print(F5,G5)
					if i == 6:
						u='F'+str(i)
						z='G'+str(i)
						# q='A'+i
						F6[z]=1
						G6[u]=1
						# o='F'+i
						# print(F6,G6)


				
			qq=qq+100
			ww=ww+100
		q=q+100
		w=w+100
  	
	##################################################
	# cv2.imshow('contour',image)
	cv2.waitKey(0)
	# print(horizontal_roads_under_construction)
	vertical_roads_under_construction=[]
	qq=95
	ww=107
	for j in range(1,7):
		q=100
		w=200
			
		for i in range(1,6):
			flag1=0
			crop_img=image[q:w ,qq:ww]
			# cv2.imshow('cropimge',crop_img)
			cv2.waitKey(2)
			gray = cv2.cvtColor(crop_img ,cv2.COLOR_RGB2HSV)
			mask = cv2.inRange(gray ,(0,0,231),(180,18,255))
			res = cv2.bitwise_and(crop_img ,crop_img, mask=mask)
			# cv2.imshow('res image ',res)
			imgGrey = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
			_, thrash = cv2.threshold(imgGrey, 50, 255, cv2.THRESH_BINARY)
			# cv2.imshow('thresh image ',thrash)
			contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
			cv2.waitKey(1)
			# print(len(contours))
			# cv2.imshow(" new", img)
			for contour in contours:
				approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
				# cv2.drawContours(crop_img, [approx], 0, (0, 0, 255), 2)
				# cv2.imshow('contour',crop_img)
				k=i
				l=i+1
				flag1=1
				if j==1 :    
					u='A'+str(k)
					z='A'+str(l)
					v=u+'-'+z
				elif j==2 :
					u='B'+str(k)
					z='B'+str(l)
					v=u+'-'+z
				elif j==3 :
					u='C'+str(k)
					z='C'+str(l)
					v=u+'-'+z
				elif j==4 :
					u='D'+str(k)
					z='D'+str(l)
					v=u+'-'+z
				elif j==5 :
					u='E'+str(k)
					z='E'+str(l)
					v=u+'-'+z
				elif j==6 :
					u='F'+str(k)
					z='F'+str(l)
					v=u+'-'+z
				elif j==7 :
					u='G'+str(k)
					z='G'+str(l)
					v=u+'-'+z
					
				# print(v)
				vertical_roads_under_construction.append(v)
				# print(list)
			if flag1 == 0:
				if j==1 :
					if i == 1:
						u='A'+str(i)
						z='A'+str(i+1)
						# q='A'+i
						# o='B'+i
						A1[z]=1
						A2[u]=1
						# print(A1,A2)
					if i == 2:
						u='A'+str(i)
						z='A'+str(i+1)
						# q='A'+i
						# o='B'+i
						A2[z]=1
						A3[u]=1
						# print(A2,A3)
					if i == 3:
						u='A'+str(i)
						z='A'+str(i+1)
						# q='A'+i
						# o='B'+i
						A3[z]=1
						A4[u]=1
						# print(A3,A4)
					if i == 4:
						u='A'+str(i)
						z='A'+str(i+1)
						# q='A'+i
						# o='B'+i
						A4[z]=1
						A5[u]=1
						# print(A4,A5)
					if i == 5:
						u='A'+str(i)
						z='A'+str(i+1)
						# q='A'+i
						# o='B'+i
						A5[z]=1
						A6[u]=1
						# print(A5,A6)

				elif j==2 :
					if i == 1:
						u='B'+str(i)
						z='B'+str(i+1)
						# q='A'+i
						# o='B'+i
						B1[z]=1
						B2[u]=1
						# print(B1,B2)
					if i == 2:
						u='B'+str(i)
						z='B'+str(i+1)
						# q='A'+i
						B2[z]=1
						B3[u]=1
						# o='B'+i
						# print(B2,B3)
					if i == 3:
						u='B'+str(i)
						z='B'+str(i+1)
						# q='A'+i
						B3[z]=1
						B4[u]=1
						# o='B'+i
						# print(B3,B4)
					if i == 4:
						u='B'+str(i)
						z='B'+str(i+1)
						# q='A'+i
						B4[z]=1
						B5[u]=1
						# o='B'+i
						# print(B4,B5)
					if i == 5:
						u='B'+str(i)
						z='B'+str(i+1)
						# q='A'+i
						B5[z]=1
						B6[u]=1
						# o='B'+i
						# print("-----------",B6)
						# print(B5,B6)
				elif j==3 :
					if i == 1:
						u='C'+str(i)
						z='C'+str(i+1)
						# q='A'+i
						# o='C'+i
						C1[z]=1
						C2[u]=1
						# print(C1,C2)
					if i == 2:
						u='C'+str(i)
						z='C'+str(i+1)
						# q='A'+i
						C2[z]=1
						C3[u]=1
						# o='C'+i
						# print(C2,C3)
					if i == 3:
						u='C'+str(i)
						z='C'+str(i+1)
						# q='A'+i
						C3[z]=1
						C4[u]=1
						# o='C'+i
						# print(C3,C4)
					if i == 4:
						u='C'+str(i)
						z='C'+str(i+1)
						# q='A'+i
						C4[z]=1
						C5[u]=1
						# o='C'+i
						# print(C4,C5)
					if i == 5:
						u='C'+str(i)
						z='C'+str(i+1)
						# q='A'+i
						C5[z]=1
						C6[u]=1
						# o='C'+i
						# print(C5,C6)

				elif j==4:
					if i == 1:
						u='D'+str(i)
						z='D'+str(i+1)
						# q='A'+i
						# o='D'+i
						D1[z]=1
						D2[u]=1
						# print(D1,D2)
					if i == 2:
						u='D'+str(i)
						z='D'+str(i+1)
						# q='A'+i
						# o='D'+i
						D2[z]=1
						D3[u]=1
						# print(D2,D3)
					if i == 3:
						u='D'+str(i)
						z='D'+str(i+1)
						# q='A'+i
						# o='D'+i
						D3[z]=1
						D4[u]=1
						# print(D3,D4)
					if i == 4:
						u='D'+str(i)
						z='D'+str(i+1)
						# q='A'+i
						# o='D'+i
						D4[z]=1
						D5[u]=1
						# print(D4,D5)
					if i == 5:
						u='D'+str(i)
						z='D'+str(i+1)
						# q='A'+i
						# o='D'+i
						D5[z]=1
						D6[u]=1
						# print(D5,D6)

				elif j==5 :
					if i == 1:
						u='E'+str(i)
						z='E'+str(i+1)
						# q='A'+i
						# o='E'+i
						E1[z]=1
						E2[u]=1
						# print(E1,E2)
					if i == 2:
						u='E'+str(i)
						z='E'+str(i+1)
						# q='A'+i
						E2[z]=1
						E3[u]=1
						# o='E'+i
						# print(E2,E3)
					if i == 3:
						u='E'+str(i)
						z='E'+str(i+1)
						# q='A'+i
						E3[z]=1
						E4[u]=1
						# o='E'+i
						# print(E3,E4)
					if i == 4:
						u='E'+str(i)
						z='E'+str(i+1)
						# q='A'+i
						E4[z]=1
						E5[u]=1
						# o='E'+i
						# print(E4,E5)
					if i == 5:
						u='E'+str(i)
						z='E'+str(i+1)
						# q='A'+i
						E5[z]=1
						E6[u]=1
						# o='E'+i
						# print(E5,E6)

				elif j==6 :
					if i == 1:
						u='F'+str(i)
						z='F'+str(i+1)
						# q='A'+i
						# o='F'+i
						F1[z]=1
						F2[u]=1
						# print(F1,F2)
					if i == 2:
						u='F'+str(i)
						z='F'+str(i+1)
						# q='A'+i
						# o='F'+i
						F2[z]=1
						F3[u]=1
						# print(F2,F3)
					if i == 3:
						u='F'+str(i)
						z='F'+str(i+1)
						# q='A'+i
						F3[z]=1
						F4[u]=1
						# o='F'+i
						# print(F3,F4)
					if i == 4:
						u='F'+str(i)
						z='F'+str(i+1)
						# q='A'+i
						F4[z]=1
						F5[u]=1
						# o='F'+i
						# print(F4,F5)
					if i == 5:
						u='F'+str(i)
						z='F'+str(i+1)
						# q='A'+i
						F5[z]=1
						F6[u]=1
						# o='F'+i
						# print(F5,F6)



			q=q+100
			w=w+100
		qq=qq+100
		ww=ww+100
	# print("'vertical_road_under_construction':",end ='')
	# print(vertical_roads_under_construction)
	# cv2.imshow('contour',crop_img)
	cv2.waitKey(0)
	# print(A1)
	sorted(A1.items())
	# dict(sorted(A1.items()))
	# print("---------",A1)
	A11={}
	for key in sorted(A1):
		# print(key)
		A11[key]=1
	A12={}
	for key in sorted(A2):
		# print(key)
		A12[key]=1
	A13={}
	for key in sorted(A3):
		# print(key)
		A13[key]=1
	A14={}
	for key in sorted(A4):
		# print(key)
		A14[key]=1
	A15={}
	for key in sorted(A5):
		# print(key)
		A15[key]=1
	A16={}
	for key in sorted(A6):
		# print(key)
		A16[key]=1
	B11={}
	for key in sorted(B1):
		# print(key)
		B11[key]=1
	B12={}
	for key in sorted(B2):
		# print(key)
		B12[key]=1
	B13={}
	for key in sorted(B3):
		# print(key)
		B13[key]=1
	B14={}
	for key in sorted(B4):
		# print(key)
		B14[key]=1
	B15={}
	for key in sorted(B5):
		# print(key)
		B15[key]=1
	B16={}
	for key in sorted(B6):
		# print(key)
		B16[key]=1
	C11={}
	for key in sorted(C1):
		# print(key)
		C11[key]=1
	C12={}
	for key in sorted(C2):
		# print(key)
		C12[key]=1
	C13={}
	for key in sorted(C3):
		# print(key)
		C13[key]=1
	C14={}
	for key in sorted(C4):
		# print(key)
		C14[key]=1
	C15={}
	for key in sorted(C5):
		# print(key)
		C15[key]=1
	C16={}
	for key in sorted(C6):
		# print(key)
		C16[key]=1
	D11={}
	for key in sorted(D1):
		# print(key)
		D11[key]=1
	D12={}
	for key in sorted(D2):
		# print(key)
		D12[key]=1
	D13={}
	for key in sorted(D3):
		# print(key)
		D13[key]=1
	D14={}
	for key in sorted(D4):
		# print(key)
		D14[key]=1
	D15={}
	for key in sorted(D5):
		# print(key)
		D15[key]=1
	D16={}
	for key in sorted(D6):
		# print(key)
		D16[key]=1
	E11={}
	for key in sorted(E1):
		# print(key)
		E11[key]=1
	E12={}
	for key in sorted(E2):
		# print(key)
		E12[key]=1
	E13={}
	for key in sorted(E3):
		# print(key)
		E13[key]=1
	E14={}
	for key in sorted(E4):
		# print(key)
		E14[key]=1
	E15={}
	for key in sorted(E5):
		# print(key)
		E15[key]=1
	E16={}
	for key in sorted(E6):
		# print(key)
		E16[key]=1
	F11={}
	for key in sorted(F1):
		# print(key)
		F11[key]=1
	F12={}
	for key in sorted(F2):
		# print(key)
		F12[key]=1
	F13={}
	for key in sorted(F3):
		# print(key)
		F13[key]=1
	F14={}
	for key in sorted(F4):
		# print(key)
		F14[key]=1
	F15={}
	for key in sorted(F5):
		# print(key)
		F15[key]=1
	F16={}
	for key in sorted(F6):
		# print(key)
		F16[key]=1

	# print(A11,A12,A13,A14,A15,A16)
	# A1=sorted(A1)
	# A2=sorted(A2)
	# A3=sorted(A3)
	# A4=sorted(A4)
	# A5=sorted(A5)
	# A6=sorted(A6)
	# B1=sorted(B1)
	# B2=sorted(B2)
	# B3=sorted(B3)
	# B4=sorted(B4)
	# B5=sorted(B5)
	# B6=sorted(B6)
	# C1=sorted(C1)
	# C2=sorted(C2)
	# C3=sorted(C3)
	# C4=sorted(C4)
	# C5=sorted(C5)
	# C6=sorted(C6)
	# D1=sorted(D1)
	# D2=sorted(D2)
	# D3=sorted(D3)
	# D4=sorted(D4)
	# D5=sorted(D5)
	# D6=sorted(D6)
	# E1=sorted(E1)
	# E2=sorted(E2)
	# E3=sorted(E3)
	# E4=sorted(E4)
	# E5=sorted(E5)
	# E6=sorted(E6)
	# F1=sorted(F1)
	# F2=sorted(F2)
	# F3=sorted(F3)
	# F4=sorted(F4)
	# F5=sorted(F5)
	# F6=sorted(F6)







	# print(A1)
	paths={}
	paths["A1"]=A11
	paths["A2"]=A12
	paths["A3"]=A13
	paths["A4"]=A14
	paths["A5"]=A15
	paths["A6"]=A16
	paths["B1"]=B11
	paths["B2"]=B12
	paths["B3"]=B13
	paths["B4"]=B14
	paths["B5"]=B15
	paths["B6"]=B16
	paths["C1"]=C11
	paths["C2"]=C12
	paths["C3"]=C13
	paths["C4"]=C14
	paths["C5"]=C15
	paths["C6"]=C16
	paths["D1"]=D11
	paths["D2"]=D12
	paths["D3"]=D13
	paths["D4"]=D14
	paths["D5"]=D15
	paths["D6"]=D16
	paths["E1"]=E11
	paths["E2"]=E12
	paths["E3"]=E13
	paths["E4"]=E14
	paths["E5"]=E15
	paths["E6"]=E16
	paths["F1"]=F11
	paths["F2"]=F12
	paths["F3"]=F13
	paths["F4"]=F14
	paths["F5"]=F15
	paths["F6"]=F16








	# paths=dict({"A1":A1})
	# paths=dict({"A2":A2})
	# paths=dict({"A3":A3})
	# paths=dict({"A4":A4})

	# print(paths)

 
	# return horizontal_roads_under_construction	


	
	##################################################

	return paths

	
	##################################################


def detect_arena_parameters(maze_image):
	"""
	Purpose:
	---
	This function takes the image as an argument and returns a dictionary
	containing the details of the different arena parameters in that image

	The arena parameters are of four categories:
	i) traffic_signals : list of nodes having a traffic signal
	ii) start_node : Start node which is mark in light green
	iii) end_node : End node which is mark in Purple
	iv) paths : list containing paths

	These four categories constitute the four keys of the dictionary

	Input Arguments:
	---
	`maze_image` :	[ numpy array ]
			numpy array of image returned by cv2 library
	Returns:
	---
	`arena_parameters` : { dictionary }
			dictionary containing details of the arena parameters
	
	Example call:
	---
	arena_parameters = detect_arena_parameters(maze_image)

	Eg. arena_parameters={"traffic_signals":[], 
	                      "start_node": "E4", 
	                      "end_node":"A3", 
	                      "paths": {}}
	"""    
	arena_parameters = {}

    ##############	ADD YOUR CODE HERE	##############
	traffic_signals, start_node, end_node = detect_all_nodes(maze_image)
	paths=detect_paths_to_graph(maze_image)
	# b = ''.join(str(traffic_signals).split(","))
	traffic_signals.sort()
	arena_parameters["traffic_signals"]=traffic_signals
	arena_parameters["start_node"]=start_node
	arena_parameters["end_node"]=end_node
	arena_parameters["paths"]=paths
	# print(arena_parameters)
	


    ##################################################

	return arena_parameters

##############################################################
##############################################################

####################### ADD ARENA SETUP ######################
####################### FUNCTIONS HERE #######################
"""
Add functions written in Task 4A for setting up the CoppeliaSim
Arena according to the configuration image in this section
"""

def place_packages(medicine_package_details, sim, all_models):
    """
	Purpose:
	---
	This function takes details (colour, shape and shop) of the packages present in 
    the arena (using "detect_arena_parameters" function from task_1a.py) and places
    them on the virtual arena. The packages should be inserted only into the 
    designated areas in each shop as mentioned in the Task document.

    Functions from Regular API References should be used to set the position of the 
    packages.

	Input Arguments:
	---
	`medicine_package_details` :	[ list ]
                                nested list containing details of the medicine packages present.
                                Each element of this list will contain 
                                - Shop number as Shop_n
                                - Color of the package as a string
                                - Shape of the package as a string
                                - Centroid co-ordinates of the package			

    `sim` : [ object ]
            ZeroMQ RemoteAPI object

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
	Returns:

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
	
	Example call:
	---
	all_models = place_packages(medicine_package_details, sim, all_models)
	"""
    models_directory = os.getcwd()
    packages_models_directory = os.path.join(models_directory, "package_models")
    arena = sim.getObject('/Arena')    

####################### ADD YOUR CODE HERE #########################
    models_directory = os.getcwd()
    packages_models_directory = os.path.join(models_directory, "package_models")
    arena = sim.getObject('/Arena')    
####################### ADD YOUR CODE HERE #########################
    # print(medicine_package_details)
    l=len(medicine_package_details)
    i=0
    # all_models=[]
    count=0
    count1=0
    count2=0
    count3=0
    count4=0
    while l:
        ix=medicine_package_details[i][3][0]
        iy=medicine_package_details[i][3][1]
        k=medicine_package_details[i][0]
        # objectHandle=sim.loadModel()

        # print(k)
        if k == 'Shop_1':
            count=count+1
            cx = -0.8305
            if count == 2:
                cx=cx+2*0.0395
            if count == 3:
                cx=cx+4*0.0395
            if count == 4:
                cx=cx+6*0.0395
        if k == 'Shop_2':
            count1=count1+1
            cx = -0.4745
            if count1 == 2:
                cx=cx+2*0.0395
            if count1 == 3:
                cx=cx+4*0.0395
            if count1 == 4:
                cx=cx+6*0.0395
        if k == 'Shop_3':
            count2=count2+1
            cx = -0.1185
            if count2 == 2:
                cx=cx+2*0.0395
            if count2 == 3:
                cx=cx+4*0.0395
            if count2 == 4:
                cx=cx+6*0.0395
        if k == 'Shop_4':
            count3=count3+1
            cx = 0.2375
            if count3 == 2:
                cx=cx+2*0.0395
            if count3 == 3:
                cx=cx+4*0.0395
            if count3 == 4:
                cx=cx+6*0.0395
        if k == 'Shop_5':
            count4=count4+1
            cx = 0.5935
            if count4 == 2:
                cx=cx+2*0.0395
            if count4 == 3:
                cx=cx+4*0.0395
            if count4 == 4:
                cx=cx+6*0.0395
        # x=350-ix
        # y=350-iy
        # cx=x/350*0.9550
        # cx=-cx
        # cy=y/350*0.9550SS
        # print(ix,iy,x,y,cx,cy)
        cy=0.6873125
        ia=medicine_package_details[i][1]
        ib=medicine_package_details[i][2]
        ic=ia + '_' + ib
        # print(ic)
        # # print(simGetStringParameter(sim_stringparam_application_path))
        # path='C:/Users/DICT/Desktop/PB Task 4A/PB Task 4A/package_models/'  + ic + '.ttm'
        # print(path)
        if ic =='Green_Triangle':
            objectHandle=sim.loadModel(r'C:/Users/DICT/Desktop/PB Task 4A/PB Task 4A/package_models/Green_cone.ttm')
        if ic =='Green_Circle':
            objectHandle=sim.loadModel(r'C:/Users/DICT/Desktop/PB Task 4A/PB Task 4A/package_models/Green_cylinder.ttm')
        if ic =='Green_Square':
            objectHandle=sim.loadModel(r'C:/Users/DICT/Desktop/PB Task 4A/PB Task 4A/package_models/Green_cube.ttm')
        if ic =='Pink_Triangle':
            objectHandle=sim.loadModel(r'C:/Users/DICT/Desktop/PB Task 4A/PB Task 4A/package_models/Pink_cone.ttm')
        if ic =='Pink_Circle':
            objectHandle=sim.loadModel(r'C:/Users/DICT/Desktop/PB Task 4A/PB Task 4A/package_models/Pink_cylinder.ttm')
        if ic =='Pink_Square':
            objectHandle=sim.loadModel(r'C:/Users/DICT/Desktop/PB Task 4A/PB Task 4A/package_models/Pink_cube.ttm')
        if ic =='Orange_Triangle':
            objectHandle=sim.loadModel(r'C:/Users/DICT/Desktop/PB Task 4A/PB Task 4A/package_models/Orange_cone.ttm')
        if ic =='Orange_Circle':
            objectHandle=sim.loadModel(r'C:/Users/DICT/Desktop/PB Task 4A/PB Task 4A/package_models/Orange_cylinder.ttm')
        if ic =='Orange_Square':
            objectHandle=sim.loadModel(r'C:/Users/DICT/Desktop/PB Task 4A/PB Task 4A/package_models/Orange_cube.ttm')
        if ic =='Skyblue_Triangle':
            objectHandle=sim.loadModel(r'C:/Users/DICT/Desktop/PB Task 4A/PB Task 4A/package_models/Skyblue_cone.ttm')
        if ic =='Skyblue_Circle':
            objectHandle=sim.loadModel(r'C:/Users/DICT/Desktop/PB Task 4A/PB Task 4A/package_models/Skyblue_cylinder.ttm')
        if ic =='Skyblue_Square':
            objectHandle=sim.loadModel(r'C:/Users/DICT/Desktop/PB Task 4A/PB Task 4A/package_models/Skyblue_cube.ttm')
        keepInPlace=True
        sim.setObjectParent(objectHandle,arena,keepInPlace)

            # e = sim.getObject(ic)
        e=objectHandle
        all_models.append(e)
        position=[]
        position.append(cx)
        position.append(cy)
        position.append(0)


        sim.setObjectPosition(e,arena,position)
        i=i+1
        l=l-1




####################################################################

    return all_models

def place_traffic_signals(traffic_signals, sim, all_models):
    """
	Purpose:
	---
	This function takes position of the traffic signals present in 
    the arena (using "detect_arena_parameters" function from task_1a.py) and places
    them on the virtual arena. The signal should be inserted at a particular node.

    Functions from Regular API References should be used to set the position of the 
    signals.

	Input Arguments:
	---
	`traffic_signals` : [ list ]
			list containing nodes in which traffic signals are present

    `sim` : [ object ]
            ZeroMQ RemoteAPI object

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
	Returns:

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
	None
	
	Example call:
	---
	all_models = place_traffic_signals(traffic_signals, sim, all_models)
	"""
    models_directory = os.getcwd()
    traffic_sig_model = os.path.join(models_directory, "signals", "traffic_signal.ttm" )
    arena = sim.getObject('/Arena')

####################### ADD YOUR CODE HERE #########################
    models_directory = os.getcwd()
    traffic_sig_model = os.path.join(models_directory, "signals", "traffic_signal.ttm" )
    arena = sim.getObject('/Arena')   
####################### ADD YOUR CODE HERE #########################
    # print(traffic_signals)
    l=len(traffic_signals)
    i=0
    while l:
        k=traffic_signals[i]
        # print(k[0],k[1])
        r=k[0]
        y=k[1]
        # print(type(r),type(y))
        if r =='A':
            # print('A')
            cx = -0.8900
        if r == 'B':
            cx = -0.5340
        if r == 'C':
            cx = -0.1780
        if r == 'D':
            cx = 0.1780
        if r == 'E':
            cx = 0.5340
        if r == 'F':
            cx = 0.8900
        if y == '1':
            cy = -0.8900
        if y == '2':
            cy = -0.5340
        if y == '3':
            cy = -0.1780
        if y == '4':
            cy = 0.1780
        if y == '5':
            cy = 0.5340
        if y == '6':
            cy = 0.8900
        objectHandle=sim.loadModel(r'C:\Users\DICT\Desktop\PB Task 4A\PB Task 4A\signals\traffic_signal.ttm')
        objectAlias='Signal_'+r+y
        # print(objectAlias)
        sim.setObjectAlias(objectHandle,objectAlias)

        keepInPlace=True
        sim.setObjectParent(objectHandle,arena,keepInPlace)

        cy=-cy
        # print(cx,cy)
        e=objectHandle
        all_models.append(e)
        position=[]
        position.append(cx)
        position.append(cy)
        position.append(0.1539)


        sim.setObjectPosition(e,arena,position)
        i=i+1
        l=l-1



####################################################################

    return all_models

def place_start_end_nodes(start_node, end_node, sim, all_models):
    """
	Purpose:
	---
	This function takes position of start and end nodes present in 
    the arena and places them on the virtual arena. 
    The models should be inserted at a particular node.

    Functions from Regular API References should be used to set the position of the 
    start and end nodes.

	Input Arguments:
	---
	`start_node` : [ string ]
    `end_node` : [ string ]
					

    `sim` : [ object ]
            ZeroMQ RemoteAPI object

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
	Returns:

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
	---
	None
	
	Example call:
	---
	all_models = place_start_end_nodes(start_node, end_node, sim, all_models)
	"""
    models_directory = os.getcwd()
    start_node_model = os.path.join(models_directory, "signals", "start_node.ttm" )
    end_node_model = os.path.join(models_directory, "signals", "end_node.ttm" )
    arena = sim.getObject('/Arena')   

####################### ADD YOUR CODE HERE #########################
    models_directory = os.getcwd()
    start_node_model = os.path.join(models_directory, "signals", "start_node.ttm" )
    end_node_model = os.path.join(models_directory, "signals", "end_node.ttm" )
    arena = sim.getObject('/Arena')   
####################### ADD YOUR CODE HERE #########################
    l=2
    while l:
        r=start_node[0]
        y=start_node[1]
        if l==1:
            r=end_node[0]
            y=end_node[1]
        if r =='A':
            # print('A')
            cx = -0.8900
        if r == 'B':
            cx = -0.5340
        if r == 'C':
            cx = -0.1780
        if r == 'D':
            cx = 0.1780
        if r == 'E':
            cx = 0.5340
        if r == 'F':
            cx = 0.8900
        if y == '1':
            cy = -0.8900
        if y == '2':
            cy = -0.5340
        if y == '3':
            cy = -0.1780
        if y == '4':
            cy = 0.1780
        if y == '5':
            cy = 0.5340
        if y == '6':
            cy = 0.8900
        if l ==2:
            objectHandle=sim.loadModel(r'C:\Users\DICT\Desktop\PB Task 4A\PB Task 4A\signals\start_node.ttm')
            objectAlias='Start_Node'

        if l==1:
            objectHandle=sim.loadModel(r'C:\Users\DICT\Desktop\PB Task 4A\PB Task 4A\signals\end_node.ttm')
            objectAlias='End_Node'

        # objectAlias='Vertical_missing_road_'+rr+yy+'_'+rrr+yyy
        # print(objectAlias)
        sim.setObjectAlias(objectHandle,objectAlias)

        keepInPlace=True
        sim.setObjectParent(objectHandle,arena,keepInPlace)

        cy=-cy
        # print(cx,cy)
        e=objectHandle
        all_models.append(e)
        position=[]
        position.append(cx)
        position.append(cy)
        position.append(0.1539)


        sim.setObjectPosition(e,arena,position)
        l=l-1


####################################################################

    return all_models

def place_horizontal_barricade(horizontal_roads_under_construction, sim, all_models):
    """
	Purpose:
	---
	This function takes the list of missing horizontal roads present in 
    the arena (using "detect_arena_parameters" function from task_1a.py) and places
    horizontal barricades on virtual arena. The barricade should be inserted 
    between two nodes as shown in Task document.

    Functions from Regular API References should be used to set the position of the 
    horizontal barricades.

	Input Arguments:
	---
	`horizontal_roads_under_construction` : [ list ]
			list containing missing horizontal links		

    `sim` : [ object ]
            ZeroMQ RemoteAPI object

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
	Returns:

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
	---
	None
	
	Example call:
	---
	all_models = place_horizontal_barricade(horizontal_roads_under_construction, sim, all_models)
	"""
    models_directory = os.getcwd()
    horiz_barricade_model = os.path.join(models_directory, "barricades", "horizontal_barricade.ttm" )
    arena = sim.getObject('/Arena')  

####################### ADD YOUR CODE HERE #########################
    models_directory = os.getcwd()
    horiz_barricade_model = os.path.join(models_directory, "barricades", "horizontal_barricade.ttm" )
    arena = sim.getObject('/Arena')  
####################### ADD YOUR CODE HERE #########################
    # print(horizontal_roads_under_construction)
    l=len(horizontal_roads_under_construction)
    i=0
    while l:
        # print(horizontal_roads_under_construction[i],horizontal_roads_under_construction[i][0],horizontal_roads_under_construction[i][3])
        r=horizontal_roads_under_construction[i][0]
        y=horizontal_roads_under_construction[i][1]
        # print(r,y,"----------")
        if r =='A':
            # print('A')
            cx = -0.8900
        if r == 'B':
            cx = -0.5340
        if r == 'C':
            cx = -0.1780
        if r == 'D':
            cx = 0.1780
        if r == 'E':
            cx = 0.5340
        if r == 'F':
            cx = 0.8900
        if y == '1':
            cy = -0.8900
        if y == '2':
            cy = -0.5340
        if y == '3':
            cy = -0.1780
        if y == '4':
            cy = 0.1780
        if y == '5':
            cy = 0.5340
        if y == '6':
            cy = 0.8900
        x1=cx
        y1=cy
        rr=r
        yy=y
        rr=str(rr)
        yy=str(yy)
        r=horizontal_roads_under_construction[i][3]
        y=horizontal_roads_under_construction[i][4]
        if r =='A':
            # print('A')
            cx = -0.8900
        if r == 'B':
            cx = -0.5340
        if r == 'C':
            cx = -0.1780
        if r == 'D':
            cx = 0.1780
        if r == 'E':
            cx = 0.5340
        if r == 'F':
            cx = 0.8900
        if y == '1':
            cy = -0.8900
        if y == '2':
            cy = -0.5340
        if y == '3':
            cy = -0.1780
        if y == '4':
            cy = 0.1780
        if y == '5':
            cy = 0.5340
        if y == '6':
            cy = 0.8900
        x2=cx
        y2=cy
        rrr=r
        yyy=y
        rrr=str(rrr)
        yyy=str(yyy)

        x=(x1+x2)/2
        y=(y1+y2)/2
        y=-y
        # print(x,y)
        objectHandle=sim.loadModel(r'C:\Users\DICT\Desktop\PB Task 4A\PB Task 4A\barricades\horizontal_barricade.ttm')
        # print(type(rr),type(yy),type(r),type(y))
        objectAlias='Horizontal_missing_road_'+rr+yy+'_'+rrr+yyy
        # print(objectAlias)
        sim.setObjectAlias(objectHandle,objectAlias)

        keepInPlace=True
        sim.setObjectParent(objectHandle,arena,keepInPlace)


        e=objectHandle
        all_models.append(e)
        position=[]
        position.append(x)
        position.append(y)
        position.append(0)


        sim.setObjectPosition(e,arena,position)


        i=i+1
        l=l-1
    
####################################################################
    return all_models




####################################################################

    return all_models


def place_vertical_barricade(vertical_roads_under_construction, sim, all_models):
    """
	Purpose:
	---
	This function takes the list of missing vertical roads present in 
    the arena (using "detect_arena_parameters" function from task_1a.py) and places
    vertical barricades on virtual arena. The barricade should be inserted 
    between two nodes as shown in Task document.

    Functions from Regular API References should be used to set the position of the 
    vertical barricades.

	Input Arguments:
	---
	`vertical_roads_under_construction` : [ list ]
			list containing missing vertical links		

    `sim` : [ object ]
            ZeroMQ RemoteAPI object

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
	Returns:

    `all_models` : [ list ]
            list containing handles of all the models imported into the scene
	---
	None
	
	Example call:
	---
	all_models = place_vertical_barricade(vertical_roads_under_construction, sim, all_models)
	"""
    models_directory = os.getcwd()
    vert_barricade_model = os.path.join(models_directory, "barricades", "vertical_barricade.ttm" )
    arena = sim.getObject('/Arena')

####################### ADD YOUR CODE HERE #########################
    models_directory = os.getcwd()
    vert_barricade_model = os.path.join(models_directory, "barricades", "vertical_barricade.ttm" )
    arena = sim.getObject('/Arena') 
####################### ADD YOUR CODE HERE #########################
    # print(vertical_roads_under_construction)
    l=len(vertical_roads_under_construction)
    i=0
    while l:
        # print(vertical_roads_under_construction[i],vertical_roads_under_construction[i][0],vertical_roads_under_construction[i][3])
        r=vertical_roads_under_construction[i][0]
        y=vertical_roads_under_construction[i][1]
        # print(r,y,"----------")
        if r =='A':
            # print('A')
            cx = -0.8900
        if r == 'B':
            cx = -0.5340
        if r == 'C':
            cx = -0.1780
        if r == 'D':
            cx = 0.1780
        if r == 'E':
            cx = 0.5340
        if r == 'F':
            cx = 0.8900
        if y == '1':
            cy = -0.8900
        if y == '2':
            cy = -0.5340
        if y == '3':
            cy = -0.1780
        if y == '4':
            cy = 0.1780
        if y == '5':
            cy = 0.5340
        if y == '6':
            cy = 0.8900
        x1=cx
        y1=cy
        rr=r
        yy=y
        rr=str(rr)
        yy=str(yy)

        r=vertical_roads_under_construction[i][3]
        y=vertical_roads_under_construction[i][4]
        if r =='A':
            # print('A')
            cx = -0.8900
        if r == 'B':
            cx = -0.5340
        if r == 'C':
            cx = -0.1780
        if r == 'D':
            cx = 0.1780
        if r == 'E':
            cx = 0.5340
        if r == 'F':
            cx = 0.8900
        if y == '1':
            cy = -0.8900
        if y == '2':
            cy = -0.5340
        if y == '3':
            cy = -0.1780
        if y == '4':
            cy = 0.1780
        if y == '5':
            cy = 0.5340
        if y == '6':
            cy = 0.8900
        x2=cx
        y2=cy
        rrr=r
        yyy=y

        rrr=str(rrr)
        yyy=str(yyy)
        x=(x1+x2)/2
        y=(y1+y2)/2
        y=-y
        # print(x,y)
        objectHandle=sim.loadModel(r'C:\Users\DICT\Desktop\PB Task 4A\PB Task 4A\barricades\vertical_barricade.ttm')
        objectAlias='Vertical_missing_road_'+rr+yy+'_'+rrr+yyy
        # print(objectAlias)
        sim.setObjectAlias(objectHandle,objectAlias)

        keepInPlace=True
        sim.setObjectParent(objectHandle,arena,keepInPlace)


        e=objectHandle
        all_models.append(e)
        position=[]
        position.append(x)
        position.append(y)
        position.append(0)


        sim.setObjectPosition(e,arena,position)


        i=i+1
        l=l-1



####################################################################

    return all_models

##############################################################
##############################################################
