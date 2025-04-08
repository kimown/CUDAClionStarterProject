#include "cudaMain.h"


void test(){
    int aa=2;
    int bb = aa+10;
}

int main(int argc, char **argv) {
    int a=1;
    int b=1+1;
    test();
    return cudaMain(argc, argv);
//    return 0;
}
