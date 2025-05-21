#!/bin/bash

NUMBER_PROCESS=$(ps -ef | tail +2 | wc -l) 

for i in {1..10}
  do 
    echo "Current time: $(date +'%T'). Count of processes: $NUMBER_PROCESS"
    # sleep 5
  done

FILE_INFO=info.txt

cat /proc/cpuinfo > $FILE_INFO 

echo " " >> $FILE_INFO

cat /etc/os-release | grep -w 'NAME' >> $FILE_INFO 

echo " " >> $FILE_INFO

cat /etc/os-release | grep -w 'NAME' | awk -F '=' '{print $2}' >> $FILE_INFO

for i in {50..100}
  do
    touch $i.txt
  done

echo "done"



