
      
#Desenvolva um código que simule uma eleição com três candidatos.
#- candidato_X => 889
#- candidato_Y => 847
#- candidato_Z => 515
#- branco => 0

#O código deve perguntar se deseja finalizar a votação depois do voto. Caso o número do voto não corresponda a nenhum candidato ou seja branco, ele deve ser tratado como nulo. Se for inserido um texto ao invés de número, o código deve retornar uma mensagem para votar novamente.

#Quando a votação for finalizada, o código deverá mostrar o vencedor, aquele com o maior número de votos e, também, a quantidade de votos de cada candidato, os brancos e nulos 

import os
def painel():
  
   print('---------------------------')
   print(' |--APURAÇÃO DOS -VOTOS--|')
   print('---------------------------')
   print(f'    Candidato X =    {cont_X}')
   print('   --------------------')
   print(f'    Candidato Y =    {cont_Y}')
   print('   --------------------')
   print(f'    Candidato Z =    {cont_Z}')
   print('   --------------------')
   print(f'    Votos Brancos =  {cont_B}')
   print('   --------------------')
   print(f'    Votos Nulos =    {cont_N}')
   print('   --------------------')

def candidatos():
    print('--------------------------')
    print('|--CANDIDATOS A ELEIÇÃO--|')
    print('--------------------------')
    print('|candidato_X = 889')
    print('|candidato_Y = 847')
    print('|candidato_Z = 515')
    print('|branco = 0')
    print('|------------------------')

cont_X = 0
cont_Y = 0
cont_Z = 0
cont_B = 0
cont_N = 0

False
resp = 'N'
valor = 0

while resp == 'N':
   
  try: 
      print(' ')
      candidatos()
      print(' ')
      print(' ')
      
      num = int(input('Digite o número do seu candidato:\n\n'))  
     
      if num == 889:
         cont_X += 1
         print(' ')
         print(f'Candidato escolhido => X\n\n')
                 
      else:

          if num == 847:    
             cont_Y += 1
             print(' ')
             print(f'Candidato escolhido => Y\n\n')
             
          if num == 515:
             cont_Z += 1
             print(' ')
             print(f'Candidato escolhido => Z\n\n' ) 
             
          if num == 0:  
             cont_B += 1
             print(' ')
             print(f'Voto em branco\n\n' ) 
             
          if num != 0:  
              if num != 889 and num != 847 and num != 515:
                  cont_N += 1
                  print(' ')
                
  except (ValueError):            
      print(' ') 
      print(f'Valor digitado não é válido, tente novamente.\n\n' )
      print(' ')   
      painel()

  else:   
          
      resp = 'N'
      painel()     
      print(' ')   
      resp = str(input('Deseja encerrar a votação?[S/N]\n')).upper().strip()[0]
      if resp not in 'SN':
         print('Dados incorretos, digite [S] para finalizar ou [N] para continuar a votação.\n')
         resp = str(input('Deseja encerrar a votação?[S/N]\n')).upper().strip()[0] 
      print(' ') 
    
  
print('Votação encerrada.')
print(' ')

maior = cont_X

if cont_Y > cont_X and cont_Y > cont_Z and cont_Y > cont_B and cont_Y > cont_N:
   maior = cont_Y 
   print(f'Vencedor foi o CANDIDATO_Y com {cont_Y} votos.')

else:
  
    if cont_Z > cont_X and cont_Z > cont_Y and cont_Z > cont_B and cont_Z > cont_N:  
        maior = cont_Z 
        print(f'Vencedor foi o CANDIDATO_Z com {cont_Z} votos.')

    if cont_X > cont_Y and cont_X > cont_Z and cont_X > cont_B and cont_X > cont_N:  
        maior = cont_X 
        print(f'Vencedor foi o CANDIDATO_X com {cont_X} votos.')


