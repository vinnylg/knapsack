#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define ERROR(str){printf("%s\n",str); return -1;}


struct Objeto{
	unsigned int weight;  //representa peso do objeto
	unsigned int value;   //representa valor do objeto
}typedef Objeto;


//n - posiçao atual no vetor de objetos
//obj - vetor de struct objetos com a lista de todos os objetos possiveis
//retorna maior valor possivel da mochila
unsigned int Knapsack(unsigned int n, Objeto obj[], unsigned int C){
	unsigned int result;

	#pragma omp parallel firstprivate(n, obj, C) shared(result)
	{
		if(n == 0 || C == 0 ) result = 0;

		else if(obj[n].weight > C){
			#pragma omp single
			{
				// #pragma omp task shared(result)
				result = Knapsack(n-1, obj, C);
			}
		}

		else{
			unsigned int tmp1, tmp2;
			#pragma omp single
			{
				#pragma omp task shared(tmp1)
				tmp1 = Knapsack(n-1, obj, C);

				#pragma omp task shared(tmp2)
				tmp2 = obj[n].value + Knapsack(n-1, obj, C - obj[n].weight);

				#pragma omp taskwait
				if(tmp1 > tmp2) result = tmp1;
				else result = tmp2;
			}
		}	
	}
	return result;

}



int main (int argc, char **argv){
	int n_itens, c_mochila;
	if(argc < 2){
		ERROR("Colocar nome do arquivo de entrada")
	}
	FILE * arq = fopen(argv[1], "r");
	if(!arq){
		printf("Arquivo não encontrado :(\n");
		exit(0);
	}
	fscanf(arq,"%i %i", &n_itens, &c_mochila);
	printf("Número de Objetos:%i  Capacidade da Mochila: %i\n\n",n_itens, c_mochila);

	Objeto objetos[n_itens]; 
	for(int i=0; i<n_itens; i++){
		fscanf(arq, "%i %i", &objetos[i].value, &objetos[i].weight);
	}

	for(int i=0; i<n_itens; i++){
		printf("objetos[%i]: valor: %i peso: %i\n",i, objetos[i].value, objetos[i].weight);
	}


	unsigned int maior_valor = Knapsack(n_itens, objetos, c_mochila);
	printf("----------------------------\n");
	printf("Maior Valor Encontrado: %d\n",maior_valor);
}