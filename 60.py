def calculate(p, r=10, t=12):
    interest = p*r*t/100
    finalAmount = interest + p
    print(f'''
        INTEREST: {interest}
        FINAL AMOUNT: {finalAmount}
    ''')

calculate(1000,7,12)
calculate(50000)