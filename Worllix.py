import os
os.system("clear")
set = ""
print ("""
 _____ _   ___  __    ____   ___   ____ ___ _____ _______   __
|_   _| | | \ \/ /   / ___| / _ \ / ___|_ _| ____|_   _\ \ / /
  | | | | | |\  /____\___ \| | | | |    | ||  _|   | |  \ V / 
  | | | |_| |/  \_____|__) | |_| | |___ | || |___  | |   | |  
  |_|  \___//_/\_\   |____/ \___/ \____|___|_____| |_|   |_|  

################################################################
Grupo:Tux-Society					       #
Autores:~@OWNDARK & Jey07				       #
Version:1.0                                                    #       
Contato:https://www.facebook.com/TuxxSociety/?fref=ts	       #
################################################################
""")
print ("")
while 1:
 opt = raw_input("tux > ")
 if(opt=="log system"):
   while 1: 
    logclear = raw_input("tux(log-system) > ")
    if(logclear=="run"):
      os.system("mkdir /root/LOGS-SYSTEM")
      print("Aguarde...")
      os.system("cp  /var/log/alternatives.log /root/LOGS-SYSTEM")
      os.system("cp /var/log/alternatives.log1 /root/LOGS-SYSTEM")
      os.system("cp /var/log/aptitude /root/LOGS-SYSTEM") 
      os.system("cp /var/log/attKS.log /root/LOGS-SYSTEM")
      os.system("cp /var/log/auth.log /root/LOGS-SYSTEM")
      os.system("cp /var/log/auth.log.1 /root/LOGS-SYSTEM")
      os.system("cp /var/log/bootstrap.log /root/LOGS-SYSTEM")
      os.system("cp /var/log/cron.log /root/LOGS-SYSTEM")
      os.system("cp /var/log/daemon.log /root/LOGS-SYSTEM")
      os.system("cp /var/log/daemon.log.1 /root/LOGS-SYSTEM")
      os.system("cp /var/log/dmesg /root/LOGS-SYSTEM")
      os.system("cp /var/log/dpkg.log /root/LOGS-SYSTEM")
      os.system("cp /var/log/dpkg.log.1 /root/LOGS-SYSTEM")
      os.system("cp /var/log/faillog /root/LOGS-SYSTEM")
      os.system("cp /var/log/fontconfig.log /root/LOGS-SYSTEM")
      os.system("cp /var/log/kern.log /root/LOGS-SYSTEM")
      os.system("cp /var/log/kern.log.1 /root/LOGS-SYSTEM")
      os.system("cp /var/log/lastlog /root/LOGS-SYSTEM")
      os.system("cp /var/log/lynis.log /root/LOGS-SYSTEM")
      os.system("cp /var/log/macchanger.log /root/LOGS-SYSTEM")
      os.system("cp /var/log/maillog /root/LOGS-SYSTEM")
      os.system("cp /var/log/messages.1 /root/LOGS-SYSTEM")
      os.system("cp /var/log/messages.log /root/LOGS-SYSTEM")
      os.system("cp /var/log/mysqld.log /root/LOGS-SYSTEM")
      os.system("cp /var/log/syslog /root/LOGS-SYSTEM")
      os.system("cp /var/log/syslog.1 /root/LOGS-SYSTEM")
      os.system("cp /var/log/user.log /root/LOGS-SYSTEM")
      os.system("cp /var/log/user.log.1 /root/LOGS-SYSTEM")
      os.system("cp /var/log/wvdialconf.log /root/LOGS-SYSTEM")
      os.system("cp /var/log/Xorg.0.log /root/LOGS-SYSTEM")
      os.system("cp /var/log/Xorg.0.log.old /root/LOGS-SYSTEM")
      os.system("cp /var/log/Xorg.1.log /root/LOGS-SYSTEM")
      os.system("cp /var/log/yum.log /root/LOGS-SYSTEM")
      os.system("cp /root/.bash_history /root/LOGS-SYSTEM")
      os.system("cp /home/*/.bash_history /root/LOGS-SYSTEM")
      os.system("cp /root/.mozilla/firefox/9s7yvxjd.default/cookies.sqlite  /root/LOGS-SYSTEM")
      os.system("cp /root/.mozilla/firefox/9s7yvxjd.default/formhistory.sqlite /root/LOGS-SYSTEM")
      print ("Os logs estao em > /root/SYS-LOGS ")
    if(logclear=="exit"):
      break


#Config do script help , clear, exit .
 if(opt=="help"):
  print("""
############################# HELP ###########################################
     								             #
help             Exibe a area de ajuda 				             # 
restart          Reinicia o script					     #
exit             Encerra o escrit    				             # 
use              Server para declara qual opcao voce quer usar               #
set              Define oque ira usar                                        #
show options     Amostra as opcoes disponiveis                               #
recovey          Recupera os arquivos de m determinado pendriver ,hd etc..   #
clear            Limpa a tela do shell				             #
##############################################################################
   """)

 if(opt=="restart"):
   os.system("exit")
   os.system("python worlix.py")
 if(opt=="clear"):
   print set

 
 if(opt=="exit"):
   break
 if(opt=="show options"):
   print("""
############################# OPTIONS ########################################
									     #
log system        Serve para pegar os logs do sistema			     #
recovery         Serve para restaura os arquivos de um dispositivo           # 
             						                     #
					                                     #
					                                     #
									     #
								             #
##############################################################################
   """)

