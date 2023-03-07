class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        
        self.is_reward_member = False
        self.gold_card_points = 0
        
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_reward_member)
        print(self.gold_card_points)
        
        return self
        
    def enroll(self):
        self.is_reward_member = True
        self.gold_card_points = 200
        
        return self
    
        if self.is_reward_member == True:
            print(f"User {self.first_name} is already a member.")
            return False
        else:
            return True
        
    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
            print(f"You just spent {amount} points. Your balance is now {self.gold_card_points}.")
        else:
            print(f"Your balance is {self.gold_card_points} points. You don't have enough to spend {amount} points.")
            
        return self
        
User1 = User("Henry", "Chen", "henrychen14505@gmail.com", 39)
User2 = User("Ellie", "Chen", "elliekipenzi@gmail.com", 5)

# User1.display_info()
# print("=====")
# User2.display_info()

# User1.enroll()
# User1.spend_points(50)
# print("=====")
# User2.enroll()
# User2.spend_points(80)

User1.display_info().enroll().spend_points(50).display_info()
print("=====")
User2.display_info().enroll().spend_points(80).display_info()