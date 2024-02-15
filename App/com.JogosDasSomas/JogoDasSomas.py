'''/**********************************************************************************
Autor: Luis Felipe Cunha Silva
Componente Curricular: MI algoritmos 
Concluido em:11/11/2022
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum 
trecho de código de colega ou de outro autor, tais como provindos de livros e apostilas
, e páginas ou documentos eletrônicos da internet. Qualquer trecho de código de outra
autoria que não a minha está destacado com uma citação do autor e a fonte do código, e estou 
ciente que estes trechos não serão considerados para fins de avaliação.
/*************************************************************************************'''

import random

def criar_tabuleiro_dificil():
    '''Cria as secoes do tabuleiro gerado com os numeros aleatórios para o modo dificil(9x9)
        -Parametros:
        Nenhum
        -retorno:
        matriz secao com os numeros de 1 a 9 randomizados
    '''
    s1 = random.sample(range(1,10),9)
    s2 = random.sample(s1, 3)
    for i in s2:
        s1.remove(i)
    s3 = random.sample(s1, 3)
    for i in s3:
        s1.remove(i)
    matriz = [s1,s2,s3]
    return matriz

def criar_tabuleiro_facil():
    '''Cria as secoes do tabuleiro gerado com os numeros aleatórios para o modo facil(4x4)
        -Parametros:
        Nenhum
        -retorno:
        matriz secao com os numeros de 1 a 4 randomizados
    '''
    s1 = random.sample(range(1,5),4)
    s2 = random.sample(s1,2)
    for i in s2:
        s1.remove(i)
    matriz = [s1,s2]
    return matriz

def criar_tab_resposta(escolha):
    '''Cria as secoes do tabuleiro resposta(zerado)
        -Parametros:
        nivel de jogo
        -retorno:
        matriz secao resposta zerada
    '''
    if escolha == '2':
        n = 3
    elif escolha == '1':
        n = 2
    matrizj = [ [ 0 for i in range(n)] for j in range(n)]
    return matrizj

def soma_linhas(secao):
    '''Realiza a soma das linhas por secao
        -Parametros:
        secao gerada nas funcoes criar_tabuleiro_facil e criar_tabuleiro_dificil
        -retorno:
        lista contendo os valores da soma de cada linha da secao
    '''
    lista_soma = []
    for listas in secao:
        soma = 0
        for numeros in listas:
            soma += numeros
        lista_soma.append(soma)
    return lista_soma

def soma_colunas(secao,escolha):
    '''Realiza a soma das colunas por secao
        -Parametros:
        secao gerada nas funcoes criar_tabuleiro_facil e criar_tabuleiro_dificil, alem do nivel de jogo para dimensionamento 
        do for.
        -retorno:
        lista contendo os valores da soma de cada coluna da secao
    '''
    if escolha == '2':
        n = 3
    elif escolha == '1':
        n = 2
    lista_somac = []
    for j in range(n):
        somac = 0
        for i in range(n):
            somac += secao[i][j]
        lista_somac.append(somac)
    return lista_somac

def soma_ps(item1,item2,item3,escolha):
    '''E necessario juntar a soma das linhas e colunas que foram feitas por secao, sendo assim, esta funcao 
        e utilizada para realizar esta juncao de somas
        -Parametros:
        tres listas com a somas(geradas em soma_linhas e soma_colunas) de tres secoes por vez para o modo dificil,
        exemplo:lista_soma da secao 1, 2 e 3 para as linhas e 1, 4 e 7 para as colunas.Para o nivel dois apenas 
        duas listas sao enviadas, mais uma variavel coringa iniciada em 0.Outro parametro utilizado e o nivel de 
        jogo para separacao das listas.
        -retorno:
        Lista com as somas por linha e coluna de tres em tres ou seja, lista_soma linha123-coluna-456(exemplo do modo dificil)
        '''
    if escolha == '2':
        s1 = sum([item1[0],item2[0],item3[0]])
        s2 = sum([item1[1],item2[1],item3[1]])
        s3 = sum([item1[2],item2[2],item3[2]])
        soma = [s1,s2,s3]
        return soma
    elif escolha == '1':
        s1=sum([item1[0],item2[0]])
        s2=sum([item1[1],item2[1]])
        soma=[s1,s2]
        return soma

def escolha_secao(escolha):
    '''Define para o usuario as secoes disponiveis para escolha, 1 a 4 no modo facil e 1 a 9 no modo dificil,
       sao utilizadas listas auxiliares para validacao do input do jogador.
        -Parametros:
        nivel de jogo para definicao de qual lista auxiliar sera utilizada.
        -retorno:
        secao escolhida pelo usuario.
    '''
    if escolha == '1':
        se = listas_aux_facil['secao_auxiliar_facil']
    elif escolha == '2':
        se = listas_aux_dificilp1['secao_auxiliar_dificil']
    while True:
        try:   
            print('SECOES DISPONIVEIS: {}\n'.format(se))
            secaod = int(input("Em qual secao deseja jogar? "))
            while secaod not in se:
                secaod = int(input("\nSECAO INVALIDA: Em qual secao deseja jogar? "))
            break
        except ValueError:
            print("\n>>>DIGITE APENAS NUMEROS INTEIROS<<<")
    return secaod

