def f_to_c(f_temp):
  c_temp=(f_temp-32) * 5/9
  return c_temp
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)


def get_force(mass,acceleration):
  return mass*acceleration



train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

train_force = get_force(train_mass,train_acceleration)

print(train_force)

print(f'The GE train supplies {train_force} Newtons of force')



def get_work(mass,acceleration,distance):
  return get_force(mass,acceleration) * distance


work = get_work(3,2,6)

print(f'work is {work}')



def dog_years(name,age):
  x=age*7
  return (name+','' '+ 'you are'+' '+ str(x) +' ' 'years old in dog years')
# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
