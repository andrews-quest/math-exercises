#include <math.h>
#include <stdio.h>
#include <stdint.h>

#define PRINT_EDGE_VALUES 0

uint16_t d = 100;
uint16_t x = 10000;
uint32_t total_area = 0;

uint16_t q_x = 0;
uint8_t q_y = 0;

// edge_x = 0; // from 0 to x
float_t edge_y = 0; // from 0 to d

uint32_t n_points = 0;
float area = 0;

// circle: x**2 + y**2 = (d/2)**2

void input_values(){
    printf("x = ");
    scanf("%i", &q_x);
    printf("y = ");
    scanf("%i", &q_y);
}

void print_result(){
    // printf("%f\n", edge_y);
    printf("\nThe allowed range is %i\n", edge_y);

    if(q_y <= edge_y){
        printf("The point is in allowed range.");
    }else{
        printf("The point is beyond the allowed range.");
    }
}

void print_area(){
    printf("The total area is %d * %d = %d\n", x, d, total_area);
    printf("The total number of points is %d\n", n_points);
    printf("The allowed area for Q(X) is %f", area);
}

void main(){
    // input_values();
    total_area = x * d;

    for(int i = 0; i < x; i++){
        q_x = i;
        edge_y = (float) (pow(d, 3) / (pow(q_x, 2) + pow(d, 2));
        n_points += round(edge_y);
        #if PRINT_EDGE_VALUES==1
            if(edge_y > 0){
                printf("%d\n", edge_y);
            }
        #endif
    }
    // printf("%i", n_points);
    
    area = (float) n_points / total_area;
    print_area();
    // print_result();
}