def traduz_termos_secao(secao,escolha):
    '''Traduz a opcao escolhida pelo usuario em escolha_secao, ou seja, se o usuario escolheu a secao 1 do modo facil,
       a funcao retorna a matriz da secao1, a matriz do jogo resposta 1 e a lista de numeros disponiveis na secao.
        -Parametros:
        secao escolhida em escolha_secao e o nivel de jogo para separacao dos termos.
        -retorno:
        tupla contendo a matriz gerada,a matriz do jogo resposta,uma lista com os numeros disponiveis na secao e o 
        proprio numero que representa a secao.
        #matrizes e listas estao guardadas em dicionarios#
    ''' 
    armazena_jogo = {1:[secoes_dificilp1['secao1_dificil'],jogos_dificilp1['jogo1_dificil'],listas_aux_dificilp1['auxiliar_dificil1']],
                     2:[secoes_dificilp1['secao2_dificil'],jogos_dificilp1['jogo2_dificil'],listas_aux_dificilp1['auxiliar_dificil2']],
                     3:[secoes_dificilp1['secao3_dificil'],jogos_dificilp1['jogo3_dificil'],listas_aux_dificilp2['auxiliar_dificil3']],
                     4:[secoes_dificilp2['secao4_dificil'],jogos_dificilp2['jogo4_dificil'],listas_aux_dificilp2['auxiliar_dificil4']],
                     5:[secoes_dificilp2['secao5_dificil'],jogos_dificilp2['jogo5_dificil'],listas_aux_dificilp2['auxiliar_dificil5']],
                     6:[secoes_dificilp2['secao6_dificil'],jogos_dificilp2['jogo6_dificil'],listas_aux_dificilp2['auxiliar_dificil6']],
                     7:[secoes_dificilp3['secao7_dificil'],jogos_dificilp3['jogo7_dificil'],listas_aux_dificilp3['auxiliar_dificil7']],
                     8:[secoes_dificilp3['secao8_dificil'],jogos_dificilp3['jogo8_dificil'],listas_aux_dificilp3['auxiliar_dificil8']],
                     9:[secoes_dificilp3['secao9_dificil'],jogos_dificilp3['jogo9_dificil'],listas_aux_dificilp3['auxiliar_dificil9']]}
    
    armazena_jogo2 = {1:[secoes_faceis['secao1_facil'],jogo_facil['jogo1_facil'],listas_aux_dificilp1['auxiliar_facil1']],
                     2:[secoes_faceis['secao2_facil'],jogo_facil['jogo2_facil'],listas_aux_dificilp1['auxiliar_facil2']],
                     3:[secoes_faceis['secao3_facil'],jogo_facil['jogo3_facil'],listas_aux_dificilp1['auxiliar_facil3']],
                     4:[secoes_faceis['secao4_facil'],jogo_facil['jogo4_facil'],listas_aux_dificilp1['auxiliar_facil4']]}
    
    if escolha == '2':
        for chave in armazena_jogo:
            if chave == secao:
                se = armazena_jogo[secao][0]
                jogo = armazena_jogo[secao][1]
                lista_auxiliar = armazena_jogo[secao][2]

        return se,jogo,lista_auxiliar,secao
    
    elif escolha == '1':
        for chave in armazena_jogo2:
            if chave == secao:
                se = armazena_jogo[secao][0]
                jogo = armazena_jogo[secao][1]
                lista_auxiliar = armazena_jogo[secao][2]

        return se,jogo,lista_auxiliar,secao

def escolha_num(tupla_traduzida,escolha):
    '''define para o ususario os numeros disponiveis para escolha.
        -Parametros:
        tupla com as informacoes geradas em traduz_temos_secao
        -retorno:
        numero escolhido pelo usuario
    '''
    for itens in tupla_traduzida:
        secao_tab,jogo,lista_auxiliar,secao = tupla_traduzida
    while True:
        try:
            print("\nNUMEROS DISPOIVEIS NA SECAO {}: {}\n".format(secao,lista_auxiliar))
            nd = int(input("Qual numero deseja encontrar: "))
            while nd not in lista_auxiliar:
                nd = int(input("NUMERO INVALIDO | Qual numero quer encontar:"))
            break
        except ValueError:
            print("\nDIGITE APENAS NUMEROS INTEIROS")               
    lista_auxiliar.remove(nd)                                            #Cada vez que um numero é escolhido, este é removido da lista
    if escolha == '2':                                                   #de numeros disponiveis naquela secao, caso esta lista fique vazia
        if lista_auxiliar == []:                                         #a secao que representa esta lista e retirada da lista de secoes 
            listas_aux_dificilp1['secao_auxiliar_dificil'].remove(secao) #disponiveis para uso.
    elif escolha == '1':
        if lista_auxiliar == []:
            listas_aux_facil['secao_auxiliar_facil'].remove(secao)
    return nd

def verifica(traducao,numero,escolha):
    '''Verifica a posicao do numero no tabuleiro gerado e o coloca na mesma posicao para revelacao no tabuleiro
       resposta.
        -Parametros:
        tupla com as informacoes geradas em traduz_temos_secao, numero que foi escolhido pelo usuario e nivel do jogo.
        -retorno:
        nenhum
    '''
    if escolha == '2':
        n = 3
    elif escolha == '1':
        n = 2
    for itens in traducao:
        secao,jogo,lista,tr = traducao
    for i in range(n):
        for j in range(n):
            if secao[i][j] == numero:
                jogo[i][j] = numero

