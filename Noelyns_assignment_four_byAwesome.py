# putting a market vendor into consideration , with examples discuss the concept of funcs
# these funcs are aiding in the market vendors daily tasks ie
# how can they know that they have made profits , losses, the total and 
#the everyday usual tasks

# calculating profit
def profits(selling_price, buying_price):
    my_profit = selling_price - buying_price
    return my_profit

print(profits(30000, 20000))
# an alternative way could be
#my_profit = profits(30000,20000)
#print(my_profit)


# calculating total
def total(item_unit_cost, quantity):
    total_amount = item_unit_cost * quantity
    return total_amount

print(total(3000, 4))

    
#calculating loss
def losses( buying_price, cost_price):
    loss = buying_price - cost_price
    return loss 
print(losses(25000, 30000))


#calculating change
def change(amount_given, total_amount ):
    balance = amount_given - total_amount 
    return balance
print(change(30000, 28000))


#calcutating debts
def debts(total_amount, amount_paid):
    unpaid = total_amount - amount_paid
    return unpaid
print(debts(40000, 20000))