ticket = input()


part1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])

part2 = int(ticket[-3]) + int(ticket[-2]) + int(ticket[-1])

if part1 == part2:
    print('Счастливый')
else:
    print('Обычный')
