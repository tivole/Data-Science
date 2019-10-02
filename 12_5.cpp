// (c) Tivole

#include <iostream>
#include <cstdio>
#include <cmath>

#define N 100
#define K 7

// Distribution Function
double F(double x) {
    return x;
}

int main() {

    int i, j, nyu[K];
    double step, X[N], _p_[K], E[K], statistics = 0;
    FILE *f = fopen("input.txt", "r");

    step = 1.0 / K;

    for (i = 0; i < K; i++) nyu[i] = 0;

    // Reading Xs and calculating nyu[i]
    for (i = 0; i < N; i ++) {
        fscanf(f, "%lf", &X[i]);
        for (j = 0; j < K; j++) {
            if (j == 0) {
                if (X[i] >= 0 && X[i] <= (step * (j+1))) nyu[j]++;
            } else {
                if (X[i] > (step * j) && X[i] <= (step * (j+1))) nyu[j]++;
            }
        }
    }

    // Calculating _p_ (p with a cap)
    for (i = 0; i < K; i++) {
        _p_[i] = F(step * (i+1)) - F(step * i);
        E[i] = (N * _p_[i]);
    }

    // Calculating Statistics
    for (i = 0; i < K; i++) {
        statistics += (pow(((double)nyu[i] - E[i]), 2) / (E[i]));
    }

    printf("%lf\n", statistics);

    return 0;
}