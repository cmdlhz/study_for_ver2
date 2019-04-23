from space.planet import Planet
from space.calc import planet_mass, planet_vol

hoth = Planet('Hoth', 200000, 5.5, 'Hoth System')
naboo = Planet('Naboo', 300000, 8, 'Naboo System')

naboo_mass = planet_mass(naboo.gravity, naboo.radius)
naboo_vol = planet_vol(naboo.radius)

print(f'{naboo.name} has a mass of {naboo_mass} and a volumn of {naboo_vol}.')