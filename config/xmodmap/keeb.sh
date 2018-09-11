#!/bin/bash

setxkbmap -layout pl
if [ "$1" = "n" ]; then
    exit
fi

setxkbmap -option ctrl:nocaps
setxkbmap -option altwin:swap_lalt_lwin
xmodmap ~/xmodmap/.Xmodmap
sudo chmod +rw -R /dev/input
PROCESS_NUM=`ps -ef | grep "keyListen.py" | grep -v "grep" | wc -l`
echo $PROCESS_NUM
if [ "$PROCESS_NUM" = "0" ]; then
    $HOME/xmodmap/keyListen.py &
fi
