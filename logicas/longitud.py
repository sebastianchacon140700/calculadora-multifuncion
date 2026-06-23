def convertir_longitud(valor, origen, destino):

    # convertir a centímetros
    if origen == "Centimetros":
        cm = valor

    elif origen == "Metros":
        cm = valor * 100

    elif origen == "Kilometros":
        cm = valor * 100000

    elif origen == "Pulgadas":
        cm = valor * 2.54

    elif origen == "Pies":
        cm = valor * 30.48

    elif origen == "Yardas":
        cm = valor * 91.44
    
    elif origen == "Millas":
        cm = valor * 160934

    else:
        raise ValueError("Unidad de origen no válida")

    # convertir desde centímetros
    if destino == "Centimetros":
        return cm
  
    elif destino == "Metros":
        return cm / 100
    
    elif destino == "Kilometros":
        return cm / 100000

    elif destino == "Pulgadas":
        return cm / 2.54

    elif destino == "Pies":
        return cm / 30.48

    elif destino == "Yardas":
        return cm / 91.44
    
    elif destino == "Millas":
        return cm / 160934

    else:
        raise ValueError("Unidad de destino no válida")