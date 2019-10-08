#include <stdio.h>
#include <string.h>

#define N 20

int main(){
    char s1[20] = "Hello!"; // if you allocate 10 for s1, it will actually result in the leaking of memory
    // from strcat into s2, resulting in d!/0 leaking into s2, and s2 will print as "d!"
    char s2[20] = "World!";

    int x = 20;
    printf("%d\n", x);
    //char s3[n] = "Hello World!"; // This will result in an error as a variable-sized object may not
    // be initialised.
    
    //BUT
    char s4[N] = "Helloooo!"; // will work!

    printf("s1 (%p) = %s, s2 (%p) = %s\n", &s1, s1, &s2, s2);
    strcat(s1, s2);
    printf("s1 (%p) = %s, s2 (%p) = %s\n", &s1, s1, &s2, s2);

    printf("%s\n", s4);

    char* s5 = "testest"; // This actually asks for the system to create an array of a certain size
    // and insert "testest" in there, then points to the array. This array is read-only.
    char s6[20] = "yoloo"; // This one can be edited.
    printf("s5 (%p) = %s, s6 (%p) = %s\n", &s5, s5, &s6, s6);
    strcat(s6, s5); // You can only strcat from s5 to s6, but not from s6 to s5, because s5 is read-only
    // and has a fixed space.
    printf("s5 (%p) = %s, s6 (%p) = %s\n", &s5, s5, &s6, s6);

    char* s7;
    char s8[20] = "hellowhatsup";
    printf("s7 (%p) = %s, s8 (%p) = %s\n", &s7, s7, &s8, s8);
    s7 = s8;
    printf("s7 (%p) = %s, s8 (%p) = %s\n", &s7, s7, &s8, s8);
    return 0;
}