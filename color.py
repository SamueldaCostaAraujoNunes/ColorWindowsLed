from typing import Tuple

class Color:

    def __init__(self, color, standard):
        self.standard = self.verify_standard(standard)
        self.color = self.verify_color(color)
        self.functions_color = {('RGB', 'HEX'): self.rgb_to_hex, ('HEX', 'RGB'): self.hex_to_rgb}

    def verify_standard(self, standard):
        padrao = standard.upper()
        if padrao in {"HEX", "RGB", "HSV"}:
            return padrao
        else:
            raise Exception("Invalid standard")

    def verify_color(self, color):
        if self.standard == "HEX":
            return self.is_hex(color)
        elif self.standard == "RGB":
            return self.is_rgb(color)
            
    def is_rgb(self, color):
        if isinstance(color, (list ,tuple)):
            if len(color) == 3:
                for espectre in color:
                    if isinstance(espectre, int):
                        if not (espectre >= 0 and espectre <= 255):
                            raise Exception(f"A cor: {color} não corresponde ao padrão RGB, pois o item: {espectre} da lista, está fora do intervalo entre 0 e 255")
                        else:
                            return color
                    else:
                        raise Exception(f"A cor: {color} não corresponde ao padrão RGB, pois o item: {espectre} da lista não é um inteiro")
                return
            else:
                raise Exception(f"A cor: {color} não corresponde ao padrão HEX, pois a quantidade de itens na lista não correspondem ao esperado")
        else:
            raise Exception(f"A cor: {color} não corresponde ao padrão RGB, pois não é uma lista ou tupla")

    def is_hex(self, color):
        if isinstance(color, str):
            color = color.lstrip('#') if color.startswith("#") else color
            if self.__is_hex(color):
                return '#'+color.upper()
            else:
                raise Exception(f"A cor: {color} não corresponde ao padrão HEX, pois não respeita a formatação de um hexadecimal")
        else:
            raise Exception(f"A cor: {color} não corresponde ao padrão HEX, pois não é uma string")

    def __is_hex(self, s):
        try:
            int(s, 16)
        except ValueError:
            return False
        return len(s) % 2 == 0

    def set_color(self, color, standard):
        self.standard = self.verify_standard(standard)
        self.color = self.verify_color(color)

    def rgb_to_hex(self, color) -> str:
        r, g, b = color
        hex_color = f"#{r:02x}{g:02x}{b:02x}"
        return hex_color.upper()

    def hex_to_rgb(self, color) -> Tuple[int, int, int]:
        value = color.lstrip('#')
        return tuple(int(value[i:i + 2], 16) for i in range(0, 6, 2))

    def to_max(self, color, standard) -> Tuple[int, int, int]:
        if standard == 'RGB':
            cores = color
        else:
            cores = self.functions_color.get((standard, 'RGB'))(color)
        max_color: int = max(cores)
        n_cor = tuple(int((cor/max_color)*255) for cor in cores)

        return n_cor if standard == 'RGB' else self.functions_color.get(('RGB', standard))(n_cor)

    def get_color(self, standard=None, max=False):
        if standard is None or self.standard == standard.upper():
            return self.to_max(self.color, standard) if max else self.color
        else:
            standard = self.verify_standard(standard)
            n_color = self.functions_color.get((self.standard, standard))(self.color)
            return self.to_max(n_color, standard) if max else n_color

if __name__ == "__main__":
    color = Color([230,67,0], standard="rgb")
    print(color.get_color(standard="hex", max=False))