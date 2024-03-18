# Conversor de Medidas

def temperatura():
    def tratamento_erro(op):
        if op not in ['1', '2', '3', '4']:
            print('Insira apenas números')
            novamente()
        else:
            pass

    def tratamento_erro2(texto):
        try:
            return float(texto)
        except ValueError:
            print("Entrada inválida. Por favor, insira um valor numérico válido.")
            return None

    def novamente():
        op = input('Escolha: \n1 - Deseja calcular novamente \n2 - Encerrar\n')
        if op == '1':
            return
        elif op == '2':
            print('Programa encerrado.')
            exit()
        else:
            print('Opção inválida.')
            novamente()

    while True:
        print('''
        Digite a unidade que será convertida:
        1 - Celsius
        2 - Fahrenheit
        3 - Kelvin
        4 - Retornar
        ''')
        op = input('Escolha a opção que será a base: ')
        tratamento_erro(op)

        if op == '1':
            print('Escolha:')
            print('1 - Fahrenheit')
            print('2 - Kelvin')
            unidade_destino = input('Será convertido para qual unidade: ')
            tratamento_erro(unidade_destino)

            if unidade_destino == '1':
                valor = input('Digite o valor: ')
                valor1 = tratamento_erro2(valor)
                if valor1 is not None:
                    fahrenheit = (9 / 5) * valor1 + 32
                    print(f'{valor1} Celsius para Fahrenheit é: {fahrenheit:.2f}')
                    novamente()

            elif unidade_destino == '2':
                valor = input('Digite o valor: ')
                valor1 = tratamento_erro2(valor)
                if valor1 is not None:
                    kelvin = valor1 + 273.15
                    print(f'{valor} Celsius para Kelvin é: {kelvin:.2f}')
                    novamente()

        elif op == '2':
            print('Escolha:')
            print('1 - Celsius')
            print('2 - Kelvin')
            unidade_destino = input('Para qual unidade será convertido: ')
            tratamento_erro(unidade_destino)

            if unidade_destino == '1':
                valor = input('Digite o valor: ')
                valor1 = tratamento_erro2(valor)
                if valor1 is not None:
                    celsius = (valor1 - 32) * 5 / 9
                    print(f'{valor} Farenheit para Celsius é: {celsius:.2f}')
                    novamente()

            elif unidade_destino == '2':
                valor = input('Digite o valor: ')
                valor1 = tratamento_erro2(valor)
                if valor1 is not None:
                    kelvin = (valor1 - 32) * 5 / 9 + 273.15
                    print(f'{valor} Farenheit para Kelvin é {kelvin:.2f}')
                    novamente()

        elif op == '3':
            print('Escolha:')
            print('1 - Celsius')
            print('2 - Fahrenheit')
            unidade_destino = input('Para qual unidade será convertido: ')
            tratamento_erro(unidade_destino)

            if unidade_destino == '1':
                valor = input('Digite o valor: ')
                valor1 = tratamento_erro2(valor)
                if valor1 is not None:
                    celsius = valor1 - 273.15
                    print(f'{valor} Kelvin para Celsius é: {celsius:.2f}')
                    novamente()

            elif unidade_destino == '2':
                valor = input('Digite o valor: ')
                valor1 = tratamento_erro2(valor)
                if valor1 is not None:
                    fahrenheit = (valor1 - 273.15) * 9/5 + 32
                    print(f'{valor} Kelvin para Fahrenheit é: {fahrenheit:.2f}')
                    novamente()

        elif op == '4':
            main()

        else:
            novamente()


