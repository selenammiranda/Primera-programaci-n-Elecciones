usersList = [{"name":"Dayanna","age":"17","id": "208090839","email":"drojamiran@gmail.com","typeUser":"Administrator", "password":""}] #List of registered users in the system
userLogged = {} #Keeps the user's data authenticated
territorialDistributionList = []# List of territorial distribution, stores provinces, cantons, districts
politicalList = []# list of political parties
presidentialList = []# store the presidential ballot

#Display the registration interface for new users
def registerUI():
    print("\nUser register")
    name = (input("1) Complete name: "))
    age = (input(str("2) Age: ")))
    email = (input("3) Email: "))
    id = (input(str("4) ID: ")))
    password = (input(str("5) Password:")))

    #Gets the user type and stores it in a local variable
    typeUser = registerUserTypeUI()

    #Register the user in the list
    registerUser(name,age,email,id,password,typeUser)


#Interface that obtains and returns the type of user that wishes to register
def registerUserTypeUI():
    print("\n")
    print("Type of user:\n"
          "  1) Administrator\n"
          "  2) Invited")
    option = (input(str("Option: ")))

    if (option == "1"):
        return "Administrator"
        menuLoginUI()
    elif option == "2":
        return "Invited"
    else:
        return "Unknow"




#Store the records in the dictionary
def registerUser(name,age,email,id,password,typeUser):
    newUser = {}
    newUser["name"] = name
    newUser["age"] = age
    newUser["email"] = email
    newUser["id"] = id
    newUser["password"] = password
    newUser["typeUser"] = typeUser
    usersList.append(newUser)

#Interface that obtains the id and password of the previously registered user
def loginUI():
    print("\nLog in")
    id = (input(str("ID: ")))
    password = (input(str("Password: ")))
    loginUser(id,password)

#Loge the user in the system
def loginUser(id,password):
    for i in usersList:
        if i["id"] == id:
            if i["password"] == password:
                redirectUserAutenticate(i)
            else:
                print("Wrong Credentials")

#Redirect an authenticated user to the menu
def redirectUserAutenticate(user):
    print("Welcome " + user["name"] + " you are now logged. (" + user["typeUser"] + ")")
    if user["typeUser"] == "Administrator":
        administratorOptionsUI()
    elif user["typeUser"] == "Invited":
        invitedOptionsUI()

#Initialize the entire program
def main():

    run_program = True

    while(run_program):
        print("        Welcome to the national election system!  \n    ")
        print("Do you already have an account? log in. If not register.")
        option = (input(str("Choose an option to perform \n"
                            "1) Login\n"
                            "2) Sign in\n"
                            "3) exit\n"
                            "Option: ")))
        if(option == "1"):
            loginUI()
        elif option == "2":
            registerUI()
        elif option == "3":
            run_program = False


#Administrator Options
def administratorOptionsUI():
    print("\n")
    option = (input(str("Welcome to the administrator's menu. What do you want to make? \n"
                       "1) Territorial distribution\n"
                       "2) Administration of political paties\n"
                       "3) Administration of ballots\n"
                       "4) Results\n"
                       "5) Consultation\n"
                       "6) Sing off\n"
                       "Option: ")))
    administratorOptionRediret(option)

#redirects according to the option taken by the administrator
def administratorOptionRediret(option):
    if (option == "1"):
       territorialDistributionOptions()
    elif (option == "2"):
        politicalPartyOptions()
    elif (option == "3"):
        administrationBallots()
    elif (option == "4"):
        '''# redirigir a resultados'''
    elif (option == "5"):
        '''# redirigir a consultas'''
    elif (option == "6"):
        main()
    else:
        print("Wrong option. Try again.")
        administratorOptionsUI()

# territorial distribution management options
def territorialDistributionOptions():
    print("\n")
    option = (input(str("What do you want to manage? \n"
               "1) Manage Province\n"
               "2) Manage Canton\n"
               "3) Manage District\n"
               "4) Back\n"
               "Option: ")))
    territorialDistributionOptionRediret(option)

#redirect according to the option of territorial distribution
def territorialDistributionOptionRediret(option):
    if (option == "1"):
        manageProvince()
    elif (option == "2"):
        manageCanton()
    elif (option == "3"):
       manageDistrict()
    elif (option == "4"):
        administratorOptionsUI()
    else:
        territorialDistributionOptions()

