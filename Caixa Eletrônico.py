#boas vindas ao nosso banco
print('='*20)
print('Banco do Jl095'.center(20))
print('='*20)

#pergunta para o calculo
valor=int(input('Qual o valor que será sacado? R$'))
tot=valor
div=100
sob=0
while True:
    #Calculo
    if tot>=div:
        tot-=div
        sob+=1      
    #Atribuições para o calculo
    else:
        if sob>0:
            print(f'Total de {sob} cedulas de R${div}')
        if div==100:
            div=50
        elif div==50:
            div=20
        elif div==20:
            div=10
        elif div==10:
            div=1
        sob = 0
        if tot==0:
            break
print('='*30)
print('Volte sempre :)')
