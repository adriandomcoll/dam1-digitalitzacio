from User import *
from DaoUserClient import *

class ViewConsole:

    daoClient=DaoUserClient()
    token=""
   
    def viewShowMenu(self):
        print("1: Login")
        print("2: Login Token")
        print("3: Child")
        print("4: Tap by id_child")
        print("5: Quit")
        while(True):
            option=input("Enter Option: ")
            if(option.isdigit):
                optionInt=int(option)
                if(optionInt >0 and optionInt <6):
                    return optionInt
            
            print("Error: Introdueix una opció correcta")

        
    def viewGeneral(self):
        option=-1
        while(True):
            option=self.viewShowMenu()
            match option:
                case 1:
                    #login
                    self.viewLogin()
                case 2:
                    #login Token
                    self.viewLoginToken()
                case 3:
                    #Childs
                    self.viewChilds(self.token)
                case 4:
                    #Tap
                    self.viewTaps()
                case 5:
                    # Quit
                    exit()
                    print("Adeu, Gràcies per utilitzar l'aplicació")


    def viewChilds(self, token):
        print("View Childs")
        resposta_child=self.daoClient.childToken(token)
        if(resposta_child):
            print(resposta_child)              
        

    def viewLoginToken(self):
        print("View LOGIN TOKEN")
        token_input = input("Introdueix el token: ")
        if not token_input:
            print("No token disponible")
            return
        token = token_input if token_input else self.token
        # Llamar al DAO para validar el token y obtener el usuario
        user = self.daoClient.loginToken(token)
        if user:
            # Mostrar info del usuario
            self.viewUser(user)
        else:
            self.viewUserNotAutenticated()

    def viewLogin(self):
        print("View LOGIN")
        print("Introdueix el Username o email i el password")
        username=input("Username o email: ")
        passwd=input("Password: ")
        user=User("", username, passwd, "", "", "")
        resposta_user=self.daoClient.login(user)
        if(resposta_user):
            self.viewUser(resposta_user)
            self.token=resposta_user.token
        else:
            self.viewUserNotAutenticated()
    
    def viewUser(self,user):
        print("View User Authenticated")
        print(user)
    
    def viewUserNotAutenticated(self):
        print("View User")
        print("User NOT Authenticated")

    def viewTaps(self):
        child_id = input("Introduce child_id: ")
        if not child_id:
            print("child_id requerido.")
            return
        taps = self.daoClient.tapId(child_id, self.token)
        if taps is None:
            print("Error al obtener taps o access denegado.")
        else:
            print(f"Taps para child {child_id}:")
            for t in taps:
                print(t)

viewConsole=ViewConsole()

viewConsole.viewGeneral()