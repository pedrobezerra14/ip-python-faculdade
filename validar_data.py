meses = {
    '01':'Janeiro',
    '02':'Fevereiro',
    '03':'Março',
    '04':'Abril',
    '05':'Maio',
    '06':'Junho',
    '07':'Julho',
    '08':'Agosto',
    '09':'Setembro',
    '10':'Outubro',
    '11':'Novembro',
    '12':'Dezembro'
}

ano_nascimento = input('Informe sua data de nascimento(dd/mm/aaaa): ')
dia, mes, ano = ano_nascimento.split('/')

match mes:
    case '01':
        pass
    case '02':
        pass
    case '03':
        pass
    case '04':
        pass
    case '05':
        pass
    case '06':
        pass
    case '07':
        pass
    case '08':
        pass
    case '09':
        pass
    case '10':
        pass
    case '11':
        pass
    case '12':
        pass
    
print(f'{dia} de {meses[mes]} de {ano}')