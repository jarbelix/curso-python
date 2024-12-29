# Programação Orientação a Objetos em Python
# Paradigma de programação (forma de programação)

# Classes e Objetos

class Veiculo:
    def movimentar(self):
        print(f'Sou um veículo e me desloco!')

    def __init__(self, fabricante, modelo):
        # Encapsulamento de atributo com '__'
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None

     # Getter
    def get_fabr_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}')

    def get_num_registro(self):
        return self.__num_registro

    # Setter
    def set_num_registro(self, registro):
        self.__num_registro = registro
    
# HERANÇA
class Carro(Veiculo):
    # O método __INIT__ será herdado
    def movimentar(self):
        print(f'Sou um Carro e ando pelas ruas')

class Motocicleta(Veiculo):
    def movimentar(self):
        print(f'Sou uma moto e corro muito!')

class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        super().__init__(fabricante, modelo)
        self.__cat = categoria

    def get_categoria(self):
        return self.__cat
    
    def movimentar(self):
        print(f'Eu voo alto')


if __name__ == '__main__':
    meu_veiculo = Veiculo('GM', 'Cadillac Escalade')
    meu_veiculo.movimentar()
    #print(meu_veiculo.fabricante)
    #print(meu_veiculo.modelo)
    meu_veiculo.get_fabr_modelo()
    meu_veiculo.set_num_registro('490321-1')
    print(f'Registro: {meu_veiculo.get_num_registro()}')

    meu_carro = Carro('Volkswagen', 'Polo')
    meu_carro.movimentar()
    meu_carro.get_fabr_modelo()

    seu_carro = Carro('Audi', 'A5 Sportback')
    seu_carro.movimentar()
    seu_carro.get_fabr_modelo()

    moto = Motocicleta('Harley-Davidson', 'Nighster Special')
    moto.movimentar()
    moto.get_fabr_modelo()

    meu_aviao = Aviao('Boeing', '747', 'Comercial')
    meu_aviao.movimentar()
    meu_aviao.get_fabr_modelo()
    print(f'Categoria: {meu_aviao.get_categoria()}')

    