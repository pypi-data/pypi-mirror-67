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
 * PulseGaussianFitting.cpp
 *
 *  Created on: 2017/12/6
 *      Author: Jianbo Qi
 *      Contribution: Tiangang Yin
 *
 *  Changed on: 2019/05/24
 *      Contribution: Florian de Boissieu <fdeboiss@gmail.com>, add function GaussianFitting for python binding
 */

//#include "../../../include/classes/GaussianDecomposition/PulseGaussianFitting.h"
#include "PulseGaussianFitting.h"
#include "mpfit.h"
#include <math.h>
#include <iostream>
#include <string.h>
#define pi 3.141592653


vector<int> peaksDetectFisrtOrderZeroCrosssing(const vector<double> & y, double const& thres, int const& min_dist) {
    //    double const thres_new = thres * (*max_element(y.begin(), y.end()) - *min_element(y.begin(), y.end()));


    //first order difference
    vector<double> dy;
    for (size_t i = 1; i < y.size(); i++) {
        dy.push_back(y[i] - y[i - 1]);
    }

    vector<int> peaks;
    vector<double> peaks_amp;
    for(size_t i=0;i<dy.size()-1;i++){
        for(size_t j=i+1;j<dy.size();j++){
            if (dy[i] == 0) break;
            if(dy[j] !=0){
                if(dy[i] > 0 && dy[j] < 0 && y[i+1] > thres){
                    peaks.push_back(i+1);
                    peaks_amp.push_back(y[i+1]);
                }
                break;
            }
        }
    }

    //remove peaks which are too close to each other
    if (peaks.size() > 1 && min_dist > 1) {
        vector<bool> rem;
        for (size_t i = 0; i < y.size(); i++)
            rem.push_back(true);
        for (size_t i = 0; i < peaks.size(); i++)
            rem[peaks[i]] = false;

        vector<int> sorted_index = sort_indexes(peaks_amp);
        for (size_t i = 0; i < sorted_index.size(); i++) {
            int peaks_index = peaks[sorted_index[i]];
            if (!rem[peaks_index]) {
                int left = max(0, peaks_index - min_dist);
                int right = min((int)y.size() - 1, peaks_index + min_dist + 1);
                for (int j = left; j <= right; j++)
                    rem[j] = true;
                rem[peaks_index] = false;
            }
        }
        peaks.clear();
        for (size_t i = 0; i < y.size(); i++) {
            if (!rem[i]) {
                peaks.push_back(i);
            }
        }

    }
    return peaks;
}


//flexion points detection: used for estimating the parameters for each components
vector< vector<int> > flexion_detect(vector<double> const& y, vector<int> const& peaks) {
	vector< vector<int> > intervals;
	if (peaks.size() > 0) {
		for (size_t i = 0; i < peaks.size(); i++) {
			vector<int> interval;
			int peak_index = peaks[i];
			int li = peak_index;
			while (li > 0 && y[li - 1] <= y[li] && y[li - 1] != 0) {
				li -= 1;
			}
			int ri = peak_index;
			while (ri < (int)y.size() - 1 && y[ri + 1] <= y[ri] && y[ri + 1] != 0) {
				ri += 1;
			}
			interval.push_back(li);
			interval.push_back(ri);
			intervals.push_back(interval);
		}
	}
	else {
//		Should never happen
		cerr<<"This case flexion_detect in Should never happen"<<endl;
		abort();
		vector<int> interval;
		interval.push_back(0);
		interval.push_back(y.size() - 1);
		intervals.push_back(interval);
	}
	return intervals;
}


double GaussianFunc(double x, double amp, double cen, double wid) {
    return (amp / (sqrt(2 * pi)*wid)) * exp(-(x - cen)*(x - cen) / (2 * wid*wid));
}


double CompositeGaussianFuncN(int number_of_peaks, double x, const double *par) {
    double re = 0;
    for (int i = 0; i < number_of_peaks; i++) {
        double amp = par[i*3 + 0];
        double cen = par[i*3 + 1];
        double wid = par[i*3 + 2];
        re += GaussianFunc(x, amp, cen, wid);
    }
    return re;
}

int GaussianSum(int m, int n, double *p, double *deviates,
	double **derivs, void *private_data) {
	int numPeaks = n / 3;
	/* Retrieve values of x, y and y_error from private structure */
	XYData* xydata = (XYData*)private_data;
	for (int i = 0; i < m; i++) {
		deviates[i] = (xydata->y[i] - CompositeGaussianFuncN(numPeaks, xydata->x[i], p)) / xydata->y_error[i];
	}
	return 0;
}

