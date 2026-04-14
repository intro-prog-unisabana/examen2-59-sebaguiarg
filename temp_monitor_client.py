# temp_monitor_client.py
# Programa cliente que lee temperaturas de un archivo
# e imprime la racha creciente mas larga.

import temp_monitor


def main():
    # TODO: Pedir el nombre del archivo al usuario usando input()
    filename = input("Ingrese el nombre del archivo:\n")
    # TODO: Abrir el archivo y leer el numero de lecturas n
    with open(filename, "r") as f:
        line = int(f.readline().strip())
    # TODO: Crear el monitor usando temp_monitor.init(n)
        monitor = {temp_monitor.init(line)}
    # TODO: Leer las n temperaturas y agregarlas con temp_monitor.add_reading()
        for line in f:
            temperature = float(line.strip())
            temp_monitor.add_reading(temperature)
    # TODO: Imprimir la racha creciente mas larga
    #       usando temp_monitor.longest_rising_streak()
        streak =temp_monitor.longest_rising_streak(line)
    print(streak)


if __name__ == "__main__":
    main()
