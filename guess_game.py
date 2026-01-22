n=34
count=0
y=int(input("Guess the number: "))
while n!=y:
    if y>n:
        print("TOO HIGH")
    elif y<n:
        print("TOO LOW")

    count+=1
    print("Your attempt no is: ",count)
    y=int(input("Guess the number again: "))

print("You guessed correctly!!!")
print("Total number of attempts is: ",count)