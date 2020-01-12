# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Lage tuppel
# frukt = ('Eple', 'Klementin', 'Druer')
# frukt2 = tuple(('Eple', 'Klementin', 'Druer'))

# Enkle verdier trenger komma for å gjenkjennes som tuppel
frukt2 = ('Eple',)

# Hent verdi
# print(frukt[1])

# Verdier kan ikke endres
# frukt[0] = 'Pære'

# Slette tuppel
del frukt2

# Hent Lengde
# print(len(frukt))



# A Set is a collection which is unordered and unindexed. No duplicate members.

# Lage sett
frukt_sett = {'Eple', 'Klementin', 'Mango'}

# Sjekk hvis noe er i et sett
print('Eple' in frukt_sett)

# Legg til i sett
frukt_sett.add('Druer')

# Fjerne element
frukt_sett.remove('Druer')

# Tøm sett
frukt_sett.clear()

# Slett sett
del frukt_sett

print(frukt_sett)
