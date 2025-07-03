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
