import os
import re

ruta = r"C:\DSAM_Files\Seriales\Seriales2daParte"

for archivo in os.listdir(ruta):
    if archivo.endswith(".xml"):
        ruta_completa = os.path.join(ruta, archivo)

        try:
            with open(ruta_completa, "r", encoding="utf-8", errors="ignore") as f:
                lineas = f.readlines()

            encontrado = False

            for i in range(len(lineas)):
                if "FaultStatus" in lineas[i]:
                    # Buscar en la siguiente línea
                    if i + 1 < len(lineas):
                        siguiente = lineas[i + 1]

                        match = re.search(r"<cell>(.*?)</cell>", siguiente)

                        if match:
                            valor = match.group(1).strip()
                            print(f"{archivo} | {valor}")
                        else:
                            print(f"{archivo} | FaultStatus encontrado pero sin <cell> válido")

                    encontrado = True
                    break

            if not encontrado:
                print(f"{archivo} | FaultStatus NO encontrado")

        except Exception as e:
            print(f"{archivo} | ERROR: {e}")