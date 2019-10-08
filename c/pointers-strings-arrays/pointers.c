#include <stdio.h>

int main(){
    int i; // declaring a simple integer
    int* p = NULL; // declare an integer pointer
    int q;
    int** w; // NEEDS a double star because it is a pointer that stores the address of a int*

    i= 3;
    p = &i;
    q = *&i;
    w = &p;

    scanf("%d", p); // is the exact same as
    //scanf("%d", &i); // because in this case, &i acts as a pointer, as it is a memory address by itself.
    // in other words, scanf is likely to be a function that takes in pointers e.g. scanf(int* x){}



    printf("Value of i: %d\n", i); // expect an integer
    printf("Value of p: %p\n", p); // expect memory address of 3
    printf("Value of q: %d\n", q); // expect the original i
    printf("Value of w: %p\n", w); // expect memory address of memory address of 3

    printf("*p = %d\n", *p); // This * is different from the pointer from above
    // It takes the address stored in p, and go to the location and use the value stored there.
    // Can even be recursive if the address stored in p leads to a memory storing another address.
    // aka **p will work if *p leads to a int* x for e.g.

    printf("*w = %p\n", *w); // This gives us the memory address of i.
    printf("**w = %d\n", **w);
    //p = i;

    //printf("Simple p=i: %d\n", *p);
    return 0;
}