#Oppgave 3: Problemløsning med beslutninger
print("Type in a dates. the first should be before the former ")

date1_day= input("The day: ")
date1_month= input("The month: ")

print("The second date")
date2_day= input("The day: ")
date2_month= input("The month: ")

if date2_month < date1_month:
    print("Feil rekkefølge")
elif date1_day == date2_day and date1_month ==date2_month:
    print("Same dato")
else:
    print("Riktig rekkefølge")
