import math

from scipy.stats import norm

def call_bs(S, K, r, sigma, T):
    '''Call price function (Black-Scholes)'''
    d1 = 1 / (sigma * math.sqrt(T)) * (math.log(S / K) + (r + sigma**2 / 2) * T)
    d2 = d1 - sigma * math.sqrt(T)
    return round(norm.cdf(d1) * S - norm.cdf(d2) * K * math.exp(-r * T), 3)

call_bs(S=110, K=100, r=0.085, sigma=0.8445, T=92/365)

if __name__ == "__main__":
    print("The following script will price a European option based on the inputs provided by the user.")

    # Method
    method = -1
    while method != 0:
        method = input("Enter which method you would like to use (Black-Scholes -> 0, Monte Carlo -> 1): ")  
        method = int(method)
        if method == 0:
            method_str = 'Black-Scholes' 
            print(f"The chosen method is: {method_str}")
        else:
            print('Please try again. Only Black-Scholes is currently supported.')

    # Underlying price
    S = input("Enter the price of the underlying: ")   
    print(f"The inputted price of the underlying is: {S}")
    S = float(S)

    # Strike Price
    K = input("Enter the strike price: ")   
    print(f"The inputted strike price is: {K}")
    K = float(K)

    # Risk-free rate of return (interest rate)
    r = input("Enter the risk-free rate of return as an annualised decimal (e.g. 5% should be inputted as 0.05): ")   
    print(f"The inputted risk-free rate of return is: {r}")
    r = float(r)

    # Volatility
    sigma = input("Enter sigma (volatility parameter): ")   
    print(f"The inputted volatility parameter is: {sigma}")
    sigma = float(sigma)
    
    # Time to expiry
    T = input("Enter the time to expiry in years: ")   
    print(f"The inputted time ot expiry is: {T}")
    T = float(T)

    d1 = 1 / (sigma * math.sqrt(T)) * (math.log(S / K) + (r + sigma**2 / 2) * T)
    d2 = d1 - sigma * math.sqrt(T)

    # Call price by BS
    C = norm.cdf(d1) * S - norm.cdf(d2) * K * math.exp(-r * T)
    print(f'Call price by BS: ${C:.3f}')

    # Put price by put-call parity
    D = 1 / (1 + r * T)
    P = C - S + D * K
    print(f'Put price by PCP (BS): ${P:.3f}')