class Category:
  withdrawn = 0
  balance = 0
  def __init__(self, name):
    self.name = name
    self.ledger = list()

  def __str__(self):
    max_char = 30
    stars = "*"
    s = (max_char - len(self.name)) // 2
    stars *= s
    object_display = f"{stars}{self.name}{stars}\n"

    for item in self.ledger:
      """Displays the activities added to the ledger and the total balance"""
      words = item["description"]
      if len(words) > 23:
        words = words[0:23]
      num = item["amount"]
      num = format(num, ".2f")
      add_space = max_char - (len(words) + len(num))
      object_display += words + " " * add_space + num + "\n"

    object_display += f"Total: {self.balance}"
    return object_display
      
  
  def get_balance(self):
    """Checks the current balance"""
    balance = self.balance
    return balance

  def check_funds(self, amount):
    """Checks amount against current balance"""
    if self.get_balance() >= amount:
      return True 
    else:
      return False
    
  def deposit(self, amount, description=""):
    """Takes in an amount and description and adds to ledger list"""
    deposit = dict()
    deposit["amount"] = amount
    deposit["description"] = description
    self.ledger.append(deposit)
    self.balance += amount
    
  def withdraw(self, amount, description=""):
    """If enough funds are available, adds amount and description to ledger list, updates balance and withdraw total"""
    withdraw = dict()
    if self.check_funds(amount) is True:
      withdraw["amount"] = -amount
      withdraw["description"] = description
      self.ledger.append(withdraw)
      self.balance -= amount
      self.withdrawn += amount
      return True
    else:
      return False

  def transfer(self, amount, other):
    """Checks funds against amount and if true withdraws amount from one category and deposits it into another"""
    if self.check_funds(amount) is True:
      self.withdraw(amount, description = "Transfer to " + other.name)
      other.deposit(amount, description = "Transfer from " + self.name)
      return True
    else:
      return False

  
def create_spend_chart(categories):
  """Combines the withdraw total of each category and returns a chart of percentage spent compared to that total"""
  names = list()
  percent_spent = list()
  withdraws = list()
  withdraw_total = 0
  for name in categories:
    names.append(name.name)
    w = name.withdrawn
    withdraws.append(w)
    withdraw_total += w
  for wd in withdraws:
    wd = int(wd)
    percent = wd * 100 / withdraw_total
    percent = round(percent // 10) * 10
    percent_spent.append(percent)
     
  chart = f"Percentage spent by category\n"
  count = 100
  line = ""

  while count > 1:
    if count == 100:
      line = "100|"
    else:
      line = f" {count}|"
    for p in percent_spent:
      if p >= count:
        line += " o "
      else:
        line += "   "
    chart += f"{line} \n"
    count -= 10
  chart += "  0| o  o  o  \n"
  chart += "    " + "-" * 10 + "\n"

  largest = max(names, key=len)
  largest = len(largest)
  new = ""
  i = 0

  while i < largest:
    letter_count = 0
    line = "    "
    for word in names:
      word = word.capitalize()
      letters = " "
      try:
        letters += word[i]
      except IndexError:
        letters += " "
      letters += " "
      line += letters
      letter_count += 1
      if letter_count % 3 == 0:
        if i == largest - 1:
          line += " " 
        else:
          line += " \n"
        new += line
    i += 1
  chart += new  
  
  return chart
    
  
  
