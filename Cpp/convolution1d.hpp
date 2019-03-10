#pragma once

#ifndef CONVOLUTION1D_H
#define CONVOLUTION1D_H

#include <vector>
using namespace std;

void Convolution1D (double *f, int fLEN, double *g, int gLEN, double *y);
std::vector<double> Convolution1D_Vec(vector<double> f, vector<double> g, bool delayCorrect);

#endif
