def user_info():

    prenom = input("Entrez votre prénom : ")
    nom = input("Entrez votre nom : ")
    nomMaj = nom.upper()
    age = int(input("Entrez votre âge : "))
    taille = float(input("Entrez votre taille en cm: "))
    fruits = input("Entrez des fruit : ")


    print("Bonjour" + prenom.capitalize() + " " + nomMaj())
    print('\n================Vos Informations=====================')
    print("Nom:", nom)
    print("Age:", age, "ans")
    print("Taille:", taille, "cm")
    print("Fruit:", fruits)   
print(user_info())



