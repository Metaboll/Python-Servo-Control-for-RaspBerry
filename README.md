Python-Servo-Control-for-RaspBerry
=====

Python Library and program to use with Servo Pi Raspberry Pi expansion board 

Install
====

To download to your Raspberry Pi type in terminal: 

```
git clone https://github.com/Metaboll/Python-Servo-Control-for-RaspBerry.git
```
```

IMPORTANT ---> The library and program requires i2c to be enabled and python-smbus to be installed.

Follow the tutorial at [https://www.abelectronics.co.uk/kb/article/1/i2c--smbus-and-raspbian-linux](https://www.abelectronics.co.uk/kb/article/1/i2c--smbus-and-raspbian-linux) to enable i2c and install python-smbus.

The example python files in /ABElectronics_Python_Libraries/ServoPi/ will now run from the terminal.

Functions:
----------

```
set_pwm_freq(freq) 

Usage
====

To use the Servo Pi program you must to configurate the dictionary with the configuration servo robot on nanoconfig_servo.py file:
```

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
```
Next
Set three variables for pulse length
```
servoMin = 250  # Min pulse length out of 4096
servoMed = 400  # Min pulse length out of 4096
servoMax = 500  # Max pulse length out of 4096
```
Loop to move the servo on port 0 between three points
```
while (True):
  pwm.set_pwm(0, 0, servoMin)
  time.sleep(0.5)
  pwm.set_pwm(0, 0, servoMed)
  time.sleep(0.5)
  pwm.set_pwm(0, 0, servoMax)
  time.sleep(0.5)
  # use set_all_pwm to set PWM on all outputs
```
