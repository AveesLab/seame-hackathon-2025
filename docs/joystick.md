

---
# Set Joystick

jsx
pip3 install piracer-py


jsx
mkdir remote_control
cd remote_control


jsx
touch joystick_control.py


jsx
nano joystick_control.py


아래 코드 입력 

from piracer.vehicles import PiRacerPro
from piracer.gamepads import ShanWanGamepad

if __**name__** == '__**main__**':
	
	shanwan_gamepad = ShanWanGamepad()
	piracer = PiRacerPro()
	# piracer = PiRacerStandard()
	
	while True:
	    gamepad_input = shanwan_gamepad.read_data()
	
	    throttle = gamepad_input.analog_stick_right.y * 0.5
	    steering = -gamepad_input.analog_stick_left.x
	
	    print(f'throttle={throttle}, steering={steering}')
	
	    piracer.set_throttle_percent(throttle)
	    piracer.set_steering_percent(steering)


조이스틱 실행


---
