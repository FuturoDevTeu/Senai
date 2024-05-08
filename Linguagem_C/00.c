#include <stdio.h>
#include <locale.h>
#include <string.h>
#include <stdlib.h>
#include <locale.h>
#include <time.h>
#include <stdbool.h>
#include <unistd.h>
#include <ctype.h>


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
	bool vLogin = false; 
	if(vRLOuV == '1'){
		return vLogin = false;
	}else{
		return vLogin = true;
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
			do{
			if (strcmp(login,loginCorreto) == 0 && strcmp(senha,senhaCorreta) == 0){
				return siteAcesso = true;
			}else{
			
				loginErrado = true;
				printf("LOGIN OU SENHA INCORRETA");
				sleep(2);
				system("cls || clear");
				printf("Digite o login: ");
				scanf("%s",&login);
				printf("Digite a senha: ");
				scanf("%s",&senha);
				}
				}while (loginErrado = true);
		}else{
			return siteAcesso = false;
		}
			
}
		
int menuProdutoLancamento(){
	char codigo;
	
	printf("Produto\t\t\t Valor\t\tcodigo\n");
	printf("Camisa do Corinthians\t R$299,99\t1\n");
	printf("Tenis dunk\t\t R$854,99\t2\n");
	printf("Camisa do Brasil\t R$332,99\t3\n");
	fflush(stdin);
	printf("Digite o codigo do produto: ");
	scanf("%c",&codigo);
	return codigo;

}

int menuProdutoOferta(){
	char codigo;
	
	printf("Produto\t\t\t Valor\t\tcodigo\n");
    printf("Meia Mike\t\t R$113,39\t1\n");
	printf("Mochila Mike hike\t R$427,49\t2\n");
	printf("Touca Mike Liverpool\t R$94,99\t3\n");
	printf("Digite o codigo do produto: ");
	fflush(stdin);
	scanf("%c",&codigo);
	return codigo;
}


bool siteLogin(bool boolSiteLogin){
	char codigoDoProduto,codigoProdutoLancamento,produtoLancamento[200];
	char codigoProdutoOferta,pergunta[3],produtoOferta[200];
	float precoLancamento,precoOferta=0;
	if (boolSiteLogin == true){
		do{
		system("cls || clear");
		printf("Seja bem vindo a loja MIKE!!\n");
		printf("Digite o codigo do serviço desejado:\n");
		printf("Digite 1 para Lancamentos\n");
		printf("Digite 2 para ofertas\n");
		printf("Qual o codigo desejado: ");
		
		fflush(stdin);
		scanf("%c",&codigoDoProduto);
	
		switch(codigoDoProduto){
			case '1' :
				codigoProdutoLancamento=menuProdutoLancamento();
				
				if(codigoProdutoLancamento == '1'){
					strcpy(produtoLancamento,"Camisa do Corinthians R$299,99");
					precoLancamento+=299.99;
				}else if(codigoProdutoLancamento == '2'){
					strcpy(produtoLancamento,"Dunk R$854,99");
					precoLancamento+=854.99;
				}else if(codigoProdutoLancamento == '3'){
					strcpy(produtoLancamento,"Camisa do Brasil R$332,99");
					precoLancamento+=332.99;
				}else{
					printf("Codigo Produto invalido");
				}
		
				printf("Deseja continuar: ");
				fflush(stdin);
				scanf("%c",&pergunta);
				system("cls");
				break;
			case '2' :
				codigoProdutoOferta=menuProdutoOferta();
				
				if(codigoProdutoOferta == '1'){
					strcpy(produtoOferta,"Meia Mike");
					precoOferta+=113.39;
				}else if(codigoProdutoOferta == '2'){
					strcpy(produtoOferta,"Mochila Mike hike");
					precoOferta+=427.49;
				}else if(codigoProdutoOferta == '3'){
					strcpy(produtoOferta,"Touca Mike Liverpool");
					precoOferta+=94.99;
				}else{
					printf("Codigo Produto invalido");
				}
			
				printf("Deseja continuar: ");
				fflush(stdin);
				scanf("%c",&pergunta);
				system("cls");
				break;
			
			default :
				printf("Servico invalido!!");
			}
			}while(pergunta == "sim");
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
	
	
	
<<<<<<< HEAD
}
=======
}
>>>>>>> refs/remotes/origin/main
