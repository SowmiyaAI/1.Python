class multipleFunctions():
    def oddeven():
        num=int(input("enter the number:"))
        if(num%2==0):
            print("even number")
            megs="even number"
        else:
            print("odd number")
            megs="odd number"
        return megs   
    def BMI():
        BMI=int(input("Enter the BMI index:"))
        if(BMI<18.5):
            print("underweight")
            message="underweight"
        elif(BMI<24.9):
            print("normal")
            message="normal"
        elif(BMI<29.9):
            print("overweight")
            message="overweight"
        elif(BMI<39.9):
            print("very overweight")    
            message="very overweight"
        else:
            print("morbidly obese")
            message="morbidly obese"
        return message
