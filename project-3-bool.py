def ground_shipping(weight):
  if weight <= 2:
    cost_ground_shipping = 1.50 * weight + 20
  elif weight > 2 and weight <= 6:
    cost_ground_shipping = 3.00 * weight + 20
  elif weight >= 6 and  weight <= 10:
    cost_ground_shipping = 4.00 * weight + 20
  elif weight > 10:
    cost_ground_shipping = 4.75 * weight + 20
  return cost_ground_shipping



cost_premium_ground_shipping = 125

def drone_shipping(weight):
  if weight <= 2:
    cost_drone_shipping = 4.50 * weight
  elif weight > 2 and weight <= 6:
    cost_drone_shipping = 9.00 * weight
  elif weight > 6 and weight <= 10:
    cost_drone_shipping = 12 * weight
  elif weight > 10:
    cost_drone_shipping = 14.25 * weight
  return cost_drone_shipping

def cheapest_shipping(weight):
    ground = ground_shipping(weight)
    drone = drone_shipping(weight)
    premium = cost_premium_ground_shipping

    if ground < drone and ground < premium:
        print (f'ground shipping is cheap with {ground} price')
    elif drone < ground and drone < premium:
        print(f'drone shipping is cheap with {drone}price')
    elif premium < ground and premium < drone:
        print(f'premium is cheap with {premium} price')







ground_shipping(8.4)


ground_shipping(8.4)


print(drone_shipping(1.5))

cheapest_shipping(8.4)
