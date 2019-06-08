#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long int n_obj_exp[11]={1000,2000,4000,8000,16000,32000,64000,128000,256000,512000,1024000};
long int weight_max_exp[11]={10000,20000,40000,80000,160000,320000,640000,1280000,2560000,5120000,10240000};
long int n_obj_lin[19]={1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000};
long int weight_max_lin[19]={10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,200000,300000,400000,500000,600000,700000,800000,900000,1000000};

int main(){
    char cmd[100];
    long int weight_max,n_obj;
    for( weight_max=0; weight_max < 11; weight_max++)
        for (n_obj=0; n_obj < 11; n_obj++){
            sprintf(cmd,"./createItems items/mexp%ld-%ld %ld %ld",n_obj_exp[n_obj],weight_max_exp[weight_max],n_obj_exp[n_obj],weight_max_exp[weight_max]);
            printf("%s\n",cmd);
            if(system(cmd));
        }
    for( weight_max=0; weight_max < 19; weight_max++)
        for (n_obj=0; n_obj < 19; n_obj++){
            sprintf(cmd,"./createItems items/mlin%ld-%ld %ld %ld",n_obj_lin[n_obj],weight_max_lin[weight_max],n_obj_lin[n_obj],weight_max_lin[weight_max]);
            printf("%s\n",cmd);
            if(system(cmd));
        }
}
