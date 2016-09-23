#!/usr/bin/python
#coding: utf-8
import subprocess 

print ('//////////OwnDark //////////')
print
print ('Version Beta 0.0.5v')
print

#Esta linha ira perguntar ao usuario , se ele ja possui alguns pacotes instalados , caso ele digite 'n' o script ira instalar os pacotes
pct= raw_input('Possui os seguintes pacotes instalados:Wifite , NMAP, UNISCAN , Crunch?  (S/n): ')

if (pct =='n'):
       return_code = subprocess.call(' apt-get install maltegoce', shell=True)

if (pct =='n'):
	return_code = subprocess.call(' apt-get install nmap' , shell=True)

if (pct =='n'):
	return_code = subprocess.call('apt-get install uniscan' , shell=True)

if (pct =='n'):
	return_code = subprocess.call('apt-get install wifite' , shell=True)

if (pct =='n'):
	return_code = subprocess.call('apt-get install sqlmap' , shell=True)

if (pct =='n'):
	return_code = subprocess.call('apt-get install setoolkit', shell=True)

if (pct =='n'):
	return_code = subprocess.call('clear', shell=True)

if (pct =='n'):
	return_code = subprocess.call('echo //////OwnDark//////// && echo && echo Version Beta 0.1.0v', shell=True) 

##Esta linha é o menu .
print 
print ('1) Levantamento de Dados')
print ('2) Scanner de Vulnerabilidades')
print ('3) Kit de Engenharia Social')
print ('4) Ataque via Injection')
print ('5) Gerador de Wordlists')
print ('6) Ataque em rede wiriless')
print ('7)Sniffers (Farejador ')
print  
 

atck = raw_input('Escolha uma opção: ')

if (atck =='1'):
	return_code = subprocess.call('maltegoce', shell=True)

if (atck =='2'):
	return_code = subprocess.call('echo Digite a URL do site:  && read url  && uniscan -u $url -qweds ' , shell=True)

if (atck =='3'):
	return_code = subprocess.call('setoolkit', shell=True)

if (atck =='4'):
	return_code = subprocess.call('echo 1 SQLMAP && echo   && echo Escolha uma opção:  &&    read  inject && test $inject = 1 && echo &&  echo Digite uma URL injetavel:    &&  read url &&   sqlmap -u $url --dbs  && echo Escreva o nome do Banco de dados que deseja injetar && read db &&  sqlmap -u $url -D $db --tables && echo Escreva o nome da tabela que deseja injetar:  && read tabela && sqlmap -u $url -D $db -T $tabela  --columns && echo Nome da coluna que deseja injetar  && read  coluna && sqlmap -u $url -D $db -T $tabela -C $coluna --dump ', shell=True)

if (atck =='6'):
	return_code = subprocess.call('echo 1-WIFITE && read wps && $wps =  1 && wifite --wps --wpa --aircrack', shell=True)

if (atck =='7'):
	return_code = subprocess.call('echo 1-Wireshark && read snif && test $snif = 1 && wireshark', shell=True)
