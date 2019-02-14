documentaries = "Finding The Lost"
comedies = "Forever 18"
dramas = "Batman Forever"
dramedy = "Don't Stop That Clock"

print("Please rate your most liked genre from 1 - 5.")

print("Please rate documentaries")
doc_rating = input() 

print("Please rate comedies")
com_rating = input()

print("Please rate dramas")
dra_rating = input()


if int(doc_rating) >= 4 and int(com_rating) <= 3 and int(dra_rating) <= 3:
   	print("You should watch {}.".format(documentaries)) 
   	
elif int(doc_rating) <= 3 and int(com_rating) >= 4 and int(dra_rating) >= 4:
	print("You should watch {}.".format(dramedy))

elif int(doc_rating) <= 3 and int(com_rating) <= 3 and int(dra_rating) >= 4:
	print("You should watch {}.".format(dramas))

elif int(doc_rating) <= 3 and int(com_rating) >= 4 and int(dra_rating) <= 3:
	print("You should watch {}.".format(comedies))

else:
	print("You should read 'Climbing Towers. It's a good book :).")