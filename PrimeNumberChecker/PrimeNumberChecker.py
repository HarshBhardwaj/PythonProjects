#Harsh Bhardwaj
#Prime Number Checker
print("Prime Number Checker")

#This function asks the user to enter prime number
def main():
      done = False
      while not done:
            user_prime_num = 101
            user_prime_num = int(input("Enter valid prime number: "))
            isprime(user_prime_num)
            anothertry = input("Do you want to try more? (y/n)")
            if anothertry == 'y' or anothertry == 'Y':
                  done = False
            else:
                  done = True
      
#This function will validate if it's a prime number or not
def isprime(user_prime_num):
      # prime numbers are greater than 1
      if user_prime_num > 1:
            # check for factors
            for i in range(2,user_prime_num):
                  if (user_prime_num % i) == 0:
                        print(user_prime_num,"is not a prime number")
                        print(i,"times",user_prime_num//i,"is",user_prime_num)
                        break
                  else:
                        print(user_prime_num,"is a prime number")
                        break
       # if input number is less than
       # or equal to 1, it is not prime
      else:
             print(user_prime_num,"is not a prime number")
#def usertryagain(done):
 #                 main()
main()
