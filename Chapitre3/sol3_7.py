# Ecrivez juste la fonction rendreMonnaie()

def rendreMonnaie(prix, monnaie):
	sol = None
	argent = 20*monnaie[0] + 10*monnaie[1] + 5*monnaie[2] + 2*monnaie[3] + monnaie[4]
	diff = argent - prix 
	if diff >= 0:
		if diff == 0:
			sol = (0, 0, 0, 0, 0)
		else:
			x20 = int(diff / 20)
			x10 = int((diff - 20*x20) / 10)
			x5 = int((diff - 20*x20 - 10*x10) / 5)
			x2 = int((diff - 20*x20 - 10*x10 - 5*x5) / 2)
			x1 = int((diff - 20*x20 - 10*x10 - 5*x5 - 2*x2))
			sol = (x20, x10, x5, x2, x1) 
	return sol
