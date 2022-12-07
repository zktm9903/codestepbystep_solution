# print(round(((1.03**5*100-100)*100/100), 0))
# print(round((1.08**24*5.25-5.25)*100/5.25, 0))

def calAmount(PV, r, n):
  return round(PV * (1 + r)**n, 2)

def calProfit(PV, FV):
  return int(round((FV - PV)*100/PV,0))
def investment(idx):
  PV = 0
  r = 0
  n = 0
  FV = 0
  profit = 0
  
  for i in range(idx):
    print('Investor '+ str(i+1))
    PV = float(input('Initial amount? '))
    r = float(input('Interest rate%? '))
    n = int(input('Num. of months? '))
    
    FV = calAmount(PV, r, n)
    profit = calProfit(PV, FV)
    
    print('Amount: $ ' + str(FV))
    print('Profit: $ ' + str(round(FV - PV,2)) + ' = ' + str(profit) + ' %')

    if profit <= 10:
      print('Weak')
    elif profit <= 50:
      print('Medium')
    else:
      print('Strong')
      
    print()

  print('Have a nice day!')

investment(2)