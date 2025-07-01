## Pi-Racer Setup
#### piracer-py 패키지 설치
> 터미널 창에 아래 커맨드를 한줄씩 입력한다.
```
pip install piracer-py
sudo apt install raspi-config
sudo raspi-config
```
#### i2c 통신을 활성화
```
sudo raspi-config
```

> 3. Interface Options (또는 5 Interfacing Options) 선택
> - P5 I2C 선택
>- Yes를 선택하여 I2C 기능을 활성화한다.
> - 재부팅하라는 메시지가 나오면 재부팅한다.

> 이후 finish 하여 빠져 나온다.

---

## 배터리 OLED 활성화

#### 아래 커맨드를 터미널에 한줄씩 입력한다.
```
sudo pip3 install luma.oled
sudo pip3 install luma.core
sudo pip3 install Pillow
```

#### i2c 통신을 활성화한다.
```
sudo raspi-config
```

> 3. Interface Options (또는 5 Interfacing Options) 선택
> - P5 I2C 선택
>- Yes를 선택하여 I2C 기능을 활성화한다.
> - 재부팅하라는 메시지가 나오면 재부팅한다.



#### i2c 권한 체크
> 권한문제 발생시(PermissionError: [Errno 13] Permission denied: '/dev/i2c-1’)
```    
ls -l /dev/i2c-1
```
> 만약
```
crw-rw---- 1 root **dialout** 89, 1 Feb 20 22:24 /dev/i2c-1
```
> 으로 나온다면 사용자를 dialout, i2c 그룹에 추가 해주어야한다.
```
sudo adduser avees dialout
sudo adduser avees i2c

sudo reboot
```
#### OLED 활성화
```
python3 oled.pys
```

---
## USB CAM Setup
#### 아래 커맨드를 터미널 창에 입력한다.
```
sudo apt install ros-humble-camera-info-manager
```

---

5. oled 코드 작성

jsx
mkdir oled
cd ~/oled
gedit oled.py


아래 코드 복사하여 붙혀넣기

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

sudo reboot


이후
cd ~/oled
python3 oled.py

완료

