import requests

'''
##============ CREATION DE COMPTE D'UN USER ==========##

    url = http://api.fedrelay.com/user/create ## ON DOIT LUI ENVOYER UN JSON DATA VOIR LE POINT 

    FORME DU DATA JSON à ENVOYER

    user = {
        "username": "gogochristian009@gmail.com or 6176559012",## ICI LE USER NE RENSEIGNE PAS SON USERNAME DANS LE FORMULAIRE. C'EST NOUS QUI LUI EN CREONS UN SOIT AVEC SON phone_Or_email=====##
        "phone_Or_email": "gogochristian009@gmail.com or 6176559012",
        "password": "Password@123"
    }

    NB: APRES CREATION DE COMPTE, LE PROFIL DU USER EST CREER AUTOMATIQUEMENT ET LUI EST RENVOYEE
    

    EXEMPLE DE REQUEST:

    requests.post(http://api.fedrelay.com/user/create,json=user)

'''

'''
##============ CONNEXION D'UN USER à UN COMPTE ==========##

    url = http://api.fedrelay.com/user/login ## ON DOIT LUI ENVOYER UN JSON DATA VOIR LE POINT 

    FORME DU DATA JSON à ENVOYER

    user_login = {
        "username": "gogochristian009@gmail.com",
        "password": "Password@123"
    }

    EXEMPLE DE REQUEST:

    requests.post(http://api.fedrelay.com/user/login,json=user_login)

    NB: APRES LOGIN DU USER, LES INFOS DE SON PROFIL LUI SONT AUTOMATIQUEMENT RENVOYEE.


'''

'''
##============ DECONNEXION D'UN USER à UN COMPTE ==========##

    url = http://api.fedrelay.com/user/logout ## ON DOIT LUI ENVOYER UN TOKEN DANS LE HEADERS ## ça marche sur postman


    EXEMPLE DE REQUEST:

    requests.post(https://api.fedrelay.com/user/logout)

'''

'''
##============ REINITIALISATION DE MOT DE PASSE ==========##

    url = http://api.fedrelay.com/user/password_reset/ ## ON DOIT LUI ENVOYER UN JSON DATA 

    FORME DU DATA JSON à ENVOYER

    reset_password ={
        "email": "gogochristian009@gmail.com"##Ici l'utilisateur doit entrer l'email avec lequel il avait créer son  compte,
    }

    EXEMPLE DE REQUEST:

    requests.post(http://api.fedrelay.com/user/password_reset/,json=reset_password)


    RETURN: 
    ====== UN MAIL EST RENVOYE AU CLIENT POUR QU'IL CONFIRME LA REINITIALISATION DU MOT DE PASSE.   ========
                ENSUITE IL RENVOIE CE JSON LORSQUE LE MAIL EST BIEN ENVOYE
    {
        'status':'OK'   
    }

'''

'''
##============ CONFIRMATION DE LA REINITIALISATION DU MOT DE PASSE ==========##

    url = http://api.fedrelay.com/user/password_reset/confirm/ ## ON DOIT LUI ENVOYER UN JSON DATA 

    FORME DU DATA JSON à ENVOYER

    confirm_reset_password ={
        "token": "2348492e2042c945d028bcc116e64a124be",## Ici l'utilisateur doit entrer le Token qui lui a été envoyer par mail
        "password":"gogo@123" ## Ici l'utilisateur doit entrer son nouveau password qu'il veut utiliser désormais
    }

    EXEMPLE DE REQUEST:

    requests.post(http://api.fedrelay.com/user/password_reset/confirm/,json=confirm_reset_password)

'''


'''
##============ MODIFICATION DU PROFIL POUR UN USER ==========##

    url = http://api.fedrelay.com/user/<int:user_id>/profil ## ON DOIT LUI ENVOYER UN JSON DATA ## LE TOKEN EST PASSE EN HEADERS

    FORME DU DATA JSON à ENVOYER

    profil = {
        "nom":"GOGO",
        "prenom":"Christian",
        "telephone":"6589654521",
        "email":'florent@gmail.com',
        "profession":'Ingénieur',
        "pays":'Bénin',
        "departement":'Littoral',
        "commune":'Cotonou',
        "quartier":"Finanfa"
        "avatar":"https://www.shutterstock.com/image-photo/portrait-positive-guy-specialist-sit-600w-1836307192.jpg" ## Renseigner ici l'URL de votre nouvelle image
    }
    EXEMPLE DE REQUEST:

    requests.patch(http://api.fedrelay.com/user/<int:user_id>/profil)

    NB: 
    ==> ICI LA METHODE PATCH EST REQUISE. CETTE REQUETE NE MARCHE PAS AVEC LA METHODE PUT
    ==> ICI AUCUN CHAMP N'EST REQUIS. VOUS POUVEZ MODIFIER UN SEUL CHAMP 
    LA REPONSE RETOURNEE COMPORTE TOUTES LES INFORMATIONS DU PROFIL DU USER
'''


