txt = 'Curoso em Viodeo de Poython'

print(f"se eu quiser escrever assim.{txt.count('o')}")#Usar aspas simples dentro de uma f-string que já está delimitada por aspas simples. causara conflito

print(f"Combinando metocos de string com outra.{txt.upper().count('o')}")

print(f"Combinando metocos de string com outra.{txt.split().count('em')}")