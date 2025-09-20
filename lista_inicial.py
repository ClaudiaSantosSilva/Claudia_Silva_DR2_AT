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
    
    for i, filme in enumerate(lista, start=1):
        id = {'id': i}
        id.update(filme) #adiciona os outros atributos já existentes no dicionario filme
        lista_inicial_filmes.append(id) 
    
    return lista_inicial_filmes  
parser_catalogo(texto_inicial)    

#print(lista_inicial_filmes)

#CADASTRAR FILME
def cadastrar_filme(lista_inicial_filmes):
    ultimo_filme = lista_inicial_filmes[-1]
    id_ultimo_filme = ultimo_filme.get('id')
    id = id_ultimo_filme + 1
    titulo = input("Digite o título: ").strip()
    ano = int(input("Informe o ano do filme: ")) 
    generos_informados = input("Informe o(s) genero(s) do filme separados por (;): ").lower().replace(";", ",")
    generos = [genero.strip() for genero in generos_informados.split(",")]
    sinopse = input("Digite a sinopse do filme em até 300 caracteres: ")
    sinopse_truncada = sinopse[:300]
    if len(sinopse)> 300:
        print("A sinopse foi truncada em 300 caracteres!")
        sinopse = sinopse_truncada
    
    visto = False
    novo_filme = {
        "id": id,
        "titulo" : titulo,
        "ano": ano,
        "genero": generos,
        "sinopse": sinopse,
        "visto": visto
    }
    lista_inicial_filmes.append(novo_filme)
cadastrar_filme(lista_inicial_filmes) 

print(lista_inicial_filmes)

#REMOVER FILME DA LISTA
def remover_filme(lista_inicial_filmes):
    filme_a_remover = input("Informe o titulo do filme a ser removido: ").strip().lower()
    achado = False
    for filme in lista_inicial_filmes:
        if filme_a_remover == filme['titulo'].lower():
            lista_inicial_filmes.remove(filme)
            achado = True
            print(f"Filme '{filme['titulo']}' removido com sucesso!")
            break
    
    if not achado:
        print("Esse título não existe no catálogo.")

remover_filme(lista_inicial_filmes)  

#print(lista_inicial_filmes)
    
    




def menu():
    while True:
        print("**** Menu TextFlix ****")
        print("[1] Cadastrar filme")
        print("[2] Remover filme")
        print("[3] Listar filmes")
        print("[4] Buscar titulo por palavras")
        print("[5] Buscar filme por parte do titulo")
        print("[6] Buscar filmes por genero")
        print("[7] Marcar filme assitido")
        print("[8] Listar filmes vistos / não vistos")
        print("[9] Mostrar palavras mais frequentes nos títulos e sinopses")
        print("[10] Mostrar filmes relevantes por palavras-chave")  
        print("[11] Sair do programa")     
        opcao = int(input("Escolha a opção desejada: "))

        match opcao:
            case 1: 
                cadastrar_filme()
            case 2: 
                remover_filme(lista_inicial_filmes)
            #case 3: 
             #   atualizar()
            #case 4: 
             #   excluir()
            #case 5: 
               # listar_usuario()
            #case 6: 
               # listar_usuario()
            #case 7: 
                #listar_usuario()
            #case 8: 
               # listar_usuario()
            #case 9: 
                #listar_usuario()
            #case 10: 
                #listar_usuario()
            #case 11: 
               # print("Saindo do sistema")
               # break
            case _:
                print("Opção inválida")

menu()



    
