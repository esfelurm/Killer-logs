#!/usr/bin/env python

# This is a linux log file eraser. It doesn't just clean
# certain data out of the logs - it securely deletes them
# with the shred tool (which must be installed). 

# There are no arguments to pass to this script, just run
# it with elevated privledges and it will securely wipe every
# log you have (but feel free to add more logfile locations)

# Note: I am not a python programmer, I just needed a script
# to do this, so please use eye bleach once you're done reading
# the code.

# This wouldn't have been possible without the help of tekwizz123
# to tell me how to python. Much props to him.

# I take no responsibility for any damage this causes, use it
# at your own risk! The first time I tried it, it froze my Kali
# VM, but after that it worked fine. It's also been tested
# successfully on multiple virtual private servers.

# If you have questions, comments, concerns or want to tell
# me about more logfile locations, you can email me at
# dex @at@ dexstor.org

import os
import sys
from subprocess import check_output

rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[00;34m', '\033[01;35m'
cn, k,g,c = '\033[00;36m', '\033[90m','\033[38;5;130m','\033[37m'

def clear():
	if __import__("platform").system() == 'Linux':
		os.system("clear")
	else:
		from colorama import init
		init()
		os.system("cls")

def Linux():
	null = 'null'
	logs = ['/var/adm/utmp',
	'/usr/adm/utmp',
	'/etc/utmp',
	'/var/log/utmp',
	'/var/run/utmp',
	'/usr/var/adm/utmp',
	'/var/adm/wtmp',
	'/usr/adm/wtmp',
	'/etc/wtmp',
	'/var/log/wtmp',
	'/var/run/wtmp',
	'/usr/var/adm/wtmp',
	'/var/adm/utmpx',
	'/usr/adm/utmpx',
	'/usr/run/utmpx',
	'/etc/utmpx',
	'/var/log/utmpx',
	'/var/run/utmpx',
	'/usr/var/adm/utmpx',
	'/var/adm/wtmpx',
	'/usr/adm/wtmpx',
	'/etc/wtmpx',
	'/var/log/wtmpx',
	'/var/run/wtmpx',
	'/usr/var/adm/wtmpx',
	'/var/adm/lastlog',
	'/usr/adm/lastlog',
	'/etc/lastlog',
	'/var/log/lastlog',
	'/usr/run/lastlog',
	'/usr/var/adm/lastlog',
	'/var/adm/pacct',
	'/var/account/pacct',
	'/var/log/acct',
	'/var/log/pacct',
	'/var/adm/acct',
	'/var/account/acct',
	'/usr/adm/acct',
	'/var/log/prelude.log',
	'/var/log/prelude/prelude.log',
	'/var/adm/prelude/prelude.log',
	'/var/adm/prelude/log/prelude.log',
	'/var/adm/log/prelude.log',
	'/var/ids/log/prelude.log',
	'/var/ids/prelude/log/prelude.log',
	'/var/ids/prelude.log',
	'/var/prelude/prelude.log',
	'/var/prelude/log/prelude.log',
	'/home/log/prelude.log',
	'/home/ids/log/prelude.log',
	'/home/prelude/log/prelude.log',
	'/home/ids/prelude.log',
	'/home/prelude/prelude.log',
	'/usr/local/var/log/prelude.log',
	'/var/log/prelude-xml.log',
	'/var/log/prelude/prelude-xml.log',
	'/var/adm/prelude/prelude-xml.log',
	'/var/adm/prelude/log/prelude-xml.log',
	'/var/adm/log/prelude-xml.log',
	'/var/ids/log/prelude-xml.log',
	'/var/ids/prelude/log/prelude-xml.log',
	'/var/ids/prelude-xml.log',
	'/var/prelude/prelude-xml.log',
	'/var/prelude/log/prelude-xml.log',
	'/home/log/prelude-xml.log',
	'/home/ids/log/prelude-xml.log',
	'/home/prelude/log/prelude-xml.log',
	'/home/ids/prelude-xml.log',
	'/home/prelude/prelude-xml.log',
	'/usr/local/var/log/prelude-xml.log',
	'/var/log/samba/log.smbd',
	'/var/log/samba/log.nmbd',
	'/var/log/log.smbd',
	'/var/log/log.nmbd',
	'/var/log/smb/log.smbd',
	'/var/log/smb/log.nmbd',
	'/home/samba/log.smbd',
	'/home/samba/log.nmbd',
	'/home/samba/log/log.smbd',
	'/home/samba/log/log.nmbd',
	'/home/samba/logs/log.smbd',
	'/home/samba/logs/log.nmbd',
	'/var/log/snort/snort.alert',
	'/var/log/snort.alert',
	'/var/log/ids/snort.alert',
	'/var/ids/snort/snort.alert',
	'/var/ids/snort.alert',
	'/var/snort/snort.alert',
	'/home/snort/snort.alert',
	'/home/snort/log/snort.alert',
	'/home/log/snort/snort.alert',
	'/home/log/snort.alert',
	'/home/ids/snort/snort.alert',
	'/home/ids/snort.alert',
	'/usr/local/ids/snort.alert',
	'/usr/local/var/snort.alert',
	'/usr/local/snort/snort.alert',
	'/usr/local/var/log/snort.alert',
	'/usr/local/snort/log/snort.alert',
	'/usr/local/ids/log/snort.alert',
	'/usr/local/log/snort.alert',
	'/usr/local/log/snort/snort.alert',
	'/var/log/apache2/audit_log',
	'/var/log/apache1/audit_log',
	'/var/log/apache/audit_log',
	'/home/apache2/log/audit_log',
	'/home/apache1/log/audit_log',
	'/home/apache/log/audit_log',
	'/home/http/log/audit_log',
	'/home/httpd/log/audit_log',
	'/var/log/http/audit_log',
	'/var/log/httpd/audit_log',
	'/usr/http/log/audit_log',
	'/usr/httpd/log/audit_log',
	'/usr/local/http/log/audit_log',
	'/usr/local/httpd/log/audit_log',
	'/usr/local/apache/log/audit_log',
	'/usr/local/apache2/log/audit_log',
	'/usr/local/apache1/log/audit_log',
	'/var/www/log/audit_log',
	'/var/http/log/audit_log',
	'/var/httpd/log/audit_log',
	'/var/apache/log/audit_log',
	'/var/apache2/log/audit_log',
	'/var/apache1/log/audit_log',
	'/root/.bash_history',
	'/root/.history',
	'/root/.sh_history',
	'/.bash_history',
	'/.history',
	'/.sh_history',
	'/tmp/.bash_history',
	'/tmp/.sh_history',
	'/tmp/.history',
	'/home/apache/.bash_history',
	'/home/apache/.sh_history',
	'/home/apache/.history',
	'/home/apache1/.bash_history',
	'/home/apache1/.sh_history',
	'/home/apache1/.history',
	'/home/apache2/.bash_history',
	'/home/apache2/.sh_history',
	'/home/apache2/.history',
	'/home/httpd/.bash_history',
	'/home/httpd/.sh_history',
	'/home/httpd/.history',
	'/home/ftpd/.bash_history',
	'/home/ftpd/.sh_history',
	'/home/ftpd/.history',
	'/var/log/apache2/access_log',
	'/var/log/apache2/access_log.1',
	'/var/log/apache2/access_log.2',
	'/var/log/apache2/error_log',
	'/var/log/apache2/error_log.1',
	'/var/log/apache2/error_log.2',
	'/var/log/apache2/ssl_access_log',
	'/var/log/apache2/ssl_access_log.1',
	'/var/log/apache2/ssl_access_log.2',
	'/var/log/apache2/ssl_error_log',
	'/var/log/apache2/ssl_request_log',
	'/var/log/apache2/request_log',
	'/var/log/apache/access_log',
	'/var/log/apache/access_log.1',
	'/var/log/apache/access_log.2',
	'/var/log/apache/error_log',
	'/var/log/apache/error_log.1',
	'/var/log/apache/error_log.2',
	'/var/log/apache/ssl_access_log',
	'/var/log/apache/ssl_error_log',
	'/var/log/apache/ssl_request_log',
	'/var/log/apache/request_log',
	'/var/log/apache1/access_log',
	'/var/log/apache1/error_log',
	'/var/log/apache1/ssl_access_log',
	'/var/log/apache1/ssl_error_log',
	'/var/log/apache1/ssl_request_log',
	'/var/log/apache1/request_log',
	'/var/www/log/access_log',
	'/var/www/log/error_log',
	'/var/www/log/ssl_access_log',
	'/var/www/log/ssl_error_log',
	'/var/www/log/ssl_request_log',
	'/var/www/log/request_log',
	'/var/apache2/access_log',
	'/var/apache2/error_log',
	'/var/apache2/ssl_access_log',
	'/var/apache2/ssl_error_log',
	'/var/apache2/ssl_request_log',
	'/var/apache2/request_log',
	'/home/apache2/access_log',
	'/home/apache2/error_log',
	'/home/apache2/ssl_access_log',
	'/home/apache2/ssl_error_log',
	'/home/apache2/ssl_request_log',
	'/home/apache2/request_log',
	'/var/web/log/access_log',
	'/var/web/log/error_log',
	'/var/web/log/ssl_access_log',
	'/var/web/log/ssl_error_log',
	'/var/web/log/ssl_request_log',
	'/var/web/log/request_log',
	'/var/apache/access_log',
	'/var/apache/error_log',
	'/var/apache/ssl_access_log',
	'/var/apache/ssl_error_log',
	'/var/apache/ssl_request_log',
	'/var/apache/request_log',
	'/home/apache/access_log',
	'/home/apache/error_log',
	'/home/apache/ssl_access_log',
	'/home/apache/ssl_error_log',
	'/home/apache/ssl_request_log',
	'/home/apache/request_log',
	'/var/apache1/access_log',
	'/var/apache1/error_log',
	'/var/apache1/ssl_access_log',
	'/var/apache1/ssl_error_log',
	'/var/apache1/ssl_request_log',
	'/var/apache1/request_log',
	'/home/apache1/access_log',
	'/home/apache1/error_log',
	'/home/apache1/ssl_access_log',
	'/home/apache1/ssl_error_log',
	'/home/apache1/ssl_request_log',
	'/home/apache1/request_log',
	'/usr/apache1/error_log',
	'/usr/apache1/ssl_access_log',
	'/usr/apache1/ssl_error_log',
	'/usr/apache1/ssl_request_log',
	'/usr/apache1/request_log',
	'/usr/local/apache1/error_log',
	'/usr/local/apache1/ssl_access_log',
	'/usr/local/apache1/ssl_error_log',
	'/usr/local/apache1/ssl_request_log',
	'/usr/local/apache1/request_log',
	'/usr/apache2/error_log',
	'/usr/apache2/ssl_access_log',
	'/usr/apache2/ssl_error_log',
	'/usr/apache2/ssl_request_log',
	'/usr/apache2/request_log',
	'/usr/local/apache2/error_log',
	'/usr/local/apache2/ssl_access_log',
	'/usr/local/apache2/ssl_error_log',
	'/usr/local/apache2/ssl_request_log',
	'/usr/local/apache2/request_log',
	'/usr/apache/error_log',
	'/usr/apache/ssl_access_log',
	'/usr/apache/ssl_error_log',
	'/usr/apache/ssl_request_log',
	'/usr/apache/request_log',
	'/usr/local/apache/error_log',
	'/usr/local/apache/ssl_access_log',
	'/usr/local/apache/ssl_error_log',
	'/usr/local/apache/ssl_request_log',
	'/usr/local/apache/request_log',
	'/usr/local/httpd/access_log',
	'/usr/local/httpd/ssl_access_log',
	'/usr/local/httpd/error_log',
	'/usr/local/httpd/ssl_error_log',
	'/usr/local/httpd/ssl_request_log',
	'/home/httpd/access_log',
	'/home/httpd/ssl_access_log',
	'/home/httpd/error_log',
	'/home/httpd/ssl_error_log',
	'/var/adm/SYSLOG',
	'/var/adm/sulog',
	'/var/adm/lastlog/username',
	'/usr/spool/lp/log',
	'/var/adm/lp/lpd-errs',
	'/usr/lib/cron/log',
	'/var/adm/loginlog',
	'/var/adm/dtmp',
	'/var/adm/acct/sum/loginlog',
	'/var/adm/X0msgs',
	'/var/adm/crash/vmcore',
	'/var/adm/crash/unix',
	'/var/adm/qacct',
	'/var/adm/ras/errlog',
	'/var/adm/ras/bootlog',
	'/var/adm/cron/log',
	'/etc/security/lastlog',
	'/etc/security/failedlogin',
	'/usr/spool/mqueue/syslog',
	'/var/adm/messages',
	'/var/adm/aculogs',
	'/var/adm/aculog',
	'/var/adm/vold.log',
	'/var/adm/log/asppp.log',
	'/var/log/syslog',
	'/var/log/POPlog',
	'/var/log/authlog',
	'/var/log/auth1.log',
	'/var/lp/logs/lpsched',
	'/var/lp/logs/lpNet',
	'/var/lp/logs/requests',
	'/var/cron/log',
	'/var/saf/_log',
	'/var/saf/port/log',
	'/var/log',
	'/var/adm',
	'/var/spool/mqueue',
	'/var/mail',
	'/var/log/emerge.log',
	'/var/log/Xorg.0.log',
	'/root/.bash_logout',
	'/usr/local/apache/logs',
	'/usr/local/apache/log',
	'/var/apache/logs',
	'/var/apache/log',
	'/var/logs',
	'/var/log/messages',
	'/var/log/httpd/access_log',
	'/var/log/httpd/access.log',
	'/var/log/httpd/error_log',
	'/var/log/httpd/error.log',
	'/var/log/apache2/access.log',
	'/var/log/apache2/error.log',
	'/var/log/secure',
	'/var/log/xferlog',
	'/var/log/auth.log',
	'/var/log/lighttpd/lighttpd.error.log',
	'/var/log/lighttpd/lighttpd.access.log',
	'/var/www/logs/access_log',
	'/var/www/logs/access.log',
	'/var/www/logs/error_log',
	'/var/www/logs/error.log',
	'/var/log/apache/access.log',
	'/var/log/apache/error.log',
	'/var/log/yum.log',
	'/etc/httpd/logs/access_log',
	'/etc/httpd/logs/access.log',
	'/etc/httpd/logs/error_log',
	'/etc/httpd/logs/error.log',
	]
	for log in logs:
		try:
			f = open(log)
			os.system(f'shred -fuz {log}')
			print(f'\033[34m[\033[32mSHREDDERED\033[34m] \033[37;1mLogname : \033[0m{k}{log}\n')
		except IOError:
			null = 'null'
	list = []
	users = [i.split(':') for i in open('/etc/shadow').readlines()]
	for i in users:
		if i[1] not in ('!', '*'):
			list.append(i[0])
	for user in list:
		try:
			f = open(f'/home/{user}/.bash_history')
			os.system(f'shred -fuz /home/{user}/.bash_history')
			print(f'{lgn}SHREDDED{gn}/home/{user}/.bash_history')
		except IOError:
			null = 'null'
def windows():
    logs = ['Security' , 'Application' , 'System' , 'Setup', 'Internet Explorer']

    for log in logs:
        try:
            check_output(["wevtutil.exe" , "cl" , log.strip("\r")])
            print(f"{lgn}{log} logs were deleted ")
        except:
            print(f"{lrd}Error in deleting {rd}{log}{lrd} logs ")
            
clear()
print(f"""{lrd}
       
               :.                                          -.              
             :*.                                            ==             
            -#:                                              ++            
           -#=                                               :#+           
          .##:                                                *#=          
          +##.                                                *##.         
          *##.                                                *##:         
          ###=                                               .###-         
          ###*.                                              =###-         
          +###*.                                            -####.         
          :####*:                                         .+####+          
           =#####*-               .......               :+#####*.          
            =#######*+=----===++*##########*++==-----=+#######*.           
             :*##############################################=             
               :+#########################################*-               
                 .-+###################################*=:                 
                    .+################################:                    
                    +##################################:                   
                   -###################################*                   
                   *####=+########################-#####:                  
                  :#####= -*####################=.:#####=                  
                  :###%#*   :=*##############+-.  =#####+                  
                  :#**%##=     .-#########=.     :####+#+                  
                  .=.+####*=-=+*############+=-=+#####.:-                  
                     *################################-                    
                    .#################################+                    
                    :######++*###=:.=#*-.-*##*++######*                    
                    =####%%#*-..  -:   .-. . :+########.                   
                    :####%%###*=+###=.-###*=+#########+                    
                     .*##############################-                     
                       :*##########################=.                      
                         :+#####*+##+:####*#####*=.                        
                           .-+##-:#*. :##= +#*=:                           
                               :  =.   :=   .            \n                  
                   {gn}Telegram & Github : {lgn}@esfelurm                                                                             
""")

x = input(f"""\t\t\t{lrd} ! DISCLAIMER !\n
{k}#################################################################
{k}#  {c}I take {lrd}no responsibility{c} for {lrd}any damage{c} this causes, use it  {k}#
{k}# {c}at {lrd}myour own risk\033[0m{c}! The first time I tried it, it froze my Kali{k}#
{k}#   {c}VM, but after that it worked fine. It's also been tested    {k}#
{k}#      {c}successfully on multiple virtual private servers.        {k}#
{k}#################################################################

{gn}Specify your operating system type: {yw}({lgn}LINUX {cn}OR{lgn} WINDOWS{yw}) {c}""")
x = x.upper()
if x == 'LINUX':
	Linux()
else:
	windows()