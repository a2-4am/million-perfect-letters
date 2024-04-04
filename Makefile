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

EXOMIZER=exomizer mem -lnone -P23 -f -q

BUILDDISK=build/million.po
DISKVOLUME=MILLION

asm: dirs
	$(ACME) -r build/million.lst src/million.a

compress: dirs
	for f in res/levels/*; do \
		$(EXOMIZER) "$$f"@0x9000 -o build/LEVEL."$$(basename $$f)"; \
	done
	rm -f src/data.index.a
	rm -f res/DATA
	touch res/DATA
	for f in build/LEVEL.*; do \
		echo "!word $$(wc -c < res/DATA)" >> src/data.index.a ;\
		echo "!word $$(wc -c < $$f)" >> src/data.index.a; \
		cat "$$f" >> res/DATA; \
	done

dsk: asm
	$(CADIUS) CREATEVOLUME "$(BUILDDISK)" "$(DISKVOLUME)" 140KB -C
	cp res/_FileInformation.txt build/
	$(CADIUS) ADDFILE "${BUILDDISK}" "/$(DISKVOLUME)/" "res/PROGRESS"
	$(CADIUS) ADDFILE "${BUILDDISK}" "/$(DISKVOLUME)/" "res/PREFS"
	$(CADIUS) ADDFILE "${BUILDDISK}" "/$(DISKVOLUME)/" "res/DATA"
	$(CADIUS) ADDFILE "${BUILDDISK}" "/$(DISKVOLUME)/" "res/CLOCK.SYSTEM#FF0000"
	$(CADIUS) ADDFILE "${BUILDDISK}" "/$(DISKVOLUME)/" "build/MILLION.SYSTEM"
	$(CADIUS) ADDFILE "${BUILDDISK}" "/$(DISKVOLUME)/" "res/PRODOS#FF0000"

clean:
	rm -rf build/

dirs:
	mkdir -p build

mount:
	open "$(BUILDDISK)"

all: clean dsk mount

al: all
