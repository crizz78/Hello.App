# Hello.App - Avance Funcional (Fase de Construcción)

def mostrar_saludo(nombre):
    return f"¡Hola, {nombre}! Bienvenido a Hello.App."

if __name__ == "__main__":
    usuario = input("Ingresa tu nombre: ")
    print(mostrar_saludo(usuario))
