# Assignment 3: Annual compound interest

def calculate_compound_interest(P, r, n):
    amount = P
    for year in range(1, n + 1):
        amount = amount * (1 + r)
        print(f"End of Year {year}: ₩{amount:.2f}")
    interest = amount - P
    return amount, interest

P = 10000.0         
r = 0.05             
n = 7                

final_amount, interest = calculate_compound_interest(P, r, n)

print("\nResults:")
print(f"Final Amount after {n} years: ₩{final_amount:.2f}")
print(f"Total Compound Interest Earned: ₩{interest:.2f}")

