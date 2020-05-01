#
# Million Perfect Letters makefile
# assembles source code, optionally builds a disk image and mounts it
#
# original by Quinn Dunki on 2014-08-15
# One Girl, One Laptop Productions
# http://www.quinndunki.com/blondihacks
#
# adapted by 4am on 2020-04-16
#

# third-party tools required to build

# https://sourceforge.net/projects/acme-crossass/
ACME=acme

# https://www.brutaldeluxe.fr/products/crossdevtools/cadius/
# https://github.com/sicklittlemonkey/cadius
# version 1.4.0 or later
CADIUS=cadius

BUILDDISK=build/million

asm:
	mkdir -p build
	$(ACME) -r build/million.lst src/million.a 2>build/log
	cp res/work.po "$(BUILDDISK)".po >>build/log
	cp res/_FileInformation.txt build/ >>build/log
	$(CADIUS) ADDFILE "${BUILDDISK}".po "/MILLION/" "res/PROGRESS" >>build/log
	$(CADIUS) ADDFILE "${BUILDDISK}".po "/MILLION/" "build/MILLION.SYSTEM" >>build/log
	for f in res/levels/*; do $(CADIUS) ADDFILE "${BUILDDISK}".po "/MILLION/" "$$f" >>build/log; done

clean:
	rm -rf build/

mount:
	open "$(BUILDDISK)".po

all: clean asm mount

al: all
