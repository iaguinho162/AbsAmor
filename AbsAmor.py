import os

tam = 500
cadastro_doadores = [] * tam
cadastro_instituicao = [] * tam
valor_doacao = []
qtn_adsorventes = []
quantidade_absorvente_por_valor_arrecadado = []
data_de_doacao = []
horario_de_doacao = []


def cadastro_Doa(cadastro_doadores, ):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('##########################   Cadastro de Doadores ##########################')
    print('\n')
    nome_doador = input('Digite seu nome:  ')
    cpf_doador = int(input('Digite seu CPF:  '))
    telefone_doador = int(input('Digite seu Telefone:  '))
    email_doador = input('Digite seu Email:  ')
    nasci_doador = input('Digite seu Nascimento:  ')
    login_doador = input('Digite um login:  ')
    senha_doador = input('Digite uma senha:  ')
    senha2_doador = input('Digite novamente a senha:   ')

    if senha_doador == senha2_doador:

        if len(cadastro_doadores) == 0:
            cadastro_doadores.append(
                (nome_doador,
                 cpf_doador,
                 telefone_doador,
                 email_doador,
                 nasci_doador,
                 login_doador,
                 senha2_doador)
            )

            os.system('cls' if os.name == 'nt' else 'clear')
            print('----------------------------------------------------------')
            print(f'Nome: {nome_doador}\n CPF: {cpf_doador}\n Telefone: {telefone_doador}\n Email: {email_doador}')
            print('CADASTRO REALIZADO COM SUCESSO')
            print('----------------------------------------------------------')
            perfil_doador()

        elif len(cadastro_doadores) > 0:
            for i in cadastro_doadores:
                if i[1] != cpf_doador:
                    cadastro_doadores.append(
                    (nome_doador,
                    cpf_doador,
                    telefone_doador,
                    email_doador,
                    nasci_doador,
                    login_doador,
                    senha2_doador)
                    )
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('----------------------------------------------------------')
                    print(f'Nome: {nome_doador}\n CPF: {cpf_doador}\n Telefone: {telefone_doador}\n Email: {email_doador}')
                    print('CADASTRO REALIZADO COM SUCESSO')
                    print('----------------------------------------------------------')
                    perfil_doador()
                else:
                    print('Cpf já existe!')
    else:
        print('Dados Inválidos, cadastro não realizado')

def perfil_doador():
    
    print('###########     PERFIL DO DOADOR     ##################')
    print('')
    print('')
    print('[ 1 ] Doação de Dinheiro\n')
    print('[ 2 ] Doação de Absorventes\n')
    print('[ 3 ] Sair')
    opcao_perfil_doador = int(input())

    if opcao_perfil_doador == 1:

        os.system('cls' if os.name == 'nt' else 'clear')
        print('##########################   Forma de pagamento   ##########################\n')
        print('[ 1 ] Cartão de Credito/Debíto\n')
        print('[ 2 ] Boleto\n')
        print('[ 3 ] Pix\n')
        print('[ 4 ] Voltar')
        opcao_se_perfil = int(input())

        if opcao_se_perfil == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('##########################   Cartão de Credito ##########################\n')
            valor_cartao = float(input('Digite o Valor:  '))
            nome_cartao = input('Digite o Nome no Cartão:   ')
            numero_cartao = int(input('Digite o Numero no Cartão:  '))
            cvv_cartao = int(input('Digite o código de segurança do cartão:   '))
            validade_cartao = input('Digite a validade do cartão: ')
            valor_doacao.append((valor_cartao))
            print('############################################')
            print('#######   Doação Feita com Sucesso!! #######')
            print('############################################\n\n')
            perfil_doador()

        elif opcao_se_perfil == 2:
            valor_boleto = int(input('Digite o valor da doação: '))
            if valor_boleto == 0:
                print('Nenhnum valor Informado')
                perfil_doador()
            else:
                print('Gerado seu boleto no anexo:\n')
                print('001 9 337370000000100 05009 401448 16060680935031\n')
                print('Copie o codigo do barras para realizar o pagamento!')
                perfil_doador()
                valor_doacao.append((valor_boleto))

        elif opcao_se_perfil == 3:
            print('Copie o Cole a chave pix no seu APP do banco:\n')
            print('PIX: "aboservendoamor@gmail.com" ')
            perfil_doador()

        elif opcao_se_perfil == 4:
            perfil_doador()

        valorPorAbsorvente = 10
        valorTotal = 0
        for i in valor_doacao:
            valorTotal += i

        quantidadeDeAbsorventesParaDoacao = valorTotal / valorPorAbsorvente
        print(f'Quantidade de absorventes para doação com base no valor arrecadado é: {quantidadeDeAbsorventesParaDoacao}')
        quantidade_absorvente_por_valor_arrecadado.append(quantidadeDeAbsorventesParaDoacao)

    elif opcao_perfil_doador == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('##########################   Doação de Absorventes   ##########################\n\n')
        opc = int(input('[ 1 ] Para realizar as doações\n[ 2 ] Voltar:\n'))
        if opc == 1:
            quantidade_adsorventes = int(input('Quantas unidades voçe deseja fazer a doação?  '))
            qtn_adsorventes.append((quantidade_adsorventes))
            data_doacao = input('Marque uma data: ')
            data_de_doacao.append((data_doacao))
            horario = input('Informe o horário: ')
            horario_de_doacao.append((horario))
            print('----------------------------------------------------------------------')
            print(
                'Todas as doações serão feitas de forma presencial\nna Insituição de Ensino CEST.\nEndereço: Av. Casemiro Júnior, 12\nAnil, São Luís - MA, 65045-180')
            print('\n#### Agendada!! #### \n')
            print('----------------------------------------------------------------------')
            perfil_doador()
        if opc == 2:
            perfil_doador()
        else:
            print('Opção Inválida')


    
