Fahrenheit = 70
#Kan bare sette sammen str i en print stream, derfor bruker jeg str()
print("Fahrenheit er " + str(Fahrenheit))
celcius = (Fahrenheit - 32) * (5/9)
print("celcius er " + str(round(celcius)))
bruker_input = input( "Tast inn temp i Fahrenheit: " )
tall = int(bruker_input)
cel2 = (tall - 32) * (5/9)
print("temp du tastet in  er " + str(cel2) + " i celcius")
