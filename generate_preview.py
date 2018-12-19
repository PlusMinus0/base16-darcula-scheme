#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
from yaml import load

line_height = 20
current_height = 0
padding_left = 0
padding_right = 20
box_width = 60
font_ = ImageFont.truetype("DejaVuSans.ttf", size=15)
font_size_ = font_.getsize('base0F')
text_offset = (line_height - font_size_[1]) / 2

img_height_ = 16 * line_height
img_width_ = padding_left + padding_right + box_width + font_size_[0]

img = Image.new(mode='RGB',
                size=(img_width_, img_height_),
                color=(255, 255, 255))
draw = ImageDraw.Draw(img)

with open('scheme.yaml') as f:
	scheme = load(f)
	
for k, v in scheme.items():
	if 'base' not in k:
		continue

	fill_ = '#' + v

	x0 = padding_left
	x1 = x0 + box_width
	y0 = current_height
	y1 = y0 + line_height
	draw.rectangle([x0, y0, x1, y1], fill=fill_)
	
	draw.text((x1+padding_right, y0+text_offset), k, fill='black', font=font_)

	current_height += line_height

img.save('preview.png')
