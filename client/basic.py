import requests

# ======= USING MIXINGS ===== #

# http://api.fedrelay.com/delivery/create ## ENREGISTREMENT D'UNE LIVRAISON ## ON DOIT LUI ENVOYER UN JSON DATA ## LE TOKEN EST PASSE EN HEADERS
# http://api.fedrelay.com/delivery/<user_id>/deliveries ## RECUPERATION TOUTES LES LIVRAISON ##LE TOKEN EST PASSE EN HEADERS
# http://api.fedrelay.com/<srt:follow_code>/followup ## SUIVI D'UNE LIVRAISON ## LE TOKEN EST PASSE EN HEADERS

# http://api.fedrelay.com/user/create ## CREATION DE COMPTE D'UN USER ## ON DOIT LUI ENVOYER UN JSON DATA
# http://api.fedrelay.com/user/login ## CONNEXION D'UN USER ## ON DOIT LUI ENVOYER UN JSON DATA
# http://api.fedrelay.com/user/logout ## DECONNEXION D'UN USER ## ON DOIT LUI ENVOYER UN TOKEN DANS LE HEADERS
# http://api.fedrelay.com/user/password_reset/ ## REINITIALISATION DE MOT DE PASSE ## ON DOIT LUI ENVOYER UN JSON DATA
# http://api.fedrelay.com/user/password_reset/confirm/ ## CONFIRMATION DE LA REINITIALISATION DU MOT DE PASSE ## ON DOIT LUI ENVOYER UN JSON DATA



# http://api.fedrelay.com/chat/client ## POST D'UN MESSAGE PAR UN CLIENT ## LE TOKEN EST PASSE EN HEADERS
# http://api.fedrelay.com/chat/<user_id>/client ## RECUPERATION DE TOUT LES CHATS D'UN USER ## LE TOKEN EST PASSE EN HEADERS



# http://api.fedrelay.com/dashboard/profil ## CREATION DE PROFIL ## ON DOIT LUI ENVOYER UN JSON DATA ## LE TOKEN EST PASSE EN HEADERS
# http://api.fedrelay.com/dashboard/<user_id>/avatar ## MODIFICATION D'AVATAR POUR UN USER ## LE TOKEN EST PASSE EN HEADERS




# http://api.fedrelay.com/newsletter ## CREATION D'UN NEWSLETTER ## ON DOIT LUI ENVOYER UN JSON DATA
# http://api.fedrelay.com/simulator ## SIMULATION DU PRIX DE LA LIVRAISON ## ON DOIT LUI ENVOYER UN JSON DATA
# http://api.fedrelay.com/partenariat ##ENREGISTREMENT D'UN PARTENARIAT## PARTENARIAT ## ON DOIT LUI ENVOYER UN JSON DATA
# http://api.fedrelay.com/contact ## ENREGISTREMENT D'UN CONTACT ## ## ON DOIT LUI ENVOYER UN JSON DATA

# http://127.0.0.1:8000/relaypoints ## ENREGISTREMENT D'UN CONTACT ## ## ON DOIT LUI ENVOYER UN JSON DATA
# http://127.0.0.1:8000/1/relaypoints ## ENREGISTREMENT D'UN CONTACT ## ## ON DOIT LUI ENVOYER UN JSON DATA


# Token online: 3f1f880542479b363bef73b75e2e6f3b208714f5858abbd64af0522aa7114e9c

## FORMA DU DATA à ENVOYER AU COURS DE L'ENREGISTREMENT D'UNE LIVRAISON ##
delivery = {
    "user":1,
    "client_id":1,
    "nomEmetteur": "SEDEGNAN",
    "prenomEmetteur": "Victoire",
    "telephoneEmetteur": "61765590",
    "lieuColis": "Ahelawadjè",
    "detailLocalisation": "Non loin du carrefour les trois bandes",

    "villeReception": "Togo",
    "pointRelais": "Lomè",
    "notification": "Ce colis des trucs",

    "nomDestinataire": "PAPA",
    "prenomDestinataire": "Lomè",
    "telephoneDestinataire": "617955600",
    "emailDestinataire": "gogochristian009@gmail.com",
    "typeColis": "Du gari à l'intérieur",
    "poids": "54 kg",
    "description": "Trois sacs de riz et de banane"
}


# FORMA DU DATA à ENVOYER AU COURS DE L'ENVOIE D'UN NEWSLETTER ##
newsletter = {
    'email':'setohgogo1@gmail.com'
}

