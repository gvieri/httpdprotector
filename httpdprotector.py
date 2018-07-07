###############################
# author Giovambattista Vieri
# (C) Giovambattista Vieri all rights reserved
# Status: alpha --- use this software at your own risk and peril --- 
# License GPL V2
###############################


from scapy.all import *
import iptc
import datetime 
import getopt
import logging
import os


rule = iptc.Rule() 



#################
whitelistIP=["192.168.2.251","192.168.3.250"]  ## pay attention: this ip will be not firewalled. 
iptobeprotected="192.168.2.39"          ## ip to be protected
interface= "eth0"                       ## interface to be sniffed
stringtobesearched='wp-admin'           ## maybe you can protect xmlrpc ... or other ... 
#################

iplogged=dict() 


rule.in_interface=interface 
rule.protocol="tcp" 
rule.create_target("DROP")

table = iptc.Table(iptc.Table.FILTER)
chain = iptc.Chain(table, 'INPUT')

comment = datetime.datetime.now().strftime("PROTECTOR %Y-%m-%d %H:%M:%S")

def packet_callback(packet):
    # check to make sure it has a data payload
    print "in packet_callback"
    if packet[IP].src in whitelistIP :
        #### whitelisted 
            print '[] %s is whitelisted ' % packet[IP].src
    elif packet[TCP].payload:
        mail_packet = str(packet[TCP].payload)
	if iplogged.has_key(packet[IP].src)  : 
            ### already logged
            print '[] %s has been already logged' % packet[IP].src
        elif stringtobesearched in mail_packet.lower() :
            rule.src=packet[IP].src
            rule.target = iptc.Target(rule,"DROP") 
            print '[*] Server: %s' % packet[IP].dst
            print '[*] %s' %packet[TCP].payload
            match = rule.create_match("comment")
            match.comment = "\"%s\"" % (comment) 
            chain.insert_rule(rule)
            iplogged[packet[IP].src]="bingo" 

print "Daemonizing :-)... "

sniff(filter="tcp port 80 and dst {0}".format(iptobeprotected), prn=packet_callback, store=0)