def cadastro_institui(cadastro_instituicao):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('##########################   Cadastro da Instituição ##########################\n')
    print('')
    instituicao_instituicao = input('Informe o nome da sua instuição:   ')
    cep_instituicao = int(input('Digite o CEP da sua Instituição:   '))
    CNPJ_instituicao = int(input('Digite o CNPJ da sua Instituição:   '))
    Telefone_instituicao = int(input('Informe o Telefone para contato:   '))
    email = input('Informe o email da sua Instuição:  ')
    os.system('cls' if os.name == 'nt' else 'clear')
    usuario_instituicao = input('Informe o Login: ')
    senha_instituicao = input('Senha: ')
    senha2_instituicao = input('Confirmação da senha: ')
    os.system('cls' if os.name == 'nt' else 'clear')
    print('--------------CADASTRO DE BENEFICIARIO----------\n')
    quinto_ano = int(input('Quantidade de alunas do 5º:      \n'))
    sexto_ano = int(input('Quantidade de alunas do 6º:      \n'))
    setimo_ano = int(input('Quantidade de alunas do 7º:      \n'))
    oito_ano = int(input('Quantidade de alunas do 8º:      \n'))
    nono_ano = int(input('Quantidade de alunas do 9º:      \n'))
    quantidade_total_alunas = quinto_ano + sexto_ano + setimo_ano + oito_ano + nono_ano
    


    if senha2_instituicao == senha_instituicao:
        cadastro_instituicao.append((instituicao_instituicao, cep_instituicao, CNPJ_instituicao, Telefone_instituicao,
                                     email, usuario_instituicao, senha_instituicao, senha2_instituicao, quantidade_total_alunas))
       
        os.system('cls' if os.name == 'nt' else 'clear')
        print('--------------------------------------------')
        print(
        f'Instituição: {instituicao_instituicao}\nCEP: {cep_instituicao}\n CNPJ: {CNPJ_instituicao}\nTelefone: {Telefone_instituicao}\nEmail:{email}')
        print('Cadastro Feito com Sucesso!!')
        print('--------------------------------------------')
        perfil_instituicao()
            

    else:
        print('############################################')
        print('ERRO!!!')
        print('Dados Incorretos')
        print('############################################')
        os.system('cls' if os.name == 'nt' else 'clear')
        cadastro_institui()


def perfil_instituicao():
    
    print('##########################   Perfil Institucional ##########################')
    print('[ 1 ] Cadastrar Alunos')
    print('[ 2 ] Sair')
    opcao = int(input())
    if opcao == 1:
        print('--------------CADASTRO DE BENEFICIARIO----------\n')
        quinto_ano = int(input('Quantidade de alunas do 5º:      \n'))
        sexto_ano = int(input('Quantidade de alunas do 6º:      \n'))
        setimo_ano = int(input('Quantidade de alunas do 7º:      \n'))
        oito_ano = int(input('Quantidade de alunas do 8º:      \n'))
        nono_ano = int(input('Quantidade de alunas do 9º:      \n'))
        quantidade_total_alunas = quinto_ano + sexto_ano + setimo_ano + oito_ano + nono_ano
        
    elif opcao == 2:
        menu()
        


