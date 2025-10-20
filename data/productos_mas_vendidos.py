import pandas as pd

# Convert each Google Sheets link to exportable CSV
def sheet_to_csv(url):
    base = url.split('/edit')[0]
    return base + '/export?format=csv'

urls = {
    "clientes": "https://docs.google.com/spreadsheets/d/1TeC8gGXilq1Vog4GoB2DZMsHbKztvqIf/edit?gid=1794629255#gid=1794629255",
    "detalle_ventas": "https://docs.google.com/spreadsheets/d/1FYKz8jLFiGJWZJO-volGvuSzhsUFlR7V/edit?gid=2063018695#gid=2063018695",
    "productos": "https://docs.google.com/spreadsheets/d/1BFFvqeF_guWTQ9bvSq6bdnQ-uw0hLcQD/edit?gid=1620284365#gid=1620284365",
    "ventas": "https://docs.google.com/spreadsheets/d/1dK9hqzFx7_b5sombXKt_mjL_SeGb7Fsx/edit?gid=1273816796#gid=1273816796"
}

# Load data
clientes = pd.read_csv(sheet_to_csv(urls["clientes"]))
detalle_ventas = pd.read_csv(sheet_to_csv(urls["detalle_ventas"]))
productos = pd.read_csv(sheet_to_csv(urls["productos"]))
ventas = pd.read_csv(sheet_to_csv(urls["ventas"]))

# Merge datasets
df = (detalle_ventas
      .merge(productos, on="id_producto", suffixes=('', '_prod'))
      .merge(ventas, on="id_venta", suffixes=('', '_venta'))
      .merge(clientes, on="id_cliente", suffixes=('', '_cliente'))
     )

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Function to compute top-selling products
def top_productos(n=10):
    resumen = (df.groupby('nombre_producto')['cantidad']
               .sum()
               .sort_values(ascending=False)
               .head(n))
    print("\n--- Top productos más vendidos ---")
    print(resumen)

# Function to compute top-buying clientsgit 
def top_clientes(n=10):
    resumen = (df.groupby('nombre_cliente')['importe']
               .sum()
               .sort_values(ascending=False)
               .head(n))
    print("\n--- Top clientes con mayor compra ---")
    print(resumen)

# Interactive console menu
def menu_interactivo():
    while True:
        print("n\Seleccione una opción:")
        print("1. Ver top productos más vendidos")
        print("2. Ver top clientes con mayor compra")
        print("3. Salir")

        opcion = input("Ingrese su elección (1-3): ").strip()

        if opcion == '1':
            top_productos()
        elif opcion == '2':
            top_clientes()
        elif opcion == '3':
            print("Saliendo del menú.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el menú
menu_interactivo()




