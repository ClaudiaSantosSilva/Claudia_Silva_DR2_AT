from funcoes_apoio import *
import string

#LISTA DE FILMES FOMATADA - PARSER DO CATALOGO
texto_inicial = "matrix|1999|Ação, Sci-Fi|Um hacker descobre a verdade sobre sua realidade.#Cidade de deus|2002|drama|História da ascensão do crime organizado nas favelas do Rio de Janeiro.#O senhor dos anéis: a sociedade do anel|2001|Aventura; Fantasia|Jornada épica pela Terra-média em busca do Um Anel.#Parasita|2019|Drama, Suspense|Uma família pobre se infiltra aos poucos em uma casa rica, com consequências inesperadas.#Bacurau|2019|drama;ficção|Um povoado do sertão brasileiro desaparece do mapa e precisa se defender de invasores.#Cidade de Deus|2002|Drama|A mesma história de crime, repetida de propósito.#Avatar|2009|Aventura, Sci-Fi|Em um planeta distante, humanos exploram recursos naturais enquanto um soldado humano se conecta aos nativos locais.#a vida é bela|1997|drama;romance|Durante a Segunda Guerra, um pai usa humor e imaginação para proteger o filho dos horrores de um campo de concentração.#Interestelar|2014|Sci-Fi, Drama|Exploradores espaciais viajam por buracos de minhoca em busca de um novo lar para a humanidade.#O Auto da Compadecida|2000|Comédia, Drama|Baseado na obra de Ariano Suassuna, dois nordestinos vivem aventuras que misturam humor, fé e crítica social."

lista_inicial_filmes = []
def parser_catalogo(texto_inicial):
    lista = []
    filmes = texto_inicial.split("#")
    #print(filmes)
    
    for filme in filmes:
       atributos = filme.split("|")
       #print(atributos)
       filme = {}
       filme['titulo'] = atributos[0]
       titulo_acertado = []
       desconsideradas = ['do', 'dos', 'da', 'das', 'de', 'no', 'na', 'nas', 'e', 'é']
       palavras_titulo = atributos[0].split()
       for i, palavra in enumerate(palavras_titulo):
           if palavra in desconsideradas and i != 0: #não pode ser a primeira palavra
               titulo_acertado.append(palavra.lower())
           else:
               titulo_acertado.append(palavra.capitalize()) 

       #filme['titulo'] = titulo_acertado
       filme['titulo'] = ' '.join(titulo_acertado)  
       filme['ano'] = int(atributos[1])
       filme['genero'] = atributos[2].lower().replace(";", ",")
       generos = filme['genero'].split(",") #gerou a lista
       generos = [genero.strip() for genero in generos]
       filme['genero'] = list(set(generos)) #set não permite repetição mas gera dicionario   
            
       filme['sinopse'] = atributos[3]
       filme['visto'] = False
       lista.append(filme)
    
    #incluindo o id sequencial na lista de filmes
    for i, filme in enumerate(lista, start=1):
        id = {'id': i}
        id.update(filme) #adiciona os outros atributos já existentes no dicionario filme
        lista_inicial_filmes.append(id) 
    
    return lista_inicial_filmes 
parser_catalogo(texto_inicial)    

#print(lista_inicial_filmes)

#BUSCAR TITULO POR PALAVRA OU PALAVRAS
def buscar_titulo_palavras(lista_inicial_filmes):
    print("== Encontrar titulos ==")
    palavras = [palavra.lower().strip() for palavra in input("Informe a(s) palavra(s) a ser(em) procurada(s) nos títulos dos filmes, separadas por virgula: ").split(",")]
    print("== Forma de Busca == ")
    print("[1] AND -> Todas as palavras devem estar no título")
    print("[2] OR -> Qualquer palavra já basta")
    forma_busca = receber_int("Digite a forma de busca: ")
    titulos_encontrados = []

    match forma_busca:
        case 1:
            for filme in lista_inicial_filmes:
                titulo = filme['titulo'].lower()
                if all(palavra in titulo for palavra in palavras):
                    titulos_encontrados.append(filme)
        case 2:
            for filme in lista_inicial_filmes:
                titulo = filme['titulo'].lower()
                if any(palavra in titulo for palavra in palavras):
                    titulos_encontrados.append(filme)
        case _:
            print("Digite uma forma válida de busca") 

    if titulos_encontrados:
        print("Filmes encontrados:") 
        for filme in titulos_encontrados:
            print(filme)
    else:
        print("Nenhum filme encontrado")  

