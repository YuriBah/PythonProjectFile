with open('test.txt') as my_f:
    lines = my_f.readlines()
print('Количество строк: ', len(lines))
for one_line, line in enumerate(lines, start=1):
    print('{} содержит - {} слов'.format(one_line, len(line.split())))