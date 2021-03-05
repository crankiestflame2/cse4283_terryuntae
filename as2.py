#Name: Terryuntae Griffin
#Affiliation: Mississippi State University
#Description: This application  provides users with a list of functions that they can execute which are: 
#             bmi, classification, & retirement. bmi calculates a persons Body Mass Index and classification
#             returns their level. Retirement calculates the age in which a goal will be met that pertains
#             to annual salary and percentage saved over time.
#             I have created an application that allows the user to select and run each function 
#             and receive a correct response from the program.
#Last Date Updated: 3/4/2021
import math

def bmi(inches, pounds):
    #step 1: Multiply the weight in pounds by 0.45 (the metric conversion factor)
    kg = float(pounds) * 0.45
    #print("kg", kg)

    #step 2: Multiply the height in inches by 0.025 (the metric conversion factor)
    meters = float(inches) * 0.025
    #print("meters", meters)

    #step 3: Square the answer from step 2
    m_sq = meters * meters
    #print("m_sq", m_sq)
    
    #step 4: Divide the answer from step 1 by the answer from step 3
    results = kg / m_sq
    results = round(results,1)

    print("You have a BMI of: ", results)

    return results

def classification(results):
    if results < 18.5:
        return 0 #underweight

    elif results >= 18.5 or results <= 24.9:
        return 1 #Normal weight = 18.5–24.9

    elif results == 25 or results <= 29.9:
        return 2 #Overweight = 25–29.9

    if results >= 30:
        return 3 #Obese

def retirement(salary, percent_saved, savings_goal, age):
    savings_per_year = (salary * percent_saved) * 1.35
    print("savings per year: ",savings_per_year)

    years_to_goal = math.ceil(savings_goal / savings_per_year)
    print("years to goal: ", years_to_goal)

    age_goal_met = age + years_to_goal
    print("age to goal met: ", age_goal_met)

    return age_goal_met

def main():
    x = 0
    #introduce user to application
    print("Please read the directions below to select the appropriate function.")
    while(x == 0):
        print("Enter the corresponding number below for you selection")
        print("BMI '1'  |  Retirement '2'  |  Exit '3' ")
        print()

        #recieve user selection
        user_a = int(input("Enter Selection Here: "))

        #BMI selection
        if user_a == 1:
            print("BMI Function Selected")
            print()
            #input from user
            f = int(input("Please enter height in exact feet: "))
            i = int(input("Please enter inches: "))
            inches = (f * 12) + i
            print("inches", inches)
            pounds = input("Please enter weight in pounds: ")

            #push input to bmi function
            results = bmi(inches,pounds)

            #push results to classification function
            level = classification(results)
            
            #determine level of BMI
            if level == 0:
                print("Your BMI shows that you are Underweight")
            elif level == 1:
                print("Your BMI shows that you are Normal")
            elif level == 2:
                print("Your BMI shows that you are Overweight")
            elif level == 3:
                print("Your BMI shows that you are Obese")
            print()

        #Retirement Selection
        elif user_a == 2:
            print("Retirement Function Selected")
            print()
            age = int(input("Please enter age: "))
            salary = int(input("Please enter salary: "))
            percent_saved = float(input("Please enter %* saved: "))
            savings_goal = int(input("Please enter savings goal: "))

            results = retirement(salary, percent_saved, savings_goal, age)
            print()

        #Force Exit Application
        elif user_a == 3:
            print("You have chosen to close the application.")
            print()
            x = 1

main()