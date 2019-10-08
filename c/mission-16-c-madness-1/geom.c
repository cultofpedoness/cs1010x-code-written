/*****************************************
 * CS1010X --- Programming Methodology  *
 *                                       *
 *   Mission 16, Question 2 Template     *
 *****************************************/

#include <stdio.h>
#include <math.h>

typedef struct {
    int x;
    int y;
} Point;

typedef struct {
    Point corner;        // coordinates of top-left corner
    unsigned int width;  // units to right edge from corner
    unsigned int height; // units to bottom edge from corner
} Rectangle;

void print_rect(Rectangle rect) {
    printf("x = %d, y = %d, w = %u, l = %u\n",
           rect.corner.x, rect.corner.y, rect.width, rect.height);
}

void print_circle_in(Rectangle rect, const char *name);

Rectangle bounds(Rectangle rect[], int total) {
    /************
     *  Task 1  *
     ************
     
     Compute and return the smallest rectangle enclosing all the rectangles
     in the array up to "total", i.e. from rect[0] to rect[total - 1].
     
     If the total is zero, return a rectangle with zero width and height
     positioned at the origin.
     
     Note that the positive x-axis extends to the right of the origin, while
     the positive y-axis extends downwards from the origin.
     
    */
    Rectangle result = {{0,0},0,0};
    if (total==0){
        return result;
    }
    Point origin = rect[0].corner;
    int width = rect[0].width;
    int height = rect[0].height;
    int diff;
    for (int i=0; i<total; i++){
        if (rect[i].corner.x<origin.x){
            diff = origin.x - rect[i].corner.x;
            origin.x = rect[i].corner.x;
            width += diff;
        }
        if (origin.y > rect[i].corner.y){
            diff = origin.y - rect[i].corner.y;
            origin.y = rect[i].corner.y;
            height += diff;
        }
        if ((rect[i].width+(rect[i].corner.x-origin.x))>width){
            width = rect[i].width+(rect[i].corner.x-origin.x);
        }
        if ((rect[i].height+(rect[i].corner.y-origin.y))>height){
            height = rect[i].height+(rect[i].corner.y-origin.y);
        }
    }
    result.corner = origin;
    result.width = width;
    result.height = height;
    return result;
}

/************
 *  Task 2  *
 ************
 
 Write the function make_circle to compute the largest circle that can fit in
 the given box. If the circle is only touching two sides of the box, it should
 be centered between the other two sides.
 
 This function should return a structure that contains multiple values pertaining
 to the computed circle. You will need to decide on how to define and populate
 the structure from the way the "print_circle_in" function uses it.
 
*/

// Define the required structure here.

typedef struct {
    double area;
    double perimeter;
} Stat;

typedef struct {
    double x;
    double y;
    double radius;
    Stat stats;
} Circle;


 
// Circle make_circle(Rectangle box);

Circle make_circle(Rectangle rect){
    Circle result;
    if (rect.width<=rect.height){
        result.radius = ((double)rect.width/2);
        result.stats.area = ((result.radius)*(result.radius)*M_PI);
        result.stats.perimeter = (result.radius)*M_PI*(2);
        result.x = ((double)rect.corner.x + ((double)rect.width/2));
        result.y = ((double)rect.corner.y + ((double)rect.height/2));
    }else{
        result.radius = ((double)rect.height/2);
        result.stats.area = ((result.radius)*(result.radius)*M_PI);
        result.stats.perimeter = (result.radius)*M_PI*(2);
        result.x = ((double)rect.corner.x + ((double)rect.width/2));
        result.y = ((double)rect.corner.y + ((double)rect.height/2));
    }
    return result;
}

int main(void) {
    Rectangle rect[] = {
        { {-1, 2}, 30, 60 },
        { {10, 1}, 20, 1 },
        { {0, -10}, 3, 2 },
        { {0, 0}, 55, 77 },
    };
    
    // Task 1 output
    print_rect(bounds(rect, 0));
    print_rect(bounds(rect, 1));
    print_rect(bounds(rect, 2));
    print_rect(bounds(rect, 3));
    print_rect(bounds(rect, 4));
    printf("\n");
    
    Rectangle a = { {3, 4}, 32, 32 };
    Rectangle b = { {-9, -10}, 65, 37 };
    Rectangle c = { {-12, -80}, 87, 99 };
    
    // Task 2 output
    print_circle_in(a, "a");
    print_circle_in(b, "b");
    print_circle_in(c, "c");
    
    return 0;
}

void print_circle_in(Rectangle box, const char *name) {
    // Uncomment the following lines to test your make_circle function
    // for Task 2. DO NOT MODIFY THEM.
    
   Circle circ = make_circle(box);
   printf("%s.center: %f %f\n", name, circ.x, circ.y);
   printf("%s.radius: %f\n", name, circ.radius);
   printf("%s.area: %f\n", name, circ.stats.area);
   printf("%s.perimeter: %f\n\n", name, circ.stats.perimeter);
}

/*
 EXPECTED OUTPUT:
 
    x = 0, y = 0, w = 0, l = 0
    x = -1, y = 2, w = 30, l = 60
    x = -1, y = 1, w = 31, l = 61
    x = -1, y = -10, w = 31, l = 72
    x = -1, y = -10, w = 56, l = 87

    a.center: 19.000000 20.000000
    a.radius: 16.000000
    a.area: 804.247742
    a.perimeter: 100.530968

    b.center: 23.500000 8.500000
    b.radius: 18.500000
    b.area: 1075.210083
    b.perimeter: 116.238930

    c.center: 31.500000 -30.500000
    c.radius: 43.500000
    c.area: 5944.678711
    c.perimeter: 273.318573
*/
