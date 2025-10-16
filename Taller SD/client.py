from Pyro5.api import Proxy

SERVICE_NAME = "CalculatorService"

# Mapa de alias -> nombre real del método remoto
ALIASES = {
    "add": "add", "sum": "add", "sumar": "add", "+": "add",
    "subtract": "subtract", "sub": "subtract", "restar": "subtract", "-": "subtract",
    "multiply": "multiply", "multi": "multiply", "multiplicar": "multiply", "*": "multiply",
    "multiplly": "multiply",  # <-- tu typo
    "divide": "divide", "dividir": "divide", "/": "divide"
}

def ask_number(prompt):
    # Permite 12,34 o 12.34
    s = input(prompt).strip().replace(",", ".")
    return float(s)

def main():
    with Proxy(f"PYRONAME:{SERVICE_NAME}") as remote:
        print("=== Calculadora Remota (RMI con Pyro5) ===")
        print("Operaciones: add/sumar/+, subtract/restar/-, multiply/multiplicar/*, divide/dividir/")
        print("Escribe 'exit' para salir.\n")

        while True:
            op_raw = input("Operación: ").strip().lower()
            if op_raw == "exit":
                print("Saliendo...")
                break

            op = ALIASES.get(op_raw)
            if not op:
                print("Operación no válida. Ejemplos: add, subtract, multiply, divide (o sus alias).\n")
                continue

            try:
                a = ask_number("Primer número: ")
                b = ask_number("Segundo número: ")
                method = getattr(remote, op)
                result = method(a, b)
                print(f"Resultado: {result}\n")
            except Exception as e:
                print("Error remoto:", e, "\n")

if __name__ == "__main__":
    main()
