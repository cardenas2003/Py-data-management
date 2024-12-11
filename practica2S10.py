import pandas as pd
import numpy as np

# 1. Crear el conjunto de datos
data = {
    'Nombre': ['Juan', 'Maria', 'Pedro', 'Ana', 'Luisa', 'Carlos', 'Juan'],
    'Edad': [25, 30, np.nan, 29, 28, 200, 25],
    'Email': ['juan@mail.com', 'maria@mail.com', 'pedro@mail.com', 'ana@mail.com', 'luisa@mail.com', 'carlos@mail.com', 'juan@mail.com'],
    'Pais': ['colombia', 'Colombia', 'Mexico', 'Argentina', 'colombia', 'Brazil', 'colombia'],
    'Genero': ['M', 'F', 'H', 'F', 'Femenino', 'M', 'M'],
    'Visitas': [5, 7, 6, 4, 8, 2, 5]
}

# Crear el DataFrame
df = pd.DataFrame(data)

# 2. Limpiar los datos

# a. Rellenar valores faltantes:
# - Para 'Edad', rellenamos con la media de las edades disponibles
df['Edad'].fillna(df['Edad'].mean(), inplace=True)

# - Para 'Email', reemplazamos los valores faltantes con 'desconocido@mail.com'
df['Email'].fillna('desconocido@mail.com', inplace=True)

# b. Eliminar duplicados:
# Eliminar registros duplicados basados en todas las columnas
df.drop_duplicates(inplace=True)

# c. Estandarizar los valores:
# - Estandarizamos la columna 'Genero'
df['Genero'] = df['Genero'].replace({
    'M': 'Masculino', 
    'Masculino': 'Masculino', 
    'F': 'Femenino', 
    'Femenino': 'Femenino',
    'H': 'Masculino'  # Asumimos que 'H' es un error y lo cambiamos a 'Masculino'
})

# - Estandarizamos la columna 'Pais' para que todas las letras inicien en mayúscula
df['Pais'] = df['Pais'].str.title()

# d. Corregir valores inválidos:
# - En la columna 'Edad', reemplazamos edades mayores a 100 años por NaN (o podemos eliminar esos registros)
df['Edad'] = df['Edad'].apply(lambda x: np.nan if x > 100 else x)

# - Luego, rellenamos esos valores faltantes de nuevo con la media de las edades
df['Edad'].fillna(df['Edad'].mean(), inplace=True)

# 3. Mostrar el DataFrame limpio
print(df)
