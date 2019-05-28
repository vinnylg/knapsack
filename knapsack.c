#include <stdio.h>
#include <stdlib.h>
#include <string.h> 

#define ERROR(str){printf("%s\n",str); return -1;}

void read_file(FILE *input, int *value, int *weight, int i){
    char line[32];
    while(fgets(line,32,input)){
        value[i] = atoi(strtok(line," "));
        weight[i] = atoi(strtok(NULL," "));
        i++;
    };
}                                                                                                     

int main(int argc, char **argv){
    if(!argv[1]) ERROR("USAGE: knapsack <size_of_knapsack> <file_of_items>")
    
    FILE *file = fopen(argv[1],"r");

    if(!file) ERROR("File couldn't opened")

    int k_weight, n_obj, *values, *weights;

    fscanf(file,"%d %d\n",&n_obj,&k_weight);

    values = malloc(n_obj*sizeof(int));
    weights = malloc(n_obj*sizeof(int));

    read_file(file,values,weights,0);
    fclose(file);


    printf("L%d m%d\n",n_obj,k_weight);
    printf("value weight\n");
    for(int i=0; i<n_obj; i++){
        printf("%d %d\n",values[i],weights[i]);
    }
}
