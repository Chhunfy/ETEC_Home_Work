#if else if = python we use if elif
# we can use if elif (elif can use many many times) in the end we can end with else
# example: if elif else

# price = float(input("Enter your price: "))
# quantity = int(input("Enter quantity: "))
# total = price * quantity
# if total >= 0 and total < 10:
#     discount = 0
# elif total >= 10 and total < 25:
#     discount = 5
# else:
#     discount = 10
# payment = total - (total * discount / 100)
# print(f"Total = {total}$")
# print(f"Discount = {payment}$")
# print(f"Price after discounted: {discount}%")



print("***Welcome to B Tech Computer Shop***")
print("Our gaming mouse price is:")
print(">>>If 1 to 10unit 5$ each<<<")
one_ten = 5
print(">>>If 11 to 20unit 4.8$ each<<<")
eleven_twenty = 4.8
print(">>>If 21 to 50unit 4.5$ each<<<")
twentyone_fifty = 4.5
print(">>>If 51 to 100unit 3.5$ each<<<")
fiftyone_ahundred = 3.5
print("--------------------------------")

Enter_QTY = int(input("How many do you need: "))
if Enter_QTY >= 0 and Enter_QTY < 10:
    total = one_ten * Enter_QTY
elif Enter_QTY >=10 and Enter_QTY < 20:
    total = eleven_twenty * Enter_QTY
elif Enter_QTY >= 20 and Enter_QTY <= 50:
    total = twentyone_fifty * Enter_QTY
else:
    total = fiftyone_ahundred * Enter_QTY

print("********************************")
Sub_Total = total - (Enter_QTY * total)
print(f"Your order price after discount is: {total}$")
print("--------------------------------")
print("Thank you for your ordered.")
print("Wish you have a good day sir.")