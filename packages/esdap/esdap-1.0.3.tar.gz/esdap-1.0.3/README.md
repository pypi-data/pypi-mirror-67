﻿# ESDaP

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](https://www.contributor-covenant.org/version/2/0/code_of_conduct/)

A Python package for **E**pileptic **S**eizure **D**etection **a**nd **P**rediction from EEG data.

**Authors**: [Fabian Egli](https://github.com/fabianegli/), [Nick Pullen](https://github.com/nstjhp/), [Alessandro Quercia](https://github.com/AlessioQuercia/), [Thomas Frick](https://github.com/thomfrick/), [Isabelle Dupanloup](https://github.com/idupanloup/)


# Summary

Epilepsy is a common neurological disorder that affects around 1% of the population worldwide. For approximately 30% of patients, there is no effective therapeutic strategy. The disorder manifests itself clinically by unprovoked seizures which correspond to sudden alterations in consciousness, movement or behaviour. Seizures are often unpredictable and thus detrimentally affect the quality of life of patients.

Epileptic seizures occur as a result of a malfunctioning of the electrophysiological system of the brain. Electroencephalogram (EEG) provides a direct measurement of electrical brain activity.

esdap is an open-source Python package for the detection and prediction of epileptic seizures from EEG data. It allows the extraction of features from segments, or short time windows, of the original EEG data. It also allows to run different types of neural networks to classify the original segments, using the extracted features, in ictal (during a seizure), preictal (before a seizure), postictal (after a seizure) or interictal (i.e. normal) state.
It measures the classification performance of the models, using cross-validation and a variety of metrics.


# Installation

esdap has a series of dependencies, namely:
- [joblib](https://pypi.org/project/joblib/) (version >= 0.14.1): a set of tools to provide lightweight pipelining in Python
- [matplotlib](https://pypi.org/project/matplotlib) (version >= 3.1.2): a library for creating static, animated, and interactive visualizations in Python
- [mlflow](https://pypi.org/project/mlflow) (version >= 1.5.0): a platform to streamline machine learning development, including tracking experiments, packaging code into reproducible runs, and sharing and deploying models
- [mne](https://pypi.org/project/mne) (version >= 0.19.2): a Python package for exploring, visualizing, and analyzing human neurophysiological data such as EEG
- [numba](https://pypi.org/project/numba/) (version >= 0.46.0): an open source optimizing compiler for Python
- [numpy](https://pypi.org/project/numpy) (version >= 1.18.0): a Python package for scientific computing
- [pandas](https://pypi.org/project/pandas/) (version >= 1.0.0): a Python package providing fast, flexible, and expressive data structures designed to make working with structured (tabular, multidimensional, potentially heterogeneous) and time series data both easy and intuitive
- [pywavelets](https://pypi.org/project/PyWavelets/) (version >= 1.1.1): a Python wavelet transforms module
- [scikit-learn](https://pypi.org/project/scikit-learn/) (version >= 0.22.1): a Python module for machine learning
- [scipy](https://pypi.org/project/scipy/) (version >= 1.4.1): a Python package providing efficient numerical routines for numerical integration, interpolation, optimization, linear algebra, and statistics
- [seaborn](https://pypi.org/project/seaborn/) (version >= 0.10.0): a library for making statistical graphics in Python
- [tensorflow](https://pypi.org/project/tensorflow/) (version >= 2.0.0): an open source software library for high performance numerical computation
- [xgboost](https://pypi.org/project/xgboost/) (version >= 0.90): a library which implements machine learning algorithms under the [Gradient Boosting](https://en.wikipedia.org/wiki/Gradient_boosting) framework

These dependencies can be installed using [conda](https://docs.conda.io/) environments:

`conda env create -f conda_env.yaml`

`conda activate esdap`

esdap is available on [PyPi](https://pypi.org/) and can be installed using pip.

`pip install esdap`


# Description

- esdap reads EEG data from [edf](https://en.wikipedia.org/wiki/European_Data_Format) files. It reads the list of edf files and seizure events from [summary](https://physionet.org/content/chbmit/1.0.0/chb06/chb06-summary.txt) files. 

- esdap allows to extract various types of features from EEG segments:
	- univariate time domain features
		- moments of the EEG signal (mean, variance, skewness, kurtosis, standard deviation)
		- difference between the highest and lowest amplitude
		- absolute area under the EEG signal
		- decorrelation time (i.e. the time at which the autocorrelation of the EEG signal becomes negative)
	- spectral features
		- EEG signal frequency in each of the fundamental rhythmic frequency bands (i.e. delta: 1–3 Hz, theta: 4–7 Hz, alpha: 8–13 Hz, beta: 14–30 Hz, gamma1: 31–55 Hz and gamma2: 65–110 Hz) using the Discrete Fourier Transform
		- detail (64–128 Hz, 32–64 Hz, 16–32 Hz, 8–16 Hz, 4–8 Hz, 2–4 Hz, 1–2 Hz) and approximation coefficients (<1 Hz) applying  the Discrete Wavelet Transform, using a 7-level decomposition and the Daubechies 4 (db4) as the mother wavelet
	- bivariate features
		- maximal absolute cross correlation value
		- phase-locking synchrony using the Hilbert transform

esdap generates one file for each features type (each line corresponds to a segment) and a file containing the labels (ictal, preictal, postictal, interictal) for each EEG segment. The length of the segment, an overlap between consecutive segments, the duration of the preictal and the postictal period can be chosen by the user.

Before features extraction, esdap removes non-physiological artifacts, including power line noise, by excluding components in the frequency ranges 59-61 Hz and above 120 Hz, from EEG data. It also removes the DC component at 0 Hz.

- esdap implements three neural networks which can be used to classify EEG segments into either 2 classes (ictal versus interictal (for seizure detection), or preictal versus interictal (for seizure prediction)) or 4 classes (ictal, preictal, postictal, interictal).
	- a fully connected neural network (FCN) 
	- a Long Short-Term Memory (LSTM) neural network 
	- a one-dimensional convolutional neural network (CNN) 

The performance of the classifiers is assessed by cross-validation, and measured by standard metrics (accuracy, precision, recall/sensitivity and F1 score).

esdap users can modify the architecture of the neural networks (i.e. number of hidden layers, number of neurons in each layer, the inclusion of dropout layer, the dropout rate, the convolution parameters, the number of segments to include in sequences for the LSTM and CNN, the batch size, the activation function, the loss function, etc.) by modifying parameters in the code.
- FCN architecture in:  esdap/training/models/fcn.py
- LSTM architecture in: esdap/training/models/lstm.py
- CNN architecture in: esdap/training/models/cnn.py


# Usage

We use bash scripts to run the functions implemented in the esdap python package. 
Example bash scripts can be found in the [official repository's](https://github.com/idupanloup/ESDaP) `examples` folder.

We use MLflow and its tracking component for logging parameters and metrics when running the models implemented in esdap and later visualizing the results. The MLflow logs files are stored in a mlruns directory which is generated automoatically in the same directory as esdap. The results can be visualized and compared using the command:

`mlflow ui`

and opening a web browser from any machine, including any remote machine that can connect to the tracking server, using the following URL

`http://<ip address of MLflow tracking server>:5000`

esdap allows to specify a name for the run to be easily retrieved when comparing metrics across runs. For each esdap run, esdap generates a nested MLflow run, with a parent run and a child run for each cross-validation operation. During visualization, the results are displayed along a a collapsible tree underneath each parent run.

In each parent run, esdap logs unwweighted average performance metrics (accuracy, precision, recall, F1-score) across classes and cross-validation operations. In each child run, esdap logs performance metrics, for each class, computed using [sklearn.metrics.classification_report](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html). It also reports macro average (averaging the unweighted mean per label), weighted average (averaging the support-weighted mean per label), sample average (only for multilabel classification) and micro average (averaging the total true positives, false negatives and false positives). Parameters describing the learning process during the training phase are also reported (learning rate, training loss). Validation loss is also given. Variation of the training loss and the validation loss (across epochs) is also reported and can be visualized to assess if the models are overfitting (they are not generalizing to unseen data) or underfitting.


# Contributing

Contributions to esdap are welcome.
Please note that this project is released with a Contributor Code of Conduct. By participating in this project you agree to abide by its terms.

Contributors to esdap code should use the following development tools:
- [black](https://https://pypi.org/project/black/) (version >= 19.10b0): a Python code formatter
- [flake8](https://pypi.org/project/flake8/) (version >= 3.5.0): a Python code linter tool
- [nose](https://pypi.org/project/nose/) (version >= 1.3.7): a Python testing tool.

These additional dependencies can be installed by creating a conda environment from `conda_dev_env.yaml`.


# License

esdap is published under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).
