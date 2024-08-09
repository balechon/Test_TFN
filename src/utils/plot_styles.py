"""this scrips has the style and common visualization with the  Telefonica Brand Style
"""
from typing import Union
import seaborn as sns
import plotly.graph_objects as go
import plotly.io as pio


class telefonica_style():
    """_summary_

    Returns:
        _type_: _description_
    """

    def __init__(self):
        # colores principal
        self.color_blue = '#0066FF'
        self.color_white = '#F2F4FF'
        self.color_red = '#E66C64'
        # escala de grises
        self.color_grey_0 = '#FFFFFF'
        self.color_grey_1 = '#F2F4FF'
        self.color_grey_2 = '#D1D5E4'
        self.color_grey_3 = '#B0B6CA'
        self.color_grey_4 = '#8F97AF'
        self.color_grey_5 = '#6E7894'
        self.color_grey_6 = '#58617A'
        self.color_grey_7 = '#414B61'
        self.color_grey_8 = '#2B3447'
        self.color_grey_9 = '#031A34'

        # colores secundarios
        self.color_brown_light = '#E6E4E5'
        self.color_brown = '#807477'
        self.color_brown_dark = '#524C4E'

        self.color_green_light = '#E6E9E6'
        self.color_green = '#7C877C'
        self.color_green_dark = '#535753'

        self.color_grey_light = self.color_white
        self.color_grey = '#6E7894'
        self.color_grey_dark = '#414B61'

        self.color_purple_light = '#ECE7EE'
        self.color_purple = '#9D84A3'
        self.color_purple_dark = '#64566A'
        # colores de realce
        self.color_coral_light = '#E3A19A'
        self.color_coral = '#E66C64'
        self.color_coral_dark = '#912C31'

        self.color_turquoise_light = '#67E0E5'
        self.color_turquoise = '#59C2C9'
        self.color_turquoise_dark = '#3E8A8A'

        self.color_ambar_light = '#F5E98A'
        self.color_ambar = '#EAC344'
        self.color_ambar_dark = '#AD842D'

        self.color_orchid_light = '#E7C2F8'
        self.color_orchid = '#C466EF'
        self.color_orchid_dark = '#8A1A93'

        # paletas de colores
        self.principal_colors = [self.color_grey_3, self.color_blue]
        self.principal_colors_r = self.principal_colors[::-1]

        self.gray_colors = [self.color_grey_2, self.color_grey_3, self.color_grey_4, self.color_grey_5,
                            self.color_grey_6, self.color_grey_7, self.color_grey_8, self.color_grey_8]

        self.realce_colors = [
            self.color_coral, self.color_turquoise, self.color_ambar, self.color_orchid]

        self.realce_colors_lighth = [
            self.color_coral_light, self.color_turquoise_light, self.color_ambar_light, self.color_orchid_light]

        self.realce_colors_dark = [
            self.color_coral_dark, self.color_turquoise_dark, self.color_ambar_dark, self.color_orchid_dark]

        self.secondary_colors = [
            self.color_brown, self.color_green, self.color_grey, self.color_purple]

        self.secondary_colors_light = [
            self.color_brown_light, self.color_green_light, self.color_grey_light, self.color_purple_light]

        self.secondary_colors_dark = [
            self.color_brown_dark, self.color_green_dark, self.color_grey_dark, self.color_purple_dark]
            

    def create_color_secuence(self, name, n_steps):
        colors_avaliable_dict = {
            'blue': ['#CCE0FF', '#00337F'],
            'brown': [self.color_brown_light, self.color_brown_dark],
            'green': [self.color_green_light, self.color_green_dark],
            'grey': [self.color_grey_light, self.color_grey_dark],
            'purple': [self.color_purple_light, self.color_purple_dark],
            'coral': [self.color_coral_light, self.color_coral_dark],
            'turquoise': [self.color_turquoise_light, self.color_turquoise_dark],
            'ambar': [self.color_ambar_light, self.color_ambar_dark],
            'orchid': [self.color_orchid_light, self.color_orchid_dark],
            'pink': ['#FBC7DE', '#E63780'],

        }
        if name not in list(colors_avaliable_dict.keys()):
            raise ValueError(f'Name must be :{colors_avaliable_dict.keys()}')

        colores = colors_avaliable_dict[name]
        return generate_color_scale(colores[0], colores[1], n_steps)

    # crear una funcion que ponga una lista de labels y los asigne a los colores
    def create_realce_labeled_color(self, labels_list: list, realce: Union[str, list[str]]) -> dict:
        """This function could make a palete with a common base color 
           and a realce color set by the user

        Args:
            labesl_list (list): _description_
            realce (Union[str, list[str]]): _description_

        Returns:
            dict: dictionary with the key as the name of label and the color based in the condition as value
        """
        palette_realce = {}
        colors_base = {x: self.principal_colors[0] for x in labels_list}
        if isinstance(realce, str):
            palette_realce = {
                key: self.principal_colors[1] if key == realce else value for key, value in colors_base.items()}
        elif isinstance(realce, list):
            palette_realce = {
                key: self.principal_colors[1] if key in realce else value for key, value in colors_base.items()}
        else:
            print('Error en la variable de realce')
        return palette_realce

    def create_labeled_color(self, labels_list: list, palette_in=['#E66C64', '#59C2C9', '#EAC344', '#C466EF']) -> dict:
        """_summary_

        Args:
            labels (list): _description_
            palette_in (list, optional): _description_. Defaults to ['#E66C64', '#59C2C9', '#EAC344', '#C466EF'].

        Returns:
            dict: _description_
        """

        if len(palette_in) < len(labels_list):
            raise ('La logitud de los colores no es igual a la los ')
        else:
            palette_in = palette_in[0:len(labels_list)]
            return {labels_list[i]: palette_in[i] for i in range(len(labels_list))}


