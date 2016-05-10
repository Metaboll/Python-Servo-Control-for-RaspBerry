"""
The config module allows the definition of the structure of your robot.

Configuration are written as Python dictionary so you can define/modify them programmatically. You can also import them form file such as JSON formatted file. In the configuration you have to define:

* controllers: For each defined controller, you can specify the port name, the attached motors and the synchronization mode.
* motors: You specify all motors belonging to your robot. You have to define their id, type, orientation, offset and angle_limit.
* motorgroups: It allows to define alias of group of motors. They can be nested.

"""

ergo_servo_config = {
    
    'motors': {
        'nuca1': {
            'servo': 0,
            'orientation': 'indirect',
            'offset':0,#positivo mirando hacia afuera
            'min': 0,
            'max': 40,	
        },
        'nuca2': {
            'servo': 2,
            'orientation': 'indirect',
            'offset':0,#positivo mirando hacia afuera
            'min': 0,
            'max': 40,	
        },

    }, # motors
}
