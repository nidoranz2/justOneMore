import random
current = 100.00
try:
    number = input("Please type in the amount of tries: ")
    num = int(number)
except ValueError:
    print("Please input numbers only!\n")
saving = 0.0
for i in range(num):
    if random.choice([0,1]) == 1: #heads
        current = current * 1.8
    else:
        current = current * 0.5
    saving += current * 0.625
    current = current * 0.375
print(f"The Money you would have after playing {num} times is ${saving + current:,.2f}")