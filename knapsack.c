#include <stdio.h>
#include <stdlib.h>
#include <string.h> 

#define ERROR(str){printf("%s\n",str); return -1;}

int knapsack(int *value, int *weight, int n_obj, int size_knap, int **V, int **keep){
	int w,  
	    i;
	for(w=0; w <= size_knap; w++) V[0][w] = 0;
	for(i=0; i <= n_obj; i++) V[i][0] = 0;
	
	for(i=1; i <= n_obj; i++)
		for(w = 1; w <= size_knap; w++)
			if( (weight[i] < w) && (value[i]+V[i-1][w-weight[i]] > V[i-1][w])){
				V[i][w]=value[i] + V[i-1][w-weight[i]];	
				keep[i][w]=1;
			}else{
				V[i][w] = V[i-1][w];
				keep[i][w] = 0;
			}
	int K = size_knap;
	for(i=n_obj; i>0; i--){
		if(keep[i][K] == 1){
		//	printf("i %d w %d v%d\n",i,weight[i],value[i]);
			K = K - weight[i];
		}
	}
	return V[n_obj][size_knap];
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

    values = malloc(n_obj*sizeof(int));
    weights = malloc(n_obj*sizeof(int));

    read_file(file,values,weights,1);
    fclose(file);

    int **bottom = malloc((n_obj+1)*sizeof(int *));
    int **keep = malloc((n_obj+1)*sizeof(int *));
    
    for(int i=0; i<=n_obj; i++){
    	bottom[i]= malloc(max_weight * sizeof(int));
    	keep[i]= malloc(max_weight * sizeof(int));
    }

    printf("Max Value:%d\n",knapsack(values,weights,n_obj,max_weight,bottom,keep));
	
    free(values);	
    free(weights);
	
    for(int i=0; i<=n_obj; i++){
	free(bottom[i]);
	free(keep[i]);
    }
    free(bottom);
    free(keep);
    return 0;
}
