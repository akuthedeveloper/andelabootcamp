Class m-bongo-cash():
    def deposit_to_m-bongocash()
        pass

Class m-bongo-cash():
    def_init_(self):
        self.initial_amount=500
    def deposit_to_mbongocash(self, deposit):
        if amount(deposit)== int and deposit!=""
        if deposit >=0
        self.balance += deposit
        return self.balance
    else:
        return 'Invalid Amount'
    else:
        raise ValueError()
        def withdraw(self,amount):
    if type(amount) == int and amount != "":
      if amount > 0:
        if (self.balance-amount) > 0:
          if (self.balance -amount) > 1000:
            self.balance-=amount
            return self.balance
          else:
            return 'Insufficient funds in Account'
        else:
          return 'Enter Amount below Actual balance'
      else:
        return 'Invalid Amount'
    else:
      raise ValueError()

class CurrentAccount(m-bongo-cash):
  def __init__(self):
    self.balance = 0


  def deposit_to_mbongocash(self,deposit):
    if type(deposit) == int and deposit !="":
      if deposit >= 0:
        self.balance += deposit
        return self.balance

      else:
        return 'Invalid deposit amount'

    else:
      raise ValueError()

  def withdraw_from_mbongocash(self,amount):
    if type(amount) ==  int and amount != "":
      if amount > 0:
        if (self.balance-amount) > 0:

          self.balance-=amount
          return self.balance

        else:
          return 'Enter Amount below Actual balance'
      else:
        return 'Invalid withdraw amount'
      else:
        raise ValueError()
