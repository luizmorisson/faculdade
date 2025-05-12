def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media


def main():
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = calcular_media(nota1, nota2, nota3)

    print("Aluno:", nome)
    print("Média final:", round(media, 2))
if __name__ == "__main__":
    main()