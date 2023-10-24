def personal_info():
    print("Bienvenue")
    
    user = {
        'nom': '',
        'age': 0,
        'taille': 0.0,
        'fruits_preferes': [],
        'salutation': '',
        'produit': {}
    }
    
    while True:
        print("\nMenu:")
        print("1. Saisir votre nom")
        print("2. Saisir votre âge")
        print("3. Saisir votre taille")
        print("4. Saisir vos fruits préférés")
        print("5. Saisir un message de salutation personnalisé")
        print("6. Saisir les propriétés d'un produit")
        print("7. Afficher vos informations personnelles")
        print("8. Quitter")
        
        choice = input ("Choisissez une option (1-8): ")
        
        if choice == '1':
            user['nom'] = input("Saisissez votre nom : ")
            
        elif choice == '2':
            age = input("Saisissez votre âge : ")
            
            if age():
                user['âge'] = int(age)
            else:
                print("L'âge doit être un nombre entier.")
                
        elif choice == '3':
            height = input("Saisissez votre taille (en mètres) : ")
            try:
                user['taille'] = float(height)
            except ValueError:
                print("La taille doit être un nombre décimal.")
                
        elif choice == '4':
            fruits = input("Saisissez une liste de fruits préférés (séparés par des virgules) : ")
            
            user['fruits_préférés'] = [f.strip() for f in fruits.split(',')]
        elif choice == '5':
            user['message_de_salutation'] = input("Saisissez un message de salutation personnalisé : ")
            
        elif choice == '6':
            product_name = input("Saisissez le nom du produit : ")
            product_price = float(input("Saisissez le prix du produit : "))
            product_description = input("Saisissez une description du produit : ")
            user['produit'] = {
                'nom': product_name,
                'prix': product_price,
                'description': product_description
            }
    