# allows to modify, create or eliminate provinces
def manageProvince():
    print("\n")
    option = (input(str("What do you want to do in provincial administration? \n"
                       "1) Create Province\n"
                       "2) Modify Province\n"
                       "3) Delete Province\n"
                       "4) Back\n"
                       "Option: ")))

    manageProvinceRedirect(option)

#redirects the options to create, modify and eliminate provinces
def manageProvinceRedirect(option):
    if (option == "1"):
        createProvince()
    elif (option == "2"):
        modifyProvince()
    elif (option == "3"):
        deleteProvince()
    elif (option == "4"):
        territorialDistributionOptions()
    else:
        manageProvince()

# allows to create provinces and add deputies
def createProvince():
    print("\n Enter data to create a province")
    name = (input("1) Province name: "))
    deputyNumber = input(str("2) Deputy number: "))

    newProvince(name,deputyNumber)

    print("Province  created successfully!")
    manageProvince()

#Dictionary of province
def newProvince(name,deputyNumber):
    newProvince = {}
    newProvince["name"] = name
    newProvince["deputyNumber"] = deputyNumber


    territorialDistributionList.append(newProvince)

# allows to modify the province and number of deputies
def modifyProvince():
    option = input("\nWhat do you want to change in the province?\n"
                   "1)Name Province\n"
                   "2)Deputy Number\n"
                   "3)Back\n"
                   "Chooose your option: ")
    print("\nProvince created:")
    if option == "1":
        for i in territorialDistributionList:
            name= i["name"]
            print (name)
        option = (input("Name Province: "))

        print("\n")
        for y in territorialDistributionList:
            if y["name"] == option:
                newName = input("New Name: ")
                y["name"] = newName
                print("Name province update succesfully")

    elif option == "2":
        for i in territorialDistributionList:
            name = i["name"]
            deputyNumber = i["deputyNumber"]
            print(name,deputyNumber)
        option = (input(str("Name province: ")))

        print("\n")
        for y in territorialDistributionList:
            if y["name"] == option:
                newNum = (input("New number of Diputies: "))
                y["deputyNumber"] = newNum
                print("Number of deputies update succesfully")


    elif option == "3":
        manageProvince()

    else:
        print("Invalid option, try again")
        modifyProvince()


    manageProvince()

#allows you to delete the desired province
def deleteProvince():
    for i in territorialDistributionList:
        name = i["name"]
        print(name)
    option = (input("Name of province you want to delete: "))

    print("\n")
    for y in territorialDistributionList:
        if (y["name"] == option):
            territorialDistributionList.remove(y)


    print("Province delete succesfully!")
    manageProvince()

#allows you to manage cantons
def manageCanton():
    print("\n\n")
    option = int(input("choose an option \n"
                       "1) Create Canton\n"
                       "2) Modify Canton\n"
                       "3) Delete Canton\n"
                       "4) Back\n"
                       "Option: "))

    if (option == 1):
        createCanton()
    elif (option == 2):
        modifyCanton()
    elif (option == 3):
        deleteCanton()
    else:
        territorialDistributionOptions()

#allows you to create cantons
def createCanton():
    for i in territorialDistributionList:
        name = i["name"]
        print(name)
    option = input(str("Choose a province:"))


    for x in territorialDistributionList:
        if x["name"] == option:
            nameCanton = (input(str("Name Canton: ")))
            x["nameCanton"] = nameCanton
            print("Name canton add succesfully")

    manageCanton()
#store the cantons in dictionaries
def addCanton(nameCanton):
    newCanton={}
    newCanton["nameCanton"]=nameCanton
    territorialDistributionList.append(newCanton)

#allows you to modify cantons
def modifyCanton():
    for i in territorialDistributionList:
        name = i["name"]
        print(name)
    option = (input("Name Province: "))

    for y in territorialDistributionList:
        if y["name"] == option:
            for x in territorialDistributionList:
                nameCanton = x["nameCanton"]
                print(nameCanton)
            option= input(str("Name canton: "))

            for n in territorialDistributionList:
                if n["nameCanton"] == option:
                    newName = input(str("New name canton: "))
                    n["nameCanton"] = newName
                    print("Name province update succesfully")


    manageCanton()

#Allows you to delete the cantons
def deleteCanton():
    for i in territorialDistributionList:
        name = i["name"]
        print(name)
    option = (input("Name province: "))
    print("\n")
    for y in territorialDistributionList:
        if (y["name"] == option):
            for x in territorialDistributionList:
                nameCanton = x["nameCanton"]
                print(nameCanton)
            option = (input("Name of canton do yuo want delete: "))
            for n in territorialDistributionList:
                if n["nameCanton"] == option:
                    territorialDistributionList.remove(n)
    print("Canton delete succesfully!")
    manageCanton()

