from abc import ABC, abstractmethod


class Tutor:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def listar_animais(self):
        if len(self.animais) == 0:
            print("Este tutor não possui animais cadastrados.")
            return

        for animal in self.animais:
            animal.mostrar_dados()
            print("-" * 40)


class Animal(ABC):
    def __init__(self, nome, idade, peso, tutor):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.tutor = tutor

    @abstractmethod
    def fazer_som(self):
        pass

    @abstractmethod
    def cuidados_especiais(self):
        pass

    @abstractmethod
    def protocolo_atendimento(self):
        pass

    def mostrar_dados(self):
        print("Tipo:", self.__class__.__name__)
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Peso:", self.peso)
        print("Tutor:", self.tutor.nome)
        print("Som:", self.fazer_som())

        if self.precisa_atencao_especial():
            print("Categoria: ATENÇÃO ESPECIAL")
        else:
            print("Categoria: Normal")

        print("Protocolo:", self.protocolo_atendimento())
        print("Cuidados especiais:")
        for cuidado in self.cuidados_especiais():
            print("-", cuidado)

    def precisa_atencao_especial(self):
        return self.idade >= self.idade_limite_especial


class Cachorro(Animal):
    idade_limite_especial = 8

    def __init__(self, nome, idade, peso, tutor, vacina_antirrabica_em_dia):
        super().__init__(nome, idade, peso, tutor)
        self.vacina_antirrabica_em_dia = vacina_antirrabica_em_dia

    def fazer_som(self):
        return "Au au!"

    def cuidados_especiais(self):
        cuidados = ["Vacina antirrábica anual obrigatória"]
        if self.precisa_atencao_especial():
            cuidados.append("Atenção especial por idade")
        return cuidados

    def protocolo_atendimento(self):
        if self.vacina_antirrabica_em_dia:
            return "Vacina em dia."
        return "ALERTA: vacina antirrábica não informada ou atrasada."


class Gato(Animal):
    idade_limite_especial = 10

    def __init__(self, nome, idade, peso, tutor, vacina_antirrabica_em_dia):
        super().__init__(nome, idade, peso, tutor)
        self.vacina_antirrabica_em_dia = vacina_antirrabica_em_dia

    def fazer_som(self):
        return "Miau!"

    def cuidados_especiais(self):
        cuidados = ["Vacina antirrábica anual obrigatória"]
        if self.precisa_atencao_especial():
            cuidados.append("Atenção especial por idade")
        return cuidados

    def protocolo_atendimento(self):
        if self.vacina_antirrabica_em_dia:
            return "Vacina em dia."
        return "ALERTA: vacina antirrábica não informada ou atrasada."


class Ave(Animal):
    idade_limite_especial = 6

    def __init__(self, nome, idade, peso, tutor, checkup_respiratorio_em_dia):
        super().__init__(nome, idade, peso, tutor)
        self.checkup_respiratorio_em_dia = checkup_respiratorio_em_dia

    def fazer_som(self):
        return "Piu piu!"

    def cuidados_especiais(self):
        cuidados = ["Check-up respiratório a cada 6 meses"]
        if self.precisa_atencao_especial():
            cuidados.append("Atenção especial por idade")
        return cuidados

    def protocolo_atendimento(self):
        if self.checkup_respiratorio_em_dia:
            return "Check-up respiratório em dia."
        return "ALERTA: check-up respiratório não informado ou atrasado."


class ClinicaVeterinaria:
    def __init__(self):
        self.tutores = []
        self.animais = []

    def cadastrar_tutor(self, tutor):
        self.tutores.append(tutor)

    def cadastrar_animal(self, animal):
        self.animais.append(animal)
        animal.tutor.adicionar_animal(animal)

    def listar_tutores(self):
        if len(self.tutores) == 0:
            print("Nenhum tutor cadastrado.")
            return

        for tutor in self.tutores:
            print("Nome:", tutor.nome)
            print("Telefone:", tutor.telefone)
            print("Endereço:", tutor.endereco)
            print("Quantidade de animais:", len(tutor.animais))
            print("-" * 40)

    def listar_animais(self):
        if len(self.animais) == 0:
            print("Nenhum animal cadastrado.")
            return

        for animal in self.animais:
            animal.mostrar_dados()
            print("-" * 40)

    def buscar_animal(self, nome):
        for animal in self.animais:
            if animal.nome.lower() == nome.lower():
                return animal
        return None

    def buscar_tutor(self, nome):
        for tutor in self.tutores:
            if tutor.nome.lower() == nome.lower():
                return tutor
        return None

    def listar_animais_de_um_tutor(self, nome_tutor):
        tutor = self.buscar_tutor(nome_tutor)

        if tutor is None:
            print("Tutor não encontrado.")
            return

        print("Animais do tutor:", tutor.nome)
        tutor.listar_animais()

    def listar_animais_em_atencao_especial(self):
        encontrou = False

        for animal in self.animais:
            if animal.precisa_atencao_especial():
                animal.mostrar_dados()
                print("-" * 40)
                encontrou = True

        if not encontrou:
            print("Nenhum animal em atenção especial.")


