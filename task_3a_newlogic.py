'''
*****************************************************************************************
*
*        		===============================================
*           		Pharma Bot (PB) Theme (eYRC 2022-23)
*        		===============================================
*
*  This script is to implement Task 3A of Pharma Bot (PB) Theme (eYRC 2022-23).
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
# Filename:			task_3a.py
# Functions:		detect_all_nodes, detect_horizontal_roads_under_construction, detect_vertical_roads_under_construction,
#					detect_paths_to_graph, detect_arena_parameters, path_planning_dj_algo
# 					[ Comma separated list of functions in this file ]

####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv)                    ##
##############################################################
import numpy as np
import cv2
##############################################################

################# ADD UTILITY FUNCTIONS HERE #################





##############################################################

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

	return traffic_signals, start_node, end_node

	
	##################################################



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
	arena_parameters = detect_arena_pearameters(maze_image)

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

def path_planning(graph, start, end):

	"""
	Purpose:
	---
	This function takes the graph(dict), start and end node for planning the shortest path

	** Note: You can use any path planning algorithm for this but need to produce the path in the form of 
	list given below **

	Input Arguments:
	---
	`graph` :	{ dictionary }
			dict of all connecting path
	`start` :	str
			name of start node
	`end` :		str
			name of end node


	Returns:
	---
	`backtrace_path` : [ list of nodes ]
			list of nodes, produced using path planning algorithm

		eg.: ['C6', 'C5', 'B5', 'B4', 'B3']
	
	Example call:
	---
	arena_parameters = detect_arena_parameters(maze_image)
	"""    

	backtrace_path=[]

	##############	ADD YOUR CODE HERE	##############
	k=start
	min=100
	backtrace_path.append(start)
	for i in graph[k]:
		d=distance(i,end)
		print(i,k,min,d)
		backtrace_path=[]
		backtrace_path.append(start)
		if d <= min:
			min=d 
			backtrace_path.append(i)
			print(backtrace_path)
			backtrace_path=path_planning_new(graph,i,end,min,backtrace_path)
			print("&&&&&&&&&&&&&&&&&&&&&&&&&&&",backtrace_path)
			l=len(backtrace_path)
			l=l-2
			print(l,d)
			if l == d:
				break
	o=len(backtrace_path)
	if o == 1:
		backtrace_path=path_planning_new_2(graph,start,end,backtrace_path)
 
 
 
 
 
 
 
 

 
 
 
 
 
 
#  ########################################################################
	# print("------------------",start,backtrace_path)
	# backtrace_path.append(start)
	# po='zz'
	# w='ww'
	# min=100
	# k=start
	# flag=1
	# flag1=0
	# flag2=0
	# count=0
	# while flag:
	# 	flag1=0
	# 	fagg=0
	# 	for i in graph[k]:
	# 		if fagg == 0:
	# 			qqq=k
	# 			fagg=1
	# 		# print("-------------------",i,graph[k],k)
	# 		d=distance(i,end)
	# 		if d == 0:
	# 			flag=0
	# 		# print("&&&&&",d,min)
	# 		if d <= min and flag2==0:
	# 			flag1=1
	# 			# print("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
	# 			min = d
	# 			# q=k
	# 			k=i
	# 		if flag2==1 and d<=min and i!=x:
	# 			flag1=1
	# 			min = d
	# 			q=k
	# 			k=i

	# 	if flag1==1:
	# 		print(min)
	# 		ooo=qqq
	# 		backtrace_path.append(k)
	# 		# print(backtrace_path)
	# 		flag2=0
	# 	if flag1==0:
	# 		count=count+1
	# 		if count == 2:
	# 			l=[]
	# 			o=k
	# 			# print(backtrace_path)
	# 			# l=path(end,graph,backtrace_path)z
	# 			flag=0
	# 			min2=100
	# 			min=20
	# 			kk=k
	# 			# print("@@@@@@@@@@@@@@@@@@@@@@",kk)
	# 			while kk != end:
	# 				flag=0
	# 				fag=1	
	# 				flag10=0
	# 				flag101=0
	# 				for i in graph[kk]:
	# 					# print("###################################################################################")
	# 					if fag == 1:
	# 						q=kk
	# 						# print(q)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
	# 						fag=0
	# 					# print(i)
	# 					d=distance(i,end)
	# 					if d < min:
	# 						# print("%%%%%%%%",d,min)
	# 						min = d
	# 						# print(kk)
	# 						# q=kk
	# 						kk=i
	# 						flag=1
	# 				if flag == 0:   
	# 					for j in graph[kk]:
	# 						flag10=0
	# 						# print("99999999999999999999999999999999999999999",po,w,j,kk)
	# 						if j != w and j != po:
	# 							for y in backtrace_path:
	# 								if j == y:
	# 									flag10=1
	# 									po=kk
	# 							if flag10 == 0:
	# 								dd=distance(j,end)
	# 								if dd <= min2:
	# 									flag101=1
	# 									# print("xsftcdstttttttttttttttttttt",min,kk,j,q,w,flag10)
	# 									min2=dd
	# 									kk=j
	# 					if flag101 == 1:
	# 						flag10=0
	# 						backtrace_path.append(kk)
	# 						w=q
	# 						# print("------------",w)
	# 						min2=100
	# 						# print("yyyyyyyyyyyyyyyyyyyy",backtrace_path)
	# 					if flag10 == 1:
	# 						backtrace_path=backtrace_path[:-1]
	# 						ll=kk
	# 						kk=backtrace_path[-1]
	# 						w=backtrace_path[-2]
	# 						# print("ooooooooooooooooooooooooooooooooooooooooooooooooooo",kk,backtrace_path)
	# 				# if flag == 1:
	# 				# 	backtrace_path.append(kk)
	# 			# print(backtrace_path)
	# 			break

	# 		x=k
	# 		# backtrace_path=backtrace_path[:-1]
	# 		k=ooo
	# 		# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",k)
	# 		flag2=1	
	##################################################


	return backtrace_path

def paths_to_moves(paths, traffic_signal):

	"""
	Purpose:
	---
	This function takes the list of all nodes produces from the path planning algorithm
	and connecting both start and end nodes

	Input Arguments:
	---
	`paths` :	[ list of all nodes ]
			list of all nodes connecting both start and end nodes (SHORTEST PATH)
	`traffic_signal` : [ list of all traffic signals ]
			list of all traffic signals
	---
	`moves` : [ list of moves from start to end nodes ]
			list containing moves for the bot to move from start to end

			Eg. : ['UP', 'LEFT', 'UP', 'UP', 'RIGHT', 'DOWN']
	
	Example call:
	---
	moves = paths_to_moves(paths, traffic_signal)
	"""    
	
	list_moves=[]

	##############	ADD YOUR CODE HERE	##############
	# print(paths,traffic_signal)
	k=len(paths)
	kk=k-1
	flag=0
	flag1=0
	dir='l'
	for i in range(0,kk):
		# print("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",i)
		o=i+1
		# print(i,o)
		# print(paths[i],paths[o],list_moves)
		q=paths[i]
		w=paths[i+1]
		r=paths[i-1]
		flag=0
		for j in traffic_signal:
			if q==j:
				flag=1
			if w==j:
				flag1=1
		fag2=0
		fak=0
		if flag == 0 or flag ==1:
			if flag == 1:
				list_moves.append("WAIT_5")
			q1=q[0]
			# print("((((((((((",q1)
			q11=ord(q1)
			q2=q[1]
			# print("(((((((((((",q2)
			q2=int(q2)
			w1=w[0]
			w11=ord(w1)
			w2=w[1]
			w2=int(w2)
			z1=r[0]
			z11=ord(z1)
			z2=r[1]
			z2=int(z2)
			r=q2- w2
			r1=q11-w11
			# print("----------",q11,w11,r1,r,dir)
			if i == 0 and dir == 'l':
				# print("jrmrmermjcje")
				fag2=1
				if r1==0 and r > 0 :
					list_moves.append("STRAIGHT")
					dir='N'

				if r1==0 and r < 0:
					list_moves.append("STRAIGHT")
					dir='S'
				if r==0 and r1 < 0:
					list_moves.append("RIGHT")
					dir='W'
				if r==0 and r1 > 0:
					list_moves.append("LEFT")
					dir='E'

			# if z11==q11==w11:
			# 	list_moves.append("STRAIGHT")
			# 	fag=1
			if dir == 'N' and fag2 == 0 and fak == 0:
				fak=1
				if r1==0 and r > 0 and fag2 == 0:
					list_moves.append("STRAIGHT")
					dir='N'
				if r1==0 and r < 0 and fag2 == 0:
					list_moves.append("LEFTTTTT")
				if r==0 and r1 > 0:
					list_moves.append("LEFT")
					dir='E'
				if r==0 and r1 < 0:
					list_moves.append("RIGHT")
					dir='W'
				# print("north",dir)
			if dir == 'S' and fag2 == 0 and fak == 0:
				fak=1
				if r1==0 and r > 0 and fag2 == 0:
					list_moves.append("STRAIGHT")
					dir='S'
				if r1==0 and r < 0 and fag2 == 0:
					list_moves.append("STRAIGHT")
				if r==0 and r1 > 0:
					list_moves.append("RIGHT")
					dir='E'
				if r==0 and r1 < 0:
					list_moves.append("LEFT")
					dir='W'
				# print("south",dir)
			if dir == 'E' and fag2 == 0 and fak == 0:
				fak=1
				if r1==0 and r > 0 and fag2 == 0:
					list_moves.append("RIGHT")
					dir='N'
				if r1==0 and r < 0 and fag2 == 0:
					list_moves.append("LEFT")
					dir='S'
				if r==0 and r1 > 0:
					list_moves.append("STRAIGHT")
					dir='E'
				if r==0 and r1 < 0:
					list_moves.append("RIGHT")
					dir='W'
				# print("east",dir)
			if dir == 'W' and fag2 == 0 and fak == 0:
				fak=1
				if r1==0 and r > 0 and fag2 == 0:
					list_moves.append("LEFT")
					dir='N'
				if r1==0 and r < 0 and fag2 == 0:
					list_moves.append("RIGHT")
					dir='S'
				if r==0 and r1 > 0:
					list_moves.append("STRAIGHT")
					dir='E'
				if r==0 and r1 < 0:
					list_moves.append("STRAIGHT")
					dir='W'
				# print("west",dir)

		# if flag == 1:
		# 		list_moves.append("WAIT_5")
		# print(list_moves)


	
	#################################################
	# print(paths,traffic_signal)
	return list_moves
def path_planning_new(graph,start,end,min,backtrace_path):
	k=start
	min2=min
	# min=distance(start,end)
	for i in graph[k]:
		d=distance(i,end)
		print(i,d,min,backtrace_path)
		if d < min2:
			min=d
			backtrace_path.append(i)
			print(backtrace_path,min)
			backtrace_path=path_planning_new(graph,i,end,min,backtrace_path)
			print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",backtrace_path[-1])
			if backtrace_path[-1] == end:
				return backtrace_path
		if min == 0  :
			return backtrace_path
	print("uuuuuuuuuuuuu",backtrace_path)
	backtrace_path=backtrace_path[:-1]
	print(backtrace_path)
	return backtrace_path
def path_planning_new_2(graph,start,end,backtrace_path):
				l=[]
				o=start
				po='pp'
				# print(backtrace_path)
				# l=path(end,graph,backtrace_path)z
				flag=0
				min2=100
				min=20
				kk=start
				# print("@@@@@@@@@@@@@@@@@@@@@@",kk)
				while kk != end:
					flag=0
					fag=1	
					flag10=0
					flag101=0
					for i in graph[kk]:
						# print("###################################################################################")
						if fag == 1:
							q=kk
							# print(q)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
							fag=0
						# print(i)
						d=distance(i,end)
						if d < min:
							# print("%%%%%%%%",d,min)
							min = d
							# print(kk)
							# q=kk
							kk=i
							flag=1
					if flag == 0:   
						for j in graph[kk]:
							flag10=0
							# print("99999999999999999999999999999999999999999",po,w,j,kk)
							if j != w and j != po:
								for y in backtrace_path:
									if j == y:
										flag10=1
										po=kk
								if flag10 == 0:
									dd=distance(j,end)
									if dd <= min2:
										flag101=1
										# print("xsftcdstttttttttttttttttttt",min,kk,j,q,w,flag10)
										min2=dd
										kk=j
						if flag101 == 1:
							flag10=0
							backtrace_path.append(kk)
							w=q
							# print("------------",w)
							min2=100
							# print("yyyyyyyyyyyyyyyyyyyy",backtrace_path)
						if flag10 == 1:
							backtrace_path=backtrace_path[:-1]
							ll=kk
							kk=backtrace_path[-1]
							w=backtrace_path[-2]
							# print("ooooooooooooooooooooooooooooooooooooooooooooooooooo",kk,backtrace_path)
					if flag == 1:
						w=kk
						backtrace_path.append(kk)
				print(backtrace_path)
				return backtrace_path

def distance(i,end):
    c=i[0]
    w=ord(c)
    w1=i[1]
    w1=int(w1)
    c1=end[0]
    q=ord(c1)
    q1=end[1]
    q1=int(q1)
    r=w1-q1
    if r < 0:
        r=-r
    r1=w-q
    if r1 < 0:
        r1=-r1
    f=r1+r
    return f
def path(end,graph,li):
	k=li[2]
	# print(type(k),end)
	flag=0
	while k != end:
		for i in graph(k):
			# print(i)
			d=distance(i,end)
			if d <= min:
				min = d
				k=i
				flag=1
		if flag == 0:
			for j in graph(k):
				if j != q:
					dd=distance(j,end)
					if dd < min2:
						min2=dd
						k=j
		li.append(k)
		q=k  

######### YOU ARE NOT ALLOWED TO MAKE CHANGES TO THIS FUNCTION #########	

if __name__ == "__main__":

	# # path directory of images
	img_dir_path = "test_images/"

	for file_num in range(0,10):
			
			img_key = 'maze_00' + str(file_num)
			img_file_path = img_dir_path + img_key  + '.png'
			# read image using opencv
			image = cv2.imread(img_file_path)
			
			# detect the arena parameters from the image
			arena_parameters = detect_arena_parameters(image)

			print('\n============================================')
			print("IMAGE: ", file_num)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
			print(arena_parameters["start_node"], "->>> ", arena_parameters["end_node"] )

			# path planning and getting the moves
			back_path=path_planning(arena_parameters["paths"], arena_parameters["start_node"], arena_parameters["end_node"])
			moves=paths_to_moves(back_path,arena_parameters["traffic_signals"])

			print("PATH PLANNED: ", back_path)
			print("MOVES TO TAKE: ", moves)

			# display the test image
			cv2.imshow("image", image)
			cv2.waitKey(0)
			cv2.destroyAllWindows()
