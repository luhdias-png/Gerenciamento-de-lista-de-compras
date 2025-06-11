import emoji

n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digite sua segunda nota:'))
media = (n1 + n2) / 2

if media >= 9.5:
    print (emoji.emojize(f'O aluno foi :mãos_aplaudindo::rosto_festivo:APROVADO COM LOUVOR!!!:rosto_festivo::mãos_aplaudindo: Sua nota foi {media}', language= 'pt'))
elif media >= 7 and media <= 9:
    print (emoji.emojize(f'O aluno foi :mãos_aplaudindo:APROVADO!!!:mãos_aplaudindo: Sua media foi de {media}!', language= 'pt'))
elif media >=5 and media <=6.5:
    print (emoji.emojize(f'O aluno ficou de :rosto_preocupado:RECUPERÇÃO!:rosto_preocupado: Sua media foi de {media}!', language='pt'))
elif media <5:
    print (emoji.emojize(f'O aluno foi :rosto_chorando_aos_berros:REPROVADO!:rosto_chorando_aos_berros:Sua media foi de {media}', language= 'pt'))