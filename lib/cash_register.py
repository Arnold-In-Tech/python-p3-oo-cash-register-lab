#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.transactions = []

  def add_item(self, title, price, quantity=1):
    for i in range(quantity):
      self.items.append(title)
    self.total += price*quantity
    self.transactions.append([title, price, quantity])


  def apply_discount(self):
    if self.discount > 0:
      self.total -= self.total * self.discount / 100
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
    

  def void_last_transaction(self):
    last = self.transactions.pop()
    self.total -= (last[1] * last[2]) - ((last[1] * last[2]) * self.discount / 100 ) # (price * quantity) less (discount)
    self.items = [item for item in self.items if item == last[0]] # update items list
