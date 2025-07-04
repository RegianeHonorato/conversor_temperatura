def celsius_to_fahrenheit(celsius:float) -> float:
    """Converte uma temperatura de Celsius para Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit:float) -> float:
    """Converte uma temperatura de Fahrenheit para Celsius."""
    return (fahrenheit - 32) * 5/9

def main():
    """Função principal que controla o fluxo do programa."""
    while True:
        print("\nConversor de Temperatura")
        print("1 - Celsius para Fahrenheit")
        print("2 - Fahrenheit para Celsius")
        print("3 - Sair")
        
        escolha = input("Escolha uma opção (1,1 2 ou 3): ")
        
        if escolha == '1':
            try: 
                c=float(input("Digite a temperatura em Celsius: "))
                f=celsius_to_fahrenheit(c)
                print(f"-> {c}°C é igual a {f:.2f}°F")
            except ValueError:
                print("Erro: Por favor, digite um valor numérico válido.")
        elif escolha == '2':
            try:
                f=float(input("Digite a temperatura em Fahrenheit: "))
                c=fahrenheit_to_celsius(f)
                print(f"-> {f}°F é igual a {c:.2f}°C")
            except ValueError:
                print("Erro: Por favor, digite um valor numérico válido.")
        elif escolha == '3':
                print("Saindo do programa. Até logo!")
                break
        else:
                print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main()
                