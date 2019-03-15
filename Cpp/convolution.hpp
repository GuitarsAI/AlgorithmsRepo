#pragma once

#ifndef CONVOLUTION_H
#define CONVOLUTION_H

#include <vector>
typedef std::vector<std::vector<double>> matrix;

void Convolution1D (double *f, int fLEN, double *g, int gLEN, double *y);
std::vector<double> Convolution1D_Vec(std::vector<double> f, std::vector<double> g, bool delayCorrect);
matrix Convolution2D(matrix &f, matrix &g);

#endif