class PaletaSeaborn(telefonica_style):

    def __init__(self):
        super().__init__()
        sns.set_style(rc={  # estilo principal de todos los graficos, lineas, tamaño de letras, xticks, etc.
            'figure.facecolor': '#FFFFFF',
            'axes.facecolor': '#FFFFFF',
            'axes.labelcolor': '#414B61',
            'ytick.color': '#414B61', 'xtick.color': '#414B61', 'text.color': '#2B3447',
            'axes.grid': False,
            'grid.color': self.color_white,
            'axes.edgecolor': '#D1D5E4',
            'legend.frameon': False,
        }
        )
        self.principal_palette = sns.color_palette(self.principal_colors)
        self.principal_palette_r = sns.color_palette(
            self.principal_colors[::-1])
        self.gray_palette = sns.color_palette(self.gray_colors)
        self.gray_palette_r = sns.color_palette(self.gray_colors[::-1])
        self.realce_palette = sns.color_palette(self.realce_colors)
        self.realce_palette_r = sns.color_palette(self.realce_colors[::-1])
        self.secondary_palette = sns.color_palette(self.secondary_colors)
        self.secondary_palette_r = sns.color_palette(
            self.secondary_colors[::-1])
        # # paleta degradada
        self.telefonica_cmap = sns.color_palette(
            "blend:#F2F4FF,#031A34", as_cmap=True)
        self.telefonica_cmap_r = sns.color_palette(
            "blend:#031A34,#F2F4FF", as_cmap=True)
        self.telefonica_cmap_bw = sns.color_palette(
            "blend:#2B3447,#F2F4FF,#0066FF", as_cmap=True)


class PaletaPlotly(telefonica_style):
    def __init__(self):
        super().__init__()

        fig = read_plotly_conf()
        template_figures = pio.to_templated(fig)
        pio.templates['template_figures'] = template_figures.layout.template
        pio.templates.default = 'template_figures'


def hex_to_rgb(hex_color):
    # Convertir el valor hexadecimal a RGB
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb_color):
    # Convertir el valor RGB a hexadecimal
    return '#%02x%02x%02x' % rgb_color


