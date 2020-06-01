varer =	{
  "melk" :  14.90,
  "brød": 24.90,
  "yoghurt": 12.90,
  "pizza":39.90
}
teller = 0
print(varer)
print("skriv in  varer med pris ")
#loop for input
while teller <2:
    vare = input("Vare navn: ")
    pris = input("pris: ")
    if vare.lower() in varer :
        print("Varen er allerede i systemet")
    elif pris.isdigit()==False:
        print("Invalid Input: pris må være et tall")
    else:
        varer[vare.lower()] = pris
    teller +=1
print(varer)
