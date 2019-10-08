/*****************************************
 * CS1010X --- Programming Methodology  *
 *                                       *
 *   Mission 17, Question 2 Template     *
 *****************************************/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include "data.h"

#define BY_FIRST_NAME 0
#define BY_LAST_NAME 1
#define BY_WEIGHT 2
#define BY_HEIGHT 3
#define BY_BMI 4

#define DESCENDING 0
#define ASCENDING 1

void compute_bmi(Person **data) {
    /***************
     *  Task 1(c)  *
     ***************

     NOTE: Task 1(a) and 1(b) are in data.h and data.c, respectively.

     Compute and assign the BMI to the newly added field. Note that
     BMI is defined as weight(kg) / (height(m) ** 2).
    */

    int i, size = count_data(data);
    for (i = 0; i < size; ++i) {
        Person *p = data[i];
        // Add your code here
        float sq = ((float)p->height/100)*((float)p->height/100);
        p->bmi = (float)p->weight/sq;
    }
}

void sort_data(Person **data, int key, int asc) {
    /************
     *  Task 2  *
     ************

     Parameters:
        data - Array of pointers to Person structures
        key  - Either BY_FIRST_NAME, BY_LAST_NAME, BY_WEIGHT, BY_HEIGHT or
                 BY_BMI. Determines which field to sort on -- self-explanatory.
        asc  - Sort should be either ASCENDING or DESCENDING

     Implement any one of the sorting algorithms that you were taught to sort
     the data array. The field to sort on can be changed through the "key"
     argument and the order can be changed with the "asc" argument. If two key
     values are equal (e.g. two people have the same first name, same BMI, etc),
     the sort should then use the order AS ORIGINALLY SHOWN IN THE DATA FILE as
     the tiebreaker. Use the index field on the Person struct to do this.

     You are NOT allowed to use the built-in qsort function.

     Note that only the array of pointers should be modified; NOT the Person
     structures that they point to.

     HINTS: Take reference from the compute_bmi method. Strings can be compared
            with the strcmp() function.
    */
   int i, x, size = count_data(data);
   if (key==BY_BMI){
       for (i=0; i<size; i++){
           for (x=0; x<size-1; x++){
               Person *p1 = data[x];
               Person *p2 = data[x+1];
               //float nearest1 = roundf(p1->bmi * 10) / 10;
               //printf("%lf", nearest1);
               //float nearest2 = roundf(p2->bmi * 10) / 10;
               if (asc==ASCENDING){
                   if (p1->bmi> p2->bmi){
                       Person *hold = data[x];
                       data[x] = data[x+1];
                       data[x+1] = hold;
                   } else if (p1->bmi == p2->bmi){
                        if (p1->index > p2->index){
                           Person *hold = data[x];
                            data[x] = data[x+1];
                            data[x+1] = hold;
                       }
                   }
               }else{
                   if (p1->bmi < p2->bmi){
                       Person *hold = data[x];
                       data[x] = data[x+1];
                       data[x+1] = hold;
                   }else if (p1->bmi == p2->bmi){
                        if (p1->index < p2->index){
                            Person *hold = data[x];
                            data[x] = data[x+1];
                            data[x+1] = hold;
                       }
                   }
               }
            //    if (asc==ASCENDING){
            //        if (nearest1> nearest2){
            //            Person *hold = data[x];
            //            data[x] = data[x+1];
            //            data[x+1] = hold;
            //        } else if (nearest1 == nearest2){
            //             if (p1->index > p2->index){
            //                Person *hold = data[x];
            //                 data[x] = data[x+1];
            //                 data[x+1] = hold;
            //            }
            //        }
            //    }else{
            //        if (nearest1 < nearest2){
            //            Person *hold = data[x];
            //            data[x] = data[x+1];
            //            data[x+1] = hold;
            //        }else if (nearest1 == nearest2){
            //             if (p1->index > p2->index){
            //                 Person *hold = data[x];
            //                 data[x] = data[x+1];
            //                 data[x+1] = hold;
            //            }
            //        }
            //    }
           }
       }
    //    for (i=0; i<size; i++){
    //        for (x=0; x<size-1; x++){
    //             Person *p1 = data[x];
    //             Person *p2 = data[x+1];
    //             if (p1->bmi == p2->bmi){
    //                 if (p1->index > p2->index){
    //                     Person *hold = data[x];
    //                     data[x] = data[x+1];
    //                     data[x+1] = hold;
    //                 }
    //             }
    //         }
    //     }
   } else if (key==BY_WEIGHT){
       for (i=0; i<size; i++){
           for (x=0; x<size-1; x++){
               Person *p1 = data[x];
               Person *p2 = data[x+1];
               if (asc==ASCENDING){
                   if (p1->weight > p2->weight){
                       Person *hold = data[x];
                       data[x] = data[x+1];
                       data[x+1] = hold;
                   }else if (p1->weight == p2->weight){
                        if (p1->index > p2->index){
                            Person *hold = data[x];
                            data[x] = data[x+1];
                            data[x+1] = hold;
                       }
                   }
               }else{
                   if (p1->weight < p2->weight){
                       Person *hold = data[x];
                       data[x] = data[x+1];
                       data[x+1] = hold;
                   }else if (p1->weight == p2->weight){
                        if (p1->index < p2->index){
                            Person *hold = data[x];
                            data[x] = data[x+1];
                            data[x+1] = hold;
                       }
                   }
               }
           }
       }
   } else if (key==BY_HEIGHT){
       for (i=0; i<size; i++){
           for (x=0; x<size-1; x++){
               Person *p1 = data[x];
               Person *p2 = data[x+1];
               if (asc==ASCENDING){
                   if (p1->height > p2->height){
                       Person *hold = data[x];
                       data[x] = data[x+1];
                       data[x+1] = hold;
                   }else if (p1->height == p2->height){
                        if (p1->index > p2->index){
                            Person *hold = data[x];
                            data[x] = data[x+1];
                            data[x+1] = hold;
                       }
                   }
               }else{
                   if (p1->height < p2->height){
                       Person *hold = data[x];
                       data[x] = data[x+1];
                       data[x+1] = hold;
                   }else if (p1->height == p2->height){
                        if (p1->index < p2->index){
                            Person *hold = data[x];
                            data[x] = data[x+1];
                            data[x+1] = hold;
                       }
                   }
               }
           }
       }
   } else if (key==BY_FIRST_NAME){
       for (i=0; i<size; i++){
           for (x=0; x<size-1; x++){
               Person *p1 = data[x];
               Person *p2 = data[x+1];
               if (asc==ASCENDING){
                   if (strcmp(p1->name.first, p2->name.first)>0){
                       Person *hold = data[x];
                       data[x] = data[x+1];
                       data[x+1] = hold;
                   }else if (strcmp(p1->name.first, p2->name.first)==0){
                        if (p1->index > p2->index){
                            Person *hold = data[x];
                            data[x] = data[x+1];
                            data[x+1] = hold;
                       }
                   }
               }else{
                   if (strcmp(p1->name.first, p2->name.first)<0){
                       Person *hold = data[x];
                       data[x] = data[x+1];
                       data[x+1] = hold;
                   }else if (strcmp(p1->name.first, p2->name.first)==0){
                        if (p1->index < p2->index){
                            Person *hold = data[x];
                            data[x] = data[x+1];
                            data[x+1] = hold;
                       }
                   }
               }
           }
       }
   } else if (key==BY_LAST_NAME){
       for (i=0; i<size; i++){
           for (x=0; x<size-1; x++){
               Person *p1 = data[x];
               Person *p2 = data[x+1];
               if (asc==ASCENDING){
                   if (strcmp(p1->name.last, p2->name.last)>0){
                       Person *hold = data[x];
                       data[x] = data[x+1];
                       data[x+1] = hold;
                   }else if (strcmp(p1->name.last, p2->name.last)==0){
                        if (p1->index > p2->index){
                            Person *hold = data[x];
                            data[x] = data[x+1];
                            data[x+1] = hold;
                       }
                   }
               }else{
                   if (strcmp(p1->name.last, p2->name.last)<0){
                       Person *hold = data[x];
                       data[x] = data[x+1];
                       data[x+1] = hold;
                   }else if (strcmp(p1->name.last, p2->name.last)==0){
                        if (p1->index < p2->index){
                            Person *hold = data[x];
                            data[x] = data[x+1];
                            data[x+1] = hold;
                       }
                   }
               }
           }
       }
   }
}

