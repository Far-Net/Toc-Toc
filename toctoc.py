from os import system
from time import strftime, sleep
from pyfiglet import figlet_format
from sys import stdout
from colorama import Style, init, Fore

init(autoreset = True)

hour = strftime('%H:%M:%S')
opcao = 0

def carregando():
    for i in range(1):
        print('')
        for chars in ['Tt', 'Oo', 'Cc', '-', 'Tt', 'Oo', 'Cc']:
            stdout.write(Style.BRIGHT + Fore.WHITE + '' + chars.ljust(7))
            stdout.flush()
            sleep(0.2)

print('\n\033[1;32m[!]\033[m executing Toc-Toc...')
carregando()
sleep(3)

system('clear')
banner = figlet_format('Toc - Toc', font = 'block')
print('{}{}{}'.format('\033[1;33m', banner, '\033[m'))

def toctoc():
    print('\n\033[1;33m[ Descubra portas abertas com total liberdade de escolha ]\033[m\n')
    print('[1] Escanear portas\n[2] Sair\n')
    opcao_inicial = int(input('[ Toc-Toc ] \033[1;32m>>\033[m '))

    if opcao_inicial == 1:
        endereco_web = str(input(f'\n┌──[ Endereço web ou IP \033[1;32m{hour}\033[m ]\n└─>> ')).strip().upper()
        while not '.' in endereco_web:
            print('\n\033[1;31mERRO\033[m\n')
            endereco_web = str(input(f'┌──[ Endereço web ou IP \033[1;32m{hour}\033[m ]\n└─>> ')).strip().upper()

        print('\n[1] Verificar todas as portas\n[2] Verificar somente uma porta\n[3] Sair\n')

        opcao = int(input(f'┌──[ Qual opção deseja \033[1;32m{hour}\033[m ]\n└─>> '))

        if opcao == 1:
            print('\nOpção 1 selecionada, direcionando ao setor 1...')
            carregando()
            sleep(3)
            system('clear')

            print(Style.RESET_ALL + f'\033[1;31m VERIFICAR TODAS AS PORTAS DE {endereco_web} \033[m '.center(100, '='), '\n')
            print('[1] Modo normal, pode demorar muito\n[2] T4 (Modo extra rápido)\n[3] T5 (Modo extra rápido \033[1;33mnão tão preciso\033[m)\n')
            opcao_setor1 = int(input('Qual modo gostaria de usar? '))
            print('\n\033[1;33m[ Isso pode demorar um pouco... ]\033[m \n\033[1;35m[ Enquanto escaneio, tire o tempo para fazer algo ]\033[m\n')
            try:
                if opcao_setor1 == 1:
                    system(f'nmap -p- {endereco_web}')
                elif opcao_setor1 == 2:
                    system(f'nmap -p- -T4 {endereco_web}')
                elif opcao_setor1 == 3:
                    system(f'nmap -p- -T5 {endereco_web}')
                else:
                    print('opcao invalida')
                print('='*90)
            except KeyboardInterrupt:
                print('\033[1;31m[ PROCESSO INTERROMPIDO ]\033[m')

            novamente = str(input('\nDeseja iniciar o programa de novo? ')).strip()
            if novamente == 's' or novamente == 'ss' or novamente == 'sim':
                carregando()
                system('clear')
                toctoc()
            else:
                print('\n\033[1;31m[ SAINDO... ]\033[m')
                carregando()
                sleep(2)
                system('clear')

        elif opcao == 2:
            porta = int(input(f'\n┌──[ Porta \033[1;32m{hour}\033[m ]\n└─>> '))
            print(f'\033[1;32m VERIFICANDO A PORTA {porta} DE {endereco_web} \033[m'.center(130, '='))
            system(f'nmap -p {porta} {endereco_web}')
            print('='*120)

            novamente = str(input('\nDeseja iniciar o programa de novo? ')).strip()
            if novamente == 's' or novamente == 'ss' or novamente == 'sim':
                carregando()
                system('clear')
                toctoc()
            else:
                print('\n\033[1;31m[ SAINDO... ]\033[m')
                carregando()
                sleep(2)
                system('clear')
    else:
        print('\n\033[1;31m SAINDO... \033[m')
        carregando()
        sleep(2)
        system('clear')
toctoc()
