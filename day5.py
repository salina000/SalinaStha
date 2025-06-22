#nested if

#deternine loan Eligibility

loan_age=20
loan_monthly=50000

age=int(input("Enter your age: "))
monthly_income=int(input("Enter your monthly income: "))

if(age>=loan_age):
    print("loan age pass")

    if(monthly_income>=loan_monthly):
        print("You can apply for loan")

    else:
        print("Your monthly income should be higher.")

else:
    print("You cannot apply for loan at this age.")



gender="M"
if gender=="M":
    print("Male")
else:
    print("Female")   

result="Male" if gender=="M" else "Female"

if gender=="M":
    print("Male")

elif gender=="F":
    print("Female")
    

 

