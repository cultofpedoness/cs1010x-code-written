#include <stdio.h>
#define NUM_OF_DIGITS 7
#define NUM_OF_LETTERS 11

char get_check_code(int n[]){
    int mult[] = {2, 7, 6, 5, 4, 3, 2};
    int sum = 0;
    for (int i=0; i<7; i++){
        sum += n[i]*mult[i];
    }
    sum = sum%11;
    sum = 11-sum;
    // char x = '\0';
    // switch (sum){
    //     case 1:
    //         x = 'A';
    //         break;
    //     case 2:
    //         x = 'B';
    //         break;
    //     case 3:
    //         x = 'C';
    //         break;
    //     case 4:
    //         x = 'D';
    //         break;
    //     case 5:
    //         x = 'E';
    //         break;
    //     case 6:
    //         x = 'F';
    //         break;
    //     case 7:
    //         x = 'G';
    //         break;
    //     case 8:
    //         x = 'H';
    //         break;
    //     case 9:
    //         x = 'I';
    //         break;
    //     case 10:
    //         x = 'Z';
    //         break;
    //     case 11:
    //         x = 'J';
    //         break;
    //     default:
    //         break;
    //     }
    // return x;

    char letters[NUM_OF_LETTERS + 2] = "-ABCDEFGHIZJ";
    return letters[sum];
}

int main(){
    int arr[] = {9, 3, 0, 0, 0, 0, 7};
    int nric, nric_tail;
    int nric_digits[NUM_OF_DIGITS];
    char code;

    printf("Enter your 7-digit NRIC Number: ");
    scanf("%d", &nric);

    nric_tail = nric;
    for (int i=NUM_OF_DIGITS-1; i>=0; i--){
        nric_digits[i] = nric_tail %10;
        nric_tail = nric_tail/ 10;
    }

    code = get_check_code(nric_digits);
    printf("Your check code is '%c'\n", code);
    printf("Your check code is '%c'\n", get_check_code(arr));
    return 0;
}