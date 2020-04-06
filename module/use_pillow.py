# -*- coding: utf-8 -*-
# 使用pillow模块生成字母验证码图片

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


def rndChar():
    # 随机字母
    return chr(random.randint(65, 90))


def rndColor():
    # 随机颜色1
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rndColor2():
    # 随机颜色2
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


width = 60*4  # 图像尺寸240*60
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('arial.ttf', 36)  # 创建Font对象
draw = ImageDraw.Draw(image)  # 创建Draw对象
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字
for t in range(4):
    draw.text((60*t+10, 10), rndChar(), font=font, fill=rndColor2())
image = image.filter(ImageFilter.BLUR)  # 模糊
image.save('./module/code.jpg', 'jpeg')