'''
##============ RECUPERATION DU PROFIL POUR UN USER ==========##

    url = http://api.fedrelay.com/user/<int:user_id>/getprofil ## ON DOIT LUI ENVOYER UN JSON DATA ## LE TOKEN EST PASSE EN HEADERS

'''

'''
##============ ENREGISTREMENT D'UNE LIVRAISON==========##

    url = http://api.fedrelay.com/delivery/create ## ON DOIT LUI ENVOYER UN JSON DATA ## LE TOKEN EST PASSE EN HEADERS

    FORME DU DATA JSON à ENVOYER

    delivery = {
        "user":1, ##ICI IL FAUT RENSEIGNER L'ID DE L'UTILISATEUR QUI EST CONNECTE
        "nomEmetteur": "SEDEGNAN",
        "prenomEmetteur": "Victoire",
        "telephoneEmetteur": "61765590",
        "emailEmetteur": "example@gmail.com",
        "paysEmetteur": "Benin",
        "departementEmetteur": "Borgou",
        "communeEmetteur": "Cotonou",
        "quartierEmetteur": "Fifadji",

        "lieuColis": "Ahelawadjè",
        "detailLocalisation": "Non loin du carrefour les trois bandes",

        "villeReception": "Togo",
        "pointRelais": "Lomè",
        "notification": "Ce colis des trucs",

        "nomDestinataire": "PAPA",
        "prenomDestinataire": "Lomè",
        "telephoneDestinataire": "617955600",
        "emailDestinataire": "azizvorrez8@gmail.com",
        "typeColis": "Du gari à l'intérieur",
        "poids": "54 kg",
        "description": "Trois sacs de riz et de banane"
    }

    EXEMPLE DE REQUEST:

    requests.post(http://api.fedrelay.com/delivery/create,json=delivery)

'''



'''
##============ UPDATE D'UNE LIVRAISON==========##

    url = http://api.fedrelay.com/delivery/<id_commande>/update ## ON DOIT LUI ENVOYER UN JSON DATA ## LE TOKEN EST PASSE EN HEADERS

    FORME DU DATA JSON à ENVOYER

    delivery = {
        "is_validated":True,
        "transactionId": "##63524trv1",
    }

    EXEMPLE DE REQUEST:

    requests.patch(http://api.fedrelay.com/<user_id>/update,json=delivery)

'''

'''
##============ RECUPERATION DE TOUTE LES LIVRAISONS D'UN USER==========##

    url = http://api.fedrelay.com/delivery/<user_id>/deliveries ## LE TOKEN EST PASSE EN HEADERS 

    EXEMPLE DE REQUEST:

    requests.GET(http://api.fedrelay.com/delivery/<user_id>/deliveries)
'''

'''
##============ SUIVI D'UNE LIVRAISON ==========##

    url = http://api.fedrelay.com/delivery/<str:follow_code>/followup ## ON DOIT LUI ENVOYER UN JSON DATA VOIR LE POINT ## LE TOKEN EST PASSE EN HEADERS

    EXEMPLE DE REQUEST:

    requests.get(http://api.fedrelay.com/delivery/<str:follow_code>/followup)
'''

'''
##============ RECUPERATION DE TOUT LES POINTS RELAIS ==========##

    url = http://api.fedrelay.com/relaypoints ## LE TOKEN EST PASSE EN HEADERS

    EXEMPLE DE REQUEST:

    requests.get(http://api.fedrelay.com/relaypoints)

'''

