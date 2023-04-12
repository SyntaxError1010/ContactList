
namelist = []
numberlist = []
emaillist = []
addresslist = []

running = True


def logic():
    addcontact = input("<< Would you like to add a contact or view/remove an existing one? (Add/View/Remove)\n>> ").casefold()
    if addcontact == "add":
        getname = input("<< Enter the person's name you would like to add. (First Last)\n>> ").capitalize()
        namelist.append(getname)
        getnumber = input(f"<< Enter {getname}'s phone number.\n>> ").__str__()
        numberlist.append(getnumber)
        getemail = input(f"<< Enter {getname}'s email.\n>> ").__str__().capitalize()
        emaillist.append(getemail)
        getaddress = input(f"<< Enter {getname}'s address.\n>> ").__str__().capitalize()
        addresslist.append(getaddress)

    elif addcontact == "view":
        x = 0
        for name in namelist:
            print(f"{name}, {numberlist[x]}, {emaillist[x]}, {addresslist[x]}")
            x += 1

    elif addcontact == "remove":
        removename = input("<< Enter the name of the contact you would like to remove.\n>> ").capitalize()
        removeindex = namelist.index(removename)
        sure = input(f"<< Are you sure you want to remove {removename} from your contacts? (Yes/No)\n>>").casefold()
        if sure == "yes":
            namelist.remove(namelist[removeindex])
            numberlist.remove(numberlist[removeindex])
            emaillist.remove(emaillist[removeindex])
            addresslist.remove(addresslist[removeindex])
            print("<< Contact has been removed.")
        else:
            pass

    else:
        print("<< Enter a valid option.")


while running == True:
    logic()
    continue






