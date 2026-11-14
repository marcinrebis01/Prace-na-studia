# Dane wejściowe: wydatki na reklamę w miliardach dolarów
spending = [5.00, 3.08, 2.91, 2.56, 2.44, 2.34, 2.19, 2.15, 2.09, 1.97, 1.96, 1.88]

# Krok 1: Sortowanie danych rosnąco
sorted_data = sorted(spending)
n = len(sorted_data)

print("Posortowane dane:", sorted_data)
print("-" * 50)

# a) Średnia arytmetyczna
mean_val = sum(sorted_data) / n
print(f"a) Średnia wydatków: {mean_val:.2f} mld $")

# b) Mediana
if n % 2 == 1:
    median_val = sorted_data[n // 2]
else:
    mid1 = sorted_data[(n // 2) - 1]
    mid2 = sorted_data[n // 2]
    median_val = (mid1 + mid2) / 2

print(f"b) Mediana wydatków: {median_val:.2f} mld $")

# c) Kwartyle (Q1 i Q3)
# Dzielimy dane na dolną i górną połowę
lower_half = sorted_data[:n // 2]
upper_half = sorted_data[n // 2:]

def find_median(sublist):
    m = len(sublist)
    if m % 2 == 1:
        return sublist[m // 2]
    else:
        return (sublist[(m // 2) - 1] + sublist[m // 2]) / 2

q1 = find_median(lower_half)
q3 = find_median(upper_half)

print(f"c) Pierwszy kwartyl (Q1): {q1:.2f} mld $")
print(f"   Trzeci kwartyl (Q3): {q3:.2f} mld $")