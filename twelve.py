print("Enter a,b and c of quadratic equation")  
a,b,c = int(input()),int(input()),int(input())

d = b**2-4*a*c     # Question no :- 8
if d>0:
    print("roots are real and distinct")
elif d==0:
    print("roots are real and equall")
else:
    print("roots are imaginary")
print()