"""
We'll start with Bisection, Falsi, and Secant. All require iteration till value < tolerance is found.
ALL require 2 points on f.
"""

def bisection(f,p1,p2,N, tol=1e-7):
    p1_n = p1
    p2_n= p2
    result = []

    if f(p1)*f(p2)>=0:
        return "IVT concept not met. Check P1 and P2"
    

    for i in range(1, N+1):
        midpoint = (p1_n+p2_n)/2
        result.append(midpoint)

        f_mid = f(midpoint)

        # 2. Check for success or tolerance
        if abs(f_mid) < tol:
            return midpoint, result

        # 3. Narrow the interval
        if f(p1_n) * f_mid < 0:
            p2_n = midpoint  # Root is in the left half
        else:
            p1_n = midpoint  # Root is in the right half

    return (p1_n + p2_n) / 2, result

f = lambda x: x**2 - x - 1


def falsi(f,A,B,N,tol =1e-7):
    A0 = A
    B0 = B
    R = []

    if f(A0)*f(B0)>=0:
        return "IVT concept not met. Check P1 and P2"
    
    for i in range(1,N+1):

        C = B0 - (f(B0) * (B0 - A0)) / (f(B0) - f(A0))
        R.append(C)
        f_C = f(C)
        if f(C)*f(A0)<0:
            
            B0 = f_C
        elif f(C)*f(B0)<0:
            
            A0 = f_C
        elif abs(f(C))< tol:
            return R
        

    return R

root = falsi(f,1,2,25)

print(f"answer: {root}")