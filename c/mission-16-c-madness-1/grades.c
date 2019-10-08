/*****************************************
 * CS1010X --- Programming Methodology  *
 *                                       *
 *   Mission 16, Question 1 Template     *
 *****************************************/

#include <stdio.h>
#include <math.h>

// Gives the minimum EXP required to reach level n from level 0.
int exp_for_level(int n) {
    return (int)(100 * pow(n, 2.3));
}

int compute_level(int exp, int *exp_to_levelup) {
    /************
     *  Task 1  *
     ************
     
     Return the level of the student given the total EXP gained.
     Also sets the additional EXP required to level-up through
     the exp_to_levelup pointer.
     
     If the EXP is negative (i.e. invalid), return the negative
     EXP as the level and set exp_to_levelup to zero.
     
    */
    int n = 1, level;
    int exp_needed = exp_for_level(n++);
    if (exp<0){
      *exp_to_levelup = 0;
      return exp;
    }else{
      while (exp>=exp_needed){
        exp_needed = exp_for_level(n++);
      }
    }
    level = n-2;
    exp_needed -= exp;
    *exp_to_levelup = exp_needed;
    return level;
}

char compute_grade(int level) {
    /************
     *  Task 2  *
     ************
     
     Return the letter grade assigned to the student for his/her level:
       'A' - level 38 and above
       'B' - level 29 to level 37
       'C' - level 17 to level 28
       'D' - level 11 to level 16
       'E' - level 7 to level 10
       'F' - level 0 to level 6
     
     For anything else, return '?'.
     
    */

    char result;
    if (level<0){
      result = '?';
    }else if (level<7){
      result = 'F';
    }else if (level<11){
      result = 'E';
    }else if (level<17){
      result = 'D';
    }else if (level<29){
      result = 'C';
    }else if (level<38){
      result = 'B';
    }else{
      result = 'A';
    }
    return result;
}

void print_remark(char grade) {
    /************
     *  Task 3  *
     ************
     
     Print the following messages (_exactly_ as they are shown after the
     colon + space) for each grade:
     
             A: Excellent, you scored 100% for coursemology!
             B: Very well done!
        C or D: Please work harder.
             E: Marginally better than an 'F'
             F: :\
     
     If the grade is none of the above, print instead:
                Unknown grade "X"
     where X is the unidentifiable grade between double-quotes.
     
     !!IMPORTANT!!: You are required to use the switch statement for this task.
     
    */
    switch(grade){
      case 'A':
        printf("Excellent, you scored 100%% for coursemology!");
        break;
      case 'B':
        printf("Very well done!");
        break;
      case 'C':
      case 'D':
        printf("Please work harder.");
        break;
      case 'E':
        printf("Marginally better than an 'F'");
        break;
      case 'F':
        printf(":\\");
        break;
      default:
        printf("Unknown grade \"%c\"", grade);
        break;
    }
}

int main(void) {
    int exp, exp_to_levelup;
    printf("Enter experience points: ");
    scanf("%d", &exp);
    
    int level = compute_level(exp, &exp_to_levelup);
    char grade = compute_grade(level);
    
    printf("Level: %d\n", level);
    printf("Grade: %c\n", grade);
    printf("EXP needed to level-up: %d\n", exp_to_levelup);
    printf("Remarks: ");
    print_remark(grade);
    printf("\n\n");
    return 0;
}


/*
  SAMPLE EXECUTIONS:

     Enter experience points: 100
     Level: 1
     Grade: F
     EXP needed to level-up: 392
     Remarks: :\
     
     Enter experience points: 439901
     Level: 38
     Grade: A
     EXP needed to level-up: 16607
     Remarks: Excellent, you scored 100% for coursemology!

     Enter experience points: 0
     Level: 0
     Grade: F
     EXP needed to level-up: 100
     Remarks: :\

     Enter experience points: -24
     Level: -24
     Grade: ?
     EXP needed to level-up: 0
     Remarks: Unknown grade "?"
*/
