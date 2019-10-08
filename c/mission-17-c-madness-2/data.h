/*****************************************
 * CS1010X --- Programming Methodology  *
 *                                       *
 *   Mission 17, Question 2 Template     *
 *****************************************/

#ifndef _PERSON
#define _PERSON

typedef struct {
    char first[30];
    char last[30];
} Name;

/***************
 *  Task 1(a)  *
 ***************

 Augment the Person structure below with a single-precision floating-point
 field named "bmi".
*/

typedef struct person {
    int index;
    Name name;
    unsigned short height;
    unsigned char  weight;
    // Add the field here
    float bmi;
    struct person *next;
} Person;


Person **read_data(const char *);

int count_data(Person **);

void free_data(Person **);

void print_person(Person *);

void print_data(Person **);

#endif