def print_secao(escolha):
    '''Printa o tabulerio resposta para utilizacao nas rodadas e no placar final
        -Parametros:
        nivel de jogo
        -retorno:
        nenhum
    '''
    if escolha == '1':
        print(' '*23,"=-=-=-=-=-=-=-=-=-=")
        for i in range(2):
            print(' '*23,'|',jogo_facil['jogo1_facil'][i],'|',jogo_facil['jogo2_facil'][i],'|',soma_linha12[i])
        print(' '*23,"=-=-=-=-=-=-=-=-=-=")
        for i in range(2):
            print(' '*23,'|',jogo_facil['jogo3_facil'][i],'|',jogo_facil['jogo4_facil'][i],'|',soma_linha34[i])
        print(' '*23,"=-=-=-=-=-=-=-=-=-=")
        print(' '*23,'  ',soma_coluna12[0],soma_coluna12[1],'  ',soma_coluna34[0],soma_coluna34[1])
        print(" ")
    elif escolha =='2':
        print(' '*15,"________________________________________")
        for i in range(3):
            print(' '*15,jogos_dificilp1['jogo1_dificil'][i],"|",jogos_dificilp1['jogo2_dificil'][i],"|",jogos_dificilp1['jogo3_dificil'][i],"|",soma_linha123[i],"|")
        print(' '*15,"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        for i in range(3):
            print(' '*15,jogos_dificilp2['jogo4_dificil'][i],"|",jogos_dificilp2['jogo5_dificil'][i],"|",jogos_dificilp2['jogo6_dificil'][i],"|",soma_linha456[i],"|")
        print(' '*15,"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        for i in range(3):
            print(' '*15,jogos_dificilp3['jogo7_dificil'][i],"|",jogos_dificilp3['jogo8_dificil'][i],"|",jogos_dificilp3['jogo9_dificil'][i],"|",soma_linha789[i],"|")
        print(' '*15,"________________________________________")
        print(' '*15,soma_coluna123[0],soma_coluna123[1],soma_coluna123[2],'  ',soma_coluna456[0],soma_coluna456[1],soma_coluna456[2],'  ',soma_coluna789[0],soma_coluna789[1],soma_coluna789[2])

def placar_final():
    '''Usada para printar o placar final com o vencedor, o perdedor e a quantidade de pontos para cada um,
       e usada tanto para o jogo facil como para o dificil.
        -Parametros:
        nenhum
        -retorno:
        nenhum
    '''
    print("\n",' '*20,">>>PONTUACAO FINAL<<<\n")
    if p1 > p2:
        print("PARABENS {} VOCE VENCEU COM {} PONTOS\n\nMAIS SORTE NA PROXIMA VEZ {}, VOCE OBTEVE {} PONTOS".format(jogador1,p1,jogador2,p2))
    else:
        print("PARABENS {} VOCE VENCEU COM {} PONTOS\n\nMAIS SORTE NA PROXIMA VEZ {}, VOCE OBTEVE {} PONTOS".format(jogador2,p2,jogador1,p1))
    print_secao(nivel)

def jogo(escolha):
    '''uniao de todas as funcoes responsaveis pelo controle das jogadas
        -Parametros:
        nivel de jogo
        -retorno:
        listas contendo as somas das linhas, colunas e diagonal do jogo facil ou 
        dificil para comparacao com o tabuleiro gerado e distribuicao dos pontos.
    '''
    secao = escolha_secao(nivel)
    t = traduz_termos_secao(secao,nivel)
    n = escolha_num(t,nivel)
    resultado = verifica(t,n,nivel)
    if escolha == '1':
        soma_linhaf = {'j1_facil':soma_linhas(jogo_facil['jogo1_facil']),'j2_facil':soma_linhas(jogo_facil['jogo2_facil']),'j3_facil':soma_linhas(jogo_facil['jogo3_facil']),'j4_facil': soma_linhas(jogo_facil['jogo4_facil'])}
        soma_colunaf = {'j1_facilc':soma_colunas(jogo_facil['jogo1_facil'],nivel),'j2_facilc':soma_colunas(jogo_facil['jogo2_facil'],nivel),'j3_facilc':soma_colunas(jogo_facil['jogo3_facil'],nivel),'j4_facilc':soma_colunas(jogo_facil['jogo4_facil'],nivel)}

        somaj_linha12 = soma_ps(soma_linhaf['j1_facil'],soma_linhaf['j2_facil'],coringa,nivel)
        somaj_linha34 = soma_ps(soma_linhaf['j3_facil'],soma_linhaf['j4_facil'],coringa,nivel)      
        
        somaj_coluna12 = soma_ps(soma_colunaf['j1_facilc'],soma_colunaf['j3_facilc'],coringa,nivel)     #A soma das linhas e colunas do tabuleiro resposta e realizada de forma 
        somaj_coluna34 = soma_ps(soma_colunaf['j2_facilc'],soma_colunaf['j4_facilc'],coringa,nivel)     #semelhante a feita com o tabuleiro gerado, utilizando as mesmas funcoes.

        soma_diagonalfj = 0

        for i in range(2):
            for j in range(2):
                if i == j:
                    soma_diagonalfj += jogo_facil['jogo1_facil'][i][j]
                    soma_diagonalfj += jogo_facil['jogo4_facil'][i][j]
        return somaj_linha12,somaj_linha34,somaj_coluna12,somaj_coluna34,soma_diagonalfj
    
    elif escolha == '2':
        soma_linhasdj1 = {'j1_dificil':soma_linhas(jogos_dificilp1['jogo1_dificil']),'j2_dificil':soma_linhas(jogos_dificilp1['jogo2_dificil']),'j3_dificil':soma_linhas(jogos_dificilp1['jogo3_dificil'])}
        soma_linhasdj2 = {'j4_dificil':soma_linhas(jogos_dificilp2['jogo4_dificil']),'j5_dificil':soma_linhas(jogos_dificilp2['jogo5_dificil']),'j6_dificil':soma_linhas(jogos_dificilp2['jogo6_dificil'])}
        soma_linhasdj3 = {'j7_dificil':soma_linhas(jogos_dificilp3['jogo7_dificil']),'j8_dificil':soma_linhas(jogos_dificilp3['jogo8_dificil']),'j9_dificil':soma_linhas(jogos_dificilp3['jogo9_dificil'])}

        soma_colunasdj1 = {'j1_dificilc': soma_colunas(jogos_dificilp1['jogo1_dificil'],nivel),'j2_dificilc': soma_colunas(jogos_dificilp1['jogo2_dificil'],nivel),'j3_dificilc': soma_colunas(jogos_dificilp1['jogo3_dificil'],nivel)}
        soma_colunasdj2 = {'j4_dificilc': soma_colunas(jogos_dificilp2['jogo4_dificil'],nivel),'j5_dificilc': soma_colunas(jogos_dificilp2['jogo5_dificil'],nivel),'j6_dificilc': soma_colunas(jogos_dificilp2['jogo6_dificil'],nivel)}
        soma_colunasdj3 = {'j7_dificilc': soma_colunas(jogos_dificilp3['jogo7_dificil'],nivel),'j8_dificilc': soma_colunas(jogos_dificilp3['jogo8_dificil'],nivel),'j9_dificilc': soma_colunas(jogos_dificilp3['jogo9_dificil'],nivel)}

        somaj_linha123 = soma_ps(soma_linhasdj1['j1_dificil'],soma_linhasdj1['j2_dificil'],soma_linhasdj1['j3_dificil'],nivel)
        somaj_linha456 = soma_ps(soma_linhasdj2['j4_dificil'],soma_linhasdj2['j5_dificil'],soma_linhasdj2['j6_dificil'],nivel)
        somaj_linha789 = soma_ps(soma_linhasdj3['j7_dificil'],soma_linhasdj3['j8_dificil'],soma_linhasdj3['j9_dificil'],nivel)

        somaj_coluna123 = soma_ps(soma_colunasdj1['j1_dificilc'],soma_colunasdj2['j4_dificilc'],soma_colunasdj3['j7_dificilc'],nivel)
        somaj_coluna456 = soma_ps(soma_colunasdj1['j2_dificilc'],soma_colunasdj2['j5_dificilc'],soma_colunasdj3['j8_dificilc'],nivel)
        somaj_coluna789 = soma_ps(soma_colunasdj1['j3_dificilc'],soma_colunasdj2['j6_dificilc'],soma_colunasdj3['j9_dificilc'],nivel)

        soma_diagonalj = 0

        for i in range(3):
            for j in range(3):
                if i == j:
                    soma_diagonalj += jogos_dificilp1['jogo1_dificil'][i][j]
                    soma_diagonalj += jogos_dificilp2['jogo5_dificil'][i][j]
                    soma_diagonalj += jogos_dificilp3['jogo9_dificil'][i][j]  
        return somaj_linha123,somaj_linha456,somaj_linha789,somaj_coluna123,somaj_coluna456,somaj_coluna789,soma_diagonalj       

def entregar_pontos_facil(somaj_linha12,somaj_linha34,somaj_coluna12,somaj_coluna34,soma_diagonalfj,soma_diagonalf,pontos):
    '''Recebe as somas feitas em jogo caso o nivel seja o facil, para realizar as comparacoes entre tabuleiro resposta e 
       o tabuleiro gerado com os numeros.
        -Parametros:
        somas do tabuleiro resposta,soma da diagonal do tabuleiro gerado e pontos de cada jogador
        -retorno:
        pontos
    '''
    for i in range(2):
        if somaj_linha12[i] == soma_linha12[i]:         #variaveis com final j representam o tabuleiro resposta
            pontos += soma_linha12[i]
            soma_linha12[i] = 0
    for i in range(2):
        if somaj_linha34[i] == soma_linha34[i]:
            pontos += soma_linha34[i]
            soma_linha34[i] = 0
    for i in range(2):
        if somaj_coluna12[i] == soma_coluna12[i]:
            pontos += soma_coluna12[i]
            soma_coluna12[i] = 0
    for i in range(2):
        if somaj_coluna34[i] == soma_coluna34[i]:
            pontos += soma_coluna34[i]
            soma_coluna34[i] = 0
    if soma_diagonalfj == soma_diagonalf:
        pontos += soma_diagonalf * 2
        soma_diagonalf = 0
    return pontos

def entregar_pontos_dificil(somaj_linha123,somaj_linha456,somaj_linha789,somaj_coluna123,somaj_coluna456,somaj_coluna789,soma_diagonalj,soma_diagonald,pontos):
    '''Recebe as somas feitas em jogo caso o nivel seja o dificil, para realizar as comparacoes entre tabuleiro resposta e 
       o tabuleiro gerado com os numeros.
        -Parametros:
        somas do tabuleiro resposta,soma da diagonal do tabuleiro gerado e pontos de cada jogador
        -retorno:
        pontos
    '''
    for i in range(3):
        if somaj_linha123[i] == soma_linha123[i]:
            pontos += soma_linha123[i]
            soma_linha123[i] = 0
    for i in range(3):                                      #variaveis com final j representam o tabuleiro resposta
        if somaj_linha456[i] == soma_linha456[i]:           #caso a soma de uma linha ou coluna do tabuleiro resposta
            pontos += soma_linha456[i]                      #seja igual ao do original o jogador leva os pontos(soma).
            soma_linha456[i] = 0                        
    for i in range(3):
        if somaj_linha789[i] == soma_linha789[i]:
            pontos += soma_linha789[i]
            soma_linha789[i] = 0
    for i in range(3):
        if somaj_coluna123[i] == soma_coluna123[i]:
            pontos += soma_coluna123[i]
            soma_coluna123[i] = 0
    for i in range(3):
        if somaj_coluna456[i] == soma_coluna456[i]:
            pontos += soma_coluna456[i]
            soma_coluna456[i] = 0
    for i in range(3):
        if somaj_coluna789[i] == soma_coluna789[i]:
            pontos += soma_coluna789[i]
            soma_coluna789[i] = 0
    if soma_diagonalj == soma_diagonald:
        pontos += soma_diagonald * 2
        soma_diagonald = 0
    return pontos


#Variavel coringa utilizada para completar parametros em funcoes que sao utilizadas tanto para nivel facil como para o dificil.
coringa = 0
print(' '*20,'=-=-=-=-JOGO DAS SOMAS 2.0-=-=-=-=')
print(' '*33,'BEM VINDO\n\n')

#While que controla menu inicial,permitindo que o usuario apenas escolha as opcoes disponiveis.
inicio = 1
while inicio != '2':
    print('[1] JOGAR\n[2] SAIR\n\n')
    inicio = input('QUAL DAS OPCOES ACIMA DESEJA SEGUIR? \n').strip()

#Caso o jogador escolha jogar o game,ele sera redirecionado para escolha dos nicknames.As variaveis utilizadas como parametros
#de pontos nas funcoes sao iniciadas
    if inicio == '1':
        pontos_jogador1 = pontos_jogador2 = 0
        print(' '*26,'ESCOLHAM SEUS APELIDOS\n\n')

        jogador1 = ''
        jogador2 = ''

#While superior nao permite que os jogadores entrem com nomes iguais, while interno nao permite que ele deixe o espaco em branco.
        while jogador1 == jogador2:
            print(" "*17,">>>SEUS APELIDOS NAO PODEM SER IGUAIS<<<\n")
            jogador1 = input('JOGADOR 01: DIGITE SEU APELIDO>\n').strip()
            while jogador1 == '':
                jogador1 = input('DIGITE SEU APELIDO>').strip()
            jogador2 = input('JOGADOR 02: DIGITE SEU APELIDO>\n').strip()
            while jogador2 == '':
                jogador2 = input('DIGITE SEU APELIDO>').strip()

#Menu de escolha do nivel de jogo, while e utilizado para nao permitir entrada de opcoes invalidas.
        print('\n'," "*13,'NIVEL DE JOGO\n')
        print('[1] NIVEL FACIL',' '*10,'[2] NIVEL DIFICIL\n')
        nivel = input("EM QUAL NIVEL DESEJA JOGAR: ").strip()
        while nivel != '1' and nivel != '2':
            nivel = input("\n(VOSSA SENHORIA ESCOLHEU UMA OPCAO INVALIDA)-\nEm qual nivel deseja jogar: ").strip()

#variaveis que acumulam os pontos dos jogadores sao inicializadas.
        print('\n',' '*26,'VAMOS JOGAR!\n')
        p1 = p2 = 0
        if nivel == '1':

#Caso o nivel 1 seja escolhido o modo facil(4x4) e iniciado.           
#Dicionarios sao utilizados para armazenar todos os dados do jogo, como as listas de auxilio, somas e matrizes.

#GRUPO DE DICIONARIOS 01: Armazenam as listas auxiliares utilizadas para controle dos inputs do usuario na escolha
#do numero e da secao.As matrizes geradas com os numeros randomizados e a matriz resposta gerada tambem sao armazendas
#nestes dicionarios.
            listas_aux_facil = {'secao_auxiliar_facil': [1,2,3,4],'auxiliar_facil1': [1,2,3,4],'auxiliar_facil2': [1,2,3,4],'auxiliar_facil3': [1,2,3,4],'auxiliar_facil4': [1,2,3,4]}
            secoes_faceis = {'secao1_facil':criar_tabuleiro_facil(),'secao2_facil':criar_tabuleiro_facil(),'secao3_facil':criar_tabuleiro_facil(),'secao4_facil':criar_tabuleiro_facil()}
            jogo_facil = {'jogo1_facil':criar_tab_resposta(nivel),'jogo2_facil':criar_tab_resposta(nivel),'jogo3_facil':criar_tab_resposta(nivel),'jogo4_facil':criar_tab_resposta(nivel),}

#GRUPO DE DICIONARIOS 02: Armazenam as somas das linhas e colunas de cada secao.(s1_facil le-se como soma linha 1 facil,
#s1_facilc le_se como soma da coluna da secao 1)
            soma_linhaf = {'s1_facil':soma_linhas(secoes_faceis['secao1_facil']),'s2_facil':soma_linhas(secoes_faceis['secao2_facil']),'s3_facil':soma_linhas(secoes_faceis['secao3_facil']),'s4_facil':soma_linhas(secoes_faceis['secao4_facil'])}
            soma_colunaf = {'s1_facilc':soma_colunas(secoes_faceis['secao1_facil'],nivel),'s2_facilc':soma_colunas(secoes_faceis['secao2_facil'],nivel),'s3_facilc':soma_colunas(secoes_faceis['secao3_facil'],nivel),'s4_facilc':soma_colunas(secoes_faceis['secao4_facil'],nivel),}

#GRUPO DE DICIONARIOS 03: Armazenam a soma das linhas do tabuleiro gerado como um todo, ou seja, soma da linha 1, soma da linha2
#e assim por diante.      
            soma_linha12 = soma_ps(soma_linhaf['s1_facil'],soma_linhaf['s2_facil'],coringa,nivel)
            soma_linha34 = soma_ps(soma_linhaf['s3_facil'],soma_linhaf['s4_facil'],coringa,nivel)

#GRUPO DE DICIONARIOS 04: Armazenam a soma das colunas do tabuleiro gerado como um todo, ou seja, soma da coluna 1, soma da coluna 2
#e assim por diante.
            soma_coluna12 = soma_ps(soma_colunaf['s1_facilc'],soma_colunaf['s3_facilc'],coringa,nivel)
            soma_coluna34 = soma_ps(soma_colunaf['s2_facilc'],soma_colunaf['s4_facilc'],coringa,nivel)

#For utilizado para somar a diagonal de todo o tabuleiro, no modo facil as secoes por onde a diagonal passa sao as secoes 1 e 4.
#Soma diagonalf e a variavel que armazena a soma da diagonal do tabuleiro gerado.
            soma_diagonalf = 0
            for i in range(2):
                for j in range(2):
                    if i == j:
                        soma_diagonalf += secoes_faceis['secao1_facil'][i][j]
                        soma_diagonalf += secoes_faceis['secao4_facil'][i][j]

#O modo facil e composto por oito rodadas, um while e uma variaval acumuladora sao utilizados para controlar a mecanica das rodadas.           
            soma = 0
            while soma < 8:
                soma += 1

#A funcao print secao e chamada para printar o tabuleiro resposta no comeco da primeira rodada e ao londo das rodadas, conforme os 
#numeros sao verificados, o jogo vai se completando com os numeros do tabuleiro gerado.              
                print_secao(nivel)

#Jogador 1 comeca a rodada, funcao jogo contendo as funcoes responsaveis pelos inputs e chamada, retornando logo em seguida a soma 
#do tabuleiro resposta para verificar se o valor de alguma linha, coluna ou da diagonal e igual ao da matriz gerada para atribuicao dos pontos
#em entregar pontos facil.
                print(' '*20,">>>{} FACA SUA JOGADA<<<\n\n".format(jogador1))
                respostas = jogo(nivel)
                
                for itens in respostas:
                    somaj_linha12,somaj_linha34,somaj_coluna12,somaj_coluna34,soma_diagonalfj = respostas

#Entregar pontos e chamada para verificar se existe igualdade entre a soma do tabuleiro gerado e o tabuleiro resposta, usando os pontos
#do jogador 1 como parametro e uma variavel acumuladora para receber os pontos              
                p1 += entregar_pontos_facil(somaj_linha12,somaj_linha34,somaj_coluna12,somaj_coluna34,soma_diagonalfj,soma_diagonalf,pontos_jogador1)

#Os processos realizados com o jogador 1 sao os mesmo para o jogador 2, existe alteracao apenas nas variaveis de pontuacao.
                print('\n'," "*20,">>>{} FACA SUA JOGADA<<<\n\n".format(jogador2))
                respostas = jogo(nivel)
                
                for itens in respostas:
                    somaj_linha12,somaj_linha34,somaj_coluna12,somaj_coluna34,soma_diagonalfj = respostas
                
                p2 += entregar_pontos_facil(somaj_linha12,somaj_linha34,somaj_coluna12,somaj_coluna34,soma_diagonalfj,soma_diagonalf,pontos_jogador2)
                if soma < 8:  print("\nPONTUACAO>\n{}: {} pontos\n\n{}: {} pontos".format(jogador1,p1,jogador2,p2))

#A variavel acumuladora de rodadas atinge seu maximo e logo em seguida a funcao placar final e chamada para revelar o ganhador da partida
#e o tabuleiro totalmente completo com as somas das linhas e colunas zeradas.O vencedor e o perdedor do jogo tamebem sao revelados. 
            placar_final()

#Caso o nivel escolhido seja o 2, o modo dificil(9x9) e iniciado.           
        elif nivel == '2':

#GRUPO DE DICIONARIOS 01: Armazenam as listas auxiliares utilizadas para controle dos inputs do usuario na escolha
#do numero e da secao.As matrizes geradas com os numeros randomizados e a matriz resposta gerada tambem sao armazendas
#nestes dicionarios.           
            listas_aux_dificilp1 = {'secao_auxiliar_dificil': [1,2,3,4,5,6,7,8,9],'auxiliar_dificil1': [1,2,3,4,5,6,7,8,9],'auxiliar_dificil2': [1,2,3,4,5,6,7,8,9]}
            listas_aux_dificilp2 = {'auxiliar_dificil3': [1,2,3,4,5,6,7,8,9],'auxiliar_dificil4': [1,2,3,4,5,6,7,8,9],'auxiliar_dificil5': [1,2,3,4,5,6,7,8,9],'auxiliar_dificil6': [1,2,3,4,5,6,7,8,9]}
            listas_aux_dificilp3 = {'auxiliar_dificil7': [1,2,3,4,5,6,7,8,9],'auxiliar_dificil8': [1,2,3,4,5,6,7,8,9],'auxiliar_dificil9': [1,2,3,4,5,6,7,8,9]}
            secoes_dificilp1 = {'secao1_dificil': criar_tabuleiro_dificil(),'secao2_dificil': criar_tabuleiro_dificil(),'secao3_dificil': criar_tabuleiro_dificil()}
            secoes_dificilp2 = {'secao4_dificil': criar_tabuleiro_dificil(),'secao5_dificil': criar_tabuleiro_dificil(),'secao6_dificil': criar_tabuleiro_dificil()}
            secoes_dificilp3 = {'secao7_dificil': criar_tabuleiro_dificil(),'secao8_dificil': criar_tabuleiro_dificil(),'secao9_dificil': criar_tabuleiro_dificil()}
            jogos_dificilp1 = {'jogo1_dificil': criar_tab_resposta(nivel),'jogo2_dificil': criar_tab_resposta(nivel),'jogo3_dificil': criar_tab_resposta(nivel)}
            jogos_dificilp2 = {'jogo4_dificil': criar_tab_resposta(nivel),'jogo5_dificil': criar_tab_resposta(nivel),'jogo6_dificil': criar_tab_resposta(nivel)}
            jogos_dificilp3 = {'jogo7_dificil': criar_tab_resposta(nivel),'jogo8_dificil': criar_tab_resposta(nivel),'jogo9_dificil': criar_tab_resposta(nivel)}
            
#GRUPO DE DICIONARIOS 02: Armazenam as somas das linhas e colunas de cada secao.Devido ao tamanho do tabuleiro
#as informacoes foram dividas em tres partes(d1,d2,d3).(s1_dificil le-se como soma linha 1 dificil,
#s1_dificilc le_se como soma da coluna da secao 1)        
            soma_linhasd1 = {'s1_dificil':soma_linhas(secoes_dificilp1['secao1_dificil']),'s2_dificil':soma_linhas(secoes_dificilp1['secao2_dificil']),'s3_dificil':soma_linhas(secoes_dificilp1['secao3_dificil'])}
            soma_linhasd2 = {'s4_dificil':soma_linhas(secoes_dificilp2['secao4_dificil']),'s5_dificil':soma_linhas(secoes_dificilp2['secao5_dificil']),'s6_dificil':soma_linhas(secoes_dificilp2['secao6_dificil'])}
            soma_linhasd3 = {'s7_dificil':soma_linhas(secoes_dificilp3['secao7_dificil']),'s8_dificil':soma_linhas(secoes_dificilp3['secao8_dificil']),'s9_dificil':soma_linhas(secoes_dificilp3['secao9_dificil'])}
            soma_colunasd1 = {'s1_dificilc':soma_colunas(secoes_dificilp1['secao1_dificil'],nivel),'s2_dificilc':soma_colunas(secoes_dificilp1['secao2_dificil'],nivel),'s3_dificilc': soma_colunas(secoes_dificilp1['secao3_dificil'],nivel)}
            soma_colunasd2 = {'s4_dificilc':soma_colunas(secoes_dificilp2['secao4_dificil'],nivel),'s5_dificilc':soma_colunas(secoes_dificilp2['secao5_dificil'],nivel),'s6_dificilc': soma_colunas(secoes_dificilp2['secao6_dificil'],nivel)}
            soma_colunasd3 = {'s7_dificilc':soma_colunas(secoes_dificilp3['secao7_dificil'],nivel),'s8_dificilc':soma_colunas(secoes_dificilp3['secao8_dificil'],nivel),'s9_dificilc': soma_colunas(secoes_dificilp3['secao9_dificil'],nivel)}
            
#GRUPO DE DICIONARIOS 03: Armazenam a soma das colunas do tabuleiro gerado como um todo, ou seja, soma da coluna 1, soma da coluna 2
#e assim por diante.
            soma_coluna123 = soma_ps(soma_colunasd1['s1_dificilc'],soma_colunasd2['s4_dificilc'],soma_colunasd3['s7_dificilc'],nivel)
            soma_coluna456 = soma_ps(soma_colunasd1['s2_dificilc'],soma_colunasd2['s5_dificilc'],soma_colunasd3['s8_dificilc'],nivel)
            soma_coluna789 = soma_ps(soma_colunasd1['s3_dificilc'],soma_colunasd2['s6_dificilc'],soma_colunasd3['s9_dificilc'],nivel)

#GRUPO DE DICIONARIOS 04: Armazenam a soma das linhas do tabuleiro gerado como um todo, ou seja, soma da linha 1, soma da linha2
#e assim por diante.              
            soma_linha123 = soma_ps(soma_linhasd1['s1_dificil'],soma_linhasd1['s2_dificil'],soma_linhasd1['s3_dificil'],nivel)
            soma_linha456 = soma_ps(soma_linhasd2['s4_dificil'],soma_linhasd2['s5_dificil'],soma_linhasd2['s6_dificil'],nivel)
            soma_linha789 = soma_ps(soma_linhasd3['s7_dificil'],soma_linhasd3['s8_dificil'],soma_linhasd3['s9_dificil'],nivel)

#For utilizado para somar a diagonal de todo o tabuleiro, no modo dificil as secoes por onde a diagonal passa sao as secoes 1, 5 e 9.
#Soma diagonald e a variavel que armazena a soma da diagonal do tabuleiro gerado.
            soma_diagonald = 0
            for i in range(3):
                for j in range(3):
                    if i == j:
                        soma_diagonald += secoes_dificilp1['secao1_dificil'][i][j]
                        soma_diagonald += secoes_dificilp2['secao5_dificil'][i][j]
                        soma_diagonald += secoes_dificilp3['secao9_dificil'][i][j]

#O modo dificil e composto por 41 rodadas, um while e uma variaval acumuladora sao utilizados para controlar a mecanica das rodadas.           
            soma = 0
            while soma < 41:
                soma += 1

#A funcao print secao e chamada para printar o tabuleiro resposta no comeco da primeira rodada e ao londo das rodadas, conforme os 
#numeros sao verificados, o jogo vai se completando com os numeros do tabuleiro gerado.  
                print_secao(nivel)

#Jogador 1 comeca a rodada, funcao jogo contendo as funcoes responsaveis pelos inputs e chamada, retornando logo em seguida a soma 
#do tabuleiro resposta para verificar se o valor de alguma linha, coluna ou da diagonal e igual ao da matriz gerada para atribuicao dos pontos
#em entregar pontos dificil.               
                print("\n\n",' '*21,">>>{} FACA SUA JOGADA<<<\n".format(jogador1))
                respostas = jogo(nivel)

                for itens in respostas:
                    somaj_linha123,somaj_linha456,somaj_linha789,somaj_coluna123,somaj_coluna456,somaj_coluna789,soma_diagonalj = respostas

#Entregar pontos e chamada para verificar se existe igualdade entre a soma do tabuleiro gerado e o tabuleiro resposta, usando os pontos
#do jogador 1 como parametro e uma variavel acumuladora para receber os pontos.       
                p1 += entregar_pontos_dificil(somaj_linha123,somaj_linha456,somaj_linha789,somaj_coluna123,somaj_coluna456,somaj_coluna789,soma_diagonalj,soma_diagonald,pontos_jogador1)

#As jogadas no modo dificil sao impares, ou seja, o jogo termina no jogador 1, portanto um break e acionado assim que a variavel acumuladora de 
#rodadas chega ao seu limite para que a rodada nao siga em frente.               
                if soma == 41:
                    break
                
                print("\n\n",' '*21,">>>{} FACA SUA JOGADA<<<\n".format(jogador2))
                respostas = jogo(nivel)

                for itens in respostas:
                    somaj_linha123,somaj_linha456,somaj_linha789,somaj_coluna123,somaj_coluna456,somaj_coluna789,soma_diagonalj = respostas

#Os processos realizados com o jogador 1 sao os mesmo para o jogador 2, existe alteracao apenas nas variaveis de pontuacao.
                p2 += entregar_pontos_dificil(somaj_linha123,somaj_linha456,somaj_linha789,somaj_coluna123,somaj_coluna456,somaj_coluna789,soma_diagonalj,soma_diagonald,pontos_jogador1)
                if soma < 41: print("\nPONTUACAO>\n{}: {} pontos\n\n{}: {} pontos".format(jogador1,p1,jogador2,p2))

#A variavel acumuladora de rodadas atinge seu maximo e logo em seguida o break e acionado, com isso o laco e finalizado e a funcao placar final 
# e chamada para revelar o ganhador da partida e o tabuleiro e totalmente completo com as somas das linhas e colunas zeradas.O vencedor e o 
#perdedor do jogo tamebem sao revelados.  
            placar_final()
