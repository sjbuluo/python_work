person = {
	'first_name' : 'Jina',
	'last_name' : 'Sun',
	'age' : 25,
	'city' : 'TaiZhou'
}

print(person)

for item in person:
	print(item, person[item])


for item in sorted(person):
	print(item, person[item])
