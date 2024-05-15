#include <math.h>
#include <stdio.h>
#include <stdint.h>

#define PRINT_EDGE_VALUES 0

uint16_t d = 100;
uint16_t x = 5000;
uint16_t x_2 = 400;
uint32_t total_area = 0;
uint32_t total_area_2 = 0;

uint16_t q_x = 0;
uint8_t q_y = 0;

// edge_x = 0; // from 0 to x
float edge_y = 0; // from 0 to d

uint32_t n_points = 0;
uint32_t n_points_2 = 0;
float area = 0;
float area_2 = 0;

// circle: x**2 + y**2 = (d/2)**2

void print_area(){
    printf("\nThe total area is %d * %d = %d\n", x_2, d, total_area_2);
    printf("The total number of points is %d\n", n_points_2);
    printf("The allowed fraction area for Q(X) is %f\n\n of 1", area_2);

    printf("The total area is %d * %d = %d\n", x, d, total_area);
    printf("The total number of points is %d\n", n_points);
    printf("The allowed fraction of area for Q(X) is %f\n of 1", area);
}

void main(){
    // input_values();
    total_area = x * d * 2;
    total_area_2 = x_2 * d * 2;

    for(int i = 0; i < x; i++){
        q_x = i;
        edge_y = (float) (pow(d, 3) / (pow(q_x, 2) + pow(d, 2)));
        n_points += round(edge_y * 2);
        if(i == x_2){
            n_points_2 = n_points;
        }
        #if PRINT_EDGE_VALUES==1
            if(edge_y > 0){
                printf("%d\n", edge_y);
            }
        #endif
    }
    // printf("%i", n_points);
    
    area = (float) n_points / total_area;
    area_2 = (float) n_points_2 / total_area_2;
    print_area();
    // print_result();
}