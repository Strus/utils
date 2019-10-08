#!/bin/bash

setxkbmap -layout pl
if [ "$1" = "n" ]; then
    exit
fi

setxkbmap -option ctrl:nocaps
#setxkbmap -option altwin:swap_lalt_lwin
xmodmap ~/xmodmap/xmodmap

# Use Spacebar as a Modifier
#spare_modifier="Hyper_L" 
#xmodmap -e "keycode 65 = $spare_modifier"   
#xmodmap -e "add Hyper_L = $spare_modifier"
#xmodmap -e "keycode any = space"  
#xcape -e "$spare_modifier=space"

sudo chmod +rw -R /dev/input
LAUNCHED=`ps -ef | grep "keyListen.py" | grep -v "grep" | wc -l`
if [ "$LAUNCHED" = "0" ]; then
    $HOME/xmodmap/keyListen.py &
else
    PROCESS_NUM=`ps -aef | grep -v grep | grep "keyListen.py" | awk '{{print $2}}'`
    kill -9 $PROCESS_NUM
    $HOME/xmodmap/keyListen.py &
fi
