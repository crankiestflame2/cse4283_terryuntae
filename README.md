# cse4283_terryuntae
This application provides users with a list of functions that they can execute which are: bmi, classification, &amp; retirement. bmi calculates a persons Body Mass Index and classification returns their level. Retirement calculates the age in which a goal will be met that pertains to annual salary and percentage saved over time.

**Introduction:**
This application was built with using Windows 10 machine and Python version 3.8.4 extension through Visual Studio Code. Python can be downloaded from its home site at https://www.python.org/downloads/ . To set up the application download the repository at https://github.com/crankiestflame2/cse4283_terryuntae and run the program from the command line or through a coding editor using the command “python as2.py”.

**BMI Function:**
This function utilizes the information given by the user to calculate their Body Mass Index. It begins by multiplying the weight in pounds by 0.45 to convert it to kilograms. The next step takes the converted inches from the main function and multiplies it by 0.025 to obtain meters. It then squares the meters so that it can form the final operation which is to divide kg by m_sq (meters squared). Finally, it rounds the result to 1 decimal place and shows it to the user before sending it to the classification function to receive a level of underweight, normal, overweight, or obese.

Unittest was used to test this function in python. The test was created with a composition of data provided at http://extoxnet.orst.edu/faqs/dietcancer/web2/twohowto.html . This data calculated the BMI of a person with a height of 5’3” and a weight of 125 lbs. The unit test uses the converted inches of this height 63” and the weight to reach a result of “22.7”. The formulas provided where used to compare the accuracy of the function.

**Retirement Function:**
This function calculates the age in which a savings goal will be met based on annual salary, percent saved and current age. For this scenario, the employer matches 35% of savings as well. It begins by calculating savings per year and the following formula is used: (salary * %saved) * 1.35. The next calculation is the years to goal and its formula is: Гsavings goal / savings per yearႨ. Finally, it sums up the current age with the number of years to goal. The function prints the results to the user after all calculations are complete.

Unittest was used to test this function in python. The test was created based on the example scenario of a user that has an annual salary of 100,000, a 0.15% savings, a savings goal of 500,000, and is 45 years old.
