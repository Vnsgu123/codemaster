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
# Functions:		detect_all_nodes,detect_paths_to_graph, detect_arena_parameters, path_planning, paths_to_move
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
	# frame=cv2.imread('maze_14.png')
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
			cv2.drawContours(frame, [approx], 0, (0, 255, 155), 2)
			# cv2.imshow('contour',frame)
			M = cv2.moments(contour)
			if len(approx) == 4:				
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
			print("'traffic signals':",end ='')
			print(traffic_signals)

		if i==1:
			start_node=li
			print("'start node':",end ='')
			print(start_node)

		if i==2:
			end_node=li
			print("'End node':",end ='')
			print(end_node)


		# print("'traffic signals':",end ='')
		# print(li)
		li=[]

	
	##################################################

	return traffic_signals, start_node, end_node


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
	Returns:
	---
	`paths` : { dictionary }
			Every node's connection to other node
			Eg. : { "D3":{"C3", "E3", "D2", "D4" }, 
					"D5":{"C5", "D2", "D6" }  }
	Example call:
	---
	paths = detect_paths_to_graph(maze_image)
	"""    

	paths = {}

	##############	ADD YOUR CODE HERE	##############
	
	##################################################

	return paths



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
	`graph` :	[ numpy array ]
			numpy array of image returned by cv2 library
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

	##################################################

	return list_moves

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
			# print(arena_parameters["start_node"], "->>> ", arena_parameters["end_node"] )

			# path planning and getting the moves
			# back_path=path_planning(arena_parameters["paths"], arena_parameters["start_node"], arena_parameters["end_node"])
			# moves=paths_to_moves(back_path, arena_parameters["traffic_signals"])

			# print("PATH PLANNED: ", back_path)
			# print("MOVES TO TAKE: ", moves)

			# display the test image
			cv2.imshow("image", image)
			cv2.waitKey(0)
			cv2.destroyAllWindows()