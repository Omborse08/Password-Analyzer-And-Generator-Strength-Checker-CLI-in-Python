import string
import random

def line():
    print("-"*50)

def totals(total):
    if total > 80:
        print("\n🔐 Security Level: 🟢Best ")
    elif total > 60:
        print("\n🔐 Security Level: 🟡Intermediate ")
    elif total > 40:
        print("\n🔐 Security Level: 🟠Easy ")
    else:
        print("\n🔐 Security Level: 🔴Weakest  ")


Accounts = {}
CommonPattern = ["123","12345","abc","111","000","password","qwerty","123456789"]
while True:
    print("""
\n1. Analyze a Password  
2. Generate Strong Password  
3. View Report  
4. Exit
""")
    choose_option = input("Choose Option: ")
    match choose_option:
        case "1":
            password = input("\n> Enter Password to analyze: ")
            print("\n🔍 Analyzing Password...")
            
            len1 = False
            if len(password) >= 8:
                print(f" ✔ Length: {len(password)} characters ✅")
                len1 = True
            else:
                print(f"❌Length: {len(password)} characters ❌")

            lower = False
            for i in password:                
                if i.islower() == True:
                    lower = True
            if (lower) == True:
                print(" ✔ Contains lowercase ✅")
            else:
                print("❌ Contains lowercase ❌")

            upper = False
            for j in password:
                if j.isupper() == True:
                    upper = True
            if (upper) == True:
                print(" ✔ Contains Uppercase ✅")
            else:
                print("❌ Contains Uppercase ❌")
            
            digit = False
            for k in password:
                if k.isdigit() == True:
                    digit = True
            if (digit) == True:
                print(" ✔ Contains Digit ✅")
            else:
                print("❌ Contains Digit ❌")
            
            symbol = False
            for l in password:
                if l in string.punctuation:
                    symbol = True
            if (symbol) == True:
                print(" ✔ Contains Symbol ✅")
            else:
                print("❌ Contains Symbol ❌")

            pattern = False
            if any(pattern in password.lower() for pattern in CommonPattern):
                  print("❌ Common pattern detected ❌")
            else:
                print("✔ No Common pattern ✅")
                pattern = True
            
            line()
            input("> Check Your Password Score! ")
            total1 = 0
            print("\n🔢 Score Breakdown:")
            if len1 == True:
                print("+20 ✅ Perfect Lenght ")
                total1 += 20
            else:
                print("-20 ❌ Small Lenght ")
            if lower == True:
                print("+10 ✅ Lowercase ")
                total1 += 10
            else:
                print("-10 ❌ Lowercase ")
            if upper == True:
                print("+10 ✅ Uppercase ")
                total1 += 10
            else:
                print("-10 ❌ Uppercase ")
            if digit == True:
                print("+20 ✅ Digits ")
                total1 += 20
            else:
                print("-20 ❌ Digits ")
            if symbol == True:
                print("+20 ✅ Symbol ")
                total1 += 20
            else:
                print("-20 ❌ No Symbol ")
            if pattern == True:
                print("+20 ✅ No Pattern Detected ")
                total1 += 20
            else:
                print("-20 ❌ Pattern Detected") 
            line()
            input("> Check Your Password Final Strength! ")
            print(f"📊 Final Strength Score: {total1}/100")
            totals(total1)
            
            line()
            print("\n> Password Saved To Report Log! ")
            input("> Press any key to continue! ")
            passwords = {
                password:total1
            }
            Accounts.update(passwords)
        
        case "2":
            length = int(input("\n> Enter desired password length: "))
            password = str()
            randomness = string.ascii_letters + string.digits + string.punctuation        
            for i in range(length):
                genrated = random.choice(randomness)
                password += genrated
            print("\n✅ Your Generated Password is:", password)
            print("\n✅ Tip: saved this password! ")
        
        case "3":
            print("\nPassword Analysis Report ")
            line()
            for u in Accounts.items():
                print(f"\n✅ > Password: {u[0]}")
                print(f"✅ > Strenght: {u[1]}")
            line()

        case "4":
            print("Thank You For Using Password Analyzer! ")
            break