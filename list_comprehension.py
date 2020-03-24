temps = [221, 234, -340, -9999, 230]

new_temps = []

for temp in temps:
    new_temps.append(temp / 10)

print(new_temps)

new_temps2 = [temp / 10 for temp in temps]
print(new_temps2)

new_temps2 = [temp / 10 for temp in temps if temp != -9999]
print(new_temps2)

new_temps2 = [temp / 10 if temp != -9999 else 0 for temp in temps]
print(new_temps2)


def foo(*args):
    return [a.upper() for a in args]


print(foo('snow', 'wind'))
