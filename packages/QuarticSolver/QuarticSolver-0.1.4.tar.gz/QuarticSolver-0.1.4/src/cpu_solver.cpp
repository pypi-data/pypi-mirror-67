#include <algorithm>
#include <complex>
#include <stdio.h>

void cubicSolver_cpu(int n, float *A, float *B, float *C, float *D, float *Q, float *R, float *del, float *theta, float *sqrtQ,
	float *x1, float *x2, float *x3, float *x1_img, float *x2_img, float *x3_img)
{
	// solver for finding roots (x1, x2, x3) for ax^3 + bx^2 + cx + d = 0

	const float twopi = 2 * 3.1415927;
	const float fourpi = 4 * 3.1415927;

	for (int i = 0; i < n; ++i) {

		// Q = ((3c/a) - (b^2/a^2)) /9;
		// R = ((9bc)/a^2 - (2b^3)/a^3 - 27d/a) /54;
		// del = Q^3 + R^2;

		Q[i] = ((3 * C[i]) / A[i] - ((B[i] * B[i]) / (A[i] * A[i]))) / 9;
		R[i] = (((-(2 * (B[i] * B[i] * B[i])) / (A[i] * A[i] * A[i]))) + ((9 * (B[i] * C[i])) / (A[i] * A[i])) - ((27 * D[i]) / A[i])) / 54;
		del[i] = ((R[i] * R[i])) + ((Q[i] * Q[i] * Q[i]));

	}

	for (int i = 0; i<n; ++i) {

		// all 3 roots real
		if (del[i] <= 0) { 

			/*sqrtQ = 2 * sqrt(-Q);
			theta = acos(R / (sqrtQ ^ 3));

			x1 = (sqrtQ*cos(theta / 3) - b/3a;
			x2 = (sqrtQ*cos((theta + 2 * pi) / 3) - b/3a);
			x3 = (sqrtQ*cos((theta + 4 * pi) / 3) - b/3a);*/

			theta[i] = acosf((float)(R[i] / sqrtf((float)-(Q[i]* Q[i]* Q[i]))));
			sqrtQ[i] = 2 * sqrtf((float)-Q[i]);

			x1[i] = (sqrtQ[i] * cosf((float)(theta[i] / 3)) - (B[i] / (A[i]*3)));
			x2[i] = (sqrtQ[i] * cosf((float)(theta[i] + twopi) / 3)) - (B[i] / (A[i] * 3));
			x3[i] = (sqrtQ[i] * cosf((float)(theta[i] + fourpi) / 3)) - (B[i] / (A[i] * 3));
		}

		if (del[i] > 0) { // only 1 real root

			/*S = (R + sqrtD)^(1 / 3);
			T = (R - sqrtD)^(1 / 3);
			x = S + T - b/3a;*/

			// real root

			x1[i] = ((cbrtf((float)(R[i] + sqrtf((float)del[i]))))
				+ cbrtf((float)(R[i] - sqrtf((float)del[i])))) - (B[i] / (3 * A[i]));

			x1_img[i] = 0;

			// complex conjugate roots

			x2[i] = -((cbrtf((float)(R[i] + sqrtf((float)del[i])))
				+ cbrtf((float)(R[i] - sqrtf((float)del[i]))))/2) - (B[i] / (3*A[i]));

			x2_img[i] = ((sqrtf((float)3)/2)*(cbrtf((float)(R[i] + sqrtf((float)del[i])))
			- cbrtf((float)(R[i] - sqrtf((float)del[i])))));

			x3[i] = x2[i];

			x3_img[i] = -x2_img[i];

		}

		if (Q[i] == 0 && R[i] == 0) { // all roots real and equal

			x1[i] = -(B[i] / 3);
			x2[i] = x1[i];
			x3[i] = x1[i];

		}

	}
}

