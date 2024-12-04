#Advent of Code Day1
with open ('/home/sanktem/Desktop/Scripting/AdventofCode/Day1/data.txt', 'r') as f:

    elf_count = []
    elf_total = []
    line = f.readlines()
    for cal in line:
        if cal.strip() == '':
            elf_sum = sum(elf_count)
            elf_total.append(elf_sum)
            elf_count.clear()
            continue
        else:
            elf_count.append(int(cal.strip()))

    elf_total.sort(reverse=True)
    print('PartOne:', max(elf_total))
    print('PartTwo:', elf_total[0] + elf_total[1] + elf_total[2])