from Pyro5.api import Daemon, locate_ns
from calculator import CalculatorService

SERVICE_NAME = "CalculatorService"

def main():
    calc = CalculatorService()

    with Daemon() as daemon:
        uri = daemon.register(calc)
        print("Objeto remoto URI:", uri)

        ns = locate_ns()
        ns.register(SERVICE_NAME, uri)
        print(f"Registrado en Name Server como '{SERVICE_NAME}'")

        print("Servidor listo. Esperando invocaciones...")
        daemon.requestLoop()

if __name__ == "__main__":
    main()
