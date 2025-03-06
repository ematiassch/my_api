from flask import Flask
app = Flask(__name__)

def execute_script():
    # Aquí irá el código de tu script de Python
    import datetime
import os

def main():
    # Obtener la fecha y hora actual
    now = datetime.datetime.now()
    
    # Realizar una operación simple
    result = sum(range(1, 101))  # Suma de números del 1 al 100
    
    # Crear un mensaje con los resultados
    message = f"""
    Script ejecutado el: {now}
    Resultado de la suma: {result}
    """
    
    # Definir la ruta del archivo de salida
    # Usamos una ruta raw string para evitar problemas con las barras invertidas
    output_path = r"C:\Users\FROM\OneDrive - PETROBRAS\Proyecto Automatización SAC\Prueba Automate\output.txt"
    
    # Asegurarse de que el directorio existe
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Escribir los resultados en un archivo
    with open(output_path, "a") as file:
        file.write(message)
    
    print("Script ejecutado con éxito. Resultados guardados en:", output_path)

if __name__ == "__main__":
    main()
    return 'Script ejecutado con éxito'

@app.route('/execute_script', methods=['POST'])
def execute_script_route():
    return execute_script()

if __name__ == '__main__':
    app.run(port=5000)

