#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
from yaml import load

description = {
	"base00": "Default Background",
	"base01": "Lighter Background (Used for status bars)",
	"base02": "Selection Background",
	"base03": "Comments, Invisibles, Line Highlighting",
	"base04": "Dark Foreground (Used for status bars)",
	"base05": "Default Foreground, Caret, Delimiters, Operators",
	"base06": "Light Foreground (Not often used)",
	"base07": "Light Background (Not often used)",
	"base08": "Variables, XML Tags, Markup Link Text, Markup Lists, Diff Deleted",
	"base09": "Integers, Boolean, Constants, XML Attributes, Markup Link Url",
	"base0A": "Classes, Markup Bold, Search Text Background",
	"base0B": "Strings, Inherited Class, Markup Code, Diff Inserted",
	"base0C": "Support, Regular Expressions, Escape Characters, Markup Quotes",
	"base0D": "Functions, Methods, Attribute IDs, Headings",
	"base0E": "Keywords, Storage, Selector, Markup Italic, Diff Changed",
	"base0F": "Deprecated, Opening/Closing Embedded Language Tags, e.g. <?php ?>"
}

line_height = 20
current_height = 0
padding_left = 0
padding_right = 20
box_width = 60
font_ = ImageFont.truetype("DejaVuSansMono.ttf", size=15)
font_size_ = font_.getsize('(#FFFFFF) base0F - Deprecated, Opening/Closing Embedded Language Tags, e.g. <?php ?>')
text_offset = (line_height - font_size_[1]) / 2

img_height_ = 16 * line_height
img_width_ = padding_left + padding_right + box_width + font_size_[0] + padding_right

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
	
	draw.text((x1+padding_right, y0+text_offset),
	          "(#{}) {} - {}".format(v, k, description[k]),
	          fill='black',
	          font=font_)

	current_height += line_height

img.save('preview.png')
