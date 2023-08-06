[![licence](https://img.shields.io/badge/Licence-GPL--3-blue.svg)](https://www.r-project.org/Licenses/GPL-3)
[![python](https://img.shields.io/badge/Python-3-blue.svg)](https://www.python.org)
[![PyPI version](https://badge.fury.io/py/gdecomp.svg)](https://badge.fury.io/py/gdecomp)

# gdecomp: python binding of C++ signal gaussian decomposition.
This package aims at decomposing a signal (1D numpy array) into a sum of gaussian, 
typically used in full waveform lidar analysis.
It is used in particular to process lidar simulations produced with [pytools4dart](http://pytools4dart.giltab.io/pytools4dart). 
This code is inspired from C++ code developped by DART team (Jianbo Qi, Tiangang Yin), 
for [DART](http://www.cesbio.ups-tlse.fr/dart/index.php) radiative transfer simulator.

- Creation date: 2019-05-24
- Author: Florian de Boissieu

# Install
Package `gdecomp` can be installed with:

```bash
pip install gdecomp
```

# Example

```python
import gdecomp
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(100)
gaus=np.array([[130, 20, 5],
      [50, 50, 10],
      [10, 70, 5]])

y=np.zeros(x.shape)
for i in range(gaus.shape[0]):
    y += gaus[i,0] / (np.sqrt(2 * np.pi)*gaus[i,2]) * np.exp(-(x - gaus[i,1])**2 / (2 * gaus[i,2]**2))




out = gdecomp.GaussianDecomposition(y)
out = np.reshape(out, (-1, 3))

fit = np.zeros(y.size)
for i in range(out.shape[0]):
    fit += out[i,0] / (np.sqrt(2 * np.pi)*out[i,2]) * np.exp(-(x - out[i,1])**2 / (2 * out[i,2]**2))

line1 = plt.plot(x, y, color='k', label='waveform')
line2 = plt.plot(x, fit, color='r', linestyle='--', label='fit')
plt.legend(loc='upper right')
```

# Aknowledgements

This package includes cmpfit source code of [CMPFIT library](http://cow.physics.wisc.edu/~craigm/idl/cmpfit.html), 
software developed by the University of Chicago, as Operator of Argonne Nationa Laboratory.
See src/mpfit/DISCLAIMER for copyright details of that code.