def entrar_adm():
    
    print('##########################   ADMINISTRADOR  ##########################')
    print('')
    print('')
    print('[ 1 ] Exibir Valores / Doações Arrecadados\n')
    print('[ 2 ] Horarios de doações agendados pelos Doadores\n')
    print('[ 3 ] Consultar / Excluir  / Listar Doadores\n')
    print('[ 4 ] Consultar / Excluir  / Listar Instituição\n')
    print('[ 5 ] Agendar Horario para entrega\n')
    print('[ 6 ] Sair')
    opcao_adm = int(input(''))

    if opcao_adm == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('--------------------------------------------')
        print('##########################   Valores e Doações ##########################\n\n')
        if len(valor_doacao) == 0:
            if len(qtn_adsorventes) == 0:
                print('Nenhnum valor encontrado!')
                sair = int(input('[ 1 ] Voltar: '))
                if sair == 1:
                    entrar_adm()
                
        else: 
            print('##########################   Valores e Doações  ##########################')
            print(f'Quantidade de Valores Arrecadados : {valor_doacao}R$ (Reais)')
            print(f'Número de pacotes: {quantidade_absorvente_por_valor_arrecadado}, com base no valor arrecadado: {valor_doacao}')
            print(f'Quantidade de absorventes por doação direta: {qtn_adsorventes}')
            print('')
            print('--------------------------------------------')
            sair = int(input('[ 1 ] Voltar: '))
            if sair == 1:
                entrar_adm()


    elif opcao_adm == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('##########################   Horários Agendandos  ##########################\n\n')
        print('--------------------------------------------')
        print('Datas Marcadas:')
        print(f'Data: {data_de_doacao}\t Horário: {horario_de_doacao}')
        print('--------------------------------------------')
        sair = int(input('[ 1 ] Voltar: '))
        if sair == 1:
            entrar_adm()

    elif opcao_adm == 3:
        remove_doares()
        entrar_adm()

    elif opcao_adm == 4:
        remove_benefi()
        entrar_adm()

    elif opcao_adm == 5:
        if len (cadastro_instituicao) == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Sem instituição Cadastrado!!')
            sair = int(input('[ 1 ] Voltar: '))
            if sair == 1:
                entrar_adm()
        else: 
            print('Qual Instituição Deseja agendar a doação? ')
            busca_escola = int(input('Digite CNPJ:  '))
            print('-----------------------------------------------------')
            for k in cadastro_instituicao:
                instituicao_instituicao, cep_instituicao, CNPJ_instituicao, Telefone_instituicao, email, usuario_instituicao, senha_instituicao, senha2_instituicao, quantidade_total_alunas = k
                if busca_escola == CNPJ_instituicao and CNPJ_instituicao in k:
                    print(
                         f'Instituição: {instituicao_instituicao}  \t CEP: {cep_instituicao} \t Telefone: `{Telefone_instituicao}\n  ')
                    print('-------------------------------------------------------------')
                    print(f"Quantidade de alunas que necessita: {quantidade_total_alunas} ")
                    print(f'Quantidade no Estoque por doação direta : {qtn_adsorventes}, e por valor arrecadado {quantidade_absorvente_por_valor_arrecadado}')

                    quantidadeDeAbsorvente = 0
                    for i in qtn_adsorventes:
                        quantidadeDeAbsorvente += i
                        if quantidadeDeAbsorvente < quantidade_total_alunas:
                            print('Estoque insuficiente!')
                        else:
                            quantidadeEmEstoque = quantidadeDeAbsorvente - quantidade_total_alunas
                            print(f'A quantidade de absorventes doados foram {quantidadeDeAbsorvente} '
                            f' e ainda temos em estoque {quantidadeEmEstoque} disponível')
                            agendar = input('Digite uma data para agendar com a instituição: ')                    
                            print('-------------------------------------------------------------')
                            print(f'Horario agendando para doação: {agendar}\n' )
                            print(f'Foi enviado um email para o endereço:\t{email}\tcom a data informada!! \n')
                            print('Obrigadoo!!')
                            print('-------------------------------------------------------------')
                            entrar_adm()
                else:
                    print('Instituição não encontrada! ')
                    entrar_adm()

            

    elif opcao_adm == 6:
        menu()


def remove_benefi():
    if len (cadastro_instituicao) == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Sem instituição Cadastrada!!')
        sair = int(input('[ 1 ] Voltar: '))
        if sair == 1:
            entrar_adm()
    else:
        print("########### Lista de Beneficiario: ##########")
        for lista in cadastro_instituicao:
            instituicao_instituicao, cep_instituicao, CNPJ_instituicao, Telefone_instituicao, email, usuario_instituicao, senha_instituicao, senha2_instituicao, quantidade_total_alunas = lista
            print(f'\nInstituição: {instituicao_instituicao}\t CEP: {cep_instituicao}\t CNPJ: {CNPJ_instituicao}\t Telefone: {Telefone_instituicao}\t Email: {email}')
            print('-----------------------------------------------------------------')
        excluir_benefi_adm = input('Deseja Excluir? [ S ], [ N ]: ')
        if excluir_benefi_adm == 'S':
            excluir_insti_adm = int(input('Informe o CNPJ:  '))
            for insti_loop in cadastro_instituicao:
                for i in insti_loop:
                    instituicao_instituicao, cep_instituicao, CNPJ_instituicao, Telefone_instituicao, email, usuario_instituicao, senha_instituicao, senha2_instituicao, quantidade_total_alunas = insti_loop
                    if excluir_insti_adm == CNPJ_instituicao and CNPJ_instituicao in insti_loop:
                        cadastro_instituicao.remove(insti_loop)
                        print('Instituição Removida!!')
                        break
                    
                