int main(void) {
    Person **data = read_data("people.txt");
    if (data) {
        compute_bmi(data);
        // printf("----By BMI----\n");
        // sort_data(data, BY_BMI, ASCENDING);
        // print_data(data);
        // sort_data(data, BY_BMI, DESCENDING);
        // print_data(data);
        // printf("----By HEIGHT----\n");
        // sort_data(data, BY_HEIGHT, ASCENDING);
        // print_data(data);
        // sort_data(data, BY_HEIGHT, DESCENDING);
        // print_data(data);
        // printf("----By WEIGHT----\n");
        // sort_data(data, BY_WEIGHT, ASCENDING);
        // print_data(data);
        // sort_data(data, BY_WEIGHT, DESCENDING);
        // print_data(data);
        printf("----By FIRST NAME----\n");
        sort_data(data, BY_FIRST_NAME, ASCENDING);
        print_data(data);
        sort_data(data, BY_FIRST_NAME, DESCENDING);
        print_data(data);
        printf("----By LAST NAME----\n");
        sort_data(data, BY_LAST_NAME, ASCENDING);
        print_data(data);
        sort_data(data, BY_LAST_NAME, DESCENDING);
        print_data(data);

        free_data(data);
        return 0;
    } else {
        printf("Error reading file!\n");
        return 1;
    }
}

/*
 EXPECTED OUTPUT:

    Marilee Bartling, height: 194 cm, weight: 56 kg, bmi: 14.9
    Carlie Feltmann, height: 208 cm, weight: 66 kg, bmi: 15.3
    Elba Rousselle, height: 190 cm, weight: 58 kg, bmi: 16.1
    Earleen Swindell, height: 204 cm, weight: 68 kg, bmi: 16.3
    Christene Dahm, height: 196 cm, weight: 66 kg, bmi: 17.2
    Caprice Creekmore, height: 165 cm, weight: 50 kg, bmi: 18.4
    Jose Harshberger, height: 187 cm, weight: 66 kg, bmi: 18.9
    ...

    Yi Saine, height: 163 cm, weight: 79 kg, bmi: 29.7
    Wiley Hawke, height: 187 cm, weight: 90 kg, bmi: 25.7
    Vivian Allsop, height: 173 cm, weight: 89 kg, bmi: 29.7
    Troy Kulpa, height: 150 cm, weight: 71 kg, bmi: 31.6
    Trang Spore, height: 193 cm, weight: 81 kg, bmi: 21.7
    Teressa Gugino, height: 132 cm, weight: 59 kg, bmi: 33.9
    Teressa Buzzard, height: 170 cm, weight: 65 kg, bmi: 22.5
    ...
*/
