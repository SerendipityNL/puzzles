from pathlib import Path

print( 'Running solution 01' )

input = list(map(int, Path( 'day01_input1.txt' ).read_text().splitlines()))

print( sum( input ) )