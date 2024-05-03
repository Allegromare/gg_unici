import pandas as pd

def merge_intervals(intervals):
    # Ordina gli intervalli per data
    sorted_intervals = sorted(intervals)
    merged = [sorted_intervals[0]]

    # Fonde gli intervalli sovrapposti
    for current in sorted_intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:
            merged[-1] = (previous[0], max(previous[1], current[1]))
        else:
            merged.append(current)

    # Calcola la somma delle differenze tra le date di inizio e fine
    return sum((interval[1] - interval[0]).days +1 for interval in merged)


# Supponiamo che il file Excel contenga una colonna "Start Date" e una colonna "End Date"
# Carica i dati dal file Excel nel dataframe
df = pd.read_excel("file.xlsx")

# Estrai gli intervalli di date
intervalli = [(pd.to_datetime(row["Start Date"]), pd.to_datetime(row["End Date"])) for _, row in df.iterrows()]

print(df)  # Stampa la riga 1 del DataFrame df


# Esempio di utilizzo
# intervalli = [(pd.to_datetime('2024-04-10'), pd.to_datetime('2024-04-15')),
#               (pd.to_datetime('2024-04-12'), pd.to_datetime('2024-04-18')),
#               (pd.to_datetime('2024-04-20'), pd.to_datetime('2024-04-22'))]

# print(intervalli)

# risultato = merge_intervals(intervalli)
# print(f"I giorni unici negli intervalli sono: {risultato}")
