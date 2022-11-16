'''
*****************************************************************************************
*
*        =================================================
*             Pharma Bot Theme (eYRC 2022-23)
*        =================================================
*                                                         
*  This script is intended for implementation of Task 2A   
*  of Pharma Bot (PB) Theme (eYRC 2022-23).
*
*  Filename:			task_2a.py
*  Created:				
*  Last Modified:		8/10/2022
*  Author:				e-Yantra Team
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*****************************************************************************************
'''

# Team ID:			[ Team-ID ]
# Author List:		[ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:			task_2a.py
# Functions:		control_logic, detect_distance_sensor_1, detect_distance_sensor_2
# 					[ Comma separated list of functions in this file ]
# Global variables:	
# 					[ List of global variables defined in this file ]

####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
##############################################################
from difflib import diff_bytes
import  sys
import traceback
import time
import os
import math
from zmqRemoteApi import RemoteAPIClient
import zmq
##############################################################

def control_logic(sim):
	"""
	Purpose:
	---
	This function should implement the control logic for the given problem statement
	You are required to actuate the rotary joints of the robot in this function, such that
	it traverses the points in given order

	Input Arguments:
	---
	`sim`    :   [ object ]
		ZeroMQ RemoteAPI object

	Returns:
	---
	None

	Example call:
	---
	control_logic(sim)
	"""
	##############  ADD YOUR CODE HERE  ##############
	defaultIdleFps = sim.getInt32Param(sim.intparam_idle_fps)
	sim.setInt32Param(sim.intparam_idle_fps, 0)


	# q=objectHandle=sim.getObject("/distance_sensor_1")
	# w=objectHandle=sim.getObject("/distance_sensor_2")
	e=objectHandle=sim.getObject("/left_joint")
	r=objectHandle=sim.getObject("/right_joint")
	t=objectHandle=sim.getObject("/right_wheel")
	y=objectHandle=sim.getObject("/left_joint")
	# list=[]
	# list.append(0)
	# list.append(0)
	# list.append(0)
	list=[]
	list.append(30.0)
	# list1.append(0)
	# list1.append(0)
	# sim.setJointTargetForce(e,0)
	# sim.setJointTargetForce(r,0)
	# sim.addForceAndTorque(y,list,list1)
	# sim.addForceAndTorque(t,list,list1)
	# linearVelocity,angularVelocity=sim.getObjectVelocity(e)
	# linearVelocity1,angularVelocity=sim.getObjectVelocity(r)


	sim.setJointTargetVelocity(e,3)
	sim.setJointTargetVelocity(r,3)
	t6=1
	bb=1
	while bb:
		t=t2=t3=t4=t5=1
		m=m2=m3=m4=m5=1
		t6=1
		m6=1
		t7=1
		m7=1
		t8=t9=t10=1
		m8=m9=m10=1
		w=1
		p=1
		while t:
			distance_1 = detect_distance_sensor_1(sim)
			distance_2 = detect_distance_sensor_2(sim)
			# print(distance_1)
			# print(distance_2)
			diff=distance_1 - distance_2
			# print("--------",diff)
			if diff < 0.051 and diff > -0.065:
				# print("iiiiii")
				t=0
				# yy=1s
				sim.setJointTargetVelocity(r,0.7)
				sim.setJointTargetVelocity(e,-0.7)
				# sim.setJointTargetVelocity(r,)160
		while m:
			distance_11 = detect_distance_sensor_1(sim)
			distance_22 = detect_distance_sensor_2(sim)
			# print(distance_22,distance_11)
			if (distance_11==0) and (distance_22 >= 0.150 and distance_22 <= 0.1894):
				# print("@@@@@@@")
				# sim.setJointTargetVelocity(r,0)s
				# sim.setJointTargetVelocity(e,0)
				# sim.setJointTargetVelocity(r,2)
				sim.setJointTargetVelocity(e,0.7)

				# time.sleep(0.5)			
				# resultt=sim.pauseSimulation()
				# time.sleep(5)
				# sim.startSimulation()
				# sim.setJointTargetVelocity(r,0)
				m=0
		sim.setJointTargetVelocity(r,1)
		sim.setJointTargetVelocity(e,1)
		while t2:
			distance_1 = detect_distance_sensor_1(sim)
			distance_2 = detect_distance_sensor_2(sim)
			# print(distance_1)
			# print(distance_2)
			diff=distance_1 - distance_2
			# print("--------",diff)
			if diff < 0.02 and diff > -0.017:
				# print("iiiiii")
				t2=0
				# yy=1s
				sim.setJointTargetVelocity(r,0.7)
				sim.setJointTargetVelocity(e,-0.7)
				# sim.setJointTargetVelocity(r,)
		while m2:
			distance_11 = detect_distance_sensor_1(sim)
			distance_22 = detect_distance_sensor_2(sim)
			# print(distance_22,distance_11)
			if (distance_11==0) and (distance_22 >= -0.1705 and distance_22 <= 0.19925):
				# print("@@@@@@@")
				# sim.setJointTargetVelocity(r,0)0.175
				# sim.setJointTargetVelocity(e,0)
				# sim.setJointTargetVelocity(r,2)
				sim.setJointTargetVelocity(e,0.7)

				# time.sleep(0.5)			
				# resultt=sim.pauseSimulation()
				# time.sleep(5)
				# sim.startSimulation()
				# sim.setJointTargetVelocity(r,0)
				m2=0
		sim.setJointTargetVelocity(r,1)
		sim.setJointTargetVelocity(e,1)
		sim.setJointTargetVelocity(r,1)
		sim.setJointTargetVelocity(e,1)

		while t3:
			distance_3 = detect_distance_sensor_3(sim)
			distance_1 = detect_distance_sensor_1(sim)
			# print(distance_1)
			# print(distance_3)
			diff=distance_3 - distance_1
			# print("--------",diff)
			if diff > 0.015 and diff < 0.03 and distance_3 > 0:
				# print("iiiiii")
				t3=0
				# yy=1s
				sim.setJointTargetVelocity(e,0.7)
				sim.setJointTargetVelocity(r,-0.7)
				# sim.setJointTargetVelocity(r,)
		while m3:
			distance_11 = detect_distance_sensor_1(sim)
			distance_33 = detect_distance_sensor_3(sim)
			# print(distance_33,distance_11)
			if (distance_11==0) and (distance_33 >= 0.150 and distance_33 <= 0.1672):
				# print("@@@@@@@")
				# sim.setJointTargetVelocity(r,0)0.1735
				# sim.setJointTargetVelocity(e,0)
				# sim.setJointTargetVelocity(r,2)
				sim.setJointTargetVelocity(r,0.7)

				# time.sleep(0.5)			
				# resultt=sim.pauseSimulation()
				# time.sleep(5)
				# sim.startSimulation()
				# sim.setJointTargetVelocity(r,0)
				m3=0
		sim.setJointTargetVelocity(r,1)
		sim.setJointTargetVelocity(e,1)
		sim.setJointTargetVelocity(r,1.5)
		sim.setJointTargetVelocity(e,1.5)
		while t4:
			distance_3 = detect_distance_sensor_3(sim)
			distance_1 = detect_distance_sensor_1(sim)
			# print(distance_1)
			# print(distance_3)
			diff=distance_1 - distance_3
			# print("--------",diff)
			if diff < 0.007 and diff > -0.01 and distance_3 > 0:
				# print("iiiiii")
				t4=0
				# yy=1s
				sim.setJointTargetVelocity(e,0.7)
				sim.setJointTargetVelocity(r,-0.7)

				# sim.setJointTargetVelocity(r,)
		while m4:
			distance_11 = detect_distance_sensor_1(sim)
			distance_33 = detect_distance_sensor_3(sim)
			# print(distance_33,distance_11)
			if (distance_11==0) and (distance_33 >= 0.140 and distance_33 <= 0.1702):
				# print("@@@@@@@")
				# sim.setJointTargetVelocity(r,0)0.159
				# sim.setJointTargetVelocity(e,0)
				# sim.setJointTargetVelocity(r,2)
				sim.setJointTargetVelocity(r,0.7)

				# time.sleep(0.5)			
				# resultt=sim.pauseSimulation()
				# time.sleep(5)
				# sim.startSimulation()
				# sim.setJointTargetVelocity(r,0)
				m4=0
		sim.setJointTargetVelocity(r,1)
		sim.setJointTargetVelocity(e,1)
		sim.setJointTargetVelocity(r,2)
		sim.setJointTargetVelocity(e,2)

		while t5:
			distance_3 = detect_distance_sensor_3(sim)
			distance_1 = detect_distance_sensor_1(sim)
			# print(distance_1)
			# print(distance_3)
			diff=distance_1 - distance_3
			# print("--------",diff)
			if diff < 0.02 and diff > -0.01 and distance_3 > 0:
				# print("iiiiii")
				t5=0
				# yy=1s
				sim.setJointTargetVelocity(e,0.7)
				sim.setJointTargetVelocity(r,-0.7)

				# sim.setJointTargetVelocity(r,)
		while m5:
			distance_11 = detect_distance_sensor_1(sim)
			distance_33 = detect_distance_sensor_3(sim)
			# print(distance_33,distance_11)
			if (distance_11==0) and (distance_33 >= -0.220 and distance_33 <= 0.1799):
				# print("@@@@@@@")
				# sim.setJointTargetVelocity(r,0)0.225
				# sim.setJointTargetVelocity(e,0)
				# sim.setJointTargetVelocity(r,2)
				sim.setJointTargetVelocity(r,0.7)

				# time.sleep(0.5)			
				# resultt=sim.pauseSimulation()
				# time.sleep(5)
				# sim.startSimulation()
				# sim.setJointTargetVelocity(r,0)
				m5=0
		sim.setJointTargetVelocity(r,1)
		sim.setJointTargetVelocity(e,1)
		sim.setJointTargetVelocity(r,2)
		sim.setJointTargetVelocity(e,2)
		sim.setJointTargetVelocity(r,1)
		sim.setJointTargetVelocity(e,1)

		while t6:
			distance_1 = detect_distance_sensor_1(sim)
			distance_2 = detect_distance_sensor_2(sim)
			# print(distance_1)
			# print(distance_2)
			diff=distance_1 - distance_2
			# print("--------",diff)
			if diff < 0.0450 and diff > -0.0450 and distance_2 > 0:
				# print("iiiiii")
				t6=0
				# yy=1s
				sim.setJointTargetVelocity(r,0.7)
				sim.setJointTargetVelocity(e,-0.7)
				# sim.setJointTargetVelocity(r,)
		while m6:
			distance_11 = detect_distance_sensor_1(sim)
			distance_22 = detect_distance_sensor_2(sim)
			# print(distance_22,distance_11)
			if (distance_11==0) and (distance_22 >= 0.166 and distance_22 <= 0.2586):
				# print("@@@@@@@")
				# sim.setJointTargetVelocity(r,0)0.1938
				# sim.setJointTargetVelocity(e,0)
				# sim.setJointTargetVelocity(r,2)
				sim.setJointTargetVelocity(e,0.7)

				# time.sleep(0.5)			
				# resultt=sim.pauseSimulation()
				# time.sleep(5)
				# sim.startSimulation()
				# sim.setJointTargetVelocity(r,0)
				m6=0
		sim.setJointTargetVelocity(r,1)
		sim.setJointTargetVelocity(e,1)
		while t7:
			distance_1 = detect_distance_sensor_1(sim)
			distance_2 = detect_distance_sensor_2(sim)
			# print(distance_1)
			# print(distance_2)
			diff=distance_1 - distance_2
			# print("--------",diff)
			if (diff < 0.017 and diff > -0.003) and (distance_2 > 0):
				# print("iiiiii")
				t7=0
				# yy=1s
				sim.setJointTargetVelocity(r,0.7)
				sim.setJointTargetVelocity(e,-0.7)
				# sim.setJointTargetVelocity(r,)0.407s
		while m7:
			distance_11 = detect_distance_sensor_1(sim)
			distance_22 = detect_distance_sensor_2(sim)
			# print(distance_22,distance_11)
			if (distance_11==0) and (distance_22 >= 0.166 and distance_22 <= 0.2507):
				# print("@@@@@@@")
				# sim.setJointTargetVelocity(r,0)0.1797
				# sim.setJointTargetVelocity(e,0)
				# sim.setJointTargetVelocity(r,2)
				sim.setJointTargetVelocity(e,0.7)

				# time.sleep(0.5)			
				# resultt=sim.pauseSimulation()
				# time.sleep(5)
				# sim.startSimulation()
				# sim.setJointTargetVelocity(r,0)
				m7=0
		# sim.setJointTargetVelocity(r,1)
		# sim.setJointTargetVelocity(e,1)

		while t8:
			distance_3 = detect_distance_sensor_3(sim)
			distance_1 = detect_distance_sensor_1(sim)
			# print(distance_1)
			# print(distance_3)
			diff= distance_3 - distance_1
			# print("--------",diff)
			if diff < 0.043 and diff > 0.025 and  distance_3 > 0:
				# print("iiiiii")
				t8=0
				# yy=1s
				sim.setJointTargetVelocity(e,0.7)
				sim.setJointTargetVelocity(r,-0.7)

				# sim.setJointTargetVelocity(r,)
		while m8:
			distance_11 = detect_distance_sensor_1(sim)
			distance_33 = detect_distance_sensor_3(sim)
			# print(distance_33,distance_11)
			if (distance_11==0) and (distance_33 >= 0.120 and distance_33 <= 0.13139):
				# print("@@@@@@@")
				# sim.setJointTargetVelocity(r,0)0.1732
				# sim.setJointTargetVelocity(e,0)
				# sim.setJointTargetVelocity(r,2)
				sim.setJointTargetVelocity(r,0.7)

				# time.sleep(0.5)			
				# resultt=sim.pauseSimulation()
				# time.sleep(5)
				# sim.startSimulation()
				# sim.setJointTargetVelocity(r,0)
				m8=0
		sim.setJointTargetVelocity(r,1)
		sim.setJointTargetVelocity(e,1)
		sim.setJointTargetVelocity(r,2)
		sim.setJointTargetVelocity(e,2)
		sim.setJointTargetVelocity(r,1)
		sim.setJointTargetVelocity(e,1)

		while t9:
			distance_3 = detect_distance_sensor_3(sim)
			distance_1 = detect_distance_sensor_1(sim)
			# print(distance_1)
			# print(distance_3)
			diff= distance_1 - distance_3
			# print("--------",diff)
			if diff < 0.0154 and diff > -0.009035 and  distance_3 > 0:
				# print("iiiiii")
				t9=0
				# yy=1s
				sim.setJointTargetVelocity(e,0.7)
				sim.setJointTargetVelocity(r,-0.7)

				# sim.setJointTargetVelocity(r,)0.1872
		while m9:
			distance_11 = detect_distance_sensor_1(sim)
			distance_33 = detect_distance_sensor_3(sim)
			# print(distance_33,distance_11)
			if (distance_11==0) and (distance_33 >= 0.120 and distance_33 <= 0.21040):
				# print("@@@@@@@")
				# sim.setJointTargetVelocity(r,0)0.1749
				# sim.setJointTargetVelocity(e,0)
				# sim.setJointTargetVelocity(r,2)
				sim.setJointTargetVelocity(r,0.7)

				# time.sleep(0.5)			
				# resultt=sim.pauseSimulation()
				# time.sleep(5)
				# sim.startSimulation()
				# sim.setJointTargetVelocity(r,0)
				m9=0
    
		sim.setJointTargetVelocity(r,1)
		sim.setJointTargetVelocity(e,1)
		sim.setJointTargetVelocity(r,2)
		sim.setJointTargetVelocity(e,2)
		sim.setJointTargetVelocity(r,1)
		sim.setJointTargetVelocity(e,1)
		while t10:
			distance_3 = detect_distance_sensor_3(sim)
			distance_1 = detect_distance_sensor_1(sim)
			# print(distance_1)
			# print(distance_3)
			diff= distance_3 - distance_1
			# print("--------",diff)
			if distance_1 < 0.199 and distance_1 > 0 :
				# print("iiiiii")
				t10=0
				# yy=1s
				sim.setJointTargetVelocity(e,0)
				sim.setJointTargetVelocity(r,0)

				# sim.setJointTargetVelocity(r,)0.1872
		bb=0


	##################################################

