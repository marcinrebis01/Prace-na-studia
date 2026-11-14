# Dane wejściowe z tabeli: słownik (nazwa lotniska: liczba pasażerów w mln)
airports = {
    "Boston Logan (BOS)": 36.3,
    "Charlotte Douglas (CLT)": 44.4,
    "Chicago O'Hare (ORD)": 78.0,
    "Dallas/Ft. Worth (DFW)": 65.7,
    "Denver (DEN)": 58.3,
    "Detroit Metropolitan (DTW)": 34.4,
    "Hartsfield-Jackson Atlanta (ATL)": 104.2,
    "Houston George Bush (IAH)": 41.6,
    "Las Vegas McCarran (LAS)": 47.5,
    "Los Angeles (LAX)": 80.9,
    "Miami (MIA)": 44.6,
    "Minneapolis/St. Paul (MSP)": 37.4,
    "New York John F. Kennedy (JFK)": 59.1,
    "Newark Liberty (EWR)": 40.6,
    "Orlando (MCO)": 41.9,
    "Philadelphia (PHL)": 36.4,
    "Phoenix Sky Harbor (PHX)": 43.3,
    "San Francisco (SFO)": 53.1,
    "Seattle-Tacoma (SEA)": 45.7,
    "Toronto Pearson (YYZ)": 44.3
}

# a) Najbardziej i najmniej ruchliwe lotnisko
busiest_airport = max(airports, key=airports.get)
least_busy_airport = min(airports, key=airports.get)

print("--- PODPUNKT A ---")
print(f"Najbardziej ruchliwe lotnisko: {busiest_airport} -> {airports[busiest_airport]} mln")
print(f"Najmniej ruchliwe lotnisko:   {least_busy_airport} -> {airports[least_busy_airport]} mln\n")

# b) Rozkład liczebności (przedziały co 10, od 30 do 109.9)
# Tworzymy listę dolnych granic przedziałów: 30, 40, 50, ..., 100
bins_start = list(range(30, 110, 10))
frequencies = {start: 0 for start in bins_start}

# Zliczamy, ile lotnisk wpada do każdego przedziału
for passengers in airports.values():
    for start in bins_start:
        if start <= passengers < start + 10:
            frequencies[start] += 1
            break

print("--- PODPUNKT B: ROZKŁAD LICZEBNOŚCI ---")
print(f"{'Przedział':<15} | {'Liczebność':<12} | {'Procent'}")
print("-" * 42)
total = len(airports)
for start, count in frequencies.items():
    label = f"{start} - {start + 9.9}"
    percent = (count / total) * 100
    print(f"{label:<15} | {count:<12} | {percent:.0f}%")

# c) Histogram tekstowy w konsoli
print("\n--- PODPUNKT C: HISTOGRAM ---")
for start, count in frequencies.items():
    label = f"{start} - {start + 9.9}"
    bar = "█" * (count * 2)  # Każdy pasażer/lotnisko to 2 klocki dla czytelności
    print(f"{label:<15} | {bar} ({count})")