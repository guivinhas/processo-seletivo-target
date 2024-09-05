def is_fibonacci(n):
    def is_perfect_square(x):
        print(x)
        s = int(x**0.5)
        print(s, x)
        return s * s == x
    
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# Entrada do usuário
numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
