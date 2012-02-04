#!/bin/bash
PROJ_DIR=`dirname $0`/..
$PROJ_DIR/website/manage.py test $*