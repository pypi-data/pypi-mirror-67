H-MCRLLM
Hierarchical - Multivariate Curve Resolution by Log-Likelihood Maximization

Available at www.pypi.org


X = CS
where
X(nxk): Spectroscopic data where n spectra acquired over k energy levels
C(nxa): Composition map based on a MCRLLM components
S(axk): Spectra of the a components as computed by MCRLLM


METHOD FIRST PRESENTED IN
Lavoie F.B., Braidy N. and Gosselin R. (2016) Including Noise Characteristics in MCR to improve Mapping and Component Extraction from Spectral Images, Chemometrics and Intelligent Laboratory Systems, 153, 40-50.



# Hierarchical MCRLLM (3 steps)
# 
# MCR takes an input X spectral matrix to obtain:
# C : composition map or n components
# S : spectra of the n components
#
# STEP 1. 
# Call raw X data and repeatedly it subdivided it into n=2
# components. This generates multiple spectra (S=2 for each)
# subdivision.
#
# STEP 2.
# PCA on the multiple spectra to manually identify the
# reference spectra (i.e. pure species)
#
# STEP 3.
# Use the reference spectra (step 2) to compute C. This is either
# done using:
# - (half_MCR): MCRLLM in which the spectra S are not evaluted anew.
# - (full_MCR): MCRLLM in which the spectra S are evaluated anew.
#               spectra from step 2 are used as a starting point.





EXAMPLES
Two full examples, along with datasets, are provided in 'Download Files'.
Please refer to 'MCRLLM_example.pdf' for full details.
- Example 1: 1D spectral linescan of EELS data.
- Example 2: 2D spectral image of XPS data.


COMPATIBILITY
MCRLLM tested on Python 3.7 using the following modules:
- Numpy 1.17.2
- Scipy 1.3.1
- Sklearn 0.21.3
- Pysptools 0.15.0
- Tqdm 4.36.1


CONTACT INFO
Ryan Gosselin, Université de Sherbrooke, ryan.gosselin@usherbrooke.ca




-- Ryan Gosselin, April 15th, 2020