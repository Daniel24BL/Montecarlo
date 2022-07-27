import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Realizamos la respectiva conversión de los datos al dataframe.
datos = { '1': [0.13, 0.90], '2': [0.95, 0.41], '3': [0.62, 0.86], '4': [0.71, 0.18], '5': [0.54, 0.80], '6': [0.83, 0.70], 
         '7': [0.54, 0.09], '8': [0.63, 0.30], '9': [0.95, 0.98], '10': [0.24, 0.23], '11': [0.02, 0.85], '12': [0.57, 0.23],
         '13': [0.37, 0.89], '14': [0.02, 0.65], '15': [0.56, 0.99]}
datostabla = pd.DataFrame(datos)
# Mostramos los datos a través del dataframe creado.
print ('Nota: La fila 1 hace referencia al trabajo con un (1) hombre')
print ('Mientras que la fila 2 hace referencia al trabajo realizado con dos (2) hombres')
datostabla

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Realizamos la respectiva tabla a través de un dataframe.
datosfila1 = { 'Num_Tiempo': [1.25, 1.50, 1.75, 2.00], 'Probabilidad': [0.15, 0.25, 0.40, 0.20], 
              'Mínimo': [0, 0.15, 0.40, 0.80], 'Máximo': [0.15, 0.40, 0.80, 1]}
datosfila1_tabla = pd.DataFrame(datosfila1)
# Mostramos la tabla del número de tiempo, probabilidades, y el rango (mínimo - máximo).
datosfila1_tabla

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Realizamos la respectiva tabla a través de un dataframe.
datosfila1_sim = {'Num_Aleatorio': [0.13, 0.95, 0.62, 0.71, 0.54, 0.83, 0.54, 0.63, 0.95, 0.24, 0.02, 0.57,
                                   0.37, 0.02, 0.56],
                 'Num_Simulado': [1.25, 2.00, 1.75, 1.75, 1.75, 2.00, 1.75, 1.75, 2.00, 1.50, 1.25, 1.75,
                                 1.50, 1.25, 1.75]}
datosfila1_sim_tabla = pd.DataFrame(datosfila1_sim)
datosfila1_sim_tabla

suma = datosfila1_sim_tabla['Num_Simulado'].sum()
print('La suma total de los números simulados, para el trabajo con un hombre es de: ', suma)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Realizamos la respectiva tabla a través de un dataframe.
datosfila2 = { 'Num_Tiempo': [0.50, 0.75, 1.00, 1.25], 'Probabilidad': [0.25, 0.35, 0.30, 0.10], 
              'Mínimo': [0, 0.25, 0.60, 0.90], 'Máximo': [0.25, 0.60, 0.90, 1]}
datosfila2_tabla = pd.DataFrame(datosfila2)
# Mostramos la tabla del número de tiempo, probabilidades, y el rango (mínimo - máximo).
datosfila2_tabla

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Realizamos la respectiva tabla a través de un dataframe.
datosfila2_sim = {'Num_Aleatorio': [0.90, 0.41, 0.86, 0.18, 0.80, 0.70, 0.09, 0.30, 0.98, 0.23, 0.85, 0.23,
                                   0.89, 0.65, 0.99],
                 'Num_Simulado': [1.25, 0.75, 1.00, 0.50, 1.00, 1.00, 0.50, 0.75, 1.25, 0.50, 1.00, 0.50,
                                 1.00, 1.00, 1.25]}
datosfila2_sim_tabla = pd.DataFrame(datosfila2_sim)
datosfila2_sim_tabla

suma1 = datosfila2_sim_tabla['Num_Simulado'].sum()
print('La suma total de los números simulados, para el trabajo con un hombre es de: ', suma1)
