def lcm_naive(a,b): #very very slow
    for d in range(1,a*b+1):
        if not d%a and not d%b:
            return d

def euclid_gcd(a,b):
    return euclid_gcd(b,a%b) if b > 0 else a

def euclid_lcm(a,b):
    a,b = (a,b) if a>=b else (b,a)
    gcd = euclid_gcd(a,b)
    lcm = (a*b)//gcd
    return lcm

print(euclid_lcm(5,10))
