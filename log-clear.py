import os 
os.system("clear")
print("""
 _     ___   ____    ____ _     _____    _    ____  
| |   / _ \ / ___|  / ___| |   | ____|  / \  |  _ \ 
| |  | | | | |  _  | |   | |   |  _|   / _ \ | |_) |
| |__| |_| | |_| | | |___| |___| |___ / ___ \|  _ < 
|_____\___/ \____|  \____|_____|_____/_/   \_\_| \_\
                                                      
""")
print("")
print("Autor:Nando")
print("Version:1.0")
#a = raw_input("Precione uma tecla para limpar os logs...")
print("Aguarde...")
#Etapa 1 , apagar todos os logs escritos
os.system("> /root/.bash_history")
os.system("> /root/.mysql_history")
os.system("> /root/.rsf_history")
os.system("> /var/log/user.log")
os.system("> /var/log/user.log.1")
os.system("> /var/log/alternatives.log")
os.system("> /var/log/alternatives.log.1")
os.system("> /var/log/daemon.log")
os.system("> /var/log/daemon.log.1")
os.system("> /var/log/Xorg.0.log")
os.system("> /var/log/Xorg.1.log")
os.system("> /var/log/messages.1")
os.system("> /var/log/messages.log")
os.system("> /var/log/kern.log")
os.system("> /var/log/kern.log.1")
os.system("> /var/log/auth.log")
os.system("> /var/log/auth.log.1")
os.system("> /var/log/bootstrap.log")
os.system("> /var/log/dpkg.log")
os.system("> /var/log/dpkg.log.1")
os.system("> /var/log/fontconfig.log")
os.system("> /var/log/lynis.log")
os.system("> /var/log/macchanger.log")
os.system("> /var/log/syslog")
os.system("> /var/log/syslog.1")
os.system("> /var/log/wvdialconf.log")
os.system("> /var/log/*.log")
os.system("> /var/log/cron.log")
os.system("> /var/log/maillog")
os.system("rm -R /var/log/httpd/")
os.system("rm -R /var/log/lighttpd/")
os.system("rm /var/log/boot.log")
os.system("> /var/log/mysqld.log")
os.system("> /var/log/wtmp")
os.system("> /var/log/yum.log")
os.system("> /var/log/apt/history.log")
os.system("> /var/log/apt/term.log")
os.system("> /var/log/installer/syslog")
os.system("> /var/log/installer/Xorg.0.log")
os.system("> /var/log/installer/status")
os.system("> /var/log/installer/partman")
os.system("> /var/log/installer/lsb-release")
os.system("> /var/log/installer/hardware-summary")
os.system("> /var/log/fsck/checkfs")
os.system("> /var/log/exim4/mainlog")
os.system("> /var/log/exim4/mainlog.1")
os.system("> /var/log/mitmf/mitmf.log")
os.system("> /var/log/fsck/checkroot")
#logs apache2
os.system("> /var/log/apache2/access.log")
os.system("> /var/log/apache2/access.log.1")
os.system("> /var/log/apache2/error.log")
os.system("> /var/log/apache2/error.log.1")
#--------------------------------------------------
#Mozilla cookies e history
os.system("> /root/.mozilla/firefox/9s7yvxjd.default/places.sqlite")
os.system("> /root/.mozilla/firefox/9s7yvxjd.default/cookies.sqlite")

#Etapa 2 remover todos os logs copiados
os.system("rm /var/log/*.gz")
#--------------------------------------------------
print("Clear Log Concluido !!!")
