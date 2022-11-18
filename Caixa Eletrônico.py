print('='*20)
print('Banco do podpah'.center(20))
print('='*20)
valor=int(input('Qual o valor que será sacado? R$'))
tot=valor
div=50
sob=0
while True:
    if tot>=div:
        tot-=div
        sob+=1      
    else:
        if sob>0:
            print(f'Total de {sob} cedulas de R${div}')
        if div==50:
            div=20
        elif div==20:
            div=10
        elif div==10:
            div=1
        sob = 0
        if tot==0:
            break
        
