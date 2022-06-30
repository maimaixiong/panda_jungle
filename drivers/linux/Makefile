VERSION=0.0.1
obj-m+=panda_jungle.o

link:
	sudo dkms add `pwd`

build:
	sudo dkms build panda_jungle/$(VERSION)

install:
	sudo dkms install panda_jungle/$(VERSION)

all:	build install

uninstall:
	sudo dkms uninstall panda_jungle/$(VERSION)
	sudo dkms remove panda_jungle/$(VERSION) --all

