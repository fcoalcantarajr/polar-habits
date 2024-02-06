fez = [1, 1, -1, -1, 1]
pontos_se_fez = []
pontos_se_nao_fez = []

soma_pontos_se_fez = []
soma_pontos_se_nao_fez = []

soma_total = []

soma_se_fez = 0
soma_se_nao_fez = 0
soma_geral_se_fez = 0
soma_geral_se_nao_fez = 0

for ponto in fez:
    velha_soma_se_fez = soma_se_fez
    if ponto == 1:
        soma_se_fez = soma_se_fez + ponto
    if soma_se_fez > velha_soma_se_fez:
        pontos_se_fez.append(soma_se_fez)
    else:
        pontos_se_fez.append(None)

for nao_ponto in fez:
    velha_soma_se_nao_fez = soma_se_nao_fez
    if nao_ponto == -1:
        soma_se_nao_fez = soma_se_nao_fez + nao_ponto
    if soma_se_nao_fez < velha_soma_se_nao_fez:
        pontos_se_nao_fez.append(soma_se_nao_fez)
    else:
        pontos_se_nao_fez.append(None)

for soma_ponto in pontos_se_fez:
    if soma_ponto == None:
        soma_ponto = 0
    soma_geral_se_fez = soma_geral_se_fez + soma_ponto
    soma_pontos_se_fez.append(soma_geral_se_fez)

for soma_nao_ponto in pontos_se_nao_fez:
    if soma_nao_ponto == None:
        soma_nao_ponto = 0
    soma_geral_se_nao_fez = soma_geral_se_nao_fez + soma_nao_ponto
    soma_pontos_se_nao_fez.append(soma_geral_se_nao_fez)

tam = len(soma_pontos_se_fez)

for i in range(tam):
    soma_final = soma_pontos_se_fez[i] + soma_pontos_se_nao_fez[i]
    soma_total.append(soma_final)

print(pontos_se_fez)
print(pontos_se_nao_fez)
print(soma_pontos_se_fez)
print(soma_pontos_se_nao_fez)
print(soma_total)