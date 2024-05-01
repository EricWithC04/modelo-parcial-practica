def girl_or_boy(nombre_usuario):

    if type(nombre_usuario) != str:
        raise TypeError("El parametro recibido no es una cadena")
    
    if len(nombre_usuario) == 0:
        raise ValueError("El parametro recibido es una cadena vacia")
    
    if nombre_usuario != nombre_usuario.lower():
        raise ValueError("El parametro recibido debe ser una cadena que contenga solo minusculas")

    try:
        chars = []

        for i in nombre_usuario:
            if i not in chars:
                chars.append(i)

        if len(chars) % 2 == 0:
            return "¡ITS A GIRL!"
        else:
            return "¡ITS A BOY!"
    except Exception as e:
        return e

print(girl_or_boy("ericwithc04"))
print(girl_or_boy("rodriasd"))
print(girl_or_boy("wiclock"))