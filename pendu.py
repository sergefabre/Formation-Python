import random

words = """Communiste
Brun
Somme
Moustiquaire
Mil
Dominant
Bouquet
Imposition
Fichier
Poignarder
"""

listWords = list(words.split())
index = random.randint(0,len(listWords) - 1)
word = listWords[index]
# word = 'Brun'
lenWord = len(word)

game = {
    'life': 5,
    'word':word,
    'result': list('_' *lenWord)
}

print(f"{ game['life'] } vie(s) restante(s) | {(' ').join(game['result'])}")

while True:
    if game['life'] < 1:
        print('PERDU !!!', f"le mot a trouver été { game['word'] }")
        break
    if ''.join(game['result']) == game['word']:
        print('Bien Joué !!! :)')
        break
    letter = input(' Lettre ? > ') 
    if(letter in game['word'] and letter not in game['result']):
        nb = game['word'].count(letter)
        current = 1
        start = 0
        while current <= nb:
            ind = game['word'].find(letter,start)
            # print(ind, start)
            game['result'][ind] = letter
            start = ind + 1
            current += 1
    else:
        if(letter not in game['word'] ):
            game['life'] -= 1
    print(f"{ game['life'] } vie(s) restante(s) | {(' ').join(game['result'])}")