'''
##============ RECUPERATION DE TOUT LES POINTS RELAIS  D'UN QUARTIER==========##

    url = http://api.fedrelay.com/8000/relaypoints/<quarter_id> ## LE TOKEN EST PASSE EN HEADERS

    EXEMPLE DE REQUEST:

    requests.get(http://api.fedrelay.com/8000/relaypoints/<quarter_id>)

'''


'''
##============ ENVOIE DE MESSAGE DANS LE CHAT PAR UN CLIENT ==========##

    url = http://api.fedrelay.com/chat/client ## ON DOIT LUI ENVOYER UN JSON DATA  ## LE TOKEN EST PASSE EN HEADERS

    FORME DU DATA JSON à ENVOYER

    chat_client = {
        "user": 1, ## Ici il faut renseigner l'ID du USER en question
        "message":"Le lorem ipsum est, en imprimerie, une suite de mots sans signification utilisée à titre provisoire pour calibrer une mise en page, le texte définitif venant remplacer le faux-texte dès qu'il est prêt ou que la mise en page est achevée"
    }
    EXEMPLE DE REQUEST:

    requests.post(http://api.fedrelay.com/chat/client,json=chat_client)
'''


'''
##============ RECUPERATION DE TOUT LES CHATS D'UN USER ==========##

    url = http://api.fedrelay.com/chat/<user_id>/client ## LE TOKEN EST PASSE EN HEADERS

    EXEMPLE DE REQUEST:

    requests.post(http://api.fedrelay.com/chat/<user_id>/client)
'''


'''
##============ CREATION D'UN NEWSLETTER ==========##

    url = http://api.fedrelay.com/newsletter ## ON DOIT LUI ENVOYER UN JSON DATA 

    FORME DU DATA JSON à ENVOYER

    newsletter = {
        'email':'gogochristian009@gmail.com'
    }

    EXEMPLE DE REQUEST:

    requests.post(http://api.fedrelay.com/newsletter,json=newsletter)

    NB: Le mail renseigné par le client sera envoyer dans DATABASE puis ensuite dans le compte MAILCHIMP

'''

'''
##============ SIMULATION DU PRIX DE LA LIVRAISON ==========##

    url = http://api.fedrelay.com/simulator ## ON DOIT LUI ENVOYER UN JSON DATA 

    FORME DU DATA JSON à ENVOYER

    simulation = {
        "localisation":'cotonou',
        "product_type":'Lourd',
        "delivery_point":'Parakou',
        "delivery_delay":'3 jours',
    }

    EXEMPLE DE REQUEST:

    requests.post(http://api.fedrelay.com/simulator,json=simulation)

'''

'''
##============ ENREGISTREMENT D'UN PARTENARIAT ==========##

    url = http://api.fedrelay.com/partenariat ## ON DOIT LUI ENVOYER UN JSON DATA 

    FORME DU DATA JSON à ENVOYER

    partenariat = {
        "nom":"Bobo",
        "prenom":"Deg",
        "denomination":"Chine",
        "email":"bobmanou@gmail.com",
        "typ":"Signalisation",
        "object":"porto-novo",
        "lettre":"Le lorem ipsum est, en imprimerie, une suite de mots sans signification utilisée à titre provisoire pour calibrer une mise en page, le texte définitif venant remplacer le faux-texte dès qu'il est prêt ou que la mise en page est achevée. Généralement, on utilise un texte en faux latin, le Lorem ipsum ou Lipsum",
    }


    EXEMPLE DE REQUEST:

    requests.post(http://api.fedrelay.com/partenariat,json=partenariat)

'''



'''
##============ ENREGISTREMENT D'UN CONTACT ==========##

    url = http://api.fedrelay.com/contact ## ON DOIT LUI ENVOYER UN JSON DATA 

    FORME DU DATA JSON à ENVOYER

    contact = {
        "nom":"Bobo Contact",
        "prenom":"Deg contact",
        "telephone":"Chine contact",
        "object":"Mon objet",
        "message":"Le lorem ipsum est, en imprimerie, une suite de mots sans signification utilisée à titre provisoire pour calibrer une mise en page, le texte définitif venant remplacer le faux-texte dès qu'il est prêt ou que la mise en page est achevée. Généralement, on utilise un texte en faux latin, le Lorem ipsum ou Lipsum",
    }


    EXEMPLE DE REQUEST:

    requests.post(http://api.fedrelay.com/contact,json=contact)

'''

















