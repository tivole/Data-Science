// (c) Tivole

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

double Get_Median_From_Random_Row (double*, int*, int*, int, int);
int Partition (double*, int, int*, int*, int*, double);
void Initialize_Bounds (int*, int*, int);
void Reset_Left_Bounds (int*, int*, int);
int Compare_Double(const void*, const void*);
void Reset_Right_Bounds (int*, int*, int);
double Deal_With_Ties (double*, int*, int*, int, int, int*);
double Ti_Found_Median (double*, int);
void Free_Holders (int*, int*, int*);

int main(void) {

	int n, i;
	double *data, med, clockTimer;
	FILE *f;

	f = fopen("input.txt", "r");

	fscanf(f, "%d", &n);

	data = (double*) malloc (sizeof (double) * n);

	for(i = 0; i < n; i++) fscanf(f, "%lf", &data[i]);

	clockTimer = clock();
	qsort (data, n, sizeof (double), Compare_Double);
	med = Ti_Found_Median(data, n);
	clockTimer = clock() - clockTimer;
	clockTimer /= CLOCKS_PER_SEC;

	printf("\n\n\nMED = {%lf}\nTime = {%lf}\n\n", med, clockTimer);

	return 0;
}

double Ti_Found_Median (double* x, int n) {
	int i, iq, ipiq, nn, sm, sq, done, L, *lb, *rb, *q;
	double k1, k2, am, amn, amx, return_value;

	if (n == 1) return x[0];
	if (n == 2) return (x[0] + x[1]) / 2;

	nn = n * (n + 1) / 2;
	k1 = (nn + 1) / 2;
	k2 = (nn + 2) / 2;

	lb = (int*) malloc (sizeof (int) * n);
	rb = (int*) malloc (sizeof (int) * n);
	q = (int*) malloc (sizeof (int) * n);
	Initialize_Bounds (lb, rb, n);

	sm = nn;
	L = 0;
	am = x[n/2-1] + x[n/2];

	while (1) {
		sq = Partition (x, n, lb, rb, q, am);
		if (sq == L) {
			am = Deal_With_Ties (x, lb, rb, n, sm, &done);
			if (done == 1) {
				Free_Holders (lb, rb, q);
				return am / 2;
			} else continue;
		}

		if (sq == k2 - 1) break;
		if (sq - k1 < 0) Reset_Left_Bounds (lb, q, n);
		else if (sq - k1 > 0) Reset_Right_Bounds (rb, q, n);
		else break;

		L = 0;
		sm = 0;
		for (i = 0; i < n; i++) {
			L += lb[i] - i;
			sm += rb[i] - lb[i] + 1;
		}

		if (sm > 2) {
			am = Get_Median_From_Random_Row (x, lb, rb, n, sm);
		} else {
			am = Deal_With_Ties (x, lb, rb, n, sm, &done);
			if (done == 1) {
				Free_Holders (lb, rb, q);
				return am / 2;
			} else continue;
		}
	}

	amn = x[n-1] + x[n-1];
	amx = x[0] + x[0];

	for (i = 0; i < n; i++) {
		iq = q[i];
		ipiq = i + iq;
		if (iq > 0) amx = (amx > x[i] + x[ipiq-1]) ? amx : x[i] + x[ipiq-1];
		ipiq = i + iq;
		if (iq < n - i) amn = (amn < x[i] + x[ipiq]) ? amn : x[i] + x[ipiq];
	}

	Free_Holders (lb, rb, q);
	return_value = (amn + amx) / 4;

	if (k1 < k2) return return_value;
	if (sq == k1) return_value = amx / 2;
	if (sq == k1 - 1) return_value = amn / 2;

	return return_value;
}

double Deal_With_Ties (double* x, int* lb, int* rb, int n, int sm, int* flag) {
	int i, lbi, rbi, amx, amn, am;
	amx = x[0] + x[0];
	amn = x[n-1] + x[n-1];
	for (i = 0; i < n; i++) {
		if (lb[i] > rb[i]) continue;
		lbi = lb[i];
		if (x[lbi] + x[i] < amn) amn =  x[lbi] + x[i];
		rbi = rb[i];
		if (x[rbi] + x[i] > amx) amx = x[rbi] + x[i];
	}
	am = (amx + amn) / 2;
	if (am <= amn || am > amx) am = amx;
	if (amn != amx && sm != 2) *flag = 0;
	else *flag = 1;
	return am;
}

int Compare_Double(const void *a, const void *b) {
	const double* af = (const double*) a;
	const double* bf = (const double*) b;
	return (*af > *bf) - (*af < *bf);
}

void Reset_Right_Bounds (int* rb, int* q, int n) {
	int i;
	for (i = 0; i < n; i++) rb[i] = i + q[i] - 1;
	return;
}

void Reset_Left_Bounds (int* lb, int* q, int n) {
	int i;
	for (i = 0; i < n; i++) lb[i] = i + q[i];
	return;
}

int Partition (double* x, int n, int* lb, int* rb, int* q, double am) {
	int i, j, sq;
	sq = 0;
	j = n - 1;
	for (i = 0; i < n; i++) {
		q[i] = 0;
		for (; j >=  i; j--) {
		  if (x[i] + x[j] < am) {
			q[i] = j - i + 1;
			sq += q[i];
			break;
		  }
		}
	}
	return sq;
}

double Get_Median_From_Random_Row (double* x, int* lb, int* rb, int n, int sm) {
	int i, j, k, middlerow;
	k = (int)((sm) * (double) rand() / (RAND_MAX + 1.0));
	for (i = 0; i < n; i++) {
		j = i;
		if (k <= rb[i] - lb[i]) break;
		k = k - rb[i] + lb[i] - 1;
	}
	middlerow = (lb[j] + rb[j]) / 2;
	return x[j] + x[middlerow];
}

void Initialize_Bounds (int* lb, int* rb, int n) {
	int i;
	for (i = 0; i < n; i++) {
		lb[i] = i;
		rb[i] = n - 1;
	}
	return;
}

void Free_Holders (int* lb, int* rb, int* q) {
	free (rb);
	free (lb);
	free (q);
	return;
}
