# Email Validation using String Function
email=input("Enter Your Email:-") #g@g.in
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():  #isalpha:--- which can be used to check if the passed character is an alphabet or not.
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".")^ (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper(): # w--W
                            j=1
                    elif i.isdigit():#isdigit:-- which can be used to check if the passed digit is an number or not
                        continue
                    elif i=="_"or i=="@" or i==".":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("You enter Wrong Email..!5")
                else:
                  print("YOU ENTER RIGHT EMAIL")
            else:
                print("You enter Wrong Email..!4")
        else:
            print("You enter Wrong Email..!3")
    else:
        print("You enter Wrong Email..!2")
else:
    print("You enter Wrong Email..!1")
