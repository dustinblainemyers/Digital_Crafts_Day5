#python nested dictionaries exercise

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

# get email address of ramit
print(ramit['email'])


# write expression that gets first of Ramit's interests

print(ramit['interests'][0])

# write a python expression that gets the email address of Jasmine

print(ramit['friends'][0]['email'])

# write a python expression that gets the second of Jan's two interests.

print(ramit['friends'][1]['interests'][1])
