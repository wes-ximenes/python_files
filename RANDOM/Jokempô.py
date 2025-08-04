import random
jokempo = ['pedra','papel','tesoura']
pc = random.choice(jokempo)
escolha = input('Jokempô (pedra, papel ou tesoura): ').lower()
print('\nVocê: {}'.format(escolha))
print('PC: {}'.format(pc))
if escolha == 'pedra' and pc == 'tesoura':
    print('\nVocê venceu!')
elif escolha == 'pedra' and pc == 'papel':
    print ('\nVocê perdeu!')
elif escolha == 'pedra' and pc == 'pedra':
    print ('\nEmpatado!')
if escolha == 'papel' and pc == 'pedra':
    print('\nVocê venceu!')
elif escolha == 'papel' and pc == 'tesoura':
    print ('\nVocê perdeu!')
elif escolha == 'papel' and pc == 'papel':
    print ('\nEmpatado!')
if escolha == 'tesoura' and pc == 'papel':
    print('\nVocê venceu!')
elif escolha == 'tesoura' and pc == 'pedra':
    print ('\nVocê perdeu!')
elif escolha == 'tesoura' and pc == 'tesoura':
    print ('\nEmpatado!')    
