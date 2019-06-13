#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long int n_obj[4]={30000,60000,120000,240000};
long int weight_max[4]={100000,200000,400000,800000};

int main(){
    int count_files = 0;
    char cmd[100];
    long int weight,obj;
    for( weight=0; weight < 4; weight++)
        for (obj=0; obj < 4; obj++){
            count_files++;
            sprintf(cmd,"./createItem items/0/mf%ld-%ld %ld %ld",weight_max[weight],n_obj[obj],n_obj[obj],weight_max[weight]);
            if(system(cmd));
            sprintf(cmd,"./createItem items/1/mf%ld-%ld %ld %ld",n_obj[obj],weight_max[weight],weight_max[weight],n_obj[obj]);
            if(system(cmd));
        }

    printf("\nfiles type: mfweight_max-n_obj\nto use all %d files, run ./test.sh\n",count_files);
}
