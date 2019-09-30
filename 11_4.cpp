// (c) Tivole

#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>

using namespace std;

#define N 100

int Compare_Double(const void *a, const void *b);

int main() {

    int i;
    double X[N], mean_X = 0, MED_X;
    FILE *f = fopen("input.txt", "r");

    for (i = 0; i < N; i++) {
        fscanf(f, "%lf", &X[i]);
        X[i] = -log(1.0/X[i] - 1.0);
        mean_X += X[i];
        printf("X[%d] = %lf\n", i, X[i]);
    }

    mean_X /= N;

    qsort (X, N, sizeof(double), Compare_Double);

    MED_X = (X[N/2] + X[N/2 + 1]) / 2.0;
    
    printf("mean_X = %lf\nMED_X = %lf\n", mean_X, MED_X);

    return 0;
}

int Compare_Double(const void *a, const void *b) {
	const double* af = (const double*) a;
	const double* bf = (const double*) b;
	return (*af > *bf) - (*af < *bf);
}