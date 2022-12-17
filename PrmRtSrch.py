# This script will generate all of the primitive roots
# entered a large number (4+ digits) would take a long time

prime = 31    # the prime we want to search the primitive root
num_to_check = 0
p_minus_1_range = range(1,prime)
primitive_roots = []
for each in range(1, prime):
	num_to_check += 1
	candidate_prim_roots = []
	for i in range(1, prime):
		modulus = (num_to_check ** i) % prime
		candidate_prim_roots.append(modulus)
		cleanedup_candidate_prim_roots = set(candidate_prim_roots)
		if len(cleanedup_candidate_prim_roots) == len(range(1,prime)):
			primitive_roots.append(num_to_check)
print("Primitive roots of %d are:" % prime)
print(primitive_roots)