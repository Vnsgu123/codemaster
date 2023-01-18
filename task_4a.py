'''
*****************************************************************************************
*
*        =================================================
*             Pharma Bot Theme (eYRC 2022-23)
*        =================================================
*
*  This script is intended for implementation of Task 4A
*  of Pharma Bot (PB) Theme (eYRC 2022-23).
*
*  Filename:			task_4a.py
*  Created:
*  Last Modified:		02/01/2023
*  Author:				e-Yantra Team
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
# Filename:			task_4a.py
# Functions:		[ Comma separated list of functions in this file ]
# 					
####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
##############################################################
import numpy as np
import cv2
from zmqRemoteApi import RemoteAPIClient
import zmq
import os
import time
##############################################################

################# ADD UTILITY FUNCTIONS HERE #################

##############################################################

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

if __name__ == "__main__":
    client = RemoteAPIClient()
    sim = client.getObject('sim')

    # path directory of images in test_images folder
    img_dir = os.getcwd() + "\\test_imgs\\"

    i = 0
    config_img = cv2.imread(img_dir + 'maze_' + str(i) + '.png')

    print('\n============================================')
    print('\nFor maze_0.png')

    # object handles of each model that gets imported to the scene can be stored in this list
    # at the end of each test image, all the models will be removed    
    all_models = []

    # import task_1a.py. Make sure that task_1a.py is in same folder as task_4a.py
    task_1 = __import__('task_1a')
    detected_arena_parameters = task_1.detect_arena_parameters(config_img)

    # obtain required arena parameters
    medicine_package_details = detected_arena_parameters["medicine_packages"]
    traffic_signals = detected_arena_parameters['traffic_signals']
    start_node = detected_arena_parameters['start_node']
    end_node = detected_arena_parameters['end_node']
    horizontal_roads_under_construction = detected_arena_parameters['horizontal_roads_under_construction']
    vertical_roads_under_construction = detected_arena_parameters['vertical_roads_under_construction'] 

    print("[1] Setting up the scene in CoppeliaSim")
    all_models = place_packages(medicine_package_details, sim, all_models)
    all_models = place_traffic_signals(traffic_signals, sim, all_models)
    all_models = place_horizontal_barricade(horizontal_roads_under_construction, sim, all_models)
    all_models = place_vertical_barricade(vertical_roads_under_construction, sim, all_models)
    all_models = place_start_end_nodes(start_node, end_node, sim, all_models)
    print("[2] Completed setting up the scene in CoppeliaSim")

    # wait for 10 seconds and then remove models
    time.sleep(10)
    print("[3] Removing models for maze_0.png")
    for i in all_models:
        sim.removeModel(i)

   
    choice = input('\nDo you want to run your script on all test images ? => "y" or "n": ')
    
    if choice == 'y':
        for i in range(1,5):

            print('\n============================================')
            print('\nFor maze_' + str(i) +'.png')
            config_img = cv2.imread(img_dir + 'maze_' + str(i) + '.png')

            # object handles of each model that gets imported to the scene can be stored in this list
            # at the end of each test image, all the models will be removed    
            all_models = []

            # import task_1a.py. Make sure that task_1a.py is in same folder as task_4a.py
            task_1 = __import__('task_1a')
            detected_arena_parameters = task_1.detect_arena_parameters(config_img)

            # obtain required arena parameters
            medicine_package_details = detected_arena_parameters["medicine_packages"]
            traffic_signals = detected_arena_parameters['traffic_signals']
            start_node = detected_arena_parameters['start_node']
            end_node = detected_arena_parameters['end_node']
            horizontal_roads_under_construction = detected_arena_parameters['horizontal_roads_under_construction']
            vertical_roads_under_construction = detected_arena_parameters['vertical_roads_under_construction'] 

            print("[1] Setting up the scene in CoppeliaSim")
            place_packages(medicine_package_details, sim, all_models)
            place_traffic_signals(traffic_signals, sim, all_models)
            place_horizontal_barricade(horizontal_roads_under_construction, sim, all_models)
            place_vertical_barricade(vertical_roads_under_construction, sim, all_models)
            place_start_end_nodes(start_node, end_node, sim, all_models)
            print("[2] Completed setting up the scene in CoppeliaSim")

            # wait for 10 seconds and then remove models
            time.sleep(10)
            print("[3] Removing models for maze_" + str(i) + '.png')
            for i in all_models:
                sim.removeModel(i)
            
