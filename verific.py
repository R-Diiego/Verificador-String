def contar_a(string):
    count = string.lower().count('a')
    return count

texto = input("Informe uma string: ")

quantidade_a = contar_a(texto)

if quantidade_a > 0:
    print(f"A letra 'a' aparece {quantidade_a} vezes.")
else:
    print("A letra 'a' não aparece na string.")
