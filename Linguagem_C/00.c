#include <stdio.h>
#include <locale.h>
#include <string.h>
#include <stdlib.h>
#include <locale.h>
#include <time.h>
#include <stdbool.h>


char loginOuVisitante(){
	char resposta;
	printf("codigo  |\t descrição");	
	printf("\n1 \t|\t acesar site no modo visitante");	
	printf("\n2 \t|\t logar em uma conta\n");
	printf("Digite o codigo que deseja: ");
	scanf("%c",&resposta);
	system("cls || clear");
	
	switch (resposta){
		case '1':
			return  resposta;
			
			
		case '2':
			return  resposta;
			
		
		default:
			
				do{
				printf("Codigo invalido ");
				sleep(3);
				system("cls || clear");
				system("cls || clear");
				printf("\n1 \t|\t acesar site no modo visitante");	
				printf("\n2 \t|\t logar em uma conta\n");
				printf("Digite um codigo valido: ");
				scanf("%c",&resposta);
				if(resposta == '1' || resposta == '2'){
					break;
				}
				}while(resposta !='1');
				
	}
}



char verificacaoRLOuV(char vRLOuV){
	bool bLogin = false; 
	if(vRLOuV == '1'){
		return bLogin = false;
	}else{
		return bLogin = true;
	}	
} 

bool login(bool vLogin){
	char login[10], senha [10], loginCorreto[10] = "adm" ,senhaCorreta[10] = "12345";
	bool siteAcesso,loginErrado;
		if(vLogin == true){
		printf("Digite o login: ");
		scanf("%s",&login);
		printf("Digite a senha: ");
		scanf("%s",&senha);
		
		if (strcmp(login,loginCorreto) == 0 && strcmp(senha,senhaCorreta) == 0){
			return siteAcesso = true;
		}else{
			do{
			loginErrado = true;
			printf("LOGIN OU SENHA INCORRETA");
			sleep(2);
			system("cls || clear");
			printf("Digite o login: ");
			scanf("%s",&login);
			printf("Digite a senha: ");
			scanf("%s",&senha);
			if(strcmp(login,loginCorreto) == 0 && strcmp(senha,senhaCorreta) == 0){
				loginErrado = false;
				return siteAcesso = true;
			}
			}while (loginErrado = true);
			}
		}
}




	
	
	



bool siteLogin(bool boolSiteLogin){
	if (boolSiteLogin == true){
		
		
	}
}











int main(){
	char rLOuV; 
	bool vLogin,boolSiteLogin;
	setlocale(LC_ALL,"portuguese");
	
	rLOuV=loginOuVisitante();
	vLogin=verificacaoRLOuV(rLOuV);
	boolSiteLogin=login(vLogin);
	siteLogin(boolSiteLogin);	
	
	
	
}