def menu():
    print("\n===== CLÍNICA VIDAPET =====")
    print("1 - Cadastrar tutor")
    print("2 - Cadastrar animal")
    print("3 - Listar tutores")
    print("4 - Listar animais")
    print("5 - Buscar animal")
    print("6 - Buscar tutor")
    print("7 - Mostrar animais de um tutor")
    print("8 - Mostrar animais em atenção especial")
    print("9 - Sair")


def escolher_tutor(clinica):
    if len(clinica.tutores) == 0:
        print("Nenhum tutor cadastrado. Cadastre um tutor primeiro.")
        return None

    print("\nTutores cadastrados:")
    for i, tutor in enumerate(clinica.tutores):
        print(i + 1, "-", tutor.nome)

    try:
        opcao = int(input("Escolha o número do tutor: "))
        if opcao < 1 or opcao > len(clinica.tutores):
            print("Opção inválida.")
            return None
        return clinica.tutores[opcao - 1]
    except:
        print("Entrada inválida.")
        return None


def main():
    clinica = ClinicaVeterinaria()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do tutor: ")
            telefone = input("Telefone do tutor: ")
            endereco = input("Endereço do tutor: ")
            tutor = Tutor(nome, telefone, endereco)
            clinica.cadastrar_tutor(tutor)
            print("Tutor cadastrado com sucesso.")

        elif opcao == "2":
            tutor = escolher_tutor(clinica)
            if tutor is None:
                continue

            print("\nTipo de animal:")
            print("1 - Cachorro")
            print("2 - Gato")
            print("3 - Ave")
            tipo = input("Escolha o tipo: ")

            nome = input("Nome do animal: ")

            try:
                idade = int(input("Idade: "))
                peso = float(input("Peso: "))
            except:
                print("Idade ou peso inválido.")
                continue

            if tipo == "1":
                vacina = input("Vacina antirrábica em dia? (s/n): ").lower()
                animal = Cachorro(nome, idade, peso, tutor, vacina == "s")
            elif tipo == "2":
                vacina = input("Vacina antirrábica em dia? (s/n): ").lower()
                animal = Gato(nome, idade, peso, tutor, vacina == "s")
            elif tipo == "3":
                checkup = input("Check-up respiratório em dia? (s/n): ").lower()
                animal = Ave(nome, idade, peso, tutor, checkup == "s")
            else:
                print("Tipo inválido.")
                continue

            clinica.cadastrar_animal(animal)
            print("Animal cadastrado com sucesso.")

        elif opcao == "3":
            clinica.listar_tutores()

        elif opcao == "4":
            clinica.listar_animais()

        elif opcao == "5":
            nome = input("Nome do animal: ")
            animal = clinica.buscar_animal(nome)
            if animal is None:
                print("Animal não encontrado.")
            else:
                animal.mostrar_dados()

        elif opcao == "6":
            nome = input("Nome do tutor: ")
            tutor = clinica.buscar_tutor(nome)
            if tutor is None:
                print("Tutor não encontrado.")
            else:
                print("Nome:", tutor.nome)
                print("Telefone:", tutor.telefone)
                print("Endereço:", tutor.endereco)
                print("Quantidade de animais:", len(tutor.animais))

        elif opcao == "7":
            nome = input("Nome do tutor: ")
            clinica.listar_animais_de_um_tutor(nome)

        elif opcao == "8":
            clinica.listar_animais_em_atencao_especial()

        elif opcao == "9":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida.")


main()