vector<double> guess(vector<double> const& x, vector<double> const& y) {
    vector<double>::const_iterator max_iterator = max_element(y.begin(), y.end());
    int index_maxy = distance(y.begin(), max_iterator);
    double maxy = *max_iterator;
    double miny = *min_element(y.begin(), y.end());
    double maxx = *max_element(x.begin(), x.end());
    double minx = *min_element(x.begin(), x.end());

    vector<double> par;
    double cen = x[index_maxy];
    double amp = (maxy - miny)*3.0;
    double wid = (maxx - minx) / 6.0;
    amp = amp*wid;

    par.push_back(amp);
    par.push_back(cen);
    par.push_back(wid);
    return par;
}

vector<double> GaussianFitting(vector<double> waveform, double thres, int min_dist) {

    vector<double> par; // amp, center, sigma
    vector<int> peaks = peaksDetectFisrtOrderZeroCrosssing(waveform, thres, min_dist); //0.005 is set to 1/200 of the maximum waveform amplitude to avoid too small peaks.
    //		cout<<"peaks.size(): "<<peaks.size()<<endl;
    if(peaks.size()>0){

//        double distLocal = 0;
//        double seudoSolidAngle = 0;
//        double targitRef = 0;
//        double amplitudeMax = 0;
//        double integral_res = 0;
//
//
        double totalPhotons = 0;
        for(unsigned int i=0;i<waveform.size();i++){
            totalPhotons+=waveform[i];
        }

        vector< vector<int> > flexions = flexion_detect(waveform, peaks);

        vector<double> y_error;
        vector<double> waveBinIndex;
        y_error.resize(waveform.size());
        waveBinIndex.resize(waveform.size());
        for(unsigned int i=0;i<waveform.size();i++){
            waveBinIndex[i] = i;
//							*_wfdto.dStep;
            y_error[i] = 0.01;
        }

        for (unsigned int i = 0; i < peaks.size(); i++) {
            vector<double> sub_x(waveBinIndex.begin() + flexions[i][0], waveBinIndex.begin() + flexions[i][1]);
            vector<double> sub_y(waveform.begin() + flexions[i][0], waveform.begin() + flexions[i][1]);
            vector<double> comp_par = guess(sub_x, sub_y);
            par.push_back(comp_par[0]);
            par.push_back(comp_par[1]);
            par.push_back(comp_par[2]);
        }
        mp_par *paramConstraints = new mp_par[peaks.size()*3*sizeof(mp_par)];
        memset(paramConstraints, 0, peaks.size()*3*sizeof(mp_par));
        for (unsigned int i = 0; i < peaks.size(); i++) {
            int idx = i * 3;

            //integral
            paramConstraints[idx].fixed = false;
            paramConstraints[idx].limited[0] = true;
            paramConstraints[idx].limits[0] = 0.0;

            //center
            paramConstraints[idx + 1].fixed = false;
            paramConstraints[idx + 1].limited[0] = true;
            paramConstraints[idx + 1].limited[1] = true;
            paramConstraints[idx + 1].limits[0] = waveBinIndex[flexions[i][0]];
            paramConstraints[idx + 1].limits[1] = waveBinIndex[flexions[i][1]];

            //sigma
            paramConstraints[idx + 2].fixed = false;
            paramConstraints[idx + 2].limited[0] = true;
            paramConstraints[idx + 2].limits[0] = 0.0;

//						cout<<"range..."<<endl;
//						cout<<paramConstraints[idx + 0].fixed<<paramConstraints[idx + 0].limited[0]<<paramConstraints[idx + 0].limited[1]<<endl;
//						cout<<paramConstraints[idx + 1].fixed<<paramConstraints[idx + 1].limited[0]<<paramConstraints[idx + 1].limited[1]<<endl;
//						cout<<paramConstraints[idx + 2].fixed<<paramConstraints[idx + 2].limited[0]<<paramConstraints[idx + 2].limited[1]<<endl;
        }
        XYData xydata;
        xydata.x = waveBinIndex.data();
        xydata.y = waveform.data();
        xydata.y_error = y_error.data();
        int status = mpfit(GaussianSum, waveBinIndex.size(), par.size(), par.data(), paramConstraints, 0,(void*)&xydata, 0);
        if(status <= 0){
            cout<<"Failed to perform Gaussian decomposition." <<endl;
        }
        delete[] paramConstraints;
    }
    return par;
}
