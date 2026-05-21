print("Vamos criar seu cartão!","Me Informe alguns dados antes:\n",sep="\n",)

nome = input("Nome: ")
prof = input("Profissão: ")
empresa = input("Empresa: ")
email = input("E-mail: ")
telefone = input("Telefone: ")
borda_do_cartao = "="*15+"="*len(nome)

print("\nSeu cartão de visita está pronto!:\n")

print(borda_do_cartao)
print(f"{nome.center(len(borda_do_cartao))}")
print(f"{prof.center(len(borda_do_cartao))}")
print(f"{empresa.center(len(borda_do_cartao))}")
print(f"{email.center(len(borda_do_cartao))}")
print(f"{telefone.center(len(borda_do_cartao))}")
print(borda_do_cartao)