def distancia():

    def tratamento_erro(num):
        valor = num
        lista = []
        for cada in valor:
            if cada.isdigit():
                lista.append(cada)

            elif cada == ',':
                lista.append(cada.replace(',','.'))

            elif cada.isalpha():
                print('Insira apenas numeros')
                novamente()

            elif cada == ' ':
                print('Insira apenas numeros sem espaços')
                novamente()
            else:
                print('erro')
                novamente()
        novo = ''.join(lista)
        return float(novo)


    def novamente():
        escolher = input('digite \n1 - Continuar \n2 - Sair')
        if escolher == '1':
            distancia()
        elif escolher == '2':
            exit()
        else:
            print('Opção inválida')
            novamente()

    # Conversor de comprimento: Converter entre metros, centímetros, quilômetros, polegadas, pés, etc.
    loop = 1
    while loop == 1:
        print('''
        Escolha a unidade base para conversão:
        1 - Quilômetros
        2 - Metros
        3 - Centímetros
        4 - polegadas
        5 - pes
        6 - Retornar
        ''')
        op = input('Escolha uma opção: ')
        if op == '1':
            #base quilometros
            valor = input('Digite o valor que será convertido: ')
            tratamento_erro(valor)
            valor = tratamento_erro(valor)
            metros = valor*1000
            centimetros = valor*10*10*10*10*10
            polegadas = centimetros / 2.54
            pes = centimetros/30.48
            print("               RESULTADO               ")
            print(f'{valor} quilometros em metros é: {metros}')
            print(f'{valor} quilometros em centimetros é: {centimetros}')
            print(f'{valor} quilometros em polegadas é: {polegadas}')
            print(f'{valor} quilometros em pes é: {pes}')
            novamente()

        elif op == '2':
            #base metros
            valor = input('Digite o valor que será convertido: ')
            tratamento_erro(valor)
            valor = tratamento_erro(valor)
            quilometros = valor / 10 / 10 / 10
            centimetros = valor * 10 * 10
            polegadas = centimetros / 2.54
            pes = centimetros/30.48
            print("               RESULTADO               ")
            print(f'{valor} metros em quilometros é: {quilometros}')
            print(f'{valor} metros em centimetros é: {centimetros}')
            print(f'{valor} metros em polegadas é: {polegadas}')
            print(f'{valor} metros em pes é: {pes}')
            novamente()

        elif op == '3':
            #base centímetros
            valor = input('Digite o valor que será convertido: ')
            tratamento_erro(valor)
            valor = tratamento_erro(valor)
            metros = valor / 10 / 10
            quilometros = metros / 10 / 10 / 10
            polegadas = valor / 2.54
            pes = valor/30.48
            print("               RESULTADO               ")
            print(f'{valor} centímetros em quilometros é: {quilometros}')
            print(f'{valor} centímetros em metros é: {metros}')
            print(f'{valor} centímetros em polegadas é: {polegadas}')
            print(f'{valor} centímetros em pes é: {pes}')
            novamente()

        elif op == '4':
            #base polegadas
            valor = input('Digite o valor que será convertido: ')
            tratamento_erro(valor)
            valor = tratamento_erro(valor)
            centimetros = valor * 2.54
            metros = centimetros / 10 / 10
            quilometros = centimetros / 10 / 10 / 10 / 10 / 10
            polegadas = valor / 2.54
            pes = centimetros/30.48
            print("               RESULTADO               ")
            print(f'{valor} polegadas em quilometros é: {quilometros}')
            print(f'{valor} polegadas em metros é: {metros}')
            print(f'{valor} polegadas em centímetros é: {centimetros}')
            print(f'{valor} polegadas em pes é: {pes}')
            novamente()

        elif op == '5':
            #base pe
            valor = input('Digite o valor que será convertido: ')
            tratamento_erro(valor)
            valor = tratamento_erro(valor)
            centimetros = valor * 30.48
            metros = centimetros / 10 / 10
            quilometros = centimetros / 10 / 10 / 10 / 10 / 10
            polegadas = valor * 12
            print("               RESULTADO               ")
            print(f'{valor} pés em quilometros é: {quilometros}')
            print(f'{valor} pés em metros é: {metros}')
            print(f'{valor} pés em centimetros é: {centimetros}')
            print(f'{valor} pés em polegadas é: {polegadas}')
            novamente()

        elif op == '6':
            main()

        else:
            print('Opção Inválida')
            novamente()


#Conversor de massa: Converter entre gramas, quilogramas, libras, onças, etc.
def massa():

    def tratamento_erro2(num):
        valor = num
        lista = []
        for cada in valor:
            if cada.isdigit():
                lista.append(cada)

            elif cada == ',':
                lista.append(cada.replace(',','.'))

            elif cada.isalpha():
                print('Insira apenas numeros')
                novamente()

            elif cada == ' ':
                print('Insira apenas numeros sem espaços')
                novamente()
            else:
                print('erro')
                novamente()
        novo = ''.join(lista)
        return float(novo)


    def novamente():
        escolher = input('digite \n1 - Continuar \n2 - Sair\n:')
        if escolher == '1':
            massa()
        elif escolher == '2':
            exit()
        else:
            print('Opção inválida')
            novamente()

    loop = 1
    while loop == 1:
        print('''
        Escolha uma opção base:
        1 - quilogramas 
        2 - gramas
        3 - libras
        4 - onças
        5 - Retornar
        ''')
        escolha = input(': ')
        if escolha == '1':
            #base quilograma
            valor = input('Digite um valor: ')
            tratamento_erro2(valor)
            valor = tratamento_erro2(valor)
            #base quilogramas
            grama = valor * 10 * 10 * 10
            libras = valor * 2.205
            onca = valor * 35.274
            print(f'''
            {valor} quilogramas em gramas é: {grama}
            {valor} quilogramas em libras é: {libras}
            {valor} quilogramas em onças é: {onca}''')
            novamente()

        elif escolha == '2':
            #base grama
            valor = input('Digite um valor: ')
            tratamento_erro2(valor)
            valor = tratamento_erro2(valor)
            quilogramas = valor / 10 / 10 / 10
            libra = valor / 453.6
            onca = valor / 28.35
            print(f'''
            {valor} gramas em quilogramas é: {quilogramas}
            {valor} gramas em libras é: {libra}
            {valor} gramas em onças é: {onca}''')
            novamente()


        elif escolha == '3':
            #base libra
            valor = input('Digite um valor: ')
            tratamento_erro2(valor)
            valor = tratamento_erro2(valor)
            quilogramas = valor / 2.205
            grama = valor * 453.6
            onca = valor * 16
            print(f'''
            {valor} libras em gramas é: {grama}
            {valor} libras em quilogramas é: {quilogramas}
            {valor} libras em onças é: {onca}''')
            novamente()

        elif escolha == '4':
            # base onca
            valor = input('Digite um valor: ')
            tratamento_erro2(valor)
            valor = tratamento_erro2(valor)
            quilogramas = valor / 35.274
            grama = valor * 28.35
            libra = valor / 16
            print(f'''
            {valor} onças em gramas é: {grama}
            {valor} onças em libras é: {libra}
            {valor} onças em quilograma é: {quilogramas}''')
            novamente()

        elif escolha == '5':
            main()

        else:
            print('Opção inválida')
            novamente()


