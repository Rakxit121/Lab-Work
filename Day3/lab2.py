marks_maths=int(input("Enter tha marks of  :"))
marks_science=int(input("Enter tha marks of  :"))
marks_computer=int(input("Enter tha marks of  :"))
marks_english=int(input("Enter tha marks of  :"))
Total_scored=marks_maths+marks_science+marks_computer+marks_english
print("The total marks scored in percentage is: ")
per=(Total_scored/400)*100
if per >70 and per <=100:
    print("Distinction")
elif per>60 and per<=70:
    print("1st Division")
elif per > 40 and per <=60:
    print("2nd Division")
else:
    print("Fail")