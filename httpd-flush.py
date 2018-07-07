
###############################
# author Giovambattista Vieri
# (C) Giovambattista Vieri all rights reserved
# Status: alpha --- use this software at your own risk and peril --- 
# License GPL V2
###############################


import subprocess
import sys

cmd="/sbin/iptables -L INPUT --line-numbers |grep PROTECTOR"
p= subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE)
for line in p.stdout: 
    dummy =line.split()
    delecmd="iptables -D INPUT %s " % dummy[0]
#    print delecmd
    subprocess.Popen(delecmd,shell=True)
