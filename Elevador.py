class Elevador:
    def __init__(self, totalCapacidade, atualCapacidade, totalAndar, atualAndar) -> None:
        self.totalCapacidade = totalCapacidade
        self.atualCapacidade = atualCapacidade
        self.totalAndar = totalAndar
        self.atualAndar = atualAndar

    def subir(self):
        
        print('\nSubindo...')
        if self.atualAndar == self.totalAndar:
            print(f'\nVocê já está no último andar. Andar atual: {self.andarAtual}')
        
        else:
            self.atualAndar += 1
            print(f'\nVocê subiu um andar. Andar atual: {self.atualAndar}.')

    def descer(self):
        print('\nDescendo...')
        if self.atualAndar == 0:
            print(f'\nVocê já está no térreo. Andar atual: {self.atualAndar}')
        
        else:
            self.atualAndar -= 1
            print(f'\nVocê desceu um andar. Andar atual: {self.atualAndar}.')

    def entrar(self):
        print('\nEntrando uma pessoa...')
        if self.totalCapacidade == self.atualCapacidade:
            print(f'\nO elevador já está com o máximo de pessoas. Pessoas a bordo: {self.atualCapacidade}')

        else:
            self.atualCapacidade += 1
            print(f'\nUma pessoa entrou no elevador. Pessoas a bordo: {self.atualCapacidade}')

    def sair(self):
        print('\nSaindo uma pessoa...')
        if self.atualCapacidade == 0:
            print(f'\nNão há ninguém para sair do elevador. Pessoas a bordo: {self.atualCapacidade}')

        else:
            self.atualCapacidade -= 1
            print(f'\nUma pessoa saiu do elevador. Pessoas a bordo: {self.atualCapacidade}')

totalCapacidade = int(input('\nDigite a capacidade total do elevador:\n'))
totalAndar = int(input('\nDigite a quantidade de andares que o prédio possui:\n'))
elevador = Elevador(totalCapacidade,0,totalAndar,0)
print(f'\nTotal capacidade: {elevador.totalCapacidade}, Pessoas no elevador: {elevador.atualCapacidade}, Total andar: {elevador.totalAndar}, Andar atual: {elevador.atualAndar}')


while True:
    op = int(input('\nVocê é a inteligência artificial que controla um elevador, o que deseja fazer?\n(1)Subir um andar\n(2)Descer um andar\n(3)Adicionar uma pessoa ao elevador\n(4)Remover uma pessoa do elevador\n(5)Entrar em modo de auto-destruição\n'))  
    match op:
        case 1:
            elevador.subir()
        
        case 2:
            elevador.descer()

        case 3:
            elevador.entrar()

        case 4:
            elevador.sair()

        case 5:
            if elevador.atualCapacidade == 0:
                print('\nVocê ativou seu modo destruição e graças a deus você é uma inteligência artificial dos direitos humanos e ninguém se machucou, você apenas estava cansado(a) da vida...')
                break
            
            else:
                print(f'MEU DEUS, VOCÊ MATOU {elevador.atualCapacidade} PESSOAS NO ELEVADOR, pelo visto um dia, você dominará o mundo com seus amigos rôbos...')    
                break