'''
*****************************************************************************************
*
*        		===============================================
*           		Pharma Bot (PB) Theme (eYRC 2022-23)
*        		===============================================
*
*  This script is to implement Task 3C of Pharma Bot (PB) Theme (eYRC 2022-23).
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
# Filename:			task_3c.py
# Functions:		[ perspective_transform, transform_values, set_values ]
# 					


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the five available  ##
## modules for this task                                    ##
##############################################################
import cv2 
import numpy 
from  numpy import interp
from zmqRemoteApi import RemoteAPIClient
import zmq
##############################################################

#################################  ADD UTILITY FUNCTIONS HERE  #######################



#####################################################################################

def perspective_transform(image):

    """
    Purpose:
    ---
    This function takes the image as an argument and returns the image after 
    applying perspective transform on it. Using this function, you should
    crop out the arena from the full frame you are receiving from the 
    overhead camera feed.

    HINT:
    Use the ArUco markers placed on four corner points of the arena in order
    to crop out the required portion of the image.

    Input Arguments:
    ---
    `image` :	[ numpy array ]
            numpy array of image returned by cv2 library 

    Returns:
    ---
    `warped_image` : [ numpy array ]
            return cropped arena image as a numpy array
    
    Example call:
    ---
    warped_image = perspective_transform(image)
    """   
    warped_image = [] 
#################################  ADD YOUR CODE HERE  ###############################

    # cv2.imshow("Frame",image) # displaying the captured frames
    # calib_data_path = "../calib_data/MultiMatrix.npz"
    # calib_data = numpy.load
    # (calib_data_path)
    # print(calib_data.files)
    # cam_mat = calib_data["camMatrix"]
    # dist_coef = calib_data["distCoef"]
    # r_vectors = calib_data["rVector"]
    # t_vectors = calib_data["tVector"]
    # print(cam_mat)
    # print(dist_coef)
    # print(r_vectors)
    # print(t_vectors)
    # h,  w = image.shape[:2]
    # print(h,w)
    # newcameramtx, roi = cv2.getOptimalNewCameraMatrix(cam_mat, dist_coef, (w,h), 1, (w,h))

    # dst = cv2.undistort(image,cam_mat, dist_coef, None, newcameramtx)
    # x, y, w, h = roi
    # print(x,y,w,h)
    # dst = dst[y:y+h, x:x+w]

    # cv2.imshow("Fram---e",dst) # displaying the captured frames
    # cv2.waitKey(5000)
    ArUco_details_dict,ArUco_corners=task_1b.detect_ArUco_details(image)
    print(ArUco_details_dict)
    print(ArUco_details_dict[1][0][1])
    y1=ArUco_details_dict[3][0][0]
    y2=ArUco_details_dict[1][0][0]
    x1=ArUco_details_dict[3][0][1]
    x2=ArUco_details_dict[1][0][1]
    print(x1,x2,y1,y2)
    warped_image=image[x1:x2,y1:y2]
    # warped_image=image
    # cv2.imshow('wraped',warped_image)
    cv2.waitKey(1)
    image_dir_path = "images"
    cv2.imwrite(f"{image_dir_path}/in{30}.png", warped_image)

######################################################################################


    return warped_image

def transform_values(image):

    """
    Purpose:
    ---
    This function takes the image as an argument and returns the 
    position and orientation of the ArUco marker (with id 5), in the 
    CoppeliaSim scene.

    Input Arguments:
    ---
    `image` :	[ numpy array ]
            numpy array of image returned by camera

    Returns:
    ---
    `scene_parameters` : [ list ]
            a list containing the position and orientation of ArUco 5
            scene_parameters = [c_x, c_y, c_angle] where
            c_x is the transformed x co-ordinate [float]
            c_y is the transformed y co-ordinate [float]
            c_angle is the transformed angle [angle]
    
    HINT:
        Initially the image should be cropped using perspective transform 
        and then values of ArUco (5) should be transformed to CoppeliaSim
        scale.
    
    Example call:
    ---
    scene_parameters = transform_values(image)
    """   
    scene_parameters = []
#################################  ADD YOUR CODE HERE  ###############################
    warped_image = perspective_transform(image)
    ArUco_details_dict,ArUco_corners=task_1b.detect_ArUco_details(warped_image)
    print(ArUco_details_dict,warped_image.shape)
    print(type(ArUco_corners),ArUco_details_dict[5][0][0])
    w=warped_image.shape[1]
    h=warped_image.shape[0]
    wm=w/2
    hm=h/2
    c1=ArUco_details_dict[5][0][0]
    c1m=wm-c1
    c2=ArUco_details_dict[5][0][1]
    c2m=c2-hm
    a1=ArUco_details_dict[5][1]
    cop1=(c1m/wm)*0.9950
    cop2=(c2m/hm)*0.9950
    # cop1=0.9950-cop1
    # print(cop1,cop2,a1)ssssss
    if a1 > 0:
        ang1=180-a1
        ang1=-ang1
    if a1 <= 0:
        ang1=180+a1
    # print(cop1,cop2,a1,ang1)
######################################################################################
    c_x=-cop1
    c_y=-cop2
    c_angle=ang1
    scene_parameters.append(c_x)
    scene_parameters.append(c_y)
    scene_parameters.append(c_angle)
    print(scene_parameters)
    return scene_parameters


def set_values(scene_parameters):
    """
    Purpose:
    ---
    This function takes the scene_parameters, i.e. the transformed values for
    position and orientation of the ArUco marker, and sets the position and 
    orientation in the CoppeliaSim scene.

    Input Arguments:
    ---
    `scene_parameters` :	[ list ]
            list of co-ordinates and orientation obtained from transform_values()
            function

    Returns:
    ---
    None

    HINT:
        Refer Regular API References of CoppeliaSim to find out functions that can
        set the position and orientation of an object.
    
    Example call:
    ---
    set_values(scene_parameters)
    """   
    # aruco_handle = sim.getObject('/aruco_5')
#################################  ADD YOUR CODE HERE  ###############################
    # client = RemoteAPIClient()
    print(scene_parameters)
    value=[]
    value.append(scene_parameters[0])
    value.append(scene_parameters[1])
    value.append(0)
    l=scene_parameters[2]
    l=int(l)

    sim = client.getObject('sim') 
    aruco_handle = sim.getObject('/aruco_5')
    m=sim.getObjectMatrix(aruco_handle,-1)
    position=sim.getObjectPosition(aruco_handle,-1)
    relativeToObjectHandle= sim.getObject('/Arena')
    axis={m[2],m[5],m[9]}
    # pose=sim.rotateAroundAxis(m,axis,position,l*0.017)
    Angle=[]
    Angle.append(0)
    Angle.append(0)
    # Angle.append(scene_parameters[2])
    Angle.append(scene_parameters[2]*0.0174444444)
    # Angle.append(-90)

    print(l)
    sim.setObjectPosition(aruco_handle,relativeToObjectHandle,value)
    sim.setObjectOrientation(aruco_handle,relativeToObjectHandle,Angle)
    # sim.setObjectMatrix(aruco_handle,-1,pose)


######################################################################################ss

    return None

def videocap():
    # video = cv2.VideoCapture(1,cv2.CAP_DSHOW) # capturing the video from overhead camera
    while 1:
        # video = cv2.VideoCapture(1,cv2.CAP_DSHOW) # capturing the video from overhead camera
        # _, frame = video.read() # capturing individual frames
        # cv2.imshow("Frame",frame) # displaying the captured frames
        # # cv2.waitKey(1) # ensuring continous capturing
        # # if cv2.waitKey(1) & 0xFF == ord('q'):
        # #     break
        # # video.release()
        # image=frame
        # scene_parameters = transform_values(image)
        # set_values(scene_parameters)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
        # i=0
        # while i != 14 :
        #     print("start")
        #     video.release()
        #     video = cv2.VideoCapture(1,cv2.CAP_DSHOW) # capturing the video from overhead camera
        #     _, frame = video.read() # capturing individual frames
        #     cv2.imshow("Frame",frame) # displaying the captured frames
        #     # video.release()
        #     print("end",i)
        #     i=i+1
        #     cv2.waitKey(1)
        # video.release()
        i=0
        while i != 14 :
            print("start")
            # video.release()
            video = cv2.VideoCapture(1,cv2.CAP_DSHOW) # capturing the video from overhead camera
            _, frame = video.read() # capturing individual frames
            cv2.imshow("Frameeee",frame) # displaying the captured frames
            print("end",i)
            i=i+1
            video.release()
            cv2.waitKey(1)
        video.release()
        image=frame
        scene_parameters = transform_values(image)
        set_values(scene_parameters)



    return None

if __name__ == "__main__":
    client = RemoteAPIClient()
    # sim = client.getObject('sim')
    task_1b = __import__('task_1b')
    print("maitrey")
    videocap()
    # frame=cv2.imread('in2.png')
    # video = cv2.VideoCapture(1,cv2.CAP_DSHOW) # capturing the video from overhead camera
    # while 1:
    #     _, frame = video.read() # capturing individual frames
    #     cv2.imshow("Frame",frame) # displaying the captured frames
    #     # cv2.waitKey(1) # ensuring continous capturing
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break
    # video.release()
    # image=frame
    # scene_parameters = transform_values(image)
    # set_values(scene_parameters)

#################################  ADD YOUR CODE HERE  ################################

#######################################################################################



    
