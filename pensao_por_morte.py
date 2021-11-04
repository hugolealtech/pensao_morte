#programa que calcula o valor da pensão por morte com amparo nas novas regras da reforma da previdência

salminimo = float(input('Digite o valor do salario minimo vigente R$: '))
salario = float(input('Digite o valor do salario do falecido R$: '))

if salario - salminimo == 0:
    print('O valor da sua pensão será de R$: {:.2f}'.format(salminimo))

if salario < salminimo:
    print('Segundo o art. 202, parágrafo 5º da C.F/1988, ninguém pode receber um salário menor que o salário mínimo')

elif salario > salminimo and salario <= 2 * salminimo:
    s1 = salario-salminimo
    s2 = s1*60/100
    print('O valor da sua pensão será de {:.2f}'.format(salminimo + s2))

elif salario >= 2 * salminimo and salario <= 3* salminimo:
    s3 = salario - (2 * salminimo)
    s4 = s3 * 40/100
    print('O valor da pensão será de R$: {:.2f}'.format(2 * salminimo + s4))

elif salario >= 3 * salminimo and salario <= 4 * salminimo:
    s5 = salario - (3 * salminimo)
    s6 = s5 * 20/100
    print('O valor da pensão será de R$:{:.2f}'.format(3 * salminimo + s6))

elif salario > 4 * salminimo:
    s7 = salario - (4 * salminimo)
    s8 = s7 * 10/100
    print('04 O valor da pensão será de R$:{:.2f}'.format(4 * salminimo + s8))



