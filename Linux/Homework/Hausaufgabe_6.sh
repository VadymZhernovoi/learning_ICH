#!/bin/bash

export VADYM_VARIABLE=210225-ptm

date +%D > /opt/210225-ptm/vadym/.process_management ; echo "Welcome to Amazon server" >> /opt/210225-ptm/vadym/.process_management

free -m | grep Mem | awk '{print "Total memory (MB):", $2}' >> /opt/210225-ptm/vadym/.process_management

ps -ef | grep root | wc -l >> /opt/210225-ptm/vadym/.process_management

env | grep VADYM_VAR >> /opt/210225-ptm/vadym/.process_management

ps -ef | grep "/usr/sbin/sshd -D" | grep -v grep | awk '{print "PID", $2, "PPID", $3}' >> /opt/210225-ptm/vadym/.process_management

echo "done"