def detect_distance_sensor_1(sim):
	"""
	Purpose:
	---
	Returns the distance of obstacle detected by proximity sensor named 'distance_sensor_1'

	Input Arguments:
	---
	`sim`    :   [ object ]
		ZeroMQ RemoteAPI object

	Returns:
	---
	distance  :  [ float ]
	    distance of obstacle from sensor

	Example call:
	---
	distance_1 = detect_distance_sensor_1(sim)
	"""
	distance = None
	##############  ADD YOUR CODE HERE  ##############

	q=objectHandle=sim.getObject("/distance_sensor_1")
	result,distance,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=sim.readProximitySensor(q)




	##################################################
	return distance

def detect_distance_sensor_2(sim):
	"""
	Purpose:
	---
	Returns the distance of obstacle detected by proximity sensor named 'distance_sensor_2'

	Input Arguments:
	---
	`sim`    :   [ object ]
		ZeroMQ RemoteAPI object

	Returns:
	---
	distance  :  [ float ]
	    distance of obstacle from sensor

	Example call:
	---
	distance_2 = detect_distance_sensor_2(sim)
	"""
	distance = None
	##############  ADD YOUR CODE HERE  ##############

	w=objectHandle=sim.getObject("/distance_sensor_2")
	result,distance,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=sim.readProximitySensor(w)



	##################################################
	return distance
