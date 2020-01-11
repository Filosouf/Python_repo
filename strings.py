# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name ='Soufian'
age = 22

# Inserting variable into string
print('Hei, jeg heter ' + name + ' og jeg er ' + str(age))

# String Formatting

# Argument basert på plassering
# print('Jeg heter {name} og jeg er {age}'.format(name=name,age=age))

# F-Strings (bare tilgjengelig ved 3.6+ python)
# print(f'Hei, jeg heter {name} og jeg er {age} år gammel')

# String Methods

s = 'heisann verden'

# Store bokstaver for string
print(s.capitalize())

# Store Bokstaver for alt
print(s.upper())

# Bare små bokstaver
print(s.lower())

# Hent lengde
print(len(s))

# Erstatt
print(s.replace('verden', 'alle sammen!'))

# Tell antall
sub = 'h'
print(s.count(sub))

# Om variabel starter med
print(s.startswith('heisann'))

# om variabel ender med
print(s.endswith('verden'))

# Splitter i en liste
print(s.split())

# Finner posisjon
print(s.find('n'))