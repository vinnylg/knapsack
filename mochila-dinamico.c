#include <stdio.h>
#include <stdlib.h>


struct Objeto{
	unsigned int weight;  //representa peso do objeto
	unsigned int value;   //representa valor do objeto
}typedef Objeto;


//n - posiçao atual no vetor de objetos
//obj - vetor de struct objetos com a lista de todos os objetos possiveis
//retorna maior valor possivel da mochila
unsigned int Knapsack(unsigned int n, Objeto obj[], unsigned int C, int **acc){
	unsigned int result;
	//checa para saber se valor ja foi calculado anteriormente
	if (acc[n][C] != -1) return acc[n][C];
	//caso percorreu tudo 
	if(n == 0 || C == 0) result = 0;
	
	else if (obj[n].weight > C)           						//caso objt ultrapasse capacidade da mochila, 																
		result = Knapsack(n-1, obj, C, acc);							//ir para prox elemento
	
	else{
		unsigned int tmp1, tmp2;
		tmp1 = Knapsack(n-1, obj, C, acc);    						 //move p/ prox elemento - nao adiciona item na mochila
		tmp2 = obj[n].value + Knapsack(n-1, obj, C - obj[n].weight, acc);  //adicionar item na mochila e recalcular valor da machila
														         
		if(tmp1 > tmp2) result = tmp1;							 //result recebe o maior valor entre tmp1 e tmp2
		else result = tmp2;
	}
	acc[n][C] = result;
	return result;
}




int main (){
	int n_itens, c_mochila;
	FILE * arq = fopen("mochila_simples.txt", "r");
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

	int **Acc = malloc(sizeof(int)*n_itens);
	for(int i=0; i<c_mochila; i++){
		Acc[i] = malloc(sizeof(int)* c_mochila);
	}
	//preenche matriz de valores acumulados com inteiro de sinalização
	for(int i=0; i<n_itens; i++){
		for(int j=0; j<c_mochila; j++){
			Acc[i][j] = -1;
		}
	}

	unsigned int maior_valor = Knapsack(n_itens, objetos, c_mochila, Acc);
	printf("----------------------------\n");
	printf("Maior Valor Encontrado: %d\n",maior_valor);
}