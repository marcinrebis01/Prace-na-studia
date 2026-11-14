# Środki przedziałów wiekowych
midpoints = [22, 29.5, 39.5, 49.5, 59.5]

# Liczba bezrobotnych w tysiącach (kolejno dla przedziałów)
women = [524.3, 455.1, 382.8, 132.0, 13.1]
men = [471.7, 369.6, 346.3, 152.2, 43.5]

# a) Średni wiek kobiet
total_women = sum(women)
sum_women_prod = sum(m * w for m, w in zip(midpoints, women))
mean_women = sum_women_prod / total_women

# a) Średni wiek mężczyzn
total_men = sum(men)
sum_men_prod = sum(m * man for m, man in zip(midpoints, men))
mean_men = sum_men_prod / total_men

print("--- PODPUNKT A ---")
print(f"Średni wiek bezrobotnych kobiet:   {mean_women:.2f} lat")
print(f"Średni wiek bezrobotnych mężczyzn: {mean_men:.2f} lat")

# b) Średni wiek ogółem
total_people = total_women + total_men
sum_total_prod = sum_women_prod + sum_men_prod
mean_total = sum_total_prod / total_people

print("\n--- PODPUNKT B ---")
print(f"Przeciętny wiek bezrobotnych ogółem: {mean_total:.2f} lat")