#Basic steps up to account number generation

# import random
# #creating a bank app
# #create the class user to get all the information of a user
# class User() :

#     def __init__ (self, name, age, email, phone) :

#         self.name = name
#         self.age = age
#         self.email = email
#         self.phone = phone


# #create a child class account and make it inherit from user. that way you have all the information need and not repeat yourself
# class Account(User) :

#     # balance = 0 #we could incapsulate account balance so that it is not accessible but lets leave that for now 
#     # account_no = ""

#     def __init__(self, name, age, email, phone) :
        
#         super().__init__(name, age, email, phone) #initialising attribute from parent class

#         self.balance = 0 #we could incapsulate account balance so that it is not accessible but lets leave that for now 
#         self.account_no = self.generate_account_number()

#     def generate_account_number(self) :

#         account_num = random.randint(3000000000, 3999999999)

#         return str(account_num)


# x = Account('Kelly', 19, 'kabelorji@gmail.com', '08026161769')
# print(x.account_no)





# import random
# #creating a bank app
# #create the class user to get all the information of a user
# class User() :

#     def __init__ (self, name, age, email, phone) :

#         self.name = name
#         self.age = age
#         self.email = email
#         self.phone = phone


# #create a child class account and make it inherit from user. that way you have all the information need and not repeat yourself
# class Account(User) :

#     # balance = 0 #we could incapsulate account balance so that it is not accessible but lets leave that for now 
#     # account_no = ""

#     def __init__(self, name, age, email, phone) :
        
#         super().__init__(name, age, email, phone) #initialising attribute from parent class

#         self.balance = 0 #we could incapsulate account balance so that it is not accessible but lets leave that for now 
#         self.account_no = self.generate_account_number()

#     def generate_account_number(self) :

#         account_num = random.randint(3000000000, 3999999999)

#         return str(account_num)

#     def deposit(self,amount, comment = '') :

#         self.balance += amount #add deposit amount value to the balance
#         self.store_history('credit', amount, comment)


#         print(f'welldone {self.name}, your deposit of #{amount} was sucessfull. Your new balance is #{self.balance}')

#     def withdrawal(self,amount, comment = '') :

#         self.balance -= amount #subtract withdrawal amount value to the balance
#         self.store_history('debit', amount, comment)

#         print(f'welldone {self.name}, your withdrawal of #{amount} was sucessfull. Your new balance is #{self.balance}')


#     def transfer(self, amount, recipient, comment = '') :

#             self.balance -= amount #remove transfer amount from sender's balance
#             recipient.balance += amount #add transfer amount to recipient's balance

#             self.store_history('transfer', amount, comment, recipient.name)

#             print(f'congratulations {self.name}, your transfer of #{amount} to {recipient.name} was sucessfull. Your new balance is #{self.balance}')

#     def store_history(self, type, amount, comment, receiver = 'same as sender') :
#         file = open(f'inancial_statement.csv', 'a')
#         file.write(f'{type}, {self.name}, {amount}, {comment}, {receiver} \n')
#         print(type, amount, comment, receiver)


# kelly = Account('Kelly', 19, 'kabelorji@gmail.com', '08026161769')
# print(kelly.account_no)
# kelly.deposit(20000)
# kelly.withdrawal(2000)


# moon = Account('Moon', 29, 'moonpapigmail.com', '08038776789')
# kelly.transfer(3000, moon, 'icecream')










# making changes to transaction process of deposit and withdrawal instead of recalling 


import random
#creating a bank app
#create the class user to get all the information of a user
class User() :

    def __init__ (self, name, age, email, phone) :

        self.name = name
        self.age = age
        self.email = email
        self.phone = phone


#create a child class account and make it inherit from user. that way you have all the information need and not repeat yourself
class Account(User) :

    # balance = 0 #we could incapsulate account balance so that it is not accessible but lets leave that for now 
    # account_no = ""

    def __init__(self, name, age, email, phone) :
        
        super().__init__(name, age, email, phone) #initialising attribute from parent class

        self.balance = 0 #we could incapsulate account balance so that it is not accessible but lets leave that for now 
        self.account_no = self.generate_account_number()

    def generate_account_number(self) :

        account_num = random.randint(3000000000, 3999999999)

        return str(account_num)
        
    def deposit(self,amount, comment = '') :

        self.balance += amount #add deposit amount value to the balance
        self.store_history('credit', amount, comment)


        print(f'welldone {self.name}, your deposit of #{amount} was sucessfull. Your new balance is #{self.balance}')

    def withdrawal(self,amount, comment = '') :

        self.balance -= amount #subtract withdrawal amount value to the balance
        self.store_history('debit', amount, comment)

        print(f'welldone {self.name}, your withdrawal of #{amount} was sucessfull. Your new balance is #{self.balance}')


    def transfer(self, amount, recipient, comment = '') :

            self.balance -= amount #remove transfer amount from sender's balance
            recipient.balance += amount #add transfer amount to recipient's balance

            self.store_history('transfer', amount, comment, recipient.name)

            print(f'congratulations {self.name}, your transfer of #{amount} to {recipient.name} was sucessfull. Your new balance is #{self.balance}')

    def store_history(self, type, amount, comment, receiver = 'same as sender') :
        file = open(f'inancial_statement.csv', 'a')
        file.write(f'{type}, {self.name}, {amount}, {comment}, {receiver} \n')
        print(type, amount, comment, receiver)


kelly = Account('Kelly', 19, 'kabelorji@gmail.com', '08026161769')
print(kelly.account_no)
kelly.deposit(20000)
kelly.withdrawal(2000)


moon = Account('Moon', 29, 'moonpapigmail.com', '08038776789')
kelly.transfer(3000, moon, 'icecream')
