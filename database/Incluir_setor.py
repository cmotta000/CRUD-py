from database.setor_dao import SetorDAO

print('Incluir novo setor!')

sigla= input('Digite seu sigla do setor: ')
nome=input("Digite o nome do setor: ")
email=input('Digite o email do setor: ')

dao= SetorDAO()
setor= dao.new_object()
setor.sgl_setor= sigla
setor.nme_setor=nome
setor.eml_setor=email
setor.sts_setor="A"
dao.insert(setor)
print(f"Setor{setor.idt_setor} incluído com sucesso!")