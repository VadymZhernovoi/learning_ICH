#!/bin/bash

 USER=Vadym
 date +%d-%m-%Y
 echo "Hello," $USER!

 echo "This Bash-script is running from directory" $PWD

 text=`ps -ef | grep bioset | grep -v grep | wc -l`
 echo "Count of process 'bioset': " $text

 text=`ls -l /etc | grep passwd | grep -v passwd- | awk '{print $1}'`
 echo "Permissions file '/etc/passwd': " $text

echo "done"
  
