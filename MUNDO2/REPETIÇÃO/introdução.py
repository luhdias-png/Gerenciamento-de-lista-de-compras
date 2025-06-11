#imagine um boneco indo ate uma macã, ele precisar passar por 6 blocos de espaços pra chegar la e pegar a maça.
#Vamos dar o comando PASSO para chegar ate la: passo, passo, passo, passo, passo, pegar.(todo esse comando que demos para o boneco é chamado de: ALGORITMO)
#agora imagine que ao inves de ser 6 blocos fossem 500 blocos? Nao seria bonito dar 500 * o comando "passo" no algoritmo. Entao como resolver?
#Vamos usar o comando que toda linguagem possui, incluindo PYTHON. Ela se chama: LAÇO.
#Vamos usar agora o mesmo exemplo, porem com 500 blocos de distancia. 
#Imagine que vou colocar um simbolo de infinito (∞) dentro dele o comando "passo", iria fazer o boneco andar infinitos passos deixando a maça e caindo no limbo.
#Entao para resolver isso temos que colocar qts * o boneco vai repetir "passo" ate chegar na maça, que no caso é 500.
#entao ficaria: ∞ (passo = 1 → 500, pegar.). O repetidor teve um limite de vezes que iria repetir o comando "passo" de 1 a 500 e iria parar o comando. Ddps foi dado o comando pegar.
#O NOME QUE DISSO É: "LAÇO DE ITERAÇÃO/REPETIÇÃO". ESSE LAÇO QUE USAMOS NO EXEMPLO DA O NOME DE: "LAÇO DE VARIAVEL COM CONTROLE."
#como seria codado(maneira simples para entender):
'''
laço c[variavel de controle = da o nome que quiser ao inves de "C".] no intervalo(1,500):
    passo[Tem que dar esses espaços igual em condiçoes de if. O nome desse espaço é IDENTAÇÃO.
pega[O comando pega esta fora do laço para poder realizar a ação pegar sem a necessidade de loop. Se ela estivesse dentro da IDENTAÇÃO de passo(logo embaixo dela) ele estaria fazendo parte do laço]'''
#ou seja, ele iria sempre andar 500 passos e ao final da contagem a ação de pegar infinitas *.
#Como seria codado em Python:
'''
for c in range(1,500):
    passo
pega
#fim do code
'''
#Agora daremos outro exemplo como a mesma que usamos acima so que diferente.
#Imagine que o menino tem que andar 10 casas a frente para pegar a maça, so que a cada 2 passos havera uma queda. Como resolver?
#vamos dar o comando: passo, dps o comando pula, passo pula, passo pula. Se der o comando passo ele chega na maça e ao inves de darmos comando pula, daremos o comando pegar.
#O comando passo e pulo foi repetido 3* dps ele da passo pega.
#Vamos fazer assim: dentro de ∞ colocaremos passo pula. Se nao colocar limite o PASSO PULA vai ficar repetindo eternamente. Entao daremos um limete que seria:(∞ → 0,3. passo pegar).
#Como seria codado:
'''
for c in range(0,3):
    passo
    pula
passo
pega
'''
 #Agora usando o mesmo exemplo, vamos adicionar moedas para ser pega no caminho. e vamos usar uma estrutura de controle condicional = if para pegar a moeda SE existir uma no caminho.
'''_Atenção aos niveis de identação:
for c in range(0,3):
    if moeda #_primeiro nivel=esta dentro do comando laço(for)
        pegar #_Segundo nivel=Esta dentro do controle SE(if) OU seja se no meio do caminho haver moeda ele vai pegar, se nao o laço repete normalmente sem o if.
    passo #_Rodando normalmente
    pula #_ Ronando normalmente
passo #_ Sai do laço(for) e age de forma idependente.
pula #_ Sai do laço(for) e age de forma idependente.
'''
