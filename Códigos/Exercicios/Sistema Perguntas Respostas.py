print("\n Olá! Bem vindo ao quiz APRENDENDO COISAS, um sistema",
      "simples de perguntas e respostas usando o dicionário,",
      "sua missão é responder as questões corretamente e",
      "ao final será dado um feedback de seu desempenho. GOOD LUCKY!!", sep="\n")

print()

perguntas = {
    'pergunta1': {
        'pergunta': 'Qual é a capital de Bangladesh?',
        'respostas': {'A': 'Brasília', 'B': 'Lima', 'C': 'Cabul',
                      'D': 'Pretória', 'E': 'Daca',},
        'resposta_certa': 'E',
    },
    'pergunta2': {
        'pergunta': 'Qual é a capital de Inglaterra?',
        'respostas': {'A': 'Camberra', 'B': 'Argel', 'C': 'Londres',
                      'D': 'São João', 'E': 'Manama',},
        'resposta_certa': 'C',
    },
    'pergunta3': {
        'pergunta': 'Qual é a capital de Zâmbia?',
        'respostas': {'A': 'Lomé', 'B': 'Taipé', 'C': 'Porto de Espanha',
                      'D': 'Lusaca', 'E': 'Campala',},
        'resposta_certa': 'D',
    },
}
total_Acertos = 0
for pk, pv in perguntas.items():
    print(f"{pk}: {pv['pergunta']}")
    print()

    for rk, rv in pv['respostas'].items():
        print(f'[{rk}] {rv}')

    resposta_usuario = input("Sua resposta: ").upper()

    if resposta_usuario == pv['resposta_certa']:
        print("BRABRO!! Acertou hein!")
        total_Acertos += 1
    else:
        print("IHHHHH!! Fraco de MAIS!")

    print()

total_Perguntas = len(perguntas)
porcentagem_Acertos = total_Acertos / total_Perguntas * 100
print(f"Você acertou {total_Acertos} pergunta(s).")
print(f"Sua porcentagem de acertos foi {porcentagem_Acertos:.2f}%.")