#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long int n_obj_exp[8]={1000,2000,4000,8000,16000,32000,64000,128000};
long int weight_max_exp[6]={10000,20000,40000,80000,160000,320000};
long int n_obj_lin[19]={1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000};
long int weight_max_lin[13]={10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,200000,300000,400000};

int main(){
    int count_files = 0;
    char cmd[100];
    long int weight_max,n_obj;
    for( weight_max=0; weight_max < 6; weight_max++)
        for (n_obj=0; n_obj < 8; n_obj++){
            count_files++;
            sprintf(cmd,"./createItem items/mexp%ld-%ld %ld %ld",weight_max_exp[weight_max],n_obj_exp[n_obj],n_obj_exp[n_obj],weight_max_exp[weight_max]);
            printf("%s\n",cmd);
            if(system(cmd));
        }
    for( weight_max=0; weight_max < 13; weight_max++)
        for (n_obj=0; n_obj < 19; n_obj++){
            count_files++;
            sprintf(cmd,"./createItem items/mlin%ld-%ld %ld %ld",weight_max_lin[weight_max],n_obj_lin[n_obj],n_obj_lin[n_obj],weight_max_lin[weight_max]);
            printf("%s\n",cmd);
            if(system(cmd));
        }

    printf("\nfiles type: m[exp|lin]weight_max-n_obj\nto use all %d files, run ./test.sh [mexp|mlin] \n",count_files);
}
