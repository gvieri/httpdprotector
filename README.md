httpdprotector 

This project is aimed to stop (by using iptables) people that harass your CMS based website. 
So if someone is trying to bruteforce access to wp-admin, AND, you have both knowledge of linux administration and you use a linux machine as host (with shell access and true root privilege), httprotector is the answer. 

httpdprotector is writter in python, it uses scapy to sniff the dangerous strings and then it put a new DROP line in iptables based firewall (by using ipct). 
For now you have to invoke (root user) from a screen (do you know and love scree yes ? ) terminal. 
It doesn't (yet) log anything nor delete after a time-out its own inserted rules. 
SO: 
- YOU have to delete periodically iptables unnecessary rules (can I suggest a script ?) 
- YOU have to pay attention to avoid to cut-off yourself from the IP. 
- IT IS ROUGH. It is raw code that I wrote as prove of concept for both friends and clients. 

It is released under GPL V2. 

Enjoy. 


To use:
- by using pip install python modules 
- modify the values in httpdprotector.py according to your needs and your configurations
- recheck everything ... this software can lock out you from your remote system/s 
- re-think everything... an error will make you bald :-) or locked out from you r internet server 
- create a crontab that recall httpdp-flush.py 
- check everything twice 

If everything is going well no one will bruteforce anymore your site... Otherwiese yoyo (you're on your own)... 

bye . 


