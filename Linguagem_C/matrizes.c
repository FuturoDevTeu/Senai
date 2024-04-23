#include <stdio.h>
#include <locale.h>

int main(){
	setlocale(LC_ALL,"portuguese");
	char materia[3][200];
	int nota[3][2],soma,i,j;
	float media[3];	
	
	for(i=0;i<3;i++){
		printf("Digite o nome da %i° materia: ",i+1);
		scanf("%s",&materia[i]);
		for(j=0;j<2;j++){
			printf("Digite a %i° nota de %s: ",j+1,materia[i]);
			scanf("%i",&nota[i][j]);
			soma+=nota[i][j];		
		}
	media[i]=soma/j;
	soma=0;
	printf("\n");
	}
	system("cls");
	for(i=0;i<3;i++){
		printf("Materia: %s\n",materia[i]);
		for(j=0;j<2;j++){
			printf("%i nota: %i\n",j+1,nota[i][j]);
		}
		printf("Media: %.1f\n",media[i]);
	}
	
	
}
