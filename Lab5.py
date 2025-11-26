#Write a program that asks the user to enter five test scores. 
#The program should display a letter grade for each score and the average test score. 
#Write the following functions in the program: calc_average.
#This function should accept five test scores as arguments and return the average of the scores.
#determine_grade. This function should accept a test score as an argument and
#return a letter grade for the score based on the following grading scale:

def main():
    score1 = float(input("Score 1: "))
    score2 = float(input("Score 2: "))
    score3 = float(input("Score 3: "))
    score4 = float(input("Score 4: "))
    score5 = float(input("Score 5: "))
    return [score1, score2, score3, score4, score5]

def determine_grade(num):
    if 90 <= num <= 100:
        letter_grade = "A"
    elif 80 <= num <= 89:
        letter_grade = "B"
    elif 70 <= num <= 79:
        letter_grade = "C"
    elif 60 <= num <= 69:
        letter_grade = "D"
    else:
        letter_grade = "F"
    return letter_grade

def cal_average(grades):
    average = sum(grades) / len(grades)
    grade = determine_grade(average)
    print("Average Score: \t {:.1f}  \t\t\t {}".format(average, grade))

def show_letters(num, letter_grade):
    print("Score: \t\t {:.1f} \t\t\t {}".format(num, letter_grade))

list = main()
print("\nScore \t\t Numeric Grade \t\t Letter Grade")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
for z in list:
    show_letters(z, determine_grade(z))
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
cal_average(list)
