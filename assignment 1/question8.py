from colorama import init, Style



# print(" ASSIGNMENT 8: W.A.P. TO ACCEPT AVERAGE MARKS OUT OF 100 AND PRINT THE GRADE OF THE STUDENTAS PER THE FOLLOWING CRITERIA:")
# # MARKS  |  GRADE
# # 100-80 |  A
# # 79-60  |  B
# # 59-40  |  C
# # 39-33  |  D
# # 32-0   |  F



def grade(m1, m2, m3):
    avg = (m1+m2+m3)/3
    if avg <= 100 and avg>=80:
        print("you got", f"{Style.BRIGHT}A{Style.RESET_ALL}", "grade")
    elif avg < 80 and avg>=60:
        print("you got", f"{Style.BRIGHT}B{Style.RESET_ALL}", "grade")
    elif avg < 60 and avg>=40:
        print("you got", f"{Style.BRIGHT}C{Style.RESET_ALL}", "grade")
    elif avg < 40 and avg>=33:
        print("you got", f"{Style.BRIGHT}D{Style.RESET_ALL}", "grade")
    else:
        print("you got", f"{Style.BRIGHT}f{Style.RESET_ALL}", "grade")

m1 = int(input("please enter your marks of maths out of 100 : "))
m2 = int(input("please enter your marks of science out of 100 : "))
m3 = int(input("please enter your marks of english out of 100 : "))

grade(m1, m2, m3)