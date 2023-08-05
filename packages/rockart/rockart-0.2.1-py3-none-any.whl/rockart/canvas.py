from rockart.exceptions import RockartException


class Canvas:
    __BASIS = {
        (0, 0): 2**0,  # symbol "⠁"
        (0, 1): 2**1,  # symbol "⠂"
        (0, 2): 2**2,  # symbol "⠄"
        (0, 3): 2**3,  # symbol "⡀"
        (1, 0): 2**4,  # symbol "⠈"
        (1, 1): 2**5,  # symbol "⠐"
        (1, 2): 2**6,  # symbol "⠠"
        (1, 3): 2**7,  # symbol "⢀"
    }

    __SYMBOLS = (
        " ⠁⠂⠃⠄⠅⠆⠇⡀⡁⡂⡃⡄⡅⡆⡇⠈⠉⠊⠋⠌⠍⠎⠏⡈⡉⡊⡋⡌⡍⡎⡏"
        "⠐⠑⠒⠓⠔⠕⠖⠗⡐⡑⡒⡓⡔⡕⡖⡗⠘⠙⠚⠛⠜⠝⠞⠟⡘⡙⡚⡛⡜⡝⡞⡟"
        "⠠⠡⠢⠣⠤⠥⠦⠧⡠⡡⡢⡣⡤⡥⡦⡧⠨⠩⠪⠫⠬⠭⠮⠯⡨⡩⡪⡫⡬⡭⡮⡯"
        "⠰⠱⠲⠳⠴⠵⠶⠷⡰⡱⡲⡳⡴⡵⡶⡷⠸⠹⠺⠻⠼⠽⠾⠿⡸⡹⡺⡻⡼⡽⡾⡿"
        "⢀⢁⢂⢃⢄⢅⢆⢇⣀⣁⣂⣃⣄⣅⣆⣇⢈⢉⢊⢋⢌⢍⢎⢏⣈⣉⣊⣋⣌⣍⣎⣏"
        "⢐⢑⢒⢓⢔⢕⢖⢗⣐⣑⣒⣓⣔⣕⣖⣗⢘⢙⢚⢛⢜⢝⢞⢟⣘⣙⣚⣛⣜⣝⣞⣟"
        "⢠⢡⢢⢣⢤⢥⢦⢧⣠⣡⣢⣣⣤⣥⣦⣧⢨⢩⢪⢫⢬⢭⢮⢯⣨⣩⣪⣫⣬⣭⣮⣯"
        "⢰⢱⢲⢳⢴⢵⢶⢷⣰⣱⣲⣳⣴⣵⣶⣷⢸⢹⢺⢻⢼⢽⢾⢿⣸⣹⣺⣻⣼⣽⣾⣿"
    )

    CELL_WIDTH = 2
    CELL_HEIGHT = 4

    @classmethod
    def of_size(cls, rows, columns):
        width = columns * Canvas.CELL_WIDTH
        height = rows * Canvas.CELL_HEIGHT
        canvas = Canvas(width, height)
        return canvas

    def __init__(self, width, height, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if width % Canvas.CELL_WIDTH != 0:
            raise RockartException(
                "`width` ({width}) must be divisible by "
                "`Canvas.CELL_WIDTH` ({Canvas.CELL_WIDTH}"
            )

        if height % Canvas.CELL_HEIGHT != 0:
            raise RockartException(
                "`height` ({height}) must be divisible by "
                "`Canvas.CELL_HEIGHT` ({Canvas.CELL_HEIGHT}"
            )

        self.__width = width
        self.__height = height
        self.__width_in_symbols = width // Canvas.CELL_WIDTH
        self.__height_in_symbols = height // Canvas.CELL_HEIGHT
        self.__canvas = [
            [0] * self.__width_in_symbols
            for _ in range(self.__height_in_symbols)
        ]

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def width_in_symbols(self):
        return self.__width_in_symbols

    @property
    def height_in_symbols(self):
        return self.__height_in_symbols

    def __draw(self, x, y, is_paint):
        if not 0 <= x <= self.__width:
            raise RockartException(
                "`x` must belong to a range [0; `width`] ([0; {self.__width}])"
            )

        if not 0 <= y <= self.__height:
            raise RockartException(
                "`y` must belong to a range [0; `height`] ([0; {self.__height}])"
            )

        local_x = x % Canvas.CELL_WIDTH
        local_y = y % Canvas.CELL_HEIGHT
        basis_symbol = Canvas.__BASIS[local_x, local_y]

        row = y // Canvas.CELL_HEIGHT
        column = x // Canvas.CELL_WIDTH
        if is_paint:
            self.__canvas[row][column] |= basis_symbol
        else:

            self.__canvas[row][column] &= \
                2 ** (Canvas.CELL_WIDTH * Canvas.CELL_HEIGHT) - 1 \
                - basis_symbol

    def paint(self, x, y):
        try:
            self.__draw(x, y, is_paint=True)
        except RockartException:
            raise

    def erase(self, x, y):
        try:
            self.__draw(x, y, is_paint=False)
        except RockartException:
            raise

    def render(self):
        rendered_rows = []
        for row in self.__canvas:
            symbols = []
            for symbol_index in row:
                symbol = Canvas.__SYMBOLS[symbol_index]
                symbols.append(symbol)
            rendered_row = "".join(symbols)
            rendered_rows.append(rendered_row)
        rendered_canvas = "\n".join(rendered_rows)
        return rendered_canvas