def detect_distance_sensor_3(sim):
	"""
	Purpose:
	---
	Returns the distance of obstacle detected by proximity sensor named 'distance_sensor_1'

	Input Arguments:
	---
	`sim`    :   [ object ]
		ZeroMQ RemoteAPI object

	Returns:
	---
	distance  :  [ float ]
	    distance of obstacle from sensor

	Example call:
	---
	distance_1 = detect_distance_sensor_3(sim)
	"""
	distance = None
	##############  ADD YOUR CODE HERE  ##############

	q=objectHandle=sim.getObject("/distance_sensor_3")
	result,distance,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=sim.readProximitySensor(q)




	##################################################
	return distance

######### YOU ARE NOT ALLOWED TO MAKE CHANGES TO THE MAIN CODE BELOW #########

if __name__ == "__main__":
	client = RemoteAPIClient()
	sim = client.getObject('sim')

	try:

		## Start the simulation using ZeroMQ RemoteAPI
		try:
			return_code = sim.startSimulation()
			if sim.getSimulationState() != sim.simulation_stopped:
				print('\nSimulation started correctly in CoppeliaSim.')
			else:
				print('\nSimulation could not be started correctly in CoppeliaSim.')
				sys.exit()

		except Exception:
			print('\n[ERROR] Simulation could not be started !!')
			traceback.print_exc(file=sys.stdout)
			sys.exit()

		## Runs the robot navigation logic written by participants
		try:
			control_logic(sim)
			time.sleep(5)

		except Exception:
			print('\n[ERROR] Your control_logic function throwed an Exception, kindly debug your code!')
			print('Stop the CoppeliaSim simulation manually if required.\n')
			traceback.print_exc(file=sys.stdout)
			print()
			sys.exit()

		
		## Stop the simulation using ZeroMQ RemoteAPI
		try:
			return_code = sim.stopSimulation()
			time.sleep(0.5)
			if sim.getSimulationState() == sim.simulation_stopped:
				print('\nSimulation stopped correctly in CoppeliaSim.')
			else:
				print('\nSimulation could not be stopped correctly in CoppeliaSim.')
				sys.exit()

		except Exception:
			print('\n[ERROR] Simulation could not be stopped !!')
			traceback.print_exc(file=sys.stdout)
			sys.exit()

	except KeyboardInterrupt:
		## Stop the simulation using ZeroMQ RemoteAPI
		return_code = sim.stopSimulation()
		time.sleep(0.5)
		if sim.getSimulationState() == sim.simulation_stopped:
			print('\nSimulation interrupted by user in CoppeliaSim.')
		else:
			print('\nSimulation could not be interrupted. Stop the simulation manually .')
			sys.exit()