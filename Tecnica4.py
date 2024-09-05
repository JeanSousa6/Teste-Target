

SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53

soma = SP + RJ + MG + ES + Outros
porcentagemSP = 100 * SP/soma 
porcentagemRJ = 100 * RJ/soma 
porcentagemMG = 100 * MG/soma 
porcentagemES = 100 * ES/soma 
porcentagemOutros = 100 * Outros/soma 
# teste: somaPorcentagem = porcentagemSP + porcentagemRJ + porcentagemMG + porcentagemES + porcentagemOutros = 100% 


print(
    f"SP = {porcentagemSP:.2f}%",
    f"RJ = {porcentagemRJ:.2f}%",
    f"MG = {porcentagemMG:.2f}%",
    f"ES = {porcentagemES:.2f}%",
    f"Outros = {porcentagemOutros:.2f}%" 
)

