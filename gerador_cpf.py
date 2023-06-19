import random
for _ in range(100):
    nove_digitos = ''

    for i in range(9):
        nove_digitos += str(random.randint(0,9))




    

    contador_regressivo_1 = 10

    resultado_digito_1 = 0

    for digito_1 in nove_digitos:
        resultado_digito_1 += int(digito_1) * contador_regressivo_1
        contador_regressivo_1 -= 1


    digito_1 = (resultado_digito_1 * 10) % 11


    digito_1 = digito_1 if digito_1 <= 9 else 0
    print()

    # gerar segundo digito cpf
    cpf_segundo_digito = '05608917090'

    nove_digitos_2 = cpf_segundo_digito[:9] + str(digito_1)

    contador_regressivo_2 = 11
    resultado_digito_2 = 0

    for digito_2 in nove_digitos_2:
        resultado_digito_2 += int(digito_2) * contador_regressivo_2
        contador_regressivo_2 -= 1

    digito_2 = (resultado_digito_2 * 10) % 11

    digito_2 = digito_2 if digito_2 <= 9 else 0


    cpf_gerado_calculo = f'{nove_digitos}{digito_1}{digito_2}'

    print(cpf_gerado_calculo)



