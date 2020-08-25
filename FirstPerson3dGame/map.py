from settings import *

text_map = [
	'1111111111',
	'1........1',
	'1.11.....1',
	'1.....1..1',
	'1.....1..1',
	'1........1',
	'1.11.....1',
	'1..1.....1',
	'1........1',
	'1111111111'
]

world_map = set()
for j, row in enumerate(text_map):
	for i, obj in enumerate(row):
		if obj == '1':
			world_map.add((j * TILE, i * TILE))