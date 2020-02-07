# splash screen
print("  Greetings, Robot!")
print("     ,     ,")
print("    (\\____/)")
print("     (_oo_)")
print("       (O)")
print("     __||__    \\)")
print("  []/______\\[] /")
print("  / \\______/ \\/")
print(" /    /__\\\n(\\   /____\\)")
print("Welcome to the Robot Chop Shop!")

# splash screen
print("Please enter your name:")
name = input()
print("Hello " + name + ", it is a pleasure to meet you!")

# Process the Robots requests
print("Please enter the number of arms you would like to order:")
num_arms = input()
cost_arms = int(num_arms) * 200
print("Please enter the number of legs you would like to order:")
num_legs = input()
cost_legs = int(num_legs) * 100
print("Please enter the number of hands you would like to order:")
num_hands = input()
cost_hands = int(num_hands) * 700
print("Please enter the number of feet you would like to order:")
num_feet = input()
cost_feet = int(num_feet) * 500
print("Robot Arm  \t" + num_arms + "\tB" + str(cost_arms) + ".00")
print("Robot Leg  \t" + num_legs + "\tB" + str(cost_legs) + ".00")
print("Robot Hand \t" + num_hands + "\tB" + str(cost_hands) + ".00")
print("Robot Foot \t" + num_feet + "\tB" + str(cost_feet) + ".00")
sub_total = (cost_hands + cost_feet + cost_legs + cost_arms)
print("Sub total : " + (str(cost_hands + cost_feet + cost_legs + cost_arms)) + ".00")

# Read in the tax rate and compute the total
print("Please enter the tax rate as a percent:")
tax_rate = (float(input()))
print("Tax Rate: " + (str(tax_rate)) + "%")
total_tax = tax_rate * sub_total / 100.0
print("Total Tax: B" + (str(total_tax)) + "%")
total = sub_total + total_tax
print("Total: B" + str(total))

# Read in amount paid and compute change
print("Please input amount paid:")
amount_paid = int(input())
print("Amount Paid : B" + str(amount_paid) + ".00")
print("Total Change: B" + (str(amount_paid - total)))
print("Have a nice day and visit The Robot Chop Shop Again, " + name + "!")