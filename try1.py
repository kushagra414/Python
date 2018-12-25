
meal_cost = float(raw_input().strip())
tip_percent = int(raw_input().strip())
tax_percent = int(raw_input().strip())
tip = meal_cost*20/100
tax = tip_percent*8/100
total_cost = meal_cost + tip + tax
print 'The total meal cost is %d dollars.' % total_cost