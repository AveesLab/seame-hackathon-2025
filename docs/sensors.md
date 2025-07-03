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

#### OLED 활성화
```
python3 oled.py
```

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

---
## USB CAM Setup
#### 아래 커맨드를 터미널 창에 입력한다.
```
sudo apt install ros-humble-camera-info-manager
```

---
## Test
#### 하드웨어 세팅 테스트 코드
```
test.ipynb
```
