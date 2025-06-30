# 2025 SEA:ME Hackathon
![포스터(기한연장)](https://github.com/user-attachments/assets/6112b1fe-1118-40ec-882d-eec1de128dbc)

During this hackathon, your mission is to develop a autonomous driving system based on PiRacer Pro. We'll provide you a Raspberry Pi 4 board.


![2025 해커톤 시스템 아키텍쳐](https://github.com/user-attachments/assets/4ab8e098-ef6f-4bd5-8b8e-cdb42a2befdd)

***
# Tutorial 4 Hackaton

# 1.RaspBerryPi ~Donkey CAR HW setting

라즈베리파이 핀 맵 번호 → donkey car 배터리 보드 핀 번호

```jsx
2번 -> 5V
4번 -> 5V
6번 -> GND

1번 -> 3V3
3번 -> SDA
5번 -> SCL
```

![image.png](attachment:10238d9e-87d7-4252-8c9b-1843cab0f1eb:image.png)

아래 완성본 참고

![image.png](attachment:b6772386-6b99-4c61-84e1-2ce0b6083884:image.png)

- 방열팬 세팅

1. 팬 나사 조립

![image.png](attachment:9bdd8e32-0803-484c-b68d-343e9fb3a824:image.png)

1. 방열 스티커 부착

![image.png](attachment:1354d18f-aba8-4303-9831-e1b509018bbb:image.png)

1. 방향 맞추어 라즈베리파이에 부착

![image.png](attachment:c7f8fade-98fb-470f-a92a-aebaaaf6a1af:image.png)

1. 팬 연장선 (암-수 점퍼선) 사용

![image.png](attachment:33a1cb6e-b7bb-4462-ade1-2839f68042ef:image.png)

1. 라즈베리 파이 핀 사용하여 전원 공급

```jsx
17번(3V3) -> 빨강선
20번(GND) -> 검정선
```

아래 핀 맵 참고

![image.png](attachment:10238d9e-87d7-4252-8c9b-1843cab0f1eb:image.png)

완성 시 사진

![image.png](attachment:98989cce-bda6-4efc-884d-1eeb501e08f5:image.png)

사용하지 않음
