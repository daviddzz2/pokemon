import requests
def obtener_datos(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"
    response = requests.get(url)
    if response.status_code == 200:
        datos = response.json()
        return datos
    else:
        return None

def pintar_datos(datos):
    if datos:
        print("Datos obtenidos:")
        print(f"Nombre: {datos.get('name', 'Desconocido').capitalize()}")
        print(f"Altura: {datos.get('height', 'Desconocida')} decímetros")
        print(f"Peso: {datos.get('weight', 'Desconocido')} hectogramos")
        print("Habilidades:")
        habilidades = datos.get('abilities', [])
        for habilidad in habilidades:
            print(f"  - {habilidad['ability']['name'].capitalize()}")
        print("Tipos:")
        tipos = datos.get('types', [])
        for tipo in tipos:
            print(f"  - {tipo['type']['name'].capitalize()}")
    else:
        print("No se encontraron datos.")

pikachu = obtener_datos("pikachu")
pintar_datos(pikachu)
