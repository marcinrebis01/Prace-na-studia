# Zadanie 5 Ekonometria
# Dane wejściowe
X = [400, 450, 550, 600, 700, 750]  # Wielkość produkcji
Y = [4000, 5000, 5400, 5900, 6400, 7000]  # Koszty całkowite

n = len(X)

# Obliczanie sum potrzebnych do wzorów
sum_x = sum(X)
sum_y = sum(Y)
mean_x = sum_x / n
mean_y = sum_y / n

sum_x2 = sum(x**2 for x in X)
sum_xy = sum(x * y for x, y in zip(X, Y))
sum_y2 = sum(y**2 for y in Y)

# a) Wyznaczenie współczynników b1 (nachylenie) i b0 (wyraz wolny)
# Wzór na b1 (współczynnik kierunkowy / koszt zmienny)
b1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)

# Wzór na b0 (wyraz wolny / koszt stały)
b0 = mean_y - b1 * mean_x

print("--- Odpowiedzi ---")
print(f"a) Równanie regresji: Y^ = {b0:.2f} + {b1:.2f} * X")

# b) Koszt zmienny jednostkowy
print(f"b) Koszt zmienny na jedną jednostkę: {b1:.2f} $")

# c) Współczynnik determinacji R^2
# Licznik i mianownik do R^2
numerator = b1 * (sum_xy - (sum_x * sum_y) / n)
denominator = sum_y2 - (sum_y**2) / n
r_squared = numerator / denominator

print(f"c) Współczynnik determinacji (R^2): {r_squared:.4f}")
print(f"   Wyjaśniona wariancja: {r_squared * 100:.2f}%")

# d) Prognoza dla 500 jednostek
x_forecast = 500
y_forecast = b0 + b1 * x_forecast
print(f"d) Prognozowany koszt dla 500 jednostek: {y_forecast:.2f} $")