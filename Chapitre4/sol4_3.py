# Ecrivez juste la fonction plus_grand_bord()
# Si il y a pas de bord, la fonction retourne une chaine vide

def plus_grand_bord(w):
    res = ""
    sol = []
    for i in range(int(len(w)/2)+1):
        if w[0:i+1] == w[-i-1:]:
            sol.append(w[0:i+1])
    if sol != []:
        res = sol[-1]
    return res