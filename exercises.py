# Exercise 0: Example -------------------------------

def print_greeting():
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# print_greeting()


# Exercise 1: Vowel or Consonant -----------------------

def check_letter():
    vowels = ["a", "e", "i", "o", "u"]
    
    letter = input("Enter a letter a - z: ").lower()
    
    if letter.isalpha():
        if letter in vowels:
            print(f'The letter {letter} is a vowel.')
        else:
            print(f'The letter {letter} is a consonant')
    else:
        print("input non-alphabetical")
        return check_letter()

# check_letter()

# Exercise 2: Old enough to vote? -------------------------

def check_voting_eligibility():
    
    age = input("Please enter your age:  ")
    voting_age = 18
    
    try:
        int_age = int(age)
        if int_age > 0 and int_age < voting_age :
            age_diff = voting_age - int_age
            print(f"I'm sorry at {int_age} years old, you still have {age_diff} years till you can vote.")

        elif int_age >= voting_age:
            print(f"Congratulations at {int_age} years old you can vote!")
            
        else:
            print("Please enter a postive age")
            return check_voting_eligibility()
    except ValueError:
        print("Invaild input: Please enter in a number")
        return check_voting_eligibility()
        
# check_voting_eligibility()

# Exercise 3: Calculate Dog Years -------------------------

def calculate_dog_years():
    
    dog_age = input("Input a dog's age: ")
    
    try:
        num = int(dog_age)
        
        if num <= 2 and num > 0:
            dog_years = num*10
            print(f"The dog's age in dog years is {dog_years}.")
        elif num > 2:
            dog_years = 20 + ((num - 2)* 7)
            print(f"The dog's age in dog years is {dog_years}.")
        else:
            print("Please enter a postive age")
            return calculate_dog_years()
    except ValueError:
        print("Invaild input: Please enter in a number")
        return calculate_dog_years()
        
# calculate_dog_years()

# Exercise 4: Weather Advice -------------------------

def weather_advice():
    # promt the user to enter if it is cold
    is_cold = input("Is the weather cold outside? yes/no:  ").lower()
    
    # promt the user if its raining
    is_raining = input("Is it raining outside? yes/no:  ").lower()
    
    if is_cold == "yes" and is_raining == "yes":
        print("Wear a waterproof coat.")
    elif is_cold == 'yes' and is_raining == "no":
        print("Wear a warm coat.")
    elif is_cold == 'no' and is_raining == "yes":
        print("Carry an umbrella.")
    elif is_cold == 'no' and is_raining == "no":
        print("Wear light clothing.")
    else:
        print("Please answer with yes or no")
        return weather_advice()
        
# weather_advice()

# Exercise 5: What's the Season? -------------------------

def determine_season():
    
    month_list = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep' ,'oct', 'nov', 'dec']
    
    month = input("Enter the month of the year (Jan - Dec): ").lower()

    if month in month_list:
        
        day = input("Enter the day of the month: ")
        
        try:
            num_day = int(day)
            
            if num_day <= 0:
                print("Please enter a postive date")
                return determine_season()
            
            season = None
            
            if month == "jan" and num_day <= 31 :
                season = "Winter"
            elif month == 'feb' and num_day <= 28:
                season = "Winter"
            elif month == "mar":
                if num_day <= 19:
                    season = "Winter"
                elif num_day <= 31:
                    season = "Spring"
            elif month == "apr" and num_day <= 30:
                season = 'Spring'
            elif month == "may" and num_day <= 31:
                season = "Spring"
            elif month == 'jun':
                if num_day <= 20:
                    season = "Spring"
                elif num_day <= 30:
                    season = "Summer"
            elif month == "jul" or month == 'aug' and num_day <= 31:
                season = "Summer"
            elif month == "sep":
                if num_day <= 21:
                    season = "Summer"
                elif num_day <= 30:
                    season = "Fall"
            elif month == 'oct' and num_day <= 31:
                season = "Fall"
            elif month == 'nov' and num_day <= 30:
                season = "Fall"
            elif month == 'dec':
                if num_day <= 20:
                    season = "Fall"
                elif num_day <= 31:
                    season = "Winter"
            
            if season in ("Winter", "Spring", "Summer", "Fall"):
                print(f"{month.capitalize()} {num_day} is in {season}.")
            else:
                print(f"{month.capitalize()} {num_day} does not exist")
                return determine_season()

        except ValueError:
            print("Invaild input: Please enter in a number")
            return determine_season()
    else:
        print("Please enter a month as three letter characters such as jan")
        return determine_season()
        

# determine_season()

# Exercise 6: Number Guessing Game

def guess_number():
    
    target = 74
    
    guess = input("Guess a number within a range of 1 to 100: ")
    
    try:
        guess_num = int(guess)
        
        if guess_num < 1 or guess_num > 100:
            print("Invalid input: please enter a number between 1 and 100")
            return guess_number()
        
        for guesses in range(5):
            
            print(f"This is guess number {guesses + 1}, you have 5 tries")
            
            if guess_num == target:
                print("Congratulations, you guessed correctly!")
            elif guess_num < target: 
                print("Guess is too low")
            elif guess_num > target: 
                print("Guess is too high.")
                
            if guesses == 5 and guess_num != target:
                print("Sorry, you failed to guess the number in five attempts.")
    
    except ValueError:
            print("Invaild input: Please enter in a number")
            return guess_number()
    

        
guess_number()