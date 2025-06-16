#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0, items=None):
    self.discount = discount
    self.total = total
    self.items = []
    self.transac_hist = {
      "items": [],
      "amount": 0
    }

  def add_item(self, title, price, quantity=1):
    for _ in range(quantity):
      self.items.append(title)

    self.total += price * quantity

    self.transac_hist["items"] = [title] * quantity
    self.transac_hist["amount"] = price * quantity


  def apply_discount(self):
    if self.discount > 0 or self.total > 0:
      discount_amt = self.total * (self.discount / 100)
      self.total = self.total - discount_amt
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")


  def void_last_transaction(self):
    if self.transac_hist["items"]:
      for item in self.transac_hist["items"]:
        self.items.remove(item)
      self.total -= self.transac_hist["amount"]

      self.transac_hist = {"items": [], "amount": 0}
    else:
      self.total = 0.0
    