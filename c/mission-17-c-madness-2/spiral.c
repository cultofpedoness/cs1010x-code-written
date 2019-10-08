/*****************************************
 * CS1010X --- Programming Methodology  *
 *                                       *
 *   Mission 17, Question 1 Template     *
 *****************************************/

#include <stdio.h>
#include <string.h>
#define MAX_LEN 80

void fill(char matrix[MAX_LEN][MAX_LEN], char c) {
    int row, col;
    for (row = 0; row < MAX_LEN; ++row) {
        for (col = 0; col < MAX_LEN; ++col) {
            matrix[row][col] = c;
        }
    }
}

void print(char matrix[MAX_LEN][MAX_LEN], int length) {
    int row, col;
    for (col = 0; col < length + 2; ++col) {
        printf("-");
    }
    printf("\n");
    for (row = 0; row < length; ++row) {
        printf("|");
        for (col = 0; col < length; ++col) {
            printf("%c", matrix[row][col]);
        }
        printf("|\n");
    }
    for (col = 0; col < length + 2; ++col) {
        printf("-");
    }
    printf("\n");
}

void spiral(char matrix[MAX_LEN][MAX_LEN], int length, char *text) {
    int text_length = 0;
    for (int i=0; i<MAX_LEN; i++){
        if (text[i]!='\0'){
            text_length ++;
        }else{
            break;
        }
    }
    int start = 0, top = 0, end = length, bottom = length;
    int x = 0;
    while(1==1){
        for (int i=start; i<end; i++){
            matrix[top][i] = text[x];
            if (x<text_length-1){
                x++;
            }else{
                x=0;
            }
        }
        top++;
        for (int i=top; i<bottom; i++){
            matrix[i][end-1] = text[x];
            if (x<text_length-1){
                x++;
            }else{
                x=0;
            }
        }
        end--;
        for (int i=end-1; i>=start; i--){
            matrix[bottom-1][i] = text[x];
            if (x<text_length-1){
                x++;
            }else{
                x=0;
            }
        }
        bottom--;
        if (top==bottom){
            break;
        }
        for (int i=bottom-1;i>=top;i--){
            matrix[i][start] = text[x];
            if (x<text_length-1){
                x++;
            }else{
                x=0;
            }
        }
        start++;
    }
    return;
}

int main(void) {
    char matrix[MAX_LEN][MAX_LEN] = {{'a'}};
    fill(matrix, ' ');
    spiral(matrix, 10, ".... . ._.. .__. __ .");
    print(matrix, 10);

    spiral(matrix, 20, "\\/");
    spiral(matrix, 14, "TheQuickBrownFoxJumpsOverTheLazyDog");
    print(matrix, 21);
    return 0;
}

/*
 EXPECTED OUTPUT:

    ------------
    |.... . ._.|
    |_. __ ....|
    |_.... . . |
    |..........|
    |    ._ _ _|
    |.__.._..._|
    |.__._. . .|
    |_  .__. . |
    |..__. ..__|
    | . ..... _|
    ------------
    -----------------------
    |TheQuickBrownF\/\/\/ |
    |JumpsOverTheLo/\/\/\ |
    |xTheLazyDogTax\/\/\/ |
    |orheLazyDoghzJ/\/\/\ |
    |FeTpsOverTTeyu\/\/\/ |
    |nvrmuickBhhQDm/\/\/\ |
    |wOeuQJumreeuop\/\/\/ |
    |osvJexspoLQigs/\/\/\ |
    |rpOxhoFnwaucTO\/\/\/ |
    |BmsoTgoDyzikhv/\/\/\ |
    |kupFnworBkcBee\/\/\/ |
    |cJmuJxoFnworQr/\/\/\ |
    |ixoFnworBkciuT\/\/\/ |
    |uQehTgoDyzaLeh/\/\/\ |
    |\/\/\/\/\/\/\/\/\/\/ |
    |/\/\/\/\/\/\/\/\/\/\ |
    |\/\/\/\/\/\/\/\/\/\/ |
    |/\/\/\/\/\/\/\/\/\/\ |
    |\/\/\/\/\/\/\/\/\/\/ |
    |/\/\/\/\/\/\/\/\/\/\ |
    |                     |
    -----------------------
*/
