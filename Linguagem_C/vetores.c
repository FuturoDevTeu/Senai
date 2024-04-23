#include <stdio.h>
#include <locale.h>
#include <stdlib.h>
#include <limits.h>



int par(int n[],int i){
	if(n[i]%2==0){
		return +1;
	}
	return 0;
}

int impar(int n[],int i){
	if(n[i]%2!=0){
		return +1;
	}
	return 0;
}

int positivo(int n[],int i){
	if(n[i]>=0){
		return +1;
	}	
	return 0;
}
	
int negativo(int n[],int i){
	if(n[i]<0){
		return +1;
	}
	return 0;
}



int main(){
	setlocale(LC_ALL,"portuguese");
	int numero[900],i=0,nPar=0,nImpar=0,nPositivo=0,nNegativo=0; 
	 
	 
	 
	do{
		i++;
		printf("DIgite o %i° numero: ",i);
		scanf("%i",&numero[i]);
		
		nPar+=par(numero,i);	
		nImpar+=impar(numero,i);
		nPositivo+=positivo(numero,i);
		nNegativo+=negativo(numero,i);
			
	}while(numero[i]!=0);
	
	printf("Total de pares: %i\n",nPar);
	printf("Total de impares: %i\n",nImpar);
	printf("Total de positivos: %i\n",nPositivo);
	printf("Total de negativo: %i\n",nNegativo);

}