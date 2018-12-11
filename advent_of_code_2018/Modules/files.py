from pathlib import Path

def loadAs(filename, asType):
	return list(map(asType, Path( filename ).read_text().splitlines()))