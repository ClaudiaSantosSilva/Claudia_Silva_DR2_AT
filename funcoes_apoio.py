#RECEBER INPUT INT 
def receber_int(mensagem):
    '''
    Função para tratar o input de número inteiro.
    Recebe uma mensagem que poderá ser diferente em cada função onde seja aplicada.
    OUTPUT: um número inteiro válido.
    '''
    while True:
        try:
            inteiro = int(input(mensagem))
            break
        except Exception:
            print("Erro: Digite um número válido.") 
    return inteiro              
        
#ENTRAR OPÇÃO DO MENU INICIAL
def receber_opcao(mensagem):
    '''
    Função para tratar o input do usuário quanto às opções do menu do sistema.
    Recebe uma mensagem para solicitar a opção do usuário.
    OUTPUT: o número inteiro que representa o item do menu escolhido pelo usuário.
    '''
    while True:
        try:
            opcao = int(input(mensagem))
            break
        except Exception:
            print("Erro: Opção inválida.") 
    return opcao              

#FORMATAR FILME A SER IMPRESSO
def print_filme(filme):
    '''
    Função que formata o print dos filmes, em um formato padrão e amigável.
    Recebe cada filme/seus atributos.
    OUTPUT: Print formatado dos filmes.
    '''
    return print(f"Id: {filme["id"]} | Título: {filme["titulo"]} | Ano: {filme["ano"]} | Gênero: {", ".join(filme["genero"])} | Sinopse: {filme["sinopse"]} | Filme visto: {filme["visto"]}.")

