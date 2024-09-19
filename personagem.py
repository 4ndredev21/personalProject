# Definindo a classe Personagem
class Personagem:
    def __init__(self, nome, classe, forca, agilidade, saude):
        self.nome = nome
        self.classe = classe
        self.forca = forca
        self.agilidade = agilidade
        self.saude = saude
        self.inventario = []

    # Método para exibir as informações do personagem
    def exibir_status(self):
        print(f"\nNome: {self.nome}")
        print(f"Classe: {self.classe}")
        print(f"Força: {self.forca}")
        print(f"Agilidade: {self.agilidade}")
        print(f"Saúde: {self.saude}")
        print(f"Inventário: {', '.join(self.inventario) if self.inventario else 'Vazio'}")

    # Método para atacar
    def atacar(self):
        print(f"{self.nome} ataca com força {self.forca}!")

    # Método para adicionar itens ao inventário
    def pegar_item(self, item):
        self.inventario.append(item)
        print(f"{self.nome} pegou {item}!")

    # Método para ser atacado e perder saúde
    def receber_dano(self, dano):
        self.saude -= dano
        print(f"{self.nome} recebeu {dano} de dano! Saúde atual: {self.saude}")
        if self.saude <= 0:
            print(f"{self.nome} foi derrotado!")

# Criando o personagem
nome_personagem = input("Digite o nome do seu personagem: ")
classe_personagem = input("Escolha a classe (Guerreiro, Mago, Arqueiro): ")
forca_personagem = int(input("Atribua a força do personagem (1 a 10): "))
agilidade_personagem = int(input("Atribua a agilidade do personagem (1 a 10): "))
saude_personagem = int(input("Atribua a saúde do personagem (1 a 100): "))

personagem = Personagem(nome_personagem, classe_personagem, forca_personagem, agilidade_personagem, saude_personagem)

# Exibindo o status do personagem
personagem.exibir_status()

# Simulando ações no jogo
while True:
    print("\nEscolha uma ação:")
    print("1. Atacar")
    print("2. Pegar item")
    print("3. Receber dano")
    print("4. Exibir status")
    print("5. Sair")
    
    acao = input("Digite o número da ação: ")
    
    if acao == "1":
        personagem.atacar()
    elif acao == "2":
        item = input("Digite o nome do item a ser pego: ")
        personagem.pegar_item(item)
    elif acao == "3":
        dano = int(input("Digite o valor do dano recebido: "))
        personagem.receber_dano(dano)
    elif acao == "4":
        personagem.exibir_status()
    elif acao == "5":
        print("Saindo do jogo...")
        break
    else:
        print("Ação inválida!")
