name= input("Enter your name: ")
amount= float(input("Enter your money amount:"))
price= 9.52
Nisab= price*595
Zakat= 0.0
if(amount>=Nisab):
 Zakat=round(amount*0.025,3)
print(f"As-salamu alaykum {name}, with a Nisab threshold of: {Nisab} Riyals, your Zakat due is:")
print(f"{Zakat} Saudi Riyals")
num_accounts = int(input("How many bank accounts do you have? "))
total_balance = 0.0
for i in range(1, num_accounts + 1):
    balance = float(input(f"Enter balance for bank account {i}: "))
    total_balance += balance



