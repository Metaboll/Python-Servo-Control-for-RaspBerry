#! /usr/bin/python

import time

from ABE_ServoPi import PWM

from ABE_helpers import ABEHelpers
from nanoconfig_servo import ergo_servo_config



class servo_robot(object):

	def __init__(self):
		pass
		self.set_robot(ergo_servo_config)

	def set_robot(self, servo_configuration_robot):
		self.servo_robot = servo_configuration_robot
		
		
		
		self.i2c_helper = ABEHelpers()
		self.bus = self.i2c_helper.get_smbus()
		self.pwm = PWM(self.bus, 0x6f) # take care to know the real port
		
		self.pwm.output_enable()
		self.pwm.set_pwm_freq(60)
		#self.pwm.set_pwm(0, 0, servoMed)
		#self.goto_dic_position(a)

	def example_move(self):

		while (True):
			
			a = [ -180, 100 ]# pulses
			self.goto_dic_position(a)
			time.sleep(1)
			
			a = [ 0, 140 ]
			self.goto_dic_position(a)
			time.sleep(1)

			a = [ 180, 100 ]
			self.goto_dic_position(a)
			time.sleep(1)

	def gira(self , elemento , angulo):
		pass
		


	def set_position(self , a ):
		pass
		#t = [a[0],a[1],a[2],a[3],a[4], a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13],a[14],0,0,0]
		#goto_dic_position(robot, t , 0.5)
		#self.goto_dic_position( t , 0.5)
		#time.sleep(2)	


	def goto_dic_position_anu(  self, my_array, f = 0 ):
		item = 0
		
		for key, value in self.servo_robot["motors"].iteritems():
			grade_servo = my_array[item] # en grados
			new_value_servo = 400
			max_value_servo = value["max"]
			min_value_servo = value["min"]	
			if grade_servo < 0:
				new_value_servo= 300/180*(grade_servo + 180) + 100
				if new_value_servo < min_value_servo:
					new_value_servo = min_value_servo
			if grade_servo > 0:
				new_value_servo = 300/180*( grade_servo) + 400 
				if new_value_servo > max_value_servo:
					new_value_servo = max_value_servo
			# -180 es 100
			# 0 es 400
			# 180 es 700
			item += 1
			num_servo = value["servo"]
			#print new_value_servo
			self.pwm.set_pwm(num_servo, 0, new_value_servo)

	def goto_dic_position(  self, my_array, f = 0 ): #my_arry [ pulse length out of 4096 , ... ]
		item = 0
		
		for key, value in self.servo_robot["motors"].iteritems():
			grade_servo = my_array[item] # en grados
			
			max_value_servo = value["max"]
			min_value_servo = value["min"]	
			
			if grade_servo < min_value_servo:
					grade_servo = min_value_servo
			if grade_servo > max_value_servo:
					grade_servo = max_value_servo
			# -180 es 100
			# 0 es 400
			# 180 es 700
			item += 1
			num_servo = value["servo"]
			#print new_value_servo
			self.pwm.set_pwm(num_servo, 0, grade_servo)
