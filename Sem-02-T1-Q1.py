def tamanho(a):
    return len(a)

def main():
    nome = input("Informe um nome: ")
    tam = tamanho(nome)
    print(f'Tamanho do nome digitado: {tam}')

if __name__ == '__main__':
    main()
