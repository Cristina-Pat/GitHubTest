# generate the monthly oustanding mortgage
# input: annual interest rate, a floating-point percentage
rate = 0.05
# input: monthly payment, a positive integer in a currency
payment = 200
# input/output: morgage, positive number, same currency
mortgage = 1000
print('Outstanding mortgage:', mortgage)
while mortgage > 0:
    interest = mortgage * rate / 12
    mortgage = mortgage + interest - payment
    print('Outstanding mortgage:', mortgage)