void quarticSolver_cpu(int n, float *A, float *B, float *C, float *D, float *b, float *c, float *d,
	float *Q, float *R, float *Qint, float *Rint, float *del, float *theta, float *sqrtQ, float *x1, float *x2, float *x3, float *temp, float *min)
{
	//solver for finding minimum (xmin) for f(x) = Ax^4 + Bx^3 + Cx^2 + Dx + E
	//undefined behaviour if A=0

	/*const float twopi = 2 * 3.1415927;
	const float fourpi = 4 * 3.1415927;*/

	for (int i = 0; i < n; ++i) {

		b[i] = 0.75*(B[i]/A[i]);
		c[i] = 0.50*(C[i]/A[i]);
		d[i] = 0.25*(D[i]/A[i]);

		Q[i] = (c[i]/3) - ((b[i]*b[i])/9);
		R[i] = (b[i]*c[i])/6 - (b[i] * b[i]* b[i])/27 - 0.5*d[i];

		// round Q and R to get around problems caused by floating point precision
		Q[i] = roundf(Q[i] * 1E5) / 1E5;
		R[i] = roundf(R[i] * 1E5) / 1E5;

		Qint[i] = (Q[i] * Q[i] * Q[i]);
		Rint[i] = (R[i] * R[i]);

		del[i] = Rint[i] + Qint[i];
		//del[i] = (R[i] * R[i]) + (Q[i] * Q[i] * Q[i]); // why not just Q*Q*Q + R*R? Heisenbug. Heisenbug in release code

	}

	for (int i = 0; i<n; ++i) {
		// comparing against 1E-5 to deal with potential problems with comparing floats to zero
		if (del[i] <= 1E-5) { // all 3 roots real

			/*sqrtQ = 2 * sqrt(-Q);
			theta = acos(R / (sqrtQ ^ 3));

			x1 = 2 * (sqrtQ*cos(theta / 3) - b/3;
			x2 = 2 * (sqrtQ*cos((theta + 2 * pi) / 3) - b/3);
			x3 = 2 * (sqrtQ*cos((theta + 4 * pi) / 3) - b/3);*/

			theta[i] = acosf((float)(R[i] / sqrtf((float)-(Q[i] * Q[i] * Q[i]))));
			sqrtQ[i] = 2 * sqrtf((float)-Q[i]);

			x1[i] = ((sqrtQ[i]*cosf((float)(theta[i]) / 3)) - (b[i] / 3));
			x2[i] = ((sqrtQ[i]*cosf((float)(theta[i] + 2 * 3.1415927) / 3)) - (b[i] / 3));
			x3[i] = ((sqrtQ[i]*cosf((float)(theta[i] + 4 * 3.1415927) / 3)) - (b[i] / 3));

			// unrolled bubble sort  // this vs CUDA sort??
			if (x1[i] < x2[i]) {
				temp[i] = x1[i];
				x1[i] = x2[i];
				x2[i] = temp[i];
			}// { swap(x1[i], x2[i]); }//swap
			if (x2[i] < x3[i]) {
				temp[i] = x2[i];
				x2[i] = x3[i];
				x3[i] = temp[i];
			}//{ swap(x2[i], x3[i]); }//swap
			if (x1[i] < x2[i]) {
				temp[i] = x1[i];
				x1[i] = x2[i];
				x2[i] = temp[i];
			}//{ swap(x1[i], x2[i]); }//swap

			min[i] = A[i] * ((x1[i] * x1[i] * x1[i] * x1[i]) - (x3[i] * x3[i] * x3[i] * x3[i])) / 4 
				+ B[i] * ((x1[i] * x1[i] * x1[i]) - (x3[i] * x3[i] * x3[i])) / 3
				+ C[i] * ((x1[i] * x1[i]) - (x3[i] * x3[i])) / 2 
				+ D[i] * (x1[i] - x3[i])
				<= 0 ? x1[i] : x3[i];
		}

		//if (del[i] > 0) { // only 1 real root
		else {

			/*S = (R + sqrtD)^(1 / 3);
			T = (R - sqrtD)^(1 / 3);
			x = S + T - b/3;*/

			x1[i] = cbrtf((float)(R[i] + sqrtf((float)del[i])))
				+ cbrtf((float)(R[i] - sqrtf((float)del[i]))) - (b[i] / 3); // real root

			// complex conjugate roots not relevant for minimisation

			x2[i] = 0;
			x3[i] = 0;

			min[i] = x1[i];

		}

		// no need as same result as del[i]>0
		/*if (Q[i] == 0 && R[i] == 0) { // all roots real and equal

		x1[i] = -b[i] / 3;
		x2[i] = x1[i];
		x3[i] = x1[i];

		min[i] = x1[i];

		}*/

	}
}