## FORMA DU DATA à ENVOYER AU COURS LA CREATION D'UN COMPTE ##
user = {
    "username": "gogo@gmail.com", ## ICI LE USER NE RENSEIGNE PAS SON USERNAME DANS LE FORMULAIRE. C'EST NOUS QUI LUI EN CREONS UN SOIT AVEC SON MAIL OU SON PHONE=====##
    "email": "gogo@gmail.com",
    "phone":"",
    "password": "Password@1315"
}

## FORMA DU DATA à ENVOYER AU COURS D'UNE CONNEXION à UN COMPTE ##
user_login = {
    "username": "gogochristian009@gmail.com",
    "password": "Password@1315"
}

## FORMA DU DATA à ENVOYER AU COURS D'ENVOIE DE MESSAGE PAR UN CLIENT ##
chat_client = {
    "user": 2,
    "message":"Le lorem ipsum est, en imprimerie, une suite de mots sans signification utilisée à titre provisoire pour calibrer une mise en page, le texte définitif venant remplacer le faux-texte dès qu'il est prêt ou que la mise en page est achevée"
}

## FORMA DU DATA à ENVOYER AU COURS D'ENVOIE DE MESSAGE PAR UN CLIENT ##
avatar = {
    "avatar":"https://www.shutterstock.com/image-photo/portrait-positive-guy-specialist-sit-600w-1836307192.jpg"
}

### FORMA DU DATA à ENVOYER AU COURS DE LA REINITIALISATION D'UN MOT DE PASSE ###
reset_password ={
    "email": "gogochristian009@gmail.com" ##Ici l'utilisateur doit entrer l'email avec lequel il avait créer son  compte,
}

### FORMA DU DATA à ENVOYER AU COURS DE LA CONFIRMATION DE LA REINITIALISATION D'UN MOT DE PASSE ###
confirm_reset_password ={
    "token": "becfec3df849",## Ici l'utilisateur doit entrer le Token qui lui a été envoyer par mail
    "password":"gogo@123" ## Ici l'utilisateur doit entrer son nouveau password qu'il veut utiliser désormais
}

### FORMA DU DATA à ENVOYER AU COURS DE LA CREATION D'UN PROFIL ###

profil = {
    'user':2, ## Ici il nous utilisons l'ID du user## Cet ID se retouve dans le JSON data renvoyé au client lors de la creation de compte 
    "nom":"Setoh",
    "prenom":"Victoire",
    "telephone":"6589654521",
    "email":'setoh@gmail.com',
    "profession":'Ingénieur',
    "pays":'Bénin',
    "ville":'Cotonou',
    "quartier":"Finanfa"
}


### FORMA DU DATA à ENVOYER AU COURS D'UNE SIMULATION ##
simulation = {
    "localisation":'cotonou',
    "product_type":'Lourd',
    "delivery_point":'Parakou',
    "delivery_delay":'3 jours',
}

### FORMA DU DATA à ENVOYER AU COURS DE L'ENREGISTREMENT D'UN PARTENARIAT ##
partenariat = {
    "nom":"Bobo",
    "prenom":"Deg",
    "denomination":"Chine",
    "email":"bobmanou@gmail.com",
    "typ":"Signalisation",
    "object":"porto-novo",
    "lettre":"Le lorem ipsum est, en imprimerie, une suite de mots sans signification utilisée à titre provisoire pour calibrer une mise en page, le texte définitif venant remplacer le faux-texte dès qu'il est prêt ou que la mise en page est achevée. Généralement, on utilise un texte en faux latin, le Lorem ipsum ou Lipsum",
}


## FORMA DU DATA à ENVOYER AU COURS DE L'ENREGISTREMENT D'UN CONTACT ##
contact = {
    "nom":"Bobo Contact",
    "prenom":"Deg contact",
    "telephone":"Chine contact",
    "message":"Le lorem ipsum est, en imprimerie, une suite de mots sans signification utilisée à titre provisoire pour calibrer une mise en page, le texte définitif venant remplacer le faux-texte dès qu'il est prêt ou que la mise en page est achevée. Généralement, on utilise un texte en faux latin, le Lorem ipsum ou Lipsum",
}

####================ CAS PRATIQUE DE L'UTILISATION DES LIENS =============#######

# follow_code = '2'

url = "http://api.fedrelay.com/user/login" # 49d59c6796fcc8617683d07a784a273ae122b8d84527b4e36f1ece25f93a3697

## FORMA DE REQUEST à UTILISER POUR LES REQUESTS POST
response = requests.post(url,json=user_login) 

## FORMA DE REQUEST à UTILISER POUR LES REQUESTS GET
# response = requests.get(url) 

## AFFICHAGE DES RESULTATS DES REQUETES
print(response.json())
print(response.status_code)
