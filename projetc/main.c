#include <stdio.h>
#include <stdlib.h>

int int_add(int a, int b) {
    return a + b;
}

float  float_add(float a, float b){
    return a + b;
}

void float_add_ref(float *a, float *b, float *c) {
    *c = *a + *b;
}

void add_int_vecteur(int *a, int *b, int *c, int taille) {
    for(int i = 0; i < taille; i++) {
        c[i] = a[i] + b[i];
    }
}
unsigned long * fib(unsigned n)
{
    unsigned long * fib_arr = (unsigned long *) malloc(n * sizeof(unsigned long));

    if (n >= 1)
        fib_arr[0] = 0;
    if (n >= 2)
        fib_arr[1] = 1;

    for (unsigned i = 2; i < n; ++i)
    {
        fib_arr[i] = fib_arr[i-2] + fib_arr[i-1];
    }

    return fib_arr;
}

void freeme(unsigned long * ptr) {
    free(ptr);e
}

int main() {
    printf("Hello, World!\n");
    return 0;
}