#BUSCAR TITULO POR SUBSTRING
def buscar_titulo_substring(lista_inicial_filmes):
    pedaco = input("Informe parte de alguma palavra que deseja encontrar em um título: ").lower().strip()
    titulos_encontrados = []
    for filme in lista_inicial_filmes:
        titulo = filme['titulo'].lower()
        if pedaco in titulo:
            titulos_encontrados.append(filme)

    if titulos_encontrados:
        print("Filmes encontrados:") 
        for filme in titulos_encontrados:
            filmes_encontrados = sorted(titulos_encontrados, key = lambda filme: filme['ano'])
        print(filmes_encontrados)
    else:
        print("Nenhum filme encontrado")  

#BUSCAR FILME POR GENERO
def buscar_por_genero(lista_inicial_filmes):
    genero_desejado = input("Informe o gênero do filme desejado: ").lower().strip()
    titulos_encontrados = []
    for filme in lista_inicial_filmes:
        genero = filme['genero']
        if genero_desejado in genero:
            titulos_encontrados.append(filme)

    if titulos_encontrados:
        print("Filmes encontrados:") 
        for filme in titulos_encontrados:
            filmes_encontrados = sorted(titulos_encontrados, key = lambda filme: filme['titulo'])
        print(filmes_encontrados)
    else:
        print("Nenhum filme encontrado") 

#MARCAR COMO VISTO
def marcar_visto(lista_inicial_filmes):
    titulo_informado = input("Informe o titulo do filme a ser marcado como já visto: ").lower().strip()
    filme_visto = []    
    for filme in lista_inicial_filmes:
        titulo = filme['titulo'].lower()
        if titulo_informado in titulo: #não ignora acentos! Permite parte do titulo.
           filme['visto'] = True
           filme_visto.append(filme)
                      
    if filme_visto:
        print("Status de visto alterado com sucesso!")
    else:    
        print("Titulo não encontrado. Verifique se digitou o titulo corretamente e com acentos.")

#MOSTRAR FILMES AINDA NÃO VISTOS
def mostar_não_vistos(lista_inicial_filmes):
    filmes_nao_vistos = [filme for filme in lista_inicial_filmes if filme.get('visto') == False]
    print(filmes_nao_vistos)

#MOSTRAR SINOPSES ABREVIADAS
def abreviar_sinopses(lista_de_filmes):
    for filme in lista_de_filmes:
        sinopse = filme['sinopse'].strip()
        palavras_sinopse = filme['sinopse'].split() #lista de palavras
        #print(palavras_sinopse)
        caracteres_sinopse = len(sinopse) #conta TODOS caracteres
        if caracteres_sinopse <= 50:
           print(f"{filme['titulo']} - {sinopse}")
        elif caracteres_sinopse > 50:
            sinopse_abreviada = []
            for i, palavra in enumerate(palavras_sinopse):
                if palavra.endswith(","):
                    palavras_sinopse[i] = palavra.rstrip(",")
                quantidade_letras = len(palavra)
                if quantidade_letras > 6:
                    vogal = "aeiou"
                    nova_palavra = palavra[:6]
                    if nova_palavra[-1] in vogal:
                        while nova_palavra[-1] in vogal:
                            nova_palavra = nova_palavra[:-1]
                        nova_palavra = nova_palavra + "."
                    else:                     
                        nova_palavra = nova_palavra + '.'  
                    sinopse_abreviada.append(nova_palavra)                         
                elif quantidade_letras <= 6:
                    palavra = palavra    
                    sinopse_abreviada.append(palavra)        
            sinopse_final_abreviada = " ".join(sinopse_abreviada)
            print(f"{filme['titulo']} - {sinopse_final_abreviada}")
    #print(caracteres_sinopse) 
                                                          
