# Formato geral:
#   f'{valor:[caractere][alinhamento][largura]}'
# Alinhamentos:
#   <  → Alinha à ESQUERDA
#   >  → Alinha à DIREITA
#   ^  → CENTRALIZA
#
# Largura: número total de espaços (ex: 10, 20...)
# Caractere (opcional): define o preenchimento (ex: ponto, asterisco, traço...)
#=========================================================================================================
# Exemplos:
#   nome = "SONIC"
#   f'{nome:<10}'      → 'SONIC     '     # Esquerda
#   f'{nome:>10}'      → '     SONIC'     # Direita
#   f'{nome:^10}'      → '  SONIC   '     # Centralizado
#
#   f'{nome:.<10}'     → 'SONIC.....'     # Preenche com pontos
#   f'{nome:->10}'     → '-----SONIC'     # Traços à esquerda
#   f'{nome:*^12}'     → '***SONIC****'   # Centralizado com asteriscos
#
# Também funciona com números:
#   num = 42
#   f'{num:0>5}'        → '00042'         # Número com zeros à esquerda
# Dica: pode usar com input, operações e expressões também!