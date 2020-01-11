# A List is a collection which is ordered and changeable. Allows duplicate members.

# Lister er kolleksjoner av elementer, som tillater kopieer
# Lage liste
number = [1, 2, 3, 4, 5]
frukt = ['Eple', 'Pære', 'Melon', 'Mango']

# Bruk av constructor
number2 = list((1,2,3,4,5))

# Hent Verdi
print(frukt[1])

# Hent lengde
print(len(frukt))

# Legg til i liste
frukt.append('torsk')

# Fjerne fra liste
frukt.remove('Mango')

# Legg til i plassering
frukt.insert(2, 'Jordbær')

# Rediger verdi
frukt[0] = 'Blåbær'

# Fjern med pop
frukt.pop(2)

# Reverser liste
frukt.reverse()

# Sorter liste
frukt.sort()

# Sorter reversert
frukt.sort(reverse=True)

print(frukt)