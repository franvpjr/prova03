numerocorreto = 9
chances = 3

while chances > 0:
    palpite= int(input("digite um numero de 1 a 10, voce tem 3 chances para acertar: "))
    if palpite == numerocorreto:
        print("parabens você acertou!")
        break
    elif palpite != 9:
        chances -= 1
        print("tente novamente, voce perdeu uma chance")
else: 
    print("voce perdeu, o numero correto era", numerocorreto)
    



