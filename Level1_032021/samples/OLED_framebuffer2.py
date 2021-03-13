from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
#i2c = I2C(scl=Pin(21), sda=Pin(22), freq=400000)
i2c = I2C(scl=Pin(18), sda=Pin(19), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

import framebuf

# FrameBuffer needs 2 bytes for every RGB565 pixel
# classframebuf.FrameBuffer(buffer, width, height, format, stride=width, /)
fbuf = framebuf.FrameBuffer(bytearray(10 * 100 * 2), 10, 100, framebuf.MONO_HLSB)

fbuf.fill(0)
fbuf.text('MicroPython!', 0, 0, 0xffff)
fbuf.hline(0, 10, 96, 0xffff)

#fbuf.fill(1)
oled.blit(fbuf, 10, 1) 
oled.show()