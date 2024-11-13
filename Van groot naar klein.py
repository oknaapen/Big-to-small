def van_groot_naar_klein(reeks):
# Sorteer de reeks in aflopende volgorde
   gesorteerde_reeks = sorted(reeks, reverse=True)
   print("Dit is de volgorde van groot naar klein:")
     for i in gesorteerde_reeks: print(i)

# Roep de functie aan met een lijst van getallen
 van_groot_naar_klein([2, 3, 4, 5, 55, 6, 5, 3, 3, 45, 5, 5, 3, 4, 3])
