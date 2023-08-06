#!/bin/sh --
GO2TMP=~/.go2/tmp
go2 () {
    $PYPREFIX/lib/go2/go2.py $*;
    if [ -e $GO2TMP ]; then
	cd "$(cat $GO2TMP)"
	rm $GO2TMP > /dev/null
    fi
}
