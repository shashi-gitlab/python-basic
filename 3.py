P = 2500000 # loan amount in rs
R = 8.75 #interest rate in %
N = 30  # years


# Formula for EMI Calculation is -
#P x R x (1+R)^N / [(1+R)^N-1] where-


N = 30 * 12

R = 8.75

#The rate of interest (R) on your loan is calculated per month.

R = 8.75/12/100

emi = P * R * (1+R)**N / ((1+R)**N-1)
print(emi)
print(round(emi))