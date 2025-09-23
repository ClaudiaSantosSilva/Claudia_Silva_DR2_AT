from funcoes_apoio import receber_opcao
from crud import *
from util import *

def menu():
    while True:
        print("\n**** Menu TextFlix ****")
        print("[1] Cadastrar filme")
        print("[2] Remover filme")
        print("[3] Listar filmes")
        print("[4] Buscar titulo por palavras")
        print("[5] Buscar filme por parte do titulo")
        print("[6] Buscar filmes por genero")
        print("[7] Marcar filme assitido")
        print("[8] Listar filmes ainda não vistos")
        print("[9] Mostrar sinopses abreviadas")
        print("[10] Mostrar palavras mais frequentes nos títulos e sinopses")
        print("[11] Mostrar filmes relevantes por palavras-chave")  
        print("[0] Sair do programa")     
        opcao = receber_opcao("Escolha a opção desejada: ")

        match opcao:
            case 1: 
                cadastrar_filme(lista_inicial_filmes)
            case 2: 
                remover_filme(lista_inicial_filmes)
            case 3:
                listar_filmes(lista_inicial_filmes)
            case 4: 
                buscar_titulo_palavras(lista_inicial_filmes)
            case 5: 
                buscar_titulo_substring(lista_inicial_filmes)
            case 6: 
                buscar_por_genero(lista_inicial_filmes)
            case 7: 
                marcar_visto(lista_inicial_filmes)
            case 8: 
                mostar_não_vistos(lista_inicial_filmes)
            case 9: 
                abreviar_sinopses(lista_inicial_filmes)
            case 10: 
                contar_palavras_frequentes(lista_inicial_filmes)
            case 11: 
                calcular_score_filmes(lista_inicial_filmes)    
            case 0: 
                print("Saindo do sistema...")
                break
            case _:
                print("Opção inválida")
                
menu()

    
