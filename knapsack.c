#include <stdio.h>
#include <stdlib.h>
#include <string.h> 

#define ERROR(str){printf("%s\n",str); return -1;}

void printM(size_t **M, int n, int m){
        printf("\n");        
        for(int i = 0; i <= n; i++){
                for(int j = 0; j <= m; j++){
                        printf("%ld ",M[i][j]);
                }
                printf("\n");
        }
        printf("\n");
}

size_t *zeraRow(size_t *row, int tam){
    for(int i=0; i<tam; i++)
        row[i]=0;

    return row;
}


size_t *cpRows(size_t *origin, size_t *destiny, int tam){
    for(int i=0; i<tam; i++)
        destiny[i]=origin[i];

    return destiny;
}

int knapsack(int *value, int *weight, int max_row, int max_col, size_t **V){
	int w,                                             //peso iterativo 
	    i;                                             //contador de itens 

	for(i=1; i <= max_row; i++){                    //percorre apartir do primeiro item até o ultimo (i=0==NULL)
		for(w = 1; w <= max_col; w++)               //percorre desde o peso 1 até o peso maximo da mochila
			if( (weight[i] <= w) && (value[i]+V[0][w-weight[i]] > V[0][w])){    
                //se o item i caber no peso w E o valor do item i + 
                //o valor da linha de cima no peso que sobra da mochila com o item i
                //for maior que o valor do item de cima com o peso w
                V[1][w]=value[i] + V[0][w-weight[i]];   //coloca essa soma
			}else{
				V[1][w] = V[0][w];                      //senão coloca o valor de cima 
			}
        V[0] = cpRows(V[1],V[0],max_col+1);     //coloca a linha de baixo em cima  
        V[1] = zeraRow(V[1],max_col+1);     //zera a linha de baixo
        printM(V,1,max_col);
    }
    	
    return V[0][max_col];
}

void read_file(FILE *input, int *value, int *weight, int i){
    char line[32];                          
    while(fgets(line,32,input)){                    
        value[i] = atoi(strtok(line," "));
        weight[i] = atoi(strtok(NULL," "));
        i++;
    };
}                                                                                                     

int main(int argc, char **argv){
    if(!argv[1]) ERROR("USAGE: knapsack <file_of_items>")
    
    FILE *file = fopen(argv[1],"r");

    if(!file) ERROR("File couldn't opened")

    int max_weight, n_obj, *values, *weights;

    fscanf(file,"%d %d\n",&n_obj,&max_weight);
    printf("%d items, knapsack size: %d\n",n_obj,max_weight);
 
    values = malloc((n_obj+1)*sizeof(int));
    weights = malloc((n_obj+1)*sizeof(int));

    read_file(file,values,weights,1); //le o arquivo e coloca apartir da posição 1, para deixar i igual o item 
    fclose(file);

    size_t **bottom = malloc(2*sizeof(size_t *));  //it's needly only two rows
                                            
    for(int i=0; i<2; i++){
    	bottom[i]= malloc((max_weight+1) * sizeof(size_t));
        memset(bottom[i],0,(max_weight+1) * sizeof(size_t));
    }

    printf("Max Value:%d\n",knapsack(values,weights,n_obj,max_weight,bottom));
	
    free(values);	
    free(weights);
    free(bottom[0]);
    free(bottom[1]);
    free(bottom);
    return 0;
}