float* QuarticMinimumCPU2(int N, float *A, float *B, float *C, float *D, float *E, bool debug){

	float *bi, *ci, *di, *h_theta, *h_sqrtQ, *min, *Q, *R, *Qint, *Rint, *del, *h_temp;
	float *x1_cpu, *x2_cpu, *x3_cpu, *min_cpu;

	Q = (float*)malloc(N * sizeof(float));
	R = (float*)malloc(N * sizeof(float));
	Qint = (float*)malloc(N * sizeof(float));
	Rint = (float*)malloc(N * sizeof(float));
	del = (float*)malloc(N * sizeof(float));

	bi = (float*)malloc(N * sizeof(float));
	ci = (float*)malloc(N * sizeof(float));
	di = (float*)malloc(N * sizeof(float));
	h_temp = (float*)malloc(N * sizeof(float));

	h_theta = (float*)malloc(N * sizeof(float));
	h_sqrtQ = (float*)malloc(N * sizeof(float));

	x1_cpu = (float*)malloc(N * sizeof(float));
	x2_cpu = (float*)malloc(N * sizeof(float));
	x3_cpu = (float*)malloc(N * sizeof(float));

	min_cpu = (float*)malloc(N * sizeof(float));

	/*memset(x1_cpu, 0, N * sizeof(float));
	memset(x2_cpu, 0, N * sizeof(float));
	memset(x3_cpu, 0, N * sizeof(float));

	memset(min_cpu, 0, N * sizeof(float));*/

	quarticSolver_cpu(N, A, B, C, D, bi, ci, di, Q, R, Qint, Rint, del, h_theta, h_sqrtQ, x1_cpu, x2_cpu, x3_cpu, h_temp, min_cpu);

	if (debug) {

        printf("x1[0]: %f, x2[0]: %f , x3[0]: %f , min[0]: %f \n", x1_cpu[0], x2_cpu[0], x3_cpu[0], min_cpu[0]);

		printf("Q[0]: %f, R[0]: %f , del[0]: %f \n", Q[0], R[0], del[0]);

		printf("f(x_1):  %f \n", A[0] * (powf(x1_cpu[0], 4)) / 4 + B[0] * (powf(x1_cpu[0], 3)) / 3 + C[0] * (powf(x1_cpu[0], 2)) / 2 + D[0] * (x1_cpu[0]) + E[0]);
		printf("f(x_3):  %f \n", A[0] * (powf(x3_cpu[0], 4)) / 4 + B[0] * (powf(x3_cpu[0], 3)) / 3 + C[0] * (powf(x3_cpu[0], 2)) / 2 + D[0] * (x3_cpu[0]) + E[0]);

	}

	delete x1_cpu;
	delete x2_cpu;
	delete x3_cpu;

	delete Q;
	delete R;
	delete Qint;
	delete Rint;
	delete del;
	delete bi;
	delete ci;
	delete di;
	delete h_temp;
	delete h_theta;
	delete h_sqrtQ;

	return min_cpu;
}

void QuarticMinimumCPU(int N, float *A, float *B, float *C, float *D, float *E, float *min_cpu){

	float *bi, *ci, *di, *h_theta, *h_sqrtQ, *min, *Q, *R, *Qint, *Rint, *del, *h_temp;
	float *x1_cpu, *x2_cpu, *x3_cpu;//, *min_cpu;

	Q = (float*)malloc(N * sizeof(float));
	R = (float*)malloc(N * sizeof(float));
	Qint = (float*)malloc(N * sizeof(float));
	Rint = (float*)malloc(N * sizeof(float));
	del = (float*)malloc(N * sizeof(float));

	bi = (float*)malloc(N * sizeof(float));
	ci = (float*)malloc(N * sizeof(float));
	di = (float*)malloc(N * sizeof(float));
	h_temp = (float*)malloc(N * sizeof(float));

	h_theta = (float*)malloc(N * sizeof(float));
	h_sqrtQ = (float*)malloc(N * sizeof(float));

	x1_cpu = (float*)malloc(N * sizeof(float));
	x2_cpu = (float*)malloc(N * sizeof(float));
	x3_cpu = (float*)malloc(N * sizeof(float));

	//min_cpu = (float*)malloc(N * sizeof(float));

	/*memset(x1_cpu, 0, N * sizeof(float));
	memset(x2_cpu, 0, N * sizeof(float));
	memset(x3_cpu, 0, N * sizeof(float));

	memset(min_cpu, 0, N * sizeof(float));*/

	quarticSolver_cpu(N, A, B, C, D, bi, ci, di, Q, R, Qint, Rint, del, h_theta, h_sqrtQ, x1_cpu, x2_cpu, x3_cpu, h_temp, min_cpu);

	delete x1_cpu;
	delete x2_cpu;
	delete x3_cpu;

	delete Q;
	delete R;
	delete Qint;
	delete Rint;
	delete del;
	delete bi;
	delete ci;
	delete di;
	delete h_temp;
	delete h_theta;
	delete h_sqrtQ;
}