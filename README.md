# IsogenyClassesLowDimTestCode
Test code attached to the paper "Weil polynomials of small degree" (Stefano Marseglia).

This repository contains a Magma implementation of Example 4.3, Proposition 4.8, Main Theorems A, B and C.
These implementations are given as functions `qWeilPolyDegX` where X=2,4,6,8 or 10.
The test-routines include also checks for all provided descriptions of q-Weil-Polynomials with real roots.

The purpose of the code is to test the output against the one produced by the SageMath function `weil_polynomials(deg,q)` which is based on https://github.com/kedlaya/root-unitary.
In the repository, we include a tar.gz file with the output of the SageMath function for several q's (which useful especially if a recent enough version of SageMath is not installed).

### Instructions for testing ###
1) clone this repository and cd into the folder `IsogenyClassesLowDimTestCode/`
2) extract the tar.gz.
```
    tar -xzvf kedlaya_weil_poly.tar.gz
```
This include file for testinng for q-Weil polynomials with q a prime power between 2 and 9 of degree 2g with g=1,2,3,4 and q=2,3,4 for g=5.
If one want to run test for more prime powers q, one can you modify the file `create_qWeilPoly_using_kedlaya.sage`and then run
```
    sage create_qWeilPoly_using_kedlaya.sage
````
which might require quite some time and memory.
4) run
```
    magma qWeilPoly_magma
```
5) feel free to erase all sagemath kedlaya's output
```
    rm kedlaya_weil_poly_*
```
