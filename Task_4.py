# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10


S = int(input("Введите общее число журавликов: "))
# S = Piter + Kate + Serj                               строки 13-18 рассуждения от куда взялось S/6
# Kate = (Piter + Serj) * 2
# Piter = x
# Piter == Serj 
# S = x + (2x * 2) + x
# S = 6x
Piter = Serj = int(S / 6)                  
Kate = Piter * 4
print(f"{S} -> {Piter} {Kate} {Serj}")