#TOP K PALAVRAS EM TITULOS E SINOPSES
def contar_palavras_frequentes(lista_inicial_filmes):
    k = receber_int("Quantas palavras frequentes deseja saber: ")
    palavras_titulo_sinopse = []
    for filme in lista_inicial_filmes:
        titulo = filme['titulo'].lower().strip()
        sinopse = filme['sinopse'].lower().strip()
        palavras_titulo = titulo.split()
        for i, palavra in enumerate(palavras_titulo): #Acerta AQUELA palavra na lista palavras titulo
            palavras_titulo[i] = palavra.strip(string.punctuation) #para tirar , . : etc
        palavras_sinopse = sinopse.split()
        for i, palavra in enumerate(palavras_sinopse): 
            palavras_sinopse[i] = palavra.strip(string.punctuation)  
                
        palavras_titulo_sinopse += palavras_titulo + palavras_sinopse
    #print(palavras_titulo_sinopse) #é uma lista

    contagem_k_palavras = {}
    for palavra in palavras_titulo_sinopse:
        if len(palavra) >= 5:
            if palavra in contagem_k_palavras: # fazendo assim as palavras não se repetem
                contagem_k_palavras[palavra] = contagem_k_palavras[palavra] + 1
            else:
                contagem_k_palavras[palavra] = 1  
    #print(contagem_k_palavras) #dicionario com a contagem de todas as palavras, sem as menores de 5 letras 

    ordenar_contagem_k_palavras = sorted(contagem_k_palavras.items(), key=lambda item: item[1], reverse=True) #item[0] é a chave. Ordeno pelo [1] 
    #print(ordenar_contagem_k_palavras) #devolve lista.Posso usar [:k]

    primeiras_k_palavras = dict(ordenar_contagem_k_palavras[:k])
    print(f"As primeiras {k} palavras são: ")
    for chave, valor in primeiras_k_palavras.items():
        print(f"{chave} - {valor} vezes")

#CALCULAR SCORE DE FILMES
def calcular_score_filmes(lista_inicial_filmes):
    palavras_interesse = input("Informe a(s) palavra(s) de seu interesse separadas por virgula: ").lower().strip().split(",")
    k = receber_int("Informe o número de filmes relevantes que deseja encontrar: ")
    
    score_filme={}
    for filme in lista_inicial_filmes:        
        sinopse = filme['sinopse'].lower().strip()
        palavras_sinopse = sinopse.split()
        for i, palavra in enumerate(palavras_sinopse): 
            palavras_sinopse[i] = palavra.strip(string.punctuation) 

        for palavra_interesse in palavras_interesse:
            #print(palavra_interesse)
            if len(palavra_interesse) >= 5:
                palavra_interesse = palavra_interesse.strip() #se colocar espaço apos virgula, não estava considerando a palavra na comparação
                if palavra_interesse in palavras_sinopse:
                    if filme['titulo'] in score_filme.keys():
                        score_filme[filme['titulo']] = score_filme[filme['titulo']] + 1
                    else:
                        score_filme[filme['titulo']] = 1
                    #print(score_filme)                
    #print(score_filme)                    

    score_filme_ordenado = list(sorted(score_filme.items(), key= lambda item: item[1], reverse=True))
    score_filme_ordenado = score_filme_ordenado[:k]
    print("\nFilmes mais relevantes:")
    for titulo, score in score_filme_ordenado:
        print(f"{titulo} - {score} palavras-chave")        