def generate_color_scale(start_color, end_color, steps):
    scale = []

    # Convertir los colores hexadecimales a RGB
    start_rgb = hex_to_rgb(start_color)
    end_rgb = hex_to_rgb(end_color)

    # Calcular la diferencia entre los componentes RGB de inicio y final
    red_step = (end_rgb[0] - start_rgb[0]) / (steps - 1)
    green_step = (end_rgb[1] - start_rgb[1]) / (steps - 1)
    blue_step = (end_rgb[2] - start_rgb[2]) / (steps - 1)

    # Generar la escala de colores
    for i in range(steps):
        red = start_rgb[0] + (red_step * i)
        green = start_rgb[1] + (green_step * i)
        blue = start_rgb[2] + (blue_step * i)

        color = (int(red), int(green), int(blue))
        hex_color = rgb_to_hex(color)
        scale.append(hex_color)

    return scale


def read_plotly_conf():
    fig = go.Figure(layout={
        'annotationdefaults': {'arrowcolor': '#E66C64', 'arrowhead': 0, 'arrowwidth': 1},
        'autotypenumbers': 'strict',
        'font': {'color': '#414B61','family': 'Arial Medium'},
        'geo': {'bgcolor': 'white',
                'lakecolor': 'white',
                'landcolor': 'white',
                'showlakes': True,
                'showland': True,
                'subunitcolor': '#C8D4E3'},
        'hoverlabel': {'align': 'left'},
        'hovermode': 'closest',
        'mapbox': {'style': 'light'},
        'paper_bgcolor': 'white',
        'plot_bgcolor': 'white',
        'polar': {'angularaxis': {'gridcolor': '#EBF0F8', 'linecolor': '#EBF0F8', 'ticks': ''},
                  'bgcolor': 'white',
                  'radialaxis': {'gridcolor': '#EBF0F8', 'linecolor': '#EBF0F8', 'ticks': ''}},
        'scene': {'xaxis': {'backgroundcolor': 'white',
                            'gridcolor': '#DFE8F3',
                            'gridwidth': 2,
                            'linecolor': '#EBF0F8',
                            'showbackground': True,
                            'ticks': '',
                            'zerolinecolor': '#EBF0F8'},
                  'yaxis': {'backgroundcolor': 'white',
                            'gridcolor': '#DFE8F3',
                            'gridwidth': 2,
                            'linecolor': '#EBF0F8',
                            'showbackground': True,
                            'ticks': '',
                            'zerolinecolor': '#EBF0F8'},
                  'zaxis': {'backgroundcolor': 'white',
                            'gridcolor': '#DFE8F3',
                            'gridwidth': 2,
                            'linecolor': '#EBF0F8',
                            'showbackground': True,
                            'ticks': '',
                            'zerolinecolor': '#EBF0F8'}},
        'shapedefaults': {'line': {'color': '#2a3f5f'}},
        'ternary': {'aaxis': {'gridcolor': '#DFE8F3', 'linecolor': '#A2B1C6', 'ticks': ''},
                    'baxis': {'gridcolor': '#DFE8F3', 'linecolor': '#A2B1C6', 'ticks': ''},
                    'bgcolor': 'white',
                    'caxis': {'gridcolor': '#DFE8F3', 'linecolor': '#A2B1C6', 'ticks': ''}},
        'title': {'x': 0.01,'font_size':12},
        'xaxis': {'automargin': True,
                  'ticks': '',
                  'showgrid': False,
                  'gridcolor': '#F2F4FF',
                  'gridwidth': 1,
                  'showline': True,
                  'linecolor': '#D1D5E4',
                  'linewidth': 1,
                  'title': {'standoff': 15},
                  'zerolinecolor': '#EBF0F8',
                  'zerolinewidth': 2,
                  'color': '#58617A', 'tickfont_family': 'Arial','tickfont_size': 11
                  },
        'yaxis': {'automargin': True,
                  'ticks': '',
                  'ticksuffix': "  ",
                  'showgrid': False,
                  'gridcolor': '#F2F4FF',
                  'gridwidth': 1,
                  'showline': True,
                  'linecolor': '#D1D5E4',
                  'linewidth': 1.5,
                  'title': {'standoff': 26},
                  'zerolinecolor': '#EBF0F8',
                  'zerolinewidth': 2,
                  'color': '#58617A', 'tickfont_family': 'Arial', 'tickfont_size': 13
                  },
        'width':800,
        'height':600
    })

    return fig
