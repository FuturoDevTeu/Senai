#include <stdio.h>
#include <locale.h>
#include <string.h>
#include <stdlib.h>
#include <locale.h>


char* loginOuVisitante(){
	char resposta;
	printf("codigo  |\t descrição");	
	printf("\n1 \t|\t acesar site no modo visitante");	
	printf("\n2 \t|\t logar em uma conta\n");
	printf("Digite o codigo que deseja: ");
	scanf("%c",&resposta);
	
	switch (resposta){
		case '1':
			return resposta;
		
		case '2':
			return resposta;
		
		case '3':
			return resposta;
			
	}
}


char* login(){
	
} 









int main(){
	char rLOuV; 
	char inicializadorDeFuncoes;
	
	setlocale(LC_ALL,"portuguese");
	
	rLOuV=loginOuVisitante();
	
	printf(rLOuV);
	
}
