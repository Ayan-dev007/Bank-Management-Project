import json
import random
import string
from pathlib import Path

class Bank:
    database='data.json'
    data=[]
    try:
        if Path(database).exists():
            with open(database) as fs:
                data=json.loads(fs.read())
        else:
            print("No such file exists")
    except Exception as err:
        print(f"an exception occured as {err}")
    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))
    @classmethod
    def __accountgenerate(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3)
        id=alpha+num
        random.shuffle(id)
        return"".join(id)
        
    def Createaccount(self):
        info={
            "name":input("Tell your name"),
            "age":int(input("Tell your age")),
            "email":input("Tell your email"),
            "pin":int(input("Tell your 4 number pin")),
            "Account No." : Bank.__accountgenerate(),
            "balance" : 0
            }
        if info['age']<18 or len(str(info['pin'])) !=4:
            print("Sorry You don't create bank account")
        else:
            print("Your account is successfully created")
            for i in info:
                print(f"{i} :{info[i]}")
            print("please note down your account detail properly")
        Bank.data.append(info)
        Bank.__update()
    def depositmoney(self):
        AccNumber=input("plz tell your account number")
        pin=int(input("Plz tell your pin"))
        userdata=[i for i in Bank.data if i['Account No.']==AccNumber and i['pin']==pin]
        if userdata==False:
            print("Sorry no account found")
        else:
            amount=int(input("How much you want to deposit"))
            if amount>10000 or amount<0:
                print("The amount is too high you can deposit below 10000 and above 0")
            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount depositted sucessfully")
    def withdrawmoney(self):
        Accnumber=input("Plz tell your acc number")
        pin=int(input("Plz tell your pin code"))
        userdata=[i for i in Bank.data if i['Account No.']==Accnumber and i['pin']==pin]
        if  userdata == False:
            print("Sorry no account found")
        else:
            amount=int(input("How much you want to withdraw"))
            if userdata[0]['balance'] < amount:
                print("Sorry you couldn't have that much money")
            else:
                userdata[0]['balance'] -=amount
                Bank.__update()
                print("Amount withdrew sucessfully")
    def showdetails(self):
        AccNumber=input("Tell your acc number")
        pin=int(input("Tell your pin code"))
        userdata=[i for i in Bank.data if i['Account No.']==AccNumber and i['pin']==pin]
        print("Your information are\n\n")
        for i in userdata[0]:
            print(f"{i}:{userdata[0][i]}")
    def updatedetails(self):
        AccNumber=input("Tell your acc number")
        pin=int(input("Tell your pin aswell"))
        userdata=[i for i in Bank.data if i['Account No.']==AccNumber and i['pin']==pin]
        if userdata==False:
            print("No such result found")
        else:
            print("you can't change the age, account number, balance")
            print("Fill the details for change or leave it empty if no change")
            newdata={
                "name":input("plz tell your new name or press Enter"),
                "email":input("Tell your new email or Press Enter to skip"),
                "pin":input("Tell your new pin or Press Enter to skip"),
            }
            if newdata["name"]=="":
                newdata["name"]=userdata[0]['name']
            if newdata["email"]=="":
                newdata["email"]=userdata[0]['email']
            if newdata["pin"]=="":
                newdata["pin"]=userdata[0]['pin']
            newdata['age']=userdata[0]['age']
            newdata['Account No.']=userdata[0]['Account No.']
            newdata['balance']=userdata[0]['balance']
            if type[newdata['pin']]==str:
                newdata['pin']==int(newdata['pin'])
            for i in newdata:
                if newdata[i]==userdata[0][i]:
                    continue
                else:
                    userdata[0][i]=newdata[i]
            Bank.__update()
            print("Your Details updated sucessfully")
    def delete(self):
        AccNumber=input("Tell your acc number")
        pin=int(input("Tell your pin code"))
        userdata=[i for i in Bank.data if i['Account No.']==AccNumber and i['pin']==pin]
        if userdata==False:
            print("No such account exist")
        else:
            check=input("press y if you actually want to delete or press n")
            if check=="n" or check=="N":
                print("Bypassed")
            else:
                index=Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Your account deleted sucessfully")
                Bank.__update()
user=Bank()

print("press 1 for creating an account")
print("press 2 for depositing the money to the bank")
print("press 3 for withdrawing the money")
print("press 4 for the details")
print("press 5 for updating the details")
print("press 6 for deleting the account")
check=int(input("Tell your response"))
if check==1:
    user.Createaccount()
if check==2:
    user.depositmoney()
if check==3:
    user.withdrawmoney()
if check==4:
    user.showdetails()
if check==5:
    user.updatedetails()
if check==6:
    user.delete()