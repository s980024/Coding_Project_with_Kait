#Importing pandas library
import pandas as pd 

class Fish:

    def __init__(self):
        #importing the animal crossing fish data set 
        self.fish = pd.read_csv("fish.csv")

    #this method performs basic functions to inspect the dataset
    def clean(self):
        #prints the first 5 rows in the dataset
        print(self.fish.head())
        #prints the names of the columns of the dataset
        print(self.fish.columns)
        #prints a quick descriptive summary of the dataset
        print(self.fish.describe())
    
    #this is the method that runs the whole program
    def main_screen(self):
        #this print statement prints the options that the user has
        print("1. Look up the size of a shadow\n2. Look up the selling price of a fish\n3. Look up the level of rarity of a fish")
        #the user ca input the number of the option they choose
        self.user_main_choice = int(input("What would you like to do? "))
        #this series of if statements runs the correct method for the number they choose
        if self.user_main_choice == 1:
            #if the user chooses choice 1, the choice_one method will be run
            self.choice_one()
        elif self.user_main_choice == 2:
        # if the user chooses choice 2, the choice_two method will be run
            self.choice_two()
        elif self.user_main_choice == 3:
            #if the user chooses choice 3, the choice_three method will be run
            self.choice_three()

    #this method lets the user know what fish they could catch based on the size of its shadow
    def choice_one(self):
        #this print statement and for loop just print the different sizes of shadows
        print("\nSizes:")
        for size in self.fish['Shadow'].unique():
            print(f"  {size}")
        #asking the user what size shadow they see
        user_shadow_size = input("\nWhat size shadow do you see? ")
        #the fish_type variable gets the columns "Name" and "Shadow" for the rows where the "Shadow" column value equal what the user types in
        fish_type = self.fish.loc[self.fish["Shadow"] == user_shadow_size, ["Name", "Shadow"]]
        #these print statements print the fish_type variable, which is the fish that have a "Shadow" value that the user typed in
        print("\nHere is the type(s) of fish it could possibly be:")
        print(f"{fish_type} \n")
        #then the program goes back to the main screen, so that the user can choose something else
        self.main_screen()

    #this method tells that user the selling price of the fish the user types in
    def choice_two(self):
        #first, it asks them the name of the fish
        fish = input("What fish did you catch? ")
        #the price variable holds the "Name" and "Sell" columns for the rows where the "Name" column value equals the one the user typed in
        price = self.fish.loc[self.fish["Name"] == fish, ["Name", "Sell"]]
        #then, the price variable is printed to show the user the selling price of their fish
        print(f"{price} \n")
        #the program will then go back to the main screen
        self.main_screen()  
    
    #this method makes a new column that tells the user how rare their fish is (based on the number of catches it takes to unlock the fish)
    def choice_three(self):
        #making a new column (Level of Rarity) that uses the values in the "Total Catches to Unlock" column to give the fish (row) a value of "Common", "Uncommon", "Rare", or "Ultra Rare"
        self.fish['Level of Rarity'] = self.fish['Total Catches to Unlock'].apply(lambda x: "Common" if x == 0 else "Uncommon" if x == 20 else "Rare" if x == 50 else "Ultra Rare")
        #asks the user what fish they want to see the level of rarity of 
        user_fish = input("What fish did you catch? ")
        #the level variable is the "Name" and "Level of Rarity" columns for the rows where the value for "Name" is equal to what the user typed in
        level = self.fish.loc[self.fish["Name"] == user_fish, ["Name", "Level of Rarity"]]
        #prints the level variable
        print(f"{level} \n")
        #goes back to main screen
        self.main_screen()
        
#the data object stores the fish class
data = Fish()
#this runs the clean() method
data.clean()
#this runs the main parts of the program, which are run in the main_screen method
data.main_screen()
