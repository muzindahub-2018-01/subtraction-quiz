import random
import time

# count the number of the correct answers
correctcount = 0

# count the total number of questions
count = 0

# constant
number_of_questions = 10

# get start
startTime = time.time()

while count < number_of_questions:
     
     #two random integers
     num1 = random.randint(0, 10)
     num2 = random.randint(0, 10)
     
     #answer
     count += 1
     
     ans = int(input("What is {0} - {1} ?".format(num1, num2)))#"what" + str(num1) + "-" + str(num2) + "?")
     
     #display results
     difference = (num1 - num2)
     if (difference == ans):
          print("correct")
          correctcount += 1

     else:
          print("wrong.\n", num1, "-",num2, "is", num1 - num2)

# increase the count
#count += 1

# get end
endTime = time.time()

