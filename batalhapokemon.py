import random
import time 
while True:
    
    try:
        def exibir_barra_de_vida(vida_atual):
    
            barra_de_vida = ''
            for _ in range(int(vida_atual)):
                barra_de_vida += '|'

            print(barra_de_vida)                                     # aqui defini os ataques e vida dos pokemons
        def escolhapokemon(nome):
            if not nome.isdigit():
                if nome.upper() == 'S':
                    atk = 1
                    defesa = 12
                    name = 'Squirtle'
                    tipo = 'Água'
                elif nome.upper() == 'C':
                    atk = 0.8
                    defesa = 15
                    name = 'Charmander'
                    tipo = 'Fogo'
                elif nome.upper() == 'B':
                    atk = 0.9
                    defesa = 14
                    name = 'Bulbasaur'
                    tipo = 'Grama'
                else:
                    print('Você não inseriu uma entrada válida.')
                    return None
            else:
                print('Entradas numericas são invalidas')
                return None # se alguma das entradas retornar none volta pro inicio do codigo

            return atk, defesa, name, tipo # função retorna atk defesa e nome do seu pokemon conforme as variaveis acima
        
        
        def poke_inimigo(nome_inimigo):
            if nome_inimigo == 'Meowth':
                def_inimigo = 11
                atk_inimigo = 1.1
                tipo = 'Normal'
            elif nome_inimigo == 'Arbok':
                def_inimigo = 10
                atk_inimigo = 1.3
                'Veneno'
            elif nome_inimigo == 'Weezing':
                def_inimigo = 10.2
                atk_inimigo = 1.2
                'Veneno'
        
            return atk_inimigo, def_inimigo, nome_inimigo
        
        pokemon_player = input('Escolha entre [S]quirtle, [C]harmander e [B]ulbasaur: ') # escolha do parametro nome
        pokemon_data = escolhapokemon(pokemon_player)

        listapokesinimigos = ['Meowth', 'Weezing', 'Arbok'] # lista para pegar um poke aleatorio
        pokemon_escolhido = random.choice(listapokesinimigos) # pegando um pokemon aleatorio da lista

        pokemon_atk_inimigo, poke_def_inimigo, name_inimigo = poke_inimigo(pokemon_escolhido) # retorno da função poke inimigo são os nomes atk e def do poke inimigo
        
        
        if pokemon_data is not None:
            if len(pokemon_data) == 4:
                pokemon_atk, pokemon_def, name, tipo = pokemon_data
                print(f'O Pokemon escolhido foi {name}.')
                print(f'Ataque do pokemon: {pokemon_atk}')
                print(f'Defesa do pokemon: {pokemon_def}')
                print(f'O tipo do seu pokemon é {tipo}')
            else:
                print('Escolha inválida.')
                continue
        else:
            print('Escolha inválida.')
            continue

    except TypeError as errortype:
        print('Entrada inválida erro de tipos')
        continue

    # exibe as informações inimigas
    print(f'O inimigo escolhido foi {name_inimigo}.')
    print(f'Ataque do inimigo: {pokemon_atk_inimigo}')
    print(f'Defesa do inimigo: {poke_def_inimigo}')

    # 
    turno = 1
    
    iniciar = input('Digite I para iniciar a batalha, qualquer outra entrada para escolher novamente seu pokemon: ')
    
    if iniciar.upper() != 'I':
        print('Selecione novamente seu pokemon, o pokemon inimigo será redefinido.')
        continue
    print('Batalha começando')
    
    
        # loop da batalha

    while pokemon_def > 0 or poke_def_inimigo > 0:
        multiplicador = random.uniform(1, 1.5)
        multiplicador_inimigo = random.uniform(1, 1.5)

        acao = input('Escolha a ação: [D]esistir ou [A]tacar: ')
        if acao.upper() == 'D':
                print('Você desistiu da batalha.')
                break
        
        if acao.upper() == 'A': 
            if name == 'Squirtle':
                escolha_ataque = input('Escolha o ataque que deseja usar \n 1. Játo Da Água \n 2. Investida: ' )
                if escolha_ataque == '1':
                    print('Multiplicador do Játo Da Água é de 1.3x')
                    multiplicador *= 1.3
                elif escolha_ataque == '2':
                    print('Multiplicador da Investida é de 1.2x')
                    multiplicador *= 1.2
                else:
                    print('Você não escolheu nenhum ataque, perdeu a vez.')
                    multiplicador *= 0
            
            if name == 'Charmander':
                escolha_ataque = input('Escolha o ataque que deseja usar \n 1. Játo De Fogo \n 2. Arranhão: ' )
                if escolha_ataque == '1':
                    print('Multiplicador do Játo De Fogo é de 1.3x')
                    multiplicador *= 1.3
                elif escolha_ataque == '2':
                    print('Multiplicador da Arranhão é de 1.2x')
                    multiplicador *= 1.2
                else:
                    print('Você não escolheu nenhum ataque, perdeu a vez.')
                    multiplicador *= 0

            if name == 'Bulbasaur':
                escolha_ataque = input('Escolha o ataque que deseja usar \n 1. Raio Solar \n 2. Mordida: ' )
                if escolha_ataque == '1':
                    print('Multiplicador do Raio Solar é de 1.5x porém bulbasaur perde 0.5 pontos de vida')
                    pokemon_def -= 0.5
                    multiplicador *= 1.5
                elif escolha_ataque == '2':
                    print('Multiplicador da Mordida é de 1.2x')
                    multiplicador *= 1.2
                else:
                    print('Você não escolheu nenhum ataque, perdeu a vez.')
                    multiplicador *= 0
                
        else: 
            print('Escolha entre [A]tacar ou [D]esistir.')
            continue        

        print(f'Este é o turno {turno}°')
        print(f'{name} causa o dano de {pokemon_atk * multiplicador:.2f} em {name_inimigo}.')
        poke_def_inimigo -= pokemon_atk * multiplicador
        if poke_def_inimigo < 0:
            poke_def_inimigo = 0
            print(f'{name} venceu a vida de {name_inimigo} é 0')
            break
        print(f'Vida atual de {name_inimigo} é {poke_def_inimigo:.2f}')
        exibir_barra_de_vida(poke_def_inimigo)
        time.sleep(2.5)

        # turno inimigo
        print(f'Este é o turno do inimigo')

        if name_inimigo == 'Meowth':
            ataques_meowth = ['Corte', 'Cabeçada']
            ataque_escolhido_inimigo = random.choice(ataques_meowth)
            if ataque_escolhido_inimigo == 'Corte':
                print('Meowth usou Corte.')
                multiplicador_inimigo *= 1.4
            elif ataque_escolhido_inimigo == 'Cabeçada':
                print('Meowth usou Cabeçada.')
                multiplicador_inimigo *= 1.3
            else:
                print('Algo deu errado reiniciando.')

        
        if name_inimigo == 'Weezing':
            ataques_weezing = ['Bomba de gás', 'Ataque Rápido']
            ataque_escolhido_inimigo = random.choice(ataques_weezing)
            if ataque_escolhido_inimigo == 'Bomba de gás':
                print('Weezing usou Bomba de gás.')
                multiplicador_inimigo *= 1.4
            elif ataque_escolhido_inimigo == 'Ataque Rápido':
                print('Weezing usou Ataque Rápido.')
                multiplicador_inimigo *= 1.3
            else:
                print('Algo deu errado reiniciando')

        if name_inimigo == 'Arbok':
            ataques_arbok = ['Picada', 'Agarrão']
            ataque_escolhido_inimigo = random.choice(ataques_arbok)
            if ataque_escolhido_inimigo == 'Picada':
                print('Arbok usou Picada.')
                multiplicador_inimigo *= 1.4
            elif ataque_escolhido_inimigo == 'Agarrão':
                print('Arbok usou Agarrão.')
                multiplicador_inimigo *= 1.3
            else:
                print('Algo deu errado reiniciando')

        print(f'{name_inimigo} causa o dano de {pokemon_atk_inimigo * multiplicador_inimigo:.2f} em {name}.')
        pokemon_def -= pokemon_atk_inimigo * multiplicador_inimigo
        if pokemon_def < 0:
            pokemon_def = 0
            print(f'{name_inimigo} venceu a vida de {name} é 0')
            break
        print(f'Vida atual de {name} é {pokemon_def:.2f}')

        exibir_barra_de_vida(pokemon_def)

        turno += 1
        time.sleep(1.2)
            
    sair = input('Digite [S]air para sair ou qualquer coisa para batalhar de novo: ')
    if sair.upper() == 'S':
        print('Você saiu')
        break
    
        
  
  
  
  




















   

        

