SHELL = /bin/sh

default:
	echo "usage: `make rsync' to upload"
	echo "usage: `make rsync-dry' to test"
	echo "usage: `make rsync-check' to test with checksum"


# /***********************************************************************
# // rsync via ssh (upload)
# // NOTE: you must create a group `pycurl' on your local machine!
# // see also RSYNC_USER below
# ************************************************************************/

RSYNC = rsync

RSYNC_FLAGS = -av --relative --delete --delete-after -e ssh

RSYNC_FILES = \
	htdocs \
	htdocs/download/.htaccess

RSYNC_EXCLUDES = \
	'--exclude=CVS/' \
	'--exclude=download/'

RSYNC_USER = kjetilja@shell.sourceforge.net
ifeq ($(USER),mfx)
RSYNC_USER = mfx@shell.sourceforge.net
endif

RSYNC_TARGET = /home/groups/p/py/pycurl/


rsync: __rsync-clean
	$(RSYNC) $(RSYNC_FLAGS) $(RSYNC_EXCLUDES) $(RSYNC_FILES) $(RSYNC_USER):$(RSYNC_TARGET)

rsync-dry:
	$(MAKE) rsync 'RSYNC=rsync --dry-run'

rsync-check:
	$(MAKE) rsync 'RSYNC=rsync --dry-run -c'

__rsync-clean:
	chgrp -c -R pycurl .
	chmod -c g+s `find . -type d -print`
##	chmod -c g+rws `find . -type d -perm -770 -print`
	chmod -c g+rws `find . -type d -print`
	-rm -rf `find . -name .xvpics -type d -print`


.PHONY: rsync rsync-dry rsync-check __rsync-clean
