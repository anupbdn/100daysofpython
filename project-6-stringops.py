def username_generator(first_name,last_name):
  if len(first_name)<3 and len(last_name)<4:
    username = first_name + last_name
  elif len(first_name)<3 and len(last_name)>4:
    username = first_name + last_name[:4]
  elif len(first_name)>3 and len(last_name)<4:
    username = first_name[:3] + last_name
  else:
    username = first_name[:3] + last_name[:4]
  return username


username = print(username_generator('anup','chinnu'))

def password_generator(username):
  password=""
  x = (len(username)) - 1
  for i in range(-1,x,1):
    password += username[i]
  return password

print(password_generator('anuchin'))
