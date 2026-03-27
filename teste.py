from missao import entrada_missao, missao
from personagem import entrada_personagem, personagem

ms = entrada_missao() # digitar missão
#ms = missao("Do Disapered Demons See God?", "Determine de cause of the disapperances from the Oni tribe", 50)
print(ms.exibir_dados())
ms2 = missao("Do Disapered Demons See God?", "Determine de cause of the disapperances from the Oni tribe", 50)
if ms == ms2:
    print(f"Misões são iguais: {ms2}")
else:
    print(f"Misões: {ms} e {ms2} sao diferentes")


ps = entrada_personagem() # digitar personagem
#ps = personagem("Crim")
print(ps.exibir_dados())
ps2 = personagem("Bianca")
if ps == ps2:
    print(f"personagens são iguais: {ps2}")
else:
    print(f"personagens: {ps} e {ps2} sao diferentes")
