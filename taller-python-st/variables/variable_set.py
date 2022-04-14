# variable set

conjunto_skills = {'python', 'c++', 'javascript', 'python'}
conjunto_areas = {'web', 'iot'}

print(conjunto_skills)
print(len(conjunto_skills))
print(dir(conjunto_skills))

conjunto_skills.add('golang')
print(conjunto_skills)
conjunto_skills.update(conjunto_areas)
print(conjunto_skills)
conjunto_skills.pop()
print(conjunto_skills)
