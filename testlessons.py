def divisible_by_ten(nums):
    x = [i for i in nums if i%10 == 0]
    return len(x)

print(divisible_by_ten([20, 25, 30, 35, 40]))

user_options = input("""
Welcome to 'The 100 Days of Code Slack Channel'
1. Learn Python
2. Learn Linux
3. Learn Automation

Enter selection:
""")


def reversed_list(lst1, lst2):
    if lst2 == lst1[::-1]:
        return True
    else:
        return False

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))


name1 = 'Anup'
name2 = 'Badharudheen'

x = name1[len(name1)-3:] + name2[len(name2)-3:]

print(x)
