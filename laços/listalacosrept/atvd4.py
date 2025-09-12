cidadea = 90000
taxacrescimentoa = 0.035
cidadeb = 250000
taxacrescimentob = 0.012
ano = 0

while cidadea < cidadeb:
    cidadea = cidadea + (cidadea * taxacrescimentoa)
    cidadeb = cidadeb + (cidadeb * taxacrescimentob)
    ano += 1

print("A cidade A ultrapassará ou igualará a população da cidade B em", ano, "anos.")
