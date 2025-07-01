
# Pi-Racer 구동 환경 설정

## Step.1 local setting

cpp
pip install piracer-py
sudo apt install raspi-config

sudo raspi-config


이후 finish 하여 빠져 나올 것

## Step.2 배터리 OLED 활성화

1. 의존성 체크(Tip 한줄씩 붙혀넣기할것)

jsx

sudo pip3 install luma.oled
sudo pip3 install luma.core
sudo pip3 install Pillow


2. i2c 활성화 

jsx
sudo raspi-config


- 3 Interface Options (또는 5 Interfacing Options) 선택
- P5 I2C 선택
- Yes를 선택하여 I2C 기능을 활성화합니다.
- 재부팅하라는 메시지가 나오면 재부팅합니다.

- 권한문제 발생시(PermissionError: [Errno 13] Permission denied: '/dev/i2c-1’)
    
    2-1. i2c 권한 체크
    
    
jsx
    ls -l /dev/i2c-1

    
    만약
    
    
jsx
    crw-rw---- 1 root **dialout** 89, 1 Feb 20 22:24 /dev/i2c-1

    
    으로 나온다면 그룹추가 해주어야함
    
    2-2. 사용자 계정을 dialout 그룹에 추가
    
    
jsx
    sudo adduser avees dialout
    sudo reboot

    
    이후
    
    
jsx
    python3 oled.pys

    
3. 사용자 계정을 i2c 그룹에 추가

I2C가 활성화되었는지 확인한 후, 현재 로그인된 사용자(여기서는 avees)를 i2c 그룹에 추가합니다.

이 명령을 실행하면 avees 사용자가 i2c 그룹에 추가됩니다.

4. oled 코드 작성

jsx
mkdir oled
cd ~/oled
gedit oled.py


아래 코드 복사하여 붙혀넣기

jsx
import time
from board import SCL, SDA
import busio
from adafruit_ina219 import INA219

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, ssd1309
from PIL import ImageFont, ImageDraw, Image

i2c_bus = busio.I2C(SCL, SDA)
ina219 = INA219(i2c_bus)

MAX_VOLTAGE = 16.8

MIN_VOLTAGE = 12.0

def get_battery_percentage(voltage):
    if voltage >= MAX_VOLTAGE:
        return 100
    elif voltage <= MIN_VOLTAGE:
        return 0
    else:

        percentage = ((voltage - MIN_VOLTAGE) / (MAX_VOLTAGE - MIN_VOLTAGE)) * 100
        return round(percentage)

serial = i2c(port=1, address=0x3C) 
device = ssd1306(serial)

try:
    font = ImageFont.truetype("DejaVuSans.ttf", 20) 
except IOError:
    font = ImageFont.load_default() 

try:
    while True:
        voltage = ina219.bus_voltage + ina219.shunt_voltage
        current = ina219.current
        power = ina219.power

        battery_percent = get_battery_percentage(voltage)

        with canvas(device) as draw:
            draw.text((0, 0), f"Volt: {voltage:.2f}V", font=font, fill="white")
            draw.text((0, 32), f"Batt: {battery_percent}%", font=font, fill="white")
            # draw.text((0, 32), f"Curr: {current:.2f}mA", font=font, fill="white")

        print(f"Voltage: {voltage:.2f}V, Current: {current:.2f}mA, Power: {power:.2f}W, Battery: {battery_percent}%")
        time.sleep(1) 

except KeyboardInterrupt:
    with canvas(device) as draw:
        draw.text((0, 0), "Monitoring Off", font=font, fill="white")
    time.sleep(1)


5. 재부팅 및 실행

jsx
sudo reboot


이후
jsx
cd ~/oled
python3 oled.py

완료

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



**🔧 완료 🔧**
