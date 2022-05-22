import random
import string
import requests


num = int(input('how many codes do you want to generate ? : '))


# get 19 unique chars , append to code
#write them to a file

file = open('NitroCodes.txt','w',encoding='utf-8')
for i in range(num):
    code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))
    file.write(f'https://discord.gift/{code}\n')
print(f'{num} codes were generated.')

with open('NitroCodes.txt','r') as file:
    for line in file.readlines():
        nitro = line.strip('\n')
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        r = requests.get(url)
        if r == 20:
            print(f'This code is Valid !  {nitro}')
        else :
            print(f'This code is Invalid ! {nitro}')
    




