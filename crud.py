from util import *

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
    sinopse_truncada = sinopse[:300] + "..."
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
    print("Filme cadastrado com sucesso!")

#print(lista_inicial_filmes)

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

#print(lista_inicial_filmes)

#LISTAR FILMES
def listar_filmes(lista_inicial_filmes):
    print("== Filmes do Catálogo ==")
    print("[1] Por id")
    print("[2] Por titulo")
    print("[3] Por Ano")
    forma_ordenar = int(input("Como deseja ordenar os filmes: "))
    match forma_ordenar:
        case 1:
            print("== Lista de filmes por id ==")
            for filme in lista_inicial_filmes:
                print(filme)
        case 2:
            print("== Lista de filmes por titulo ==")
            for filme in lista_inicial_filmes:
                filmes_ordem_alfabetica = sorted(lista_inicial_filmes, key = lambda filme: filme['titulo'].lower())
            for filme in filmes_ordem_alfabetica:    
                print(filme)
        case 3:
            print("== Lista de filmes por ano ==")
            for filme in lista_inicial_filmes:
                filmes_ordem_ano = sorted(lista_inicial_filmes, key = lambda filme: filme['ano'])
            for filme in filmes_ordem_ano:
                print(filme)
        case _:
            print("Escolha uma opção válida!")



