#oppgave 5
"""
oppgave 5:
1. Lag to ordbok og fyll med verdier
2. sett sammen begge ordbøkene
3. Print ut nye ordboken.
"""
ordbok1 =	{
  1 :  14,
  2 : 24,
  3 : 12,
  4: 39
}
ordbok2 =	{
  5 :  4,
  6 : 2,
  7 : 1,
  8: 3
}
ordbok3 = {}
for d in (ordbok1, ordbok2):
    ordbok3.update(d)
print(ordbok3)
