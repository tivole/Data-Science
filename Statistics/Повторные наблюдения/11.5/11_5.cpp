// (c) Tivole

#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>

using namespace std;

#define N 100

double F_emp(double *X, double x);

int main() {

    int i;
    double X[N], R = 0;
    FILE *f = fopen("input.txt", "r");

    for (i = 0; i < N; i++) {
        fscanf(f, "%lf", &X[i]);
        X[i] = -log(1.0/X[i] - 1.0);
    }

    for (i = 0; i < N; i++) {
        R += pow((1 - F_emp(X, X[i]) - F_emp(X, -X[i])), 2);
    }

    printf("R = %lf\n", R);

    return 0;
}

double F_emp(double *X, double x) {
    int value = 0;
    for (int i = 0; i < N; i++)
        if (X[i] <= x) value ++;
    return (double) value / N;
}