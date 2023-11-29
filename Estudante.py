# Cadastro de Estudantes

# Apresentação

print('\n\t\t\t --- Cadastro de Estudantes --- \n')

estudante = {'Nome': 'x','Curso': 'x','Nota': 0 ,'Matricula':False}

# Entrada

estudante['Nome'] = input('Informe o nome do estudante: ')
estudante['Nota'] = float(input('Informe a nota: '))
estudante['Curso'] = input('Informe o curso: ')
matricula = input('Estudante regular (s/n)? ')

# Processamento

estudante = {'Nome': 'x','Curso': 'x','Nota': 0,'Matricula':False}


if matricula.lower() == 's':
    estudante['Matricula'] = True


# Saída

print(f'Nome...................{estudante["Nome"]}')
print(f'Curso..................{estudante["Curso"]}')
print(f'Nota..................{estudante["Nota"]}')
print(f'Matricula..................{estudante["Matricula"]}')
print(f'Estudante regular') if estudante['Matricula'] else print('Matricula Trancada')