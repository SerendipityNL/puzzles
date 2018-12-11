from pathlib import Path

print( 'Running solution 02' )

input = list(map(int, Path( 'day01_input1.txt' ).read_text().splitlines()))

encountered = list( [0] )
list_length = len( input );

pointer = 0
position = 0
found = False

while not found:

	position += input[pointer]

	if position not in encountered:
		encountered.append(position)

		pointer += 1

		if pointer > ( list_length - 1 ):
			pointer = 0

	else:
		found = True
		break

print( position )