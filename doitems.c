#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long int n_obj[3]={40000,80000,160000};
long int weight_max[3]={400000,800000,1600000};

int main(){
    int count_files = 0;
    char cmd[100];
    long int weight,obj;
    for( weight=0; weight < 3; weight++)
        for (obj=0; obj < 3; obj++){
            count_files++;
            sprintf(cmd,"./createItem items/mf%ld-%ld %ld %ld",weight_max[weight],n_obj[obj],n_obj[obj],weight_max[weight]);
            printf("%s\n",cmd);
            if(system(cmd));
            sprintf(cmd,"./createItem items/mf%ld-%ld %ld %ld",n_obj[obj],weight_max[weight],weight_max[weight],n_obj[obj]);
            if(system(cmd));
        }

    printf("\nfiles type: mfweight_max-n_obj\nto use all %d files, run ./test.sh\n",count_files);
}
