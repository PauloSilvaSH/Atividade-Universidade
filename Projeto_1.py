
# Entrada de dados de temperatura (-60, 50)
def validar_temperatura(temperatura):
    return -60 <= temperatura <= 50

# Meses do ano (Janeiro a Dezembro)
meses_do_ano = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

# Lista para Armazenar temperaturas dos meses
temperaturas_maximas = {}

# Repetição para coletar os dados
for mes in range(1, 13):
    while True:
        try:
            temperatura = float(input(f"Digite a temperatura máxima para {meses_do_ano[mes - 1]} (em Celsius): "))
            if not validar_temperatura(temperatura):
                raise ValueError("Temperatura fora do intervalo válido (-60°C a 50°C).")
            temperaturas_maximas[mes] = temperatura
            break
        except ValueError as e:
            print(e)

# Média de temperatura do ano
media_maxima_anual = sum(temperaturas_maximas.values()) / len(temperaturas_maximas)

# Mes escalonado
meses_escaldantes = sum(1 for temperatura in temperaturas_maximas.values() if temperatura > 33)

# Mes mais quente do ano
mes_max_escaldante = meses_do_ano[max(temperaturas_maximas, key=temperaturas_maximas.get) - 1]

# Mes menos quente do ano
mes_menos_quente = meses_do_ano[min(temperaturas_maximas, key=temperaturas_maximas.get) - 1]

# Saida de dados
print("\nResultados:")
print(f"Temperatura média máxima anual: {media_maxima_anual:.2f}°C")
print(f"Quantidade de meses escaldantes: {meses_escaldantes}")
print(f"Mês mais escaldante do ano: {mes_max_escaldante}")
print(f"Mês menos quente do ano: {mes_menos_quente}")