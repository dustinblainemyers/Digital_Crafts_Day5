phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

#print Elizabeth's phone number
print(phonebook_dict['Elizabeth'])

#add entry to the dictionary :

phonebook_dict['Kareem'] = "938-489-1234"

#make sure there is an entry for Kareem now

print(phonebook_dict['Kareem'])

#see where the dictionary is at now

print(phonebook_dict)

# delete Alice's entry

del phonebook_dict['Alice']

# make sure it deleted
print(phonebook_dict)

phonebook_dict['Bob'] = '968-345-2345'

print(phonebook_dict)


#print all phone entries

print(phonebook_dict.keys(), end=" :")
print (phonebook_dict.values())

