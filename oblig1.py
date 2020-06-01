#Oppgave 1: Utskrift og innlesing med variabler

#1.2
print("--Oppgave 1: Utskrift og innlesing med variabler--")
print("Hei Student")
#1.3
navn = input("Hva heter du? ")
print("hei", navn)
#1.4
var1=20
var2=10
print("var1=",var1)
print("var2=",var2)
#1.5
differance=var1-var2
print("differance=", differance)
#1.6
nyttnavn=input("nytt navn? ")
sammen = navn + nyttnavn
print("sammensatt navn", sammen)
#1.7
sammen2 = navn+" "+"og"+" "+nyttnavn
print(sammen2)

#Oppgave 2: Beslutninger

svar=input("Har du lyst på en brus? ")

if svar=="ja":
    print("Her har du en brus")
elif svar=="nei":
    print("Den er grei")
else:
    print("Det forsto jeg ikke helt")

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
