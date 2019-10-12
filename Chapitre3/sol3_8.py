# Ecrivez juste la fonction duree()


def duree(h1, h2):
	res =  (h2[0] - h1[0], h2[1] - h1[1])
	if res[0] < 0:
		res = (24 + res[0], res[1])
		if res[1] < 0:
			res = (res[0], 60 + res[1])
	elif res[1] <0 :
		res = (res[0], 60 + res[1])
	return res
