#include <stdio.h>
#include <string.h>
#define NUM_DISCS 4

typedef struct {
    int peg[3][NUM_DISCS];
    char name[30];
} Towers;

void make_moves(Towers *t, int n, int src, int des, int aux);
void init_towers(Towers *t, const char name[]);
void print_towers(Towers t);
void move_disc(Towers *t, int src, int des);

int main(void){
    Towers t;
    init_towers(&t, "Hanoi");
    printf("Towers of %s\n", t.name);
    print_towers(t);
    make_moves(&t, NUM_DISCS, 0, 2, 1);
    return 0;
}

void make_moves(Towers *t, int n, int src, int des, int aux){
    if (n<=0) return;
    make_moves(t, n-1, src, aux, des);
    move_disc(t, src, des);
    make_moves(t, n-1, aux, des, src);
    return;
}

void init_towers(Towers *t, const char name[]){ // both t and *t will work, but t will be t.peg, while t* will be t->peg
    int name_len = strlen(name);
    for (int i=0; i<name_len; i++){
        t->name[i] = name[i];
    }
    for (int i=0; i<NUM_DISCS; i++){
        t->peg[0][i] = i;
    }
    for (int i=1; i<3; i++){
        for (int x=0; x<NUM_DISCS; x++){
            t->peg[i][x] = -1;
        }
    }
    return ;
}

void print_towers(Towers t){
    for (int i=0; i<3; i++){
        printf("[ ");
        for (int x=0; x<NUM_DISCS; x++){
            if (t.peg[i][x]>=0){
                printf("%d ", t.peg[i][x]);
            }
        }
        printf("]");
        if (i<2){
            printf(", ");
        }else{
            printf("\n");
        }
    }
}

void move_disc(Towers *t, int src, int des){
    int disc;
    for (int i=NUM_DISCS-1; i>-1;i--){
        if (t->peg[src][i]>-1){
            disc = t->peg[src][i];
            t->peg[src][i] = -1;
            break;
        }
    }
    for (int i=0; i<NUM_DISCS; i++){
        if (t->peg[des][i]==-1){
            t->peg[des][i] = disc;
            break;
        }
    }
    print_towers(*t);
    return;
}

// void move_disc(Towers *t, int src, int des) {
//     int src_last=0;
//     int des_last=0;
//     while (t->peg[src][src_last]!=-1 && src_last<NUM_DISCS){
//         src_last++;
//     }
//     while (t->peg[des][des_last]!=-1 && des_last<NUM_DISCS){
//         des_last++;
//     }
    
//     int val = t->peg[src][src_last-1];
//     t->peg[src][src_last-1]=-1;
//     t->peg[des][des_last]=val;
    
//     print_towers(*t);
//     return;
// }