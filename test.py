from datetime import datetime

def sayHello():
    heure_actuelle = int(str(datetime.now().time()).split(":")[0])
    if (heure_actuelle > 12):
        print("Bonsoir")
    else:
        print("Bonjour")

sayHello()

def is_palindrome(mot): 
    reverse = mot[::-1]  
    if (mot == reverse): 
        return True
    return False
  

saisieUtilisateur = input(("Entrez une valeur: "))
if(is_palindrome(saisieUtilisateur.lower())):
    print("Bien dit")
