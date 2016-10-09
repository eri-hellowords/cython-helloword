all: build copy test

build:
	python3 setup.py build

copy:
	cp ./build/$(shell (ls build | grep lib))/* ./build/$(shell (ls build | grep exe))/

test:
	cd ./build/$(shell (ls build | grep exe))/ ; ./main.exe
