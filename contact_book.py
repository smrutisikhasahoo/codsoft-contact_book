Contact={}
def display_Contact():
    print("name\t\tcontact Number")
    for key in Contact:
        print("{}\t\t{}" .format(key,Contact.get(key)))

while True:
    choice=int(input(" 1.ADD NEW CONTACT \n 2.SEARCH CONTACT \n 3.DISPLAY CONTACT \n 4.EDIT CONTACT \n 5.DELETE CONTACT \n 6.EXIT \n" "ENTER YOUR CHOICE:-"))
    if choice==1:
        Name=input("Enter The Contact Name:-")
        Phone=int(input("Enter The Mobile Number:-"))
        Contact[Name]=Phone
    elif choice==2:
        Search_Name=input("Enter The Contact name:- ")
        if Search_Name in Contact:
            print(Search_Name,"'s contact number is ",Contact[Search_Name])
        else:
            print("------------------Name Is Not Found in Contact Book----------------")
    elif choice==3:
        if not Contact:
            print("------------------Empty Contact Book----------------")
        else:
            display_Contact()
    elif choice==4:
        Edit_Contact=input("Enter the Contact Name To be Edited")
        if Edit_Contact in Contact:
            Phone=input("Enter mobile Number")
            Contact[Edit_Contact]=Phone
            print("------Contact Updated:------")
            display_Contact()
        else:
            print("--------------Name is not found in contact book-----------------")
    elif choice==5:
        Del_Contact=input("Enter the Contact Name to be deleted")
        if Del_Contact in Contact:
            Confirm=int(input("Do You Want To Delete This Contact 1/0"))
            if Confirm ==1:
                Contact.pop(Del_Contact)
            else:
                print("--------------Not deleted----------------")
            display_Contact()
        else:
            print("------------------------name is not Found in contact book---------------")
    else:
        break