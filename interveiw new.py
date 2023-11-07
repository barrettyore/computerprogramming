print("hello future empolyee and welcome to your automated interview for google edge")
name_question = input("what is your name?")
age_question = input("what is your age")
type_question = input("what type of programming are you intrested in:>")
years_of_expeirnce = input("how long have you been proggramming in years:>")
if float(years_of_expeirnce) > 1:
    money_question = input("what is your disred salary:>")
    if float(money_question) < 500000:
        people_question = input("how well do you work with a team:>")
        back_round_question = input("have you ever commited a crime y/n:>")
        if back_round_question == "y":
            print("sorry we cant hire criminals:>")
        else:
            phone_number = input("what is your phone number:>")
            email = input("what is your email:>")
            home_address = input("what is your home adress:>")
            billing_address = input("where do you want company mail to be sent:>")
            print("this is your submission")
            print(f"your name is {name_question} you are {age_question} years old. you want to do {type_question} for us with {years_of_expeirnce} years of experince. your disired salary is {money_question} per year. you describe you team work abillitys as {people_question}. you have not commited any crimes, your phone number is {phone_number} your email is {email} your house address is {home_address} your mailing address is {billing_address}")
    else:
        print("sorry we dont not hire beggers")
else:
    print("sorry we do not hire unexpreinced ")