#Allows adding districts
def manageDistrict():
    print("\n\n")
    option = int(input("choose an option \n"
                       "1) Create District\n"
                       "2) Modify District\n"
                       "3) Delete District\n"
                       "4) Back\n"
                       "Option: "))

    if (option == 1):
        createDistrict()
    elif (option == 2):
        modifyDistrict()
    elif (option == 3):
        '''deleteDistrict()'''
    else:
        territorialDistributionOptions()


#Create districts
def createDistrict():
    for i in territorialDistributionList:
        name = i["name"]
        print(name)
    option = input(str("Choose a province:"))

    for x in territorialDistributionList:
        if x["name"] == option:
            for y in territorialDistributionList:
                nameCanton = y["nameCanton"]
                print(nameCanton)
            option = input(str("Name canton: "))

            for n in territorialDistributionList:
                if n["nameCanton"] == option:
                    nameDistrict = input(str("Name district: "))
                    n["nameDistrict"] = nameDistrict


    print("District add succesfully")
    manageDistrict()


def modifyDistrict():
    for i in territorialDistributionList:
        name = i["name"]
        print(name)
    option = (input("Name Province: "))

    for y in territorialDistributionList:
        if y["name"] == option:
            for x in territorialDistributionList:
                nameCanton = x["nameCanton"]
                print(nameCanton)
            option= input(str("Name canton: "))

            for n in territorialDistributionList:
                if n["nameCanton"] == option:
                    for l in territorialDistributionList:
                        nameDistrict = l["nameDistrict"]
                        print(nameDistrict)
                    option = (input("Name District: "))

                    for v in territorialDistributionList:
                        if v["nameDistrict"] == option:
                            newName = input(str("New name District: "))
                            n["nameDistrict"] = newName
                    print("Name district update succesfully")
    manageDistrict()

#stote the districts in dicctionaries
def addDistrict(nameDistrict):
    newDistrict = {}
    nameDistrict["nameDistrict"] = nameDistrict
    territorialDistributionList.append(nameDistrict)



#political party administration options
def politicalPartyOptions():
    print("\n\n")
    option = (input(str("choose an option \n"
                       "1) Create political party\n"
                       "2) Modificate political party\n"
                       "3) Eliminate political party\n"
                       "4) Back\n"
                       "Option: ")))
    politicalPartyOptionRediret(option)

#redirects according to the option of political parties
def politicalPartyOptionRediret(option):
    if (option == "1"):
        addPoliticalParty()
    elif (option == "2"):
        modifyPoliticalParty()
    elif (option == "3"):
        deletePoliticalParty()
    elif (option == "4"):
        administratorOptionsUI()
    else:
        politicalPartyOptions()

#Add a new political party to the list
def addPoliticalParty():
    print("\n")
    nameParty = (input("1) Political name: "))
    foundationYear = int(input("2) Year foundation: "))
    color = (input(str("3) Colors: ")))
    ideologicalCurrent = input(str("4) Ideological current: "))

    newPoliticalParty(nameParty,foundationYear,color,ideologicalCurrent)


    print("Political party add succesfully")
    politicalPartyOptions()


#dictionary of political parties
def newPoliticalParty(nameParty,foundationYear,color,ideologicalCurrent):
    newParty = {}
    newParty["nameParty"] = nameParty
    newParty["foundationYear"] = foundationYear
    newParty["color"] = color
    newParty["ideologicalCurrent"] = ideologicalCurrent
    politicalList.append(newParty)

