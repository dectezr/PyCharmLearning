# create the planets.txt
solar_system = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
file = open("planets.txt", "w", encoding="utf-8")
file.writelines([x + '\n' for x in solar_system])
file.close()
