def contar_letras_a(string):
    quantidade_a_minuscula = string.count('a')
    quantidade_a_maiuscula = string.count('A')
    
    total_a = quantidade_a_minuscula + quantidade_a_maiuscula

    if total_a > 0:
        print(f"A letra 'a' aparece {total_a} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

entrada = input("Informe uma string: ")
contar_letras_a(entrada)
