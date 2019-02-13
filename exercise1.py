documentaries = "Finding The Lost"
comedies = "Forever 18"
dramas = "Batman Forever"
dramedy = "Don't Stop That Clock"

print("Welcome To AMAS Movie Bar\n")
print("Do You Prefer Documentaries, dramas, comedies or both dramas and comedies(For both enter 'dramedy' and for no choice enter 'nothing')?")
choice = input()

if choice == "documentaries":
	print("You Should Watch {}. It's a good documentary".format(documentaries))

elif choice == "dramedy":
	print("\nYou Have Good taste. We suggest you watch {}. It's our new DRAMEDY :)".format(dramedy))

elif choice == "comedies":
	print("\nYou Should Watch {}. It's really Good.".format(comedies))

elif choice == "dramas":
	print("\nYou Should Watch {}. It is really good.".format(dramas))

	
elif choice == "nothing":
	print("\nYou Should Read 'Run With The Wild' It's a good book.")
		


else: 
	print("GoodBye!! See You Soon :)")