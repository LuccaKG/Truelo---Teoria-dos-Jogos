import random
import pandas as pd

# script do jogo 
games_log = pd.DataFrame(columns=['Nº partida', 'Vencedor', 'Nº Rodadas até o final', 'Mr Black - 1º tiro'])

logical_win = 0 # anota em quantas vezes Mr Black ganhou errando o primeiro tiro
wins_num = {"Mr. Black": 0, "Mr. Gray": 0, "Mr. White": 0}
w_wins = g_wins = b_wins = 0 # numero de vitorias de cada um

num_partidas = int(input("Insira quantas partidas deseja simular: "))
for i in range(0, num_partidas):
  if i > 0:
    games_log.loc[len(games_log)] = [f"{i}", f"{winner}", f"{num_rodadas}", f"{b_firstshot_check}"]
  # define habilidade e status (→ 1 = vivo, 0 = morto) de cada truelista
  truel_stats = {"Mr Black Skill": 1/3, "Mr Black Status": 1, "Mr Gray Skill": 2/3, "Mr Gray Status": 1, "Mr White Skill": 1, "Mr White Status": 1}
  num_rodadas = 0
  while True:
    # verifica se o jogo acabou
    winner = str()
    if truel_stats['Mr Black Status'] == 0 and truel_stats['Mr Gray Status'] == 0 and truel_stats['Mr White Status'] == 1:
      winner = "Mr White"
      wins_num['Mr. White'] += 1
      break
    elif truel_stats['Mr Black Status'] == 0 and truel_stats['Mr Gray Status'] == 1 and truel_stats['Mr White Status'] == 0:
      winner = "Mr Gray"
      wins_num['Mr. Gray'] += 1
      break
    elif truel_stats['Mr Black Status'] == 1 and truel_stats['Mr Gray Status'] == 0 and truel_stats['Mr White Status'] == 0:
      winner = "Mr Black"
      wins_num['Mr. Black'] += 1
      if b_firstshot_check == "miss":
        logical_win += 1   # se Mr Black ganhar, anota em quantas vezes ele ganhou errando o primeiro tiro
      break

    num_rodadas += 1
    # rodada do Mr. Black
      # define um alvo
    if truel_stats['Mr Black Status'] == 1: # verifica se mr Black esta vivo
      if truel_stats['Mr Gray Status'] == 1 and truel_stats['Mr White Status'] == 1: # verifica se os outros dois estao vivos
        mrblack_target = "Mr White" if random.random() < 0.55 else "Mr Gray" # como Mr White é o mais habilidoso, colocamos 55% de chance de ser o alvo, caso vivo
      # se um dos outros dois estiver morto, obviamente o alvo será o restante
      elif truel_stats['Mr Gray Status'] == 0:
        mrblack_target = "Mr White"
      elif truel_stats['Mr White Status'] == 0:
        mrblack_target = "Mr Gray"
      # atira com chance de 1/3 de acertar
      if random.random() < 1/3:
        truel_stats[f"{mrblack_target} Status"] = 0
        if num_rodadas == 1:
          b_firstshot_check = "kill"
      else:
        if num_rodadas == 1:
          b_firstshot_check = "miss"  # verifica se Mr Black errou o primeiro tiro

    # rodada do Mr. Gray
      # define um alvo
    if truel_stats['Mr Gray Status'] == 1: # verifica se mr Gray esta vivo
      if truel_stats['Mr Black Status'] == 1 and truel_stats['Mr White Status'] == 1: # verifica se os outros dois estao vivos
        mrgray_target = "Mr White" if random.random() < 0.55 else "Mr Black" # como Mr White é o mais habilidoso, colocamos 55% de chance de ser o alvo, caso vivo
      # se um dos outros dois estiver morto, obviamente o alvo será o restante
      elif truel_stats['Mr Black Status'] == 0:
        mrgray_target = "Mr White"
      elif truel_stats['Mr White Status'] == 0:
        mrgray_target = "Mr Black"
      # atira com chance de 2/3 
      truel_stats[f"{mrgray_target} Status"] = 0 if random.random() < 2/3 else 1

    # rodada do Mr. White
      # define um alvo
    if truel_stats['Mr White Status'] == 1: # verifica se mr White esta vivo
      if truel_stats['Mr Black Status'] == 1 and truel_stats['Mr Gray Status'] == 1: # verifica se os outros dois estao vivos
        mrwhite_target = "Mr Gray" if random.random() < 0.55 else "Mr Black" # como Mr Gray é o mais habilidoso restante, colocamos 70% de chance de ser o alvo, caso vivo
      # se um dos outros dois estiver morto, obviamente o alvo será o restante
      elif truel_stats['Mr Black Status'] == 0:
        mrwhite_target = "Mr Gray"
      elif truel_stats['Mr Gray Status'] == 0:
        mrwhite_target = "Mr Black"
      # atira com 100% de chance
      truel_stats[f"{mrwhite_target} Status"] = 0 
  
# script das estatisticas gerais

sorted_winners = sorted(wins_num, key= wins_num.get, reverse=True)
print("*"*100)
print("\nPódio\n")
print(f"1º -  {sorted_winners[0]} → {wins_num[f'{sorted_winners[0]}']} vitória(s)")
print(f"2º -  {sorted_winners[1]} → {wins_num[f'{sorted_winners[1]}']} vitória(s)")
print(f"3º -  {sorted_winners[2]} → {wins_num[f'{sorted_winners[2]}']} vitória(s)\n")

perc_logiwin = round((logical_win/wins_num['Mr. Black'])*100, 2)
print(f"Número de vitórias do Mr. Black utilizando a melhor estratégia: {logical_win} → {perc_logiwin}% do total individual\n")
print("*"*100)

# script das estatisticas individuais
print(games_log)