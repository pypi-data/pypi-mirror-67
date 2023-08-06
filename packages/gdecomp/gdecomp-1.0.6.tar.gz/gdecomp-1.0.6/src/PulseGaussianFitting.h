/*
# ===============================================================================
#
# This file is part of the gdecomp package.
#
# gdecomp is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
#
#
# ===============================================================================
*/
/*
 * PulseGaussianFitting.h
 *
 *  Created on: 2017/12/5
 *      Author: Jianbo Qi
 *      Contribution: Tiangang Yin
 *
 *  Changed on: 2019/05/24
 *      Contribution: Florian de Boissieu <fdeboiss@gmail.com>, add function GaussianFitting for python binding
 */

#ifndef PULSE_GAUSSIAN_FITTING_H_
#define PULSE_GAUSSIAN_FITTING_H_
#include <vector>
#include <algorithm>
using namespace std;

struct XYData {
	double *x;
	double *y;
	double *y_error;
};

/*
* Basic sort function used to sort a vector and return the indices
*/
template <typename T>
vector<int> sort_indexes(const vector<T> &v) {

    // initialize original index locations
    vector<int> idx(v.size());
    for (size_t i = 0; i < idx.size(); i++) {
        idx[i] = i;
    }
    // sort indexes based on comparing values in v
    sort(idx.begin(), idx.end(),
        [&v](int i1, int i2) {return v[i1] > v[i2]; });

    return idx;
}

/*
* y:        1D amplitude data to search for peaks.
* thres:    between [0., 1.]
            Normalized threshold. Only the peaks with amplitude higher than the
            threshold will be detected.
* min_dist: Minimum distance between each detected peak. The peak with the highest
            amplitude is preferred to satisfy this constraint.
*/
vector<int> peaksDetectFisrtOrderZeroCrosssing(const vector<double> & y, double const& thres = 0.1, int const& min_dist = 5);

vector<double> remove_dulplicate(vector<double> y);

//flexion points detection: used for estimating the parameters for each components
vector< vector<int> > flexion_detect(vector<double> const& y, vector<int> const& peaks);

// par[0]: amp; par[1]: cen; par[2]: wid
double GaussianFunc(double x, double amp, double cen, double wid);


/* A composite version of Gaussian function with N components
*  par: [amp1, cen1, wid1, amp2, cen2, wid2,...]
*/
double CompositeGaussianFuncN(double x, const double *par);


/**
 * Gaussian function for mpfit
 */
int GaussianSum(int m, int n, double *p, double *deviates,
		double **derivs, void *private_data);

// guess initial parameters for a peak: amp, cen, wid
vector<double> guess(vector<double> const& x, vector<double> const& y);

vector<double> GaussianFitting(vector<double> waveform, double thres, int min_dist);

#endif /* PULSE_GAUSSIAN_FITTING_H_ */