#Conversor de volume: Converter entre litros, mililitros, metros cúbicos, etc.
def volume():

    def tratamento_erro2(num):
        valor = num
        lista = []
        for cada in valor:
            if cada.isdigit():
                lista.append(cada)

            elif cada == ',':
                lista.append(cada.replace(',','.'))

            elif cada.isalpha():
                print('Insira apenas numeros')
                novamente()

            elif cada == ' ':
                print('Insira apenas numeros sem espaços')
                novamente()
            else:
                print('erro')
                novamente()
        novo = ''.join(lista)
        return float(novo)


    def novamente():
        escolher = input('digite \n1 - Continuar \n2 - Sair')
        if escolher == '1':
            volume()
        elif escolher == '2':
            exit()
        else:
            print('Opção inválida')
            novamente()

    loop = 1
    while loop == 1:
        print('''
        Escolha uma opção base:
        1 - Litros  
        2 - Metros Cúbicos
        3 - Mililítros
        4 - Galões
        5 - Retornar
        ''')
        escolha = input(': ')
        if escolha == '1':
            #base litros
            valor = input('Digite um valor: ')
            tratamento_erro2(valor)
            valor = tratamento_erro2(valor)
            mililitros = valor * 1000
            metros_cubicos = valor / 1000
            galoes = valor / 264.172
            print(f'{valor} litros para é: {mililitros} mililitros')
            print(f'{valor} litros para é: {metros_cubicos} metros cúbicos')
            print(f'{valor} litros para é: {galoes} galões')
            novamente()

        elif escolha == '2':
            #base Metros cubicos
            valor = input('Digite um valor: ')
            tratamento_erro2(valor)
            valor = tratamento_erro2(valor)
            litros = valor * 1000
            mililitros = valor * 1000
            galoes = valor * 264.172
            print(f'{valor} metros cúbicos para é: {mililitros} mililitros')
            print(f'{valor} metros cúbicos para é: {litros} litros')
            print(f'{valor} metros cúbicos para é: {galoes} galões')
            novamente()

        elif escolha == '3':
            # base Mililitros
            valor = input('Digite um valor: ')
            tratamento_erro2(valor)
            valor = tratamento_erro2(valor)
            litros = valor / 1000
            metros_cubicos = valor / 1000000
            galoes = valor * 378541
            print(f'{valor} mililitros para é: {litros} litros')
            print(f'{valor} mililitros para é: {metros_cubicos} metros cúbicos')
            print(f'{valor} mililitros para é: {galoes} galões')
            novamente()

        elif escolha == '4':
            # base Galoes
            valor = input('Digite um valor: ')
            tratamento_erro2(valor)
            valor = tratamento_erro2(valor)
            litros = valor * 3.78541
            metros_cubicos = valor / 264.172
            mililitros = valor / 264.172
            print(f'{valor} galões para é: {litros} litros')
            print(f'{valor} galões para é: {metros_cubicos} metros cúbicos')
            print(f'{valor} galões para é: {mililitros} mililimetros')
            novamente()

        elif escolha == '5':
            main()

        else:
            print('Opção inválida')
            novamente()
def Tentar_novamente():
    op = input('Escolha: \n1 - Continuar \n2 - Encerrar programa\n:')
    if op == '1':
        main()
    elif op == '2':
        print('Programa Encerrado')
        exit()
    else:
        print('Opção inválida, escolha apenas uma das opções acima')
        Tentar_novamente()

def main():
    print('''
    Escolha:
    1 - Conversor de temperatura: Converter entre Celsius, Fahrenheit e Kelvin.
    2 - Conversor de comprimento: Converter entre metros, centímetros, quilômetros, polegadas, pés.
    3 - Conversor de massa: Converter entre gramas, quilogramas, libras, onças.
    4 - Conversor de volume: Converter entre litros, mililitros, metros cúbicos, galões.
    ''')
    escolher = input(':')
    if escolher == '1':
        temperatura()

    elif escolher == '2':
        distancia()

    elif escolher == '3':
        massa()

    elif escolher == '4':
        volume()

    else:
        print('Opção Inválida, escolha apenas as opções acima')
        Tentar_novamente()


if __name__ == '__main__':
    main()