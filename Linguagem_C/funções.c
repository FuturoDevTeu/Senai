#include <stdio.h>
#include <locale.h>


int calculomedia(int n1, int n2){
	return (n1+ n2)/2;
}


int main(){
	setlocale(LC_ALL,"portuguese");
	int n1,n2;
	float media;
	
	printf("Digite o 1º numero: ");
	scanf("%i",&n1);
	
	printf("Digite o 2º numero: ");
	scanf("%i",&n2);
	
	media = calculomedia(n1,n2);
	
	printf("Media: %.2f",media);
}