def remove_doares():
    if len (cadastro_doadores) == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Sem Doadores Cadastrado!!')
        sair = int(input('[ 1 ] Voltar: '))
        if sair == 1:
            entrar_adm()
    else: 
        print('########### Lista de Doadores: ##########')
        for listar_doadores in cadastro_doadores:
            nome_doador, cpf_doador, telefone_doador, email_doador, nasci_doador, login_doador, senha2_doador = listar_doadores
            print(f'Nome: {nome_doador}\t CPF: {cpf_doador}\t Telefone: {telefone_doador}\t Email: {email_doador}')
            print('-----------------------------------------------------------------')

        excluir_doadores_adm = input('Deseja Excluir? [ S ], [ N ]:')
        if excluir_doadores_adm == 'S':
            CPF_excluir = int(input('Informe O CPF: '))
            for doador in cadastro_doadores:
                for i in doador:
                    nome_doador, cpf_doador, telefone_doador, email_doador, nasci_doador, login_doador, senha2_doador = doador
                    if CPF_excluir == cpf_doador and cpf_doador in doador:
                        cadastro_doadores.remove(doador)
                        print('Doador Removido!!')
                        break
                        
                    
        if excluir_doadores_adm == 'N':
            entrar_adm()


def entrar_sistema():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('##########################  Tela de Acesso ##########################\n\n')
    login_adm = "admin"
    senha_adm = "admin"
    login_sistema = input('Login:       ')
    senha_sistema = input('Senha:       ')

    for i in cadastro_doadores:
        nome_doador, cpf_doador, telefone_doador, email_doador, nasci_doador, login_doador, senha2_doador  = i
        if senha_sistema == senha2_doador in senha2_doador in i:
            if login_sistema == login_doador in login_doador in i:
                perfil_doador()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Dados Incorrentos Ou Perfil Não Cadastrado')
        break

    for f in cadastro_instituicao:
        instituicao_instituicao, cep_instituicao, CNPJ_instituicao, Telefone_instituicao, email, usuario_instituicao, senha_instituicao, senha2_instituicao, quantidade_total_alunas = f
        if senha_sistema == senha_instituicao in senha_instituicao in f:
            if login_sistema == usuario_instituicao in usuario_instituicao in f:
                perfil_instituicao()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Dados Incorrentos Ou Perfil Não Cadastrado')
        break

    if (login_sistema == login_adm):
        if (senha_sistema == senha_adm):
            entrar_adm()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Dados Incorrentos Ou Perfil Não Cadastrado') 
    else:
           print('Dados Incorrentos Ou Perfil Não Cadastrado') 
    


def menu():
    opcao = 0
    while opcao != 6:

        print('##########################  Abosorvendo Amor ##########################')
        print('\n')
        print('[1] Entrar\n')
        print('[2] Cadastro de Doadores\n')
        print('[3] Cadastro de Instituição\n')
        print('[4] Informações\n')
        print('[5] Contatos\n')
        print('[6] Sair: \n')

        opcao = int(input())

        if opcao == 1:
            entrar_sistema()

        elif opcao == 2:
            cadastro_Doa(cadastro_doadores)

        elif opcao == 3:
            cadastro_institui(cadastro_instituicao)

        elif opcao == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('##########################   Informações ##########################')
            print('')
            print(
                'Sistema criado com intuito de assegurar saúde\nde estudantes dos ensinos fundamental e médio\nmulheres em situação de vulnerabilidade á recebe\nde forma gratuita, absorventes para sua higiene pessoal.\n')
            print('--------------------------------------------')
            sair_op_4 = int(input('1- Sair:   '))
            if sair_op_4 == 1:
                menu()

        elif opcao == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('##########################   Contatos ##########################\n\n')
            print('email: aboservendoamor@gmail.com\nContato: (98) 98665-4789\n')
            print('--------------------------------------------')
            sair_op_5 = int(input('[ 1 ] Sair: '))
            if sair_op_5 == 1:
                menu()

        elif opcao == 6:
            print('Programa Encerrado!!')


menu()