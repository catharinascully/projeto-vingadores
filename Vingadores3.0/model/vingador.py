class Vingador:
    lista_vingadores = []
 
    class CategoriaVingadores:
        HUMANO = "Humano"
        META_HUMANO = "Meta-humano"
        ALIENIGENA = "Alienígena"
        DEIDADE = "Deidade"
        CATEGORIAS_VALIDAS = [HUMANO, META_HUMANO, ALIENIGENA, DEIDADE]
 
    def __init__(self, nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca):
        self.nome_heroi = nome_heroi
        self.nome_real = nome_real
        self.categoria = categoria
        self.poderes = poderes
        self.poder_principal = poder_principal
        self.fraquezas = fraquezas
        self.nivel_forca = nivel_forca
        self.tornozeleira = False
        self.chip_gps = False
        self.convocado = False
 
    def __str__(self):
        return (f'{self.nome_heroi.ljust(20)} | {self.nome_real.ljust(20)} | {self.categoria.ljust(15)} | '
                f'{"Sim" if self.tornozeleira else "Não"} | {"Sim" if self.chip_gps else "Não"}')
 
    def detalhes(self):
        poderes_str = (self.poderes)
        fraquezas_str = (self.fraquezas)
        return (f'Nome do Herói: {self.nome_heroi}\n'
                f'Nome Real: {self.nome_real}\n'
                f'Categoria: {self.categoria}\n'
                f'Poderes: {poderes_str}\n'
                f'Poder Principal: {self.poder_principal}\n'
                f'Fraquezas: {fraquezas_str}\n'
                f'Nível de Força: {self.nivel_forca}\n'
                f'Tornozeleira: {"Aplicada" if self.tornozeleira else "Não Aplicada"}\n'
                f'Chip GPS: {"Aplicado" if self.chip_gps else "Não Aplicado"}\n'
                f'Convocado: {"Sim" if self.convocado else "Não"}')
 
 
    def aplicar_tornozeleira(self):
        if not self.convocado:
            return f'{self.nome_heroi} precisa ser convocado antes de aplicar a tornozeleira.'
        if self.tornozeleira:
            return f'{self.nome_heroi} já está com a tornozeleira aplicada.'
        self.tornozeleira = True
        if self.nome_heroi in ["Thor", "Hulk"]:
            return f'{self.nome_heroi} resistiu, mas a tornozeleira foi aplicada com sucesso.'
        return f'Tornozeleira aplicada a {self.nome_heroi}.'
 
    def aplicar_chip_gps(self):
        if not self.tornozeleira:
            return f'{self.nome_heroi} precisa estar com a tornozeleira antes de aplicar o chip GPS.'
        if self.chip_gps:
            return f'Chip GPS já foi aplicado em {self.nome_heroi}.'
        self.chip_gps = True
        return f'Chip GPS aplicado a {self.nome_heroi}.'
