# QUESTION 8: W.A.P. TO ACCEPT AVERAGE MARKS OUT OF 100 AND PRINT THE GRADE OF THE STUDENTAS PER THE FOLLOWING CRITERIA:")
# # MARKS  |  GRADE
# # 100-80 |  A
# # 79-60  |  B
# # 59-40  |  C
# # 39-33  |  D
# # 32-0   |  F


m1 = int(input("please enter your marks of maths out of 100 : "))
m2 = int(input("please enter your marks of science out of 100 : "))
m3 = int(input("please enter your marks of english out of 100 : "))

avg = (m1+m2+m3)/3
if avg <= 100 and avg>=80:
    print("you got A grade")
elif avg < 80 and avg>=60:
    print("you got B grade")
elif avg < 60 and avg>=40:
    print("you got C grade")
elif avg < 40 and avg>=33:
    print("you got D grade")
else:
    print("you got f grade")