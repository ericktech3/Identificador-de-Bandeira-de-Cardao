# identificar_bandeira.py

def identificar_bandeira(numero_cartao):
    """
    Identifica a bandeira do cartão com base no número.
    
    :param numero_cartao: Número completo do cartão
    :return: Nome da bandeira do cartão ou 'Bandeira desconhecida' se não for reconhecida.
    """
    
    numero_cartao = str(numero_cartao)

    # Identificando bandeira
    if numero_cartao.startswith("4"):
        return "Visa"
    elif numero_cartao.startswith("5"):
        return "MasterCard"
    elif numero_cartao.startswith("34") or numero_cartao.startswith("37"):
        return "American Express"
    elif numero_cartao.startswith("6"):
        return "Discover"
    else:
        return "Bandeira desconhecida"

# Exemplo de uso
numero_cartao = input("Digite o número do cartão: ")
print(f"A bandeira do cartão é: {identificar_bandeira(numero_cartao)}")
