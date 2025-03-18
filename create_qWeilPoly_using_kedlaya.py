#!/usr/bin/env sage
# coding: utf-8

R.<x> = ZZ[]
prime_powers = [ q for q in [2..10] if is_prime_power(q) ]
for g in [1..5] :
    for q in prime_powers :
        polys = [str(h.coefficients(sparse=False)) for h in R.weil_polynomials(2*g,q)];
        with open('kedlaya_weil_poly_'+str(2*g)+'_'+str(q),'w') as file:
            for h in polys :
                file.write(f"{h}\n");

# NOTE: some of the resulting files are too big for git. Don´t forget to tar-gzip them.
