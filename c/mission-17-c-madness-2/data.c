/*****************************************
 * CS1010X --- Programming Methodology  *
 *                                       *
 *   Mission 17, Question 2 Template     *
 *****************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "data.h"

void print_person(Person *p) {
    /***************
     *  Task 1(b)  *
     ***************

     Modify the printf statement below to also print the "bmi" field,
     formatted to exactly one decimal place.

     SAMPLE OUTPUT:
        Kristeen Strite, height: 177 cm, weight: 60 kg, bmi: 19.2
    */

    printf("%d  %s %s, height: %hu cm, weight: %hhu kg, bmi: %.1f\n",
           p->index, p->name.first, p->name.last, p->height, p->weight, p->bmi);
}

void print_data(Person **ptr) {
    while (*ptr) {
        print_person(*ptr++);
    }
    printf("\n");
}

int count_data(Person **data) {
    int count = 0;
    while (*data++) count++;
    return count;
}

void free_data(Person **data) {
    Person **ptr = data;
    while (*ptr) free(*ptr++);
    free(data);
}

Person **read_data(const char *filename) {
    // Scary code to read the data file.
    // Nothing to see here (unless you want to learn malloc/free :)

    FILE *in = fopen(filename, "r");
    Person *first = 0;
    Person *last = 0;
    unsigned int count = 0;

    if (in) {
        Person person;
        memset(&person, 0, sizeof(Person));

        while (fscanf(in, "%s %s %hu %hhu",
                      person.name.first, person.name.last,
                      &person.height, &person.weight) == 4) {

            Person *copy = (Person *)malloc(sizeof(Person));
            if (!copy) goto FAIL;
            memcpy(copy, &person, sizeof(Person));
            copy->index = count;

            if (last) {
                last->next = copy;
                last = copy;
            } else {
                first = last = copy;
            }
            ++count;
        }
        fclose(in);
    }

    if (count) {
        Person **data = malloc((count + 1) * sizeof(Person *));
        if (data) {
            Person **d_ptr = data;
            Person *p_ptr = first;
            while (p_ptr) {
                *d_ptr++ = p_ptr;
                p_ptr = p_ptr->next;
            }
            last->next = first;
            *d_ptr = 0;
            return data;
        }
    }

FAIL:
    fclose(in);
    while (first) {
        void *addr = first;
        first = first->next;
        free(addr);
    }
    return 0;
}
