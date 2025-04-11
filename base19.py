# TRABALHO: Projeto: Agenda de contatos

# Desenvolva um programa em Python para gerenciar uma agenda de contatos, que deve oferecer as funcionalidades listadas a seguir:

# 1 Adicionar contato: permitir que o usuário adicione novos contatos, fornecendo nome, idade, telefone, e-mail, renda e estado.
print("Adicione novos contatos!")
certo = "s"
errado= "n"
print (input"quer adicionar um novo número?")
if certo:
    numero= (int(input("adicione o número: ")))
    print (input("quer nomea-lo?"))
    nome= input("nome:")
contatos= {[nome]:[numero]}

# 2 Exibir contatos: mostrar uma lista completa de todos os contatos na agenda, incluindo nome, telefone e e-mail.

# 3 Buscar contato: permitir que o usuário busque as informações de um contato específico, fornecendo o nome do contato.

# 4 Remover contato: possibilitar a remoção de um contato da agenda com base no nome.

# 5 Corrigir contato: substituir uma informação de um contato.

# 6 Mostrar a quantidade de contatos cadastrados.

# 7 Mostrar a média de idade dos contados cadastrados.

# 8 Mostrar a quantidade de contatos cadastrados por estado

'''
Lembre-se de que o programa deve permitir que o usuário preencha os contatos até digitar “sair”
'''
#base do gus
class Contato:
    def __init__(self, nome, idade, telefone, email, renda, estado):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.email = email
        self.renda = renda
        self.estado = estado

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def exibir_contatos(self):
        print("\nLista de Contatos:")
        for contato in self.contatos:
            print(f"Nome: {contato.nome}, Telefone: {contato.telefone}, Email: {contato.email}")

    def buscar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome.lower() == nome.lower():
                print(f"Contato encontrado: Nome: {contato.nome}, Idade: {contato.idade}, Telefone: {contato.telefone}, Email: {contato.email}, Renda: {contato.renda}, Estado: {contato.estado}")
                return
        print("Contato não encontrado.")

    def remover_contato(self, nome):
        for contato in self.contatos:
            if contato.nome.lower() == nome.lower():
                self.contatos.remove(contato)
                print("Contato removido com sucesso.")
                return
        print("Contato não encontrado.")

    def corrigir_contato(self, nome, atributo, novo_valor):
        for contato in self.contatos:
            if contato.nome.lower() == nome.lower():
                if atributo == "telefone":
                    contato.telefone = novo_valor
                elif atributo == "email":
                    contato.email = novo_valor
                elif atributo == "idade":
                    contato.idade = novo_valor
                elif atributo == "renda":
                    contato.renda = novo_valor
                elif atributo == "estado":
                    contato.estado = novo_valor
                else:
                    print("Atributo inválido.")
                    return
                print("Contato corrigido com sucesso.")
                return
        print("Contato não encontrado.")

    def quantidade_contatos(self):
        return len(self.contatos)

    def media_idade(self):
        if not self.contatos:
            return 0
        total_idade = sum(contato.idade for contato in self.contatos)
        return total_idade / len(self.contatos)

    def quantidade_por_estado(self):
        estado_count = {}
        for contato in self.contatos:
            if contato.estado in estado_count:
                estado_count[contato.estado] += 1
            else:
                estado_count[contato.estado] = 1
        return estado_count

def main():
    agenda = Agenda()
    
    while True:
        print("\nMenu:")
        print("1. Adicionar Contato")
        print("2. Exibir Contatos")
        print("3. Buscar Contato")
        print("4. Remover Contato")
        print("5. Corrigir Contato")
        print("6. Mostrar Quantidade de Contatos")
        print("7. Mostrar Média de Idade dos Contatos")
        print("8. Mostrar Quantidade de Contatos por Estado")
        print("9. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            nome = input("Digite o nome: ")
            idade = int(input("Digite a idade: "))
            telefone = input("Digite o telefone: ")
            email = input("Digite o e-mail: ")
            renda = float(input("Digite a renda: "))
            estado = input("Digite o estado: ")
            contato = Contato(nome, idade, telefone, email, renda, estado)
            agenda.adicionar_contato(contato)
            print("Contato adicionado com sucesso.")
        
        elif escolha == "2":
            agenda.exibir_contatos()
        
        elif escolha == "3":
            nome = input("Digite o nome do contato a buscar: ")
            agenda.buscar_contato(nome)
        
        elif escolha == "4":
            nome = input("Digite o nome do contato a remover: ")
            agenda.remover_contato(nome)
        
        elif escolha == "5":
            nome = input("Digite o nome do contato a corrigir: ")
            atributo = input("Digite o atributo a corrigir (telefone, email, idade, renda, estado): ")
            novo_valor = input("Digite o novo valor: ")
            if atributo in ["idade", "renda"]:
                novo_valor = float(novo_valor) if atributo == "renda" else int(novo_valor)
            agenda.corrigir_contato(nome, atributo, novo_valor)
        
        elif escolha == "6":
            print(f"Quantidade de contatos cadastrados: {agenda.quantidade_contatos()}")
        
        elif escolha == "7":
            print(f"Média de idade dos contatos: {agenda.media_idade()}")
        
        elif escolha == "8":
            quantidade_estado = agenda.quantidade_por_estado()
            print("Quantidade de contatos por estado:")
            for estado, quantidade in quantidade_estado.items():
                print(f"{estado}: {quantidade}")
        
        elif escolha == "9":
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()