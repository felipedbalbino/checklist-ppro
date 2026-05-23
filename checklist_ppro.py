print ('=== CHECKLIST PPRO - INÍCIO DE OPERAÇÃO ===')
print ('')

operador = input('Nome do operador: ')  
maquina = input('Número da máquina: ')

print ('')  
print(f'Operador: {operador}')
print(f'Máquina: {maquina}')
print ('')

print ('--- TEMPERATURA ---')
print ('')
temp_pont = float(input('Temperatura do ponteador (°C): '))

if temp_pont < 340 or temp_pont > 360:
    print(' ALERTA: Temperatura do ponteador FORA do padrão!')
    print(f' valor registrado: {temp_pont}°C | Padrão: 340°C a 360°C')
else:  print(f'Ponteamento OK: {temp_pont}°C')

print ('')

temp_sel = float(input(' Temperatura de selagem (°C): '))
if temp_sel < 240 or temp_sel > 260:
    print(' ALERTA: Temperatura de selagem FORA do padrão!')
    print(f' valor registrado: {temp_sel}°C | Padrão: 240°C a 260°C')
else:   
    print(f'Selagem OK: {temp_sel}°C')

print ('')

print ('---PRESSÃO---')
print ('')

pressao = float(input('Pressão do ar comprimido (bar): '))

if pressao < 5.5 or pressao > 6.5:
    print(' ALERTA: Pressão do ar comprimido FORA do padrão!')
    print(f' valor registrado: {pressao} bar | Padrão: 5.5 bar a 6.5 bar')
else:
    print(f'Pressão OK: {pressao} bar')

print ('')

print ('--- PEÇAS CRÍTICAS ---')
print ('')

pecas_ok = input(' Todas as pessas críticas estão no lugar? (s/n): ')
if pecas_ok.lower() == 'n':
    print(' ALERTA: Peças críticas incompletas! Verificar antes de operar.')
else:
    print(' Peças críticas OK. Pronto para operar!')

print ('')  

print( '--- PROTEÇÕES DE BICOS DE ENVASE ---')
print ('')

tela_ok = input(' Telas de proteção dos bicos estão instaladas? (s/n): ')

if tela_ok.lower() == 'n':
    print(' ALERTA: Telas de proteção dos bicos ausentes! Risco de contaminação do produto.')
else: 
    print(' Telas de proteção dos bicos OK.')

print ('')

print (' --- EMBALAGEM E VALIDADE ---')
print ('')

validade_ok = input('Validade e lote conferidos? (s/n): ')

if validade_ok.lower() == 'n': 
    print(' ALERTA: Validade e lote não conferidos! Verificar antes de liberar a produção.')

else: 
    print(' Validade e Lote Ok. Pronto para operar!')

embalagem_ok = input('Embalagem dentro do padrão? (s/n): ')

if embalagem_ok.lower() == 'n':
    print(' ALERTA: Embalagens fora do padrão! Acionar responsável,')
else: 
    print(' Embalagens dentro do padrão. Pronto para operar!')

print ('')

print (' === RELATÓRIO FINAL ===')
print ('')

alertas = [] #Lista vazia, sem nenhum intem ainda

if temp_pont < 340 or temp_pont > 360:
    alertas.append('Temperatura do ponteador fora do padrão') #append adciona um intem na lista

if temp_sel < 240 or temp_sel > 260:
    alertas.append('Temperatura de selagem fora do padrão')

if pressao < 5.5 or pressao > 6.5:
    alertas.append('Pressão do ar comprimido fora do padrão')

if pecas_ok.lower() == 'n':
    alertas.append('Peças críticas incompletas')

if tela_ok.lower() == 'n':
    alertas.append('Telas de proteção dos bicos ausentes')

if validade_ok.lower() == 'n':
    alertas.append('Validade e lote não conferidos')

if embalagem_ok.lower() == 'n':
    alertas.append('Embalagens fora do padrão')

if len(alertas) == 0: #lista vazia = nenhum alerta encontrado = tudo ok
    print(f'checklist concluido por {operador} - Máquina {maquina}')
    print('Todos os itens dentro do padrão. Liberado para operação.')
else:
    print(f'Cheklist contuido por {operador} - Máquina {maquina}')
    print(f' {len(alertas)} alerta(s) encontrado(s):')
    print('')
    for alerta in alertas: #percorre cada intem da lista alertas, e para cada intem encontrado, ele imprime o alerta
        print(f'  - {alerta}')
    print('')
    print(' Acionar responsável antes de iniciar operação!')

print ('')
print('=== FIM DO CHECKLIST ===')