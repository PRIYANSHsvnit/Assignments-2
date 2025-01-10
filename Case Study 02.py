# Codedocs Admin Kidnap

T = int(input("Enter total number of Test cases = "))

N = int(input("Enter number of Boxes = "))

X = int(input("Enter the Xth box Number = "))

S = int(input("Enter number of Swaps = "))

i = 0

while i < T:
    for i in range(S):

        A=int(input("Enter A = "))
        B=int(input("Enter B = "))

        if (B == X) :
            temp=A
            A=X
            X=temp

        elif (A==X) :
            temp=B
            B=X
            X=temp

i+=1

print(X)