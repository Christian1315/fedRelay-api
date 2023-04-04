import random
list = ["A","B","C","D","E","F","G","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
letter_rand = random.choice(list)
rand = random.randint(0,10000)

def getFollowCode(client_id):
    return "R"+str(client_id)+str(rand)+letter_rand ### CODE DE SUIVI