#Modify registered political parties
def modifyPoliticalParty():
    print("\nWhat change do you want to make to the political party?")
    option = input(str("1) Name political party\n"
                       "2) Foundation year\n"
                       "3) Color\n"
                       "4) Ideological Current\n"
                       "5) Back\n"
                       "Choose your option: "))

    if option == "1":
        for i in politicalList:
            party= i["nameParty"]
            print(party)
        option = (input(str("Choose a political party: ")))

        for x in politicalList:
                if x["nameParty"] == option:
                    newNameParty = input(str("New name political party: "))
                    x["nameParty"] = newNameParty
        print("Name political party update succesfully")

    elif option == "2":
        for i in politicalList:
            party = i["nameParty"]
            foundationYear= i["foundationYear"]
            print(party,foundationYear)
        option = (input(str("Choose a political party: ")))

        for x in politicalList:
                if x["nameParty"] == option:
                    newYearParty = input(str("New foundation year political party: "))
                    x["foundationYear"] = newYearParty
        print("Foundation year of political party update succesfully")

    elif option == "3":
        for i in politicalList:
            party = i["nameParty"]
            colors= i["color"]
            print(party,colors)
        option = (input(str("Choose a political party: ")))

        for x in politicalList:
                if x["nameParty"] == option:
                    newColorParty = input(str("New color of the political party: "))
                    x["color"] = newColorParty
        print("Colors of political party update succesfully")

    elif option == "4":
        for i in politicalList:
            party = i["nameParty"]
            ideologicalCurrent= i["ideologicalCurrent"]
            print(party,ideologicalCurrent)
        option = (input(str("Choose a political party: ")))

        for x in politicalList:
                if x["nameParty"] == option:
                    newIdeologicalParty = input(str("New color of the political party: "))
                    x["ideologicalCurrent"] = newIdeologicalParty
        print("Ideological current of political party update succesfully")


    politicalPartyOptions()

#eliminate political parties
def deletePoliticalParty():
   for i in politicalList:
       nameParty = i["nameParty"]
       print(nameParty)
   option = (input(str("Choose a political party: ")))

   for x in politicalList:
        if (x["nameParty"]==option):
            politicalList.remove(x)

   print("Party delete succesfully!")
   politicalPartyOptions()


#menu that allows you to create, modify or delete a ballot
def administrationBallots():
    print("\n\n")
    option =(input(str("Choose an option \n"
                       "1) Create Ballots\n"
                       "2) Modify Ballots\n"
                       "3) Delete Ballots\n"
                       "4) Back\n"
                       "Option: ")))


    if (option == "1"):
        createBallots()
    elif (option == "2"):
        modifyBallots()
    elif (option == "3"):
       '''typeBallots()'''
    elif (option == "4"):
        '''administratorOptionsUI()'''
    else:
        '''administratorOptionsUI()'''

#allows to create ballots
def createBallots():
    for i in politicalList:
        party = i["nameParty"]
        print(party)
    option = input(str("Choose the party which you want to add to the ballot: "))

    for x in politicalList:
        if x["nameParty"]==option:
            nameParty = x["nameParty"]
            print("Type ballot")
            typeBallot = input(str("Presidential or Lesgislative"))
            if typeBallot == "Presidential":
                if typeBallot == "presidential":
                    presidential = typeBallot
                    addBallotPresidential(nameParty,presidential)

                print(nameParty,presidential)

            elif typeBallot == "Legislative":
                if typeBallot == "legislative":
                    nameParty=x["nameParty"]
                    for y in territorialDistributionList:
                        province = y["name"]
                        print(province)
                    option = input(str("Choose a province: "))
                    for n in territorialDistributionList:
                        if n["name"] == option:
                            nameProvince = n["name"]
                            legislative = typeBallot


    administrationBallots()


def addBallotPresidential(nameParty,presidential):
    ballotPresidential = {}
    ballotPresidential["presidential"]=presidential
    ballotPresidential["nameParty"]=nameParty

    presidentialList.append(ballotPresidential)

def addBallotLegislative(nameParty,legislative,nameProvince):
    ballotLegislative = {}
    ballotLegislative["legislative"]= legislative
    ballotLegislative["nameParty"] = nameParty
    ballotLegislative["namePtovince"] = nameProvince
    territorialDistributionList.append(ballotLegislative)

def modifyBallots():
    print("What type of ballot do you want to modify?")
    option = input(str("1) Presidential\n"
                       "2) Legislative\n"
                       "3) Back\n"
                       "Option: "))
    #if option == "1":
     #   for i  in presidentialList:



#It allows to eliminate the ballots
def deleteBallots():
    count = 1
    for i in politicalList:
        print(str(count) + ")" + i.name + "\n")
        count = count + 1
    option = int(input("Choose a Ballots: "))

    countDelete = 1
    for x in politicalList:
        if (option == countDelete):
             politicalList.pop(countDelete - 1)
        countDelete += 1

    print("Ballots delete succesfully!")
    administrationBallots()
#Guest options
def invitedOptionsUI():
    option = int(input("choose an option \n"
                       "1) Consultation\n"
                       "2) Sign off\n"
                       "3) Back\n"
                       "Option: "))


    #inicializa el programa

main()





