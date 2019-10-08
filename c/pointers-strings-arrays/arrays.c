#include <stdio.h>

int main(){
    float arr[10]; //creates an integer array with 10 elements

    //store numbers 0 to 9 in the array "arr"
    int i = 0;
    for (i=0; i<10; i++){
        arr[i] = (float)i;  // it's iterating by calculating the index*size of each element and adds it to the
        // current memory address to jump ahead to access the next element at the next index
    }

    printf("Value at arr: %f\n", *arr);

    float* p = arr;
    int count = 0;
    while (count<10){
        printf("Value stored at %p is %f\n", p, *p);
        p++; // as a memory address, it jumps to the next memory address based on the array type aka int 
        // will jump by 4 bytes, float will jump by 4 bytes etc.
        count++;
    }

    //print the values inside this array
    for (i=0; i<10; i++){
        printf("%f, ", arr[i]);
    }

    printf("\n");
    return 0;
}