# Donkey Car & RaspBerry Pi HW Setup

## Step 1.
> 아래 PDF 파일을 참고하여, Donkey Car와 Raspberry Pi를 조립한다.

[Piracer_pro_ai_kit-en2.pdf](https://github.com/user-attachments/files/20992632/Piracer_pro_ai_kit-en2.pdf)

라즈베리파이 핀 맵 번호 → donkey car 배터리 보드 핀 번호


| 1번 -> 3V3 | 2번 -> 5V |
|:------:|:------:|
| 3번 -> SDA | 4번 -> 5V |
| 5번 -> SCL | 6번 -> GND |


<p align="left">
  <img src="../img/7_rotated.png" alt="1" width="400" />
</p>

아래 완성본 참고
<p align="left">
  <img src="../img/2.png" alt="1" width="400" />
</p>

- 방열팬 세팅

1. 팬 나사 조립
<p align="left">
  <img src="../img/3.png" alt="1" width="400" />
</p>



3. 방열 스티커 부착
<p align="left">
  <img src="../img/4.png" alt="1" width="400" />
</p>



5. 방향 맞추어 라즈베리파이에 부착
<p align="left">
  <img src="../img/5.png" alt="1" width="400" />
</p>



7. 팬 연장선 (암-수 점퍼선) 사용

<p align="left">
  <img src="../img/6.png" alt="1" width="400" />
</p>

5. 라즈베리 파이 핀 사용하여 전원 공급
```jsx
17번(3V3) -> 빨강선
20번(GND) -> 검정선
```

아래 핀 맵 참고
<p align="left">
  <img src="../img/7_rotated.png" alt="1" width="400" />
</p>


완성 시 사진

<p align="left">
  <img src="../img/8.png" alt="1" width="400" />
</p>


사용하지 않음

<p align="left">
  <img src="../img/9.png" alt="1" width="400" />
</p>

