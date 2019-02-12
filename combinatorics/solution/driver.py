'''
Question:

I am creating my budget for the next month. Besides regular spending, I also added a list of extra items I want to buy.
I added my budget amount and realized that it has exceeded my planned spending amount, so I want to eliminate some items
in order to cut down my budget.

You are a developer at Mint. In order to help me manage my personal finance better, you are giving me suggestions of what
items I should remove from my budget. What you are given is:

1.	A list of extra items I want to buy. Each item has a name and an amount. (Ex. Name: “Backpack”, amount: 50.00).
    There are no duplicate items.
2.	My current total budget amount for next month: n dollars.
3.	My target total budget amount for next month: m dollars. (m < n)

Ex. - Name: “Backpack”, amount: $55.00
      - Name: “Monitor”, amount: $100.00
      - Name: “Water bottle”, amount: $10.00
      - Name: “Tent”, amount: $150.00
      - Name: “Headphone”, amount: $123.00

      current total budget: $1200.00
      target total budget: $1000.00

      returning pair: “Backpack”, “Tent”

If I only want to remove 2 items to lower my budget to target budget, is it possible? If so, which 2 items should I remove?

'''

from classes.suggestion import *

number=input("How many combinations(1,2,3,etc)? ")

dict1 = {55: 'item1', 100: 'item2', 10: 'item3', 150: 'item4', 123: 'item5'}

c = Suggestion(1200, 1000, dict1)

cnt = 0
print "Remove one of the following groups of items to meet target budget"
for m in c.suggestion(number):
    cnt += 1
    print "Suggestion Group {}".format(cnt)
    for i in m:
        print("Name: {} Value {}").format(i.Name, i.Value)
