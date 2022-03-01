#include <stdio.h>

int int_add(int a, int b) {
    return a + b;
}

float  float_add(float a, float b){
    return a + b;
}

void float_add_ref(float *a, float *b, float *c) {
    *c = *a + *b;
}

int main() {
    printf("Hello, World!\n");
    return 0;
}
