with open('sal.txt.txt', 'r') as my_file:
    lines = my_file.readlines()

salaries =[]
for line in lines:
    name, salary = line.split(' - ')
    salaries.append(int(salary))
    if int(salary) < 20000:
        print(line, end=" ")
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')
