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
    if(!argv[1]||!argv[2]) ERROR("USAGE: knapsack <size_of_knapsack> <file_of_items>")
    
    FILE *file = fopen(argv[2],"r");

    if(!file) ERROR("File couldn't opened")

    int max_weight, n_obj, *values, *weights, size_knap = atoi(argv[1]);

    fscanf(file,"%d %d\n",&n_obj,&max_weight);
    printf("n_obj %d max_weight %d size_knapsack %d\n",n_obj,max_weight,size_knap);
    printf("item value weight\n");

    values = malloc(n_obj*sizeof(int));
    weights = malloc(n_obj*sizeof(int));

    read_file(file,values,weights,1);
    fclose(file);

    for(int i = 1; i <= n_obj; i++){
        printf("%d %d %d\n",i,values[i],weights[i]);
    }
}
