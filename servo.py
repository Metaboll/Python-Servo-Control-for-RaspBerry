#! /usr/bin/python

import time

#from ABE_ServoPi import PWM
import time
#from ABE_helpers import ABEHelpers
from nanoconfig_servo import ergo_servo_config



class servo_robot(object):

	def __init__(self):
		pass
		self.set_robot(ergo_servo_config)

	def set_robot(self, datos_servo_robot):
		self.servo_robot = datos_servo_robot
		#print self.servo_robot["motors"]
		#print self.servo_robot.has_key("motors")
		
		a = [ 22, -3 , 5 ]
		
		self.goto_dic_position(a)
		#self.i2c_helper = ABEHelpers()
		#self.bus = self.i2c_helper.get_smbus()
		#self.pwm = PWM(self.bus, 0x40)
		#self.pwm.set_pwm(0, 0, servoMed)


	def gira(self , elemento , angulo):
		#print " gira tuuuuuuuuuuuuuuuuu"
		
	
		self.robot.motors[elemento].goto_position( angulo , 0.5 )
		


	def set_position(self , a ):
		
		t = [a[0],a[1],a[2],a[3],a[4], a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13],a[14],0,0,0]
		#goto_dic_position(robot, t , 0.5)
		self.goto_dic_position( t , 0.5)

		time.sleep(2)	


	def goto_dic_position(  self, my_array, f = 0 ):
		item = 0
		#self.robot.pie_i.goto_position( my_array[0] , f )
		for key, value in self.servo_robot["motors"].iteritems():
			new_value_servo = my_array[item]
			item = item + 1
			num_servo = value["servo"]
			max_value_servo = value["max"]
			min_value_servo = value["min"]			
			if new_value_servo < min_value_servo:
				new_value_servo = min_value_servo
			if new_value_servo > max_value_servo:
				new_value_servo = max_value_servo
			print new_value_servo
			self.pwm.set_pwm(num_servo, 0, new_value_servo)


