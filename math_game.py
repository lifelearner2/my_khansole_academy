import random

def main():
    print("Khansole Academy")
    # TODO: your code here
    
    #Generate two random numbers and prompt user to add them together
    first_random_num=random.randint(10,99)
    second_random_num=random.randint(10,99)
    user_answer = input("What is " + str(first_random_num) + " + "  + str(second_random_num) + "? " )       
    print("Your answer: " + user_answer)
    #This will determine the result of the math problem and assess if the users number matches the expected answer
    check_answer(first_random_num, second_random_num, user_answer)
    
def check_answer(first_random_num, second_random_num, user_answer):
    expected_answer = str(first_random_num + second_random_num)
    if user_answer == expected_answer:
        print("Correct")
    else:
        print("Incorrect." )
        print("The expected answer is " + expected_answer)

if __name__ == '__main__':
    main()