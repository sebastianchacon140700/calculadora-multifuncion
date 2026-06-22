from datetime import datetime

RUTA_HISTORIAL_UNA = (
    "historiales/historial_una_variable.txt"
)

RUTA_HISTORIAL_DOS = (
    "historiales/historial_dos_variables.txt"
)


def guardar_historial_una(
    origen,
    destino,
    valor,
    resultado
):
    fecha_hora = datetime.now().strftime(
        "%d/%m/%Y %H:%M"
    )

    linea = (
        f"[{fecha_hora}] "
        f"{valor} {origen} -> "
        f"{resultado} {destino}\n"
    )

    with open(
        RUTA_HISTORIAL_UNA,
        "a",
        encoding="utf-8"
    ) as archivo:
        archivo.write(linea)


def guardar_historial_dos(
    operacion,
    dato1,
    dato2,
    resultado
):
    fecha_hora = datetime.now().strftime(
        "%d/%m/%Y %H:%M"
    )

    linea = (
        f"[{fecha_hora}] "
        f"{operacion} | "
        f"Dato1={dato1} | "
        f"Dato2={dato2} | "
        f"Resultado={resultado}\n"
    )

    with open(
        RUTA_HISTORIAL_DOS,
        "a",
        encoding="utf-8"
    ) as archivo:
        archivo.write(linea)


def leer_historial_una():

    try:
        with open(
            RUTA_HISTORIAL_UNA,
            "r",
            encoding="utf-8"
        ) as archivo:
            return archivo.read()

    except FileNotFoundError:
        return "No existe historial."


def leer_historial_dos():

    try:
        with open(
            RUTA_HISTORIAL_DOS,
            "r",
            encoding="utf-8"
        ) as archivo:
            return archivo.read()

    except FileNotFoundError:
        return "No existe historial."


def limpiar_historial_una():

    with open(
        RUTA_HISTORIAL_UNA,
        "w",
        encoding="utf-8"
    ):
        pass


def limpiar_historial_dos():

    with open(
        RUTA_HISTORIAL_DOS,
        "w",
        encoding="utf-8"
    ):
        pass