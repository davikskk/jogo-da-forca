import os, random
opcoes=["naruto", "pizza", "engenheiro", "interestelar", "breaking bad", "japao", "futebol", "espaguete", "medico", "attack on titan", "inception", "stranger things", "hamburguer", "advogado", "one piece", "death note", "sushi", "arquiteto", "the matrix", "game of thrones", "canada", "basquete", "lasanha", "professor", "demon slayer", "gladiador", "dark", "batata frita", "psicologo", "bleach", "chocolate", "designer", "avatar", "the crown", "franca", "tacos", "biologo", "jujutsu kaisen", "interestelar", "chernobyl", "italia", "volei", "croissant", "programador", "my hero academia", "pulp fiction", "sherlock", "sorvete", "veterinario", "hunter x hunter"]
while True:
    print("JOGO DA FORCAAA!")
    print("1.jogar")
    print("2.sair")
    jous=input()
    if jous=='1':
        os.system('clear')
        palavra=random.choice(opcoes)
        acertos=0
        letra=list(palavra)
        certas=[]
        while acertos<len(palavra):
            for i in palavra:
                if i==" ":
                    print("  ", end="")
                elif i in certas:
                    print(i, end="")
                else:
                    print("_ ", flush=True, end="")
            print("\n")
            resposta=input()
            os.system('clear')
            if resposta in letra:
                acertos=acertos+1
                certas.append(resposta)
        print("acertou!")
        print(f"a palavra é: {palavra}")
        break