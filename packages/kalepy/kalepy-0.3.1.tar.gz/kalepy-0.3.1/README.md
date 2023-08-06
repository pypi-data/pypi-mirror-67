# kalepy: Kernel Density Estimation and Sampling

[![Build Status](https://travis-ci.org/lzkelley/kalepy.svg?branch=master)](https://travis-ci.org/lzkelley/kalepy)
[![codecov](https://codecov.io/gh/lzkelley/kalepy/branch/master/graph/badge.svg)](https://codecov.io/gh/lzkelley/kalepy)

<!-- dev: [![Build Status](https://travis-ci.org/lzkelley/kalepy.svg?branch=dev)](https://travis-ci.org/lzkelley/kalepy) -->


![kalepy animated logo](https://raw.githubusercontent.com/lzkelley/kalepy/dev/docs/media/logo_anim_small.gif)

This package performs KDE operations on multidimensional data to: **1) calculate estimated PDFs** (probability distribution functions), and **2) resample new data** from those PDFs.

## Installation

#### from pypi (i.e. via pip)

```bash
pip install kalepy
```

#### from source (e.g. for development)

```bash
git clone https://github.com/lzkelley/kalepy.git
pip install -e kalepy/
```

In this case the package can easily be updated by changing into the source directory, pulling, and rebuilding:

```bash
cd kalepy
git pull
pip install -e .
# Optional: run unit tests (using the `nosetests` package)
nosetests
```


## Examples

### Use 'reflecting' boundary conditions to improve PDF reconstruction at boundaries

Without reflection, the KDE (red line) noticeably underestimates the edges of this uniform distribution (grey histogram).  When resampling from the KDE, the new samples (red carpet and histogram) are drawn outside of the original distribution edges.  Reflecting boundary conditions better estimate the PDF, and constrain new samples to be within bounds.

```python
import kalepy as kale
# here `data` has shape (N,) for N data points
kde = kale.KDE(data)
grid = np.linspace(-0.5, 2.5, 1000)
# choose reflection boundaries
boundaries = [0.0, 2.0]
pdf = kde.pdf(grid, reflect=boundaries)
samples = kde.resample(100, reflect=boundaries)
```



![1D Samples with Reflection](https://raw.githubusercontent.com/lzkelley/kalepy/master/docs/media/kde_1d_reflect.png)

This also works in multiple dimensions.  In each dimension, reflecting boundaries can be applied either on both sides (e.g. x-axis), or only on one side (e.g. y-axis).

```python
import kalepy as kale
# here `data` has shape (2,N) 2-parameters and N data points
kde = kale.KDE(data)
xc, yc = np.meshgrid([np.linspace(-0.5, 2.5, 100), np.linspace(-3.0, 2.5, 200)])
grid = np.vstack([xc.ravel(), yc.ravel()])
# choose reflection boundaries in each parameter
boundaries = [[0.0, 2.0], [None, 2.0]]
pdf = kde.pdf(grid, reflect=boundaries)
samples = kde.resample(1000, reflect=boundaries)
```

![2D Samples with Reflection](https://raw.githubusercontent.com/lzkelley/kalepy/master/docs/media/kde_2d_reflect.png)



### Comparison of Different Histogram Parameters and Different Kernel

The choice in bin-widths and bin-origins makes a significant difference in how a histogram appears.  In general, both parameters are chosen arbitrarily.  KDE also have freedom in what kernel is used, and the bandwidth (amount of smoothing), but there are heuristics for optimizing these parameters.  In particular, for general data, the Parabola/"Epanechnikov" kernel is optimal in reducing bias, and the bandwidth can be estimated using Scott's method.

![Different Histograms and Kernels](https://raw.githubusercontent.com/lzkelley/kalepy/master/docs/media/kde_motivation.png)



### Calculate projected / marginalized PDF across target parameters

```python
# 2-parameter data, shaped (2,N) for N data-points
kde = kale.KDE(data)
# Create bins in each dimension
edges = [np.linspace(-7.5, 10.5, 100), np.linspace(-3, 9, 100)]
xe, ye = np.meshgrid(*edges)
# Grid of test points
grid = np.vstack([xe.ravel(), ye.ravel()])
# Calculate 2D PDF
pdf_2d = kde.pdf(grid)
# Calculate each 1D PDF
pdf_x = kde.pdf(edges[0], param=0)
pdf_y = kde.pdf(edges[1], param=1)
```

![2D PDF with projections](https://raw.githubusercontent.com/lzkelley/kalepy/master/docs/media/2d_pdf_projection.png)



### KDE Refinement with increasing data points

![2D PDF with projections](https://raw.githubusercontent.com/lzkelley/kalepy/master/docs/media/movie.gif)
