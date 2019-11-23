
try:
    t1 = {"Sachin": "icc",
         "Saurav": "BCCI",
         "Rahul": "Coach",
         "Virat": "Captian"
         }
    user = input("Enter the user")
    password = input("Enter the password")
    if user not in t1:
        raise Exception("Invalid Username")
    elif password != t1[user]:
        raise Exception("Password Incorrect")
    else:
        print("Welcome " + user)
except Exception as e:
    print(e)

