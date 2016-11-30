# create a function called generate_primes
def generate_primes(n):
    # if the value of n is equal to 2 output value 2
	if n==2: return [2]
    # if the value is less than two return empty set and print error statement
	elif n<2: return []
# generate a range between 3 and the value of n
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]
print generate_primes(13)
