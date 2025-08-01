def div(k, j):
    return round(k / j, 2)

if __name__ == '__main__':
    while True:
        try:
            n1 = int(input('Digite um número: '))
            n2 = int(input('Digite Outros número: '))
            break
        except ValueError:
            print(f'Ocorreu um erro ao ler o valor. Tente novamente.')

    try:
        r = div(n1, n2)
    except ZeroDivisionError:
        print(f'Não é possível dividir por zero!')
    except:
        print(f'Ocorreu um erro descomhecido...')
    else:
        print(f'Resultado: {r}')
    finally: #é executado sempre
        print(f'\nFim do cálculo')

    