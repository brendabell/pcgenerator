#!/usr/local/bin/python

from xml.dom import minidom
import svgwrite
import sys


# default values

# number of overlapping blank rows at the top of the card
blank_rows = 2

# width of the side margin in mm
side_margin = 17.0

# height of one row on the card in mm
row_height = 5.0

# width of one stitch on the card in mm
stitch_width = 4.5
#stitch_width = 9.0

# radius of a pattern hole in mm
pattern_hole_radius = 3.5

# radius of a clip hole in mm
clip_hole_radius = 3.0

# radius of a sprocket hole in mm
sprocket_hole_radius = 3.5

# drawing stroke width
stroke_width='.1'

# fill color
fill_color = 'white'

# stroke_color
stroke_color = 'black'

def init():
	global ofname
	
	lines = []
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		print 'reading', filename, '...'
		with open(filename, 'r') as f:
			for line in f:
				line = line.rstrip()
				chars = []
				for char in line:
					chars.append(char)
				lines.append(chars)
		ofname = '{0}.svg'.format(filename)
	else:
		print 'using default pattern...'
		for row in range(48):
			chars = []
			for stitch in range(24):
				chars.append('X')
			lines.append(chars)
		ofname = 'punchcard.svg'
		
	return lines

def create_card():
	global card_width
	global card_height
	
	print 'creating card...'
	diagram = svgwrite.Drawing(
		ofname,
		size=(
			'{0}mm'.format(card_width),
			'{0}mm'.format(card_height)),
		viewBox=(
			'0 0 {0} {1}'.format(card_width, card_height)),
		preserveAspectRatio='none')
	
	shape_points = [
		(2, 0),
		(card_width-2, 0),
		(card_width-1, 1),
		(card_width-1, 20),
		(card_width, 22),
		(card_width, card_height-22),
		(card_width-1, card_height-20),
		(card_width-1, card_height-1),
		(card_width-2, card_height),
		(2, card_height),
		(1, card_height-1),
		(1, card_height-20),
		(0, card_height-22),
		(0, 22),
		(1, 20),
		(1, 1)]
	diagram.add(diagram.polygon(
		points=shape_points,
		fill=fill_color,
		stroke=stroke_color,
		stroke_width=stroke_width))
		
	return diagram

def draw_pattern(diagram, lines, objects):
	global card_rows
	global card_stitches
	global fill_color
	global pattern_hole_radius
	global row_color
	global row_height
	global side_margin
	global stitch_width
	global stroke_color
	global stroke_width
	
	print 'drawing pattern...'
	# main body of card
	rows = 0
	yoffset = 10.0 + (row_height / 2)
	while rows < card_rows:
		stitches = 0
		xoffset = side_margin + (stitch_width / 2)
		while stitches < card_stitches:
			if lines[rows][stitches].upper() == 'X':
				objects.append(diagram.circle(
					center=(xoffset, yoffset),
					fill=fill_color,
					r = (pattern_hole_radius / 2),
					stroke=stroke_color,
					stroke_width=stroke_width))
			stitches += 1
			xoffset += stitch_width
		rows += 1
		yoffset += row_height
		
def draw_blank_lines(diagram, objects):
	global blank_rows
	global card_stitches
	global fill_color
	global pattern_hole_radius
	global row_height
	global side_margin
	global stitch_width
	global stroke_color
	global stroke_width
	
	print 'drawing blank lines...'
	# blank rows at top
	rows = 0
	yoffset = row_height / 2
	while rows < blank_rows:
		stitches = 0
		xoffset = side_margin + (stitch_width / 2)
		while stitches < card_stitches:
			objects.append(diagram.circle(
				center=(xoffset, yoffset),
				fill=fill_color,
				r = (pattern_hole_radius / 2),
				stroke=stroke_color,
				stroke_width=stroke_width))
			stitches += 1
			xoffset += stitch_width
		rows += 1
		yoffset += row_height

	# blank rows at bottom	
	rows = 0
	yoffset = (card_height - (row_height * blank_rows)) + (row_height / 2)
	while rows < blank_rows:
		stitches = 0
		xoffset = side_margin + (stitch_width / 2)
		while stitches < card_stitches:
			objects.append(diagram.circle(
				center=(xoffset, yoffset),
				fill=fill_color,
				r = (pattern_hole_radius / 2),
				stroke=stroke_color,
				stroke_width=stroke_width))
			stitches += 1
			xoffset += stitch_width
		rows += 1
		yoffset += row_height
		
def draw_clip_holes(diagram, objects):
	global card_height
	global clip_hole_radius
	global fill_color
	global row_height
	global side_margin
	global stitch_width
	global stroke_color
	global stroke_width
	
	print 'drawing clip holes...'
	left_xoffset = side_margin + (stitch_width / 2) - 6.0
	right_xoffset = (card_width - side_margin - (stitch_width / 2)) + 6.0
	yoffset = row_height / 2
	
	while yoffset < card_height:
		objects.append(diagram.circle(
			center=(left_xoffset, yoffset),
			fill=fill_color,
			r = (clip_hole_radius / 2),
			stroke=stroke_color,
			stroke_width=stroke_width))
		objects.append(diagram.circle(
			center=(right_xoffset, yoffset),
			fill=fill_color,
			r = (clip_hole_radius / 2),
			stroke=stroke_color,
			stroke_width=stroke_width))
		yoffset += row_height

def draw_sprocket_holes(diagram, objects):
	print 'drawing sprocket holes...'
	
	left_xoffset = 6.5
	right_xoffset = card_width - 6.5
	yoffset = row_height
	rows = 0
	while rows < (card_rows + (blank_rows * 2)) / 2:
		objects.append(diagram.circle(
			center=(left_xoffset, yoffset),
			fill=fill_color,
			r = (sprocket_hole_radius / 2),
			stroke=stroke_color,
			stroke_width=stroke_width))
		objects.append(diagram.circle(
			center=(right_xoffset, yoffset),
			fill=fill_color,
			r = (sprocket_hole_radius / 2),
			stroke=stroke_color,
			stroke_width=stroke_width))
		rows += 1
		yoffset += (row_height * 2)
	
lines = init()
card_rows = len(lines)
card_stitches = len(lines[0])
print 'pattern size:', card_rows, 'rows x', card_stitches, 'stitches'

card_width = (side_margin * 2) + (card_stitches * stitch_width)
card_height = ((blank_rows * 2) + card_rows) * row_height
print 'card size:', card_width, 'mm x', card_height, 'mm'

diagram = create_card()

objects = []
draw_pattern(diagram, lines, objects)
draw_blank_lines(diagram, objects)
draw_clip_holes(diagram, objects)
draw_sprocket_holes(diagram, objects)

# sort the list to optimize cutting
sorted_objects = sorted(objects, key=lambda x: (float(x.attribs['cy']), float(x.attribs['cx'])))
for i in sorted_objects:
	diagram.add(i)

diagram.save()
print 'saved', ofname
