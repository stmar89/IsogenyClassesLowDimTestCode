# IsogenyClassesLowDimTestCode
Test code attached to the paper "Weil polynomials of small degree" (Jun Jie Lin and Stefano Marseglia).

This repository contains a Magma implementation of Example 4.3, Proposition 4.7, Main Theorems B, C and D from the paper "Weil polynomials of small degree".
These implementations are given as functions qWeilPolyDegX where X=2,4,6,8 or 10.
The test-routines include also checks for all provided descriptions of q-Weil-Polynomials with real roots.

The purpose of the code is to test the output against the one produced by the SageMath function weil_polynomials(deg,q) which is based on https://github.com/kedlaya/root-unitary.
In the repository, we include a tar.gz file with the output of the SageMath function for several q's (which useful especially if a recent enough version of SageMath is not installed).
If one want to run test for more prime powers q, one can use create_qWeilPoly_using_kedlaya.py, which might require quite some time and memory.

### Instructions for testing ###
1) move to the folder IsogenyClassesLowDimTestCode/
2) extract the tar.gz 
    tar -xzvf kedlaya_weil_poly.tar.gz
3) run with magma
    magma qWeilPoly_magma
4) feel free to erase all sagemath kedlaya's output
    rm kedlaya_weil_poly_*