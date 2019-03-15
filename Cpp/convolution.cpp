#include <vector>
#include <cmath>
#include "convolution.hpp"
typedef std::vector<std::vector<double>> matrix;
using namespace std;

// Define Convolution1D
void Convolution1D (double *f, int fLEN, double *g, int gLEN, double *y)
{
    for (int n=0; n < fLEN; n++)
    {
        for (int m=0; m < gLEN; m++)
        {
            y[n+m] +=  f[n]*g[m];
        }
    }
}

// Define Convolution1D Vector
std::vector<double> Convolution1D_Vec(vector<double> f, vector<double> g, bool delayCorrect)
{
    //Initialize output vector
    std::vector<double> y(f.size()+g.size()-1, 0.0);
    
    
    for(auto fn = f.begin(); fn != f.end();fn++)
    {    
        for(auto gm = g.begin();gm != g.end();gm++)
        {
             y[distance(f.begin(),fn)+distance(g.begin(),gm)]+= (*fn)*(*gm);
        }
    }
    
    if (delayCorrect)
    {
        return vector<double>(y.begin()+ceil((g.size()-1.0)/2.0),y.end()-g.size()+1);
    }
    else
    {
        return y;
    }
       
}

// Define Convolution2D Vector
matrix Convolution2D(matrix &f, matrix &g)
{
    //Initialize output vector
    matrix result(f.size()+g.size()-1, std::vector<double>(f[0].size()+g[0].size()-1,0.0));
    
    
    for(auto fx = f.begin(); fx != f.end();fx++)
    {    
        for(auto fy = fx->begin(); fy != fx->end();fy++)
        {
            for(auto gi = g.begin(); gi != g.end(); gi++)
            {
                for (auto gj = gi->begin(); gj != gi->end(); gj++)
                {
                    result[distance(f.begin(),fx)+distance(g.begin(),gi)][distance(fx->begin(),fy)+distance(gi->begin(),gj)]+= (*fy)*(*gj);
                }
            }
        }
    
    }
    return result;
    
}
