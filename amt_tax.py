#!/usr/bin/python

filling_status = {'single','married joint'}
tax_bracket = {'single':    
                [(9525, 0.1),
                (38700, 0.12),
                (82500, 0.22),
                (157500, 0.24),
                (200000, 0.32),
                (500000, 0.35),
                (10000000000, 0.37)],
               'married joint':    
                [(19050, 0.1),
                (77400, 0.12),
                (165000, 0.22),
                (315000, 0.24),
                (400000, 0.32),
                (600000, 0.35),
                (10000000000, 0.37)]
                }

amt_exempt = {'single': 70300, 'married joint':109400}
reg_exempt = {'single': 12000, 'married joint':24000}
amt_rate = {'single': [(179500,0.26),(1000000000,0.28)], 
            'married joint':[(179500,0.26),(1000000000,0.28)]}

def brack_tax(bracket, income):
    tax_amount = 0
    prev_bracket = 0
    for bk in bracket:
        limit, rate = bk
        if limit <= income:
            tax_amount += (limit - prev_bracket) * rate
            prev_bracket = limit 
        else:
            tax_amount += (income - prev_bracket) * rate
            break
    return tax_amount
    

def calculate_regular_tax(status, income):
    taxable_income = income - reg_exempt[status]
    return brack_tax(tax_bracket[status],taxable_income)

def calculate_amt_tax(status, income):
    taxable_income = income - amt_exempt[status]
    if (taxable_income <=0 ):
        return 0
    return brack_tax(amt_rate[status], taxable_income)

for x in range(1,1000):
    reg_tax = calculate_regular_tax('married joint',x*1000)
    amt_tax = calculate_amt_tax('married joint', x*1000)
    print x, reg_tax, amt_tax, reg_tax - amt_tax