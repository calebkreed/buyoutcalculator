from dateutil import parser
from dateutil.relativedelta import relativedelta
import os 
global months

#Equipment script
def get_equipment_cost():
  has_equipment = input("Equipment? (y/n) > ")
  print("")
  if has_equipment.lower() == 'y':
    equip_monthly = float(input("Enter monthly equipment cost: "))
    return equip_monthly * months
  else: 
    return 0

#Discount script
def get_discount():
  percent_str = input("What is the discount percent? > ")
  percent = int(percent_str) / 100
  return percent

def program():
  global months
  date1 = input("Date with previous provider (MM/DD/YYYY): ")  
  date2 = input("Date with Vivint (MM/DD/YYYY): ")

  date1 = parser.parse(date1)
  date2 = parser.parse(date2)
  global months
  
  rd = relativedelta(date2, date1)
  months = rd.years * 12 + rd.months

  rd = relativedelta(date2, date1)
  day_diff = rd.days
  
  print("")
  print(f"There are {months} months between {date1:%m/%d/%Y} and {date2:%m/%d/%Y}")
  print("")
  monthdif = int(input("How many months long is the customers contract > "))
  trumonth = monthdif-months
  if 0 <= day_diff <= 3:
    print("\nThe difference between the dates is less than 3 days. The extra month will be calculated automatically.")
    print(f"\nThe payoff period has increased from the initial {trumonth} months to {trumonth + 1} months after applying the 3-day rule")
    trumonth = trumonth + 1
  else:
    print("\nThree day rule does not apply")
    print(f"\nThere are {trumonth} months left for the customer to pay")

  rmr = float(input("\nWhat is the monthly rate? > "))

  discount = input("\nDiscount? (y/n) > ")
  equip_cost = get_equipment_cost()
  
  if discount == 'y':
    percent = get_discount() 
    total = (rmr * trumonth * percent) + equip_cost
  else:
    total = (rmr * trumonth) + equip_cost
  total = round(total, 2)
  print("")
  print(f"The total buyout is ${total}")

program()

while True:
  print("")
  again = input("Run calculation again? (y/n): ")
  if again.lower() == 'y':
    print("")  
    os.system('cls' if os.name == 'nt' else 'clear')
    program() 
  else:
    break

print("Done")
