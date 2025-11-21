pao_frances = 0.75
broa = 1.50

quant_paes = int(input("Quantos pães franceses você deseja? "))
quant_broas = int(input("Quantas broas você deseja? "))

total_paes = quant_paes * pao_frances
total_broas = quant_broas * broa
total_geral = total_paes + total_broas

print("Total a pagar: R$", total_geral)
