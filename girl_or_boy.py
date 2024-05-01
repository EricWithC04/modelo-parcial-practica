def girl_or_boy(nombre_usuario):
    chars = []

    for i in nombre_usuario:
        if i not in chars:
            chars.append(i)

    if len(chars) % 2 == 0:
        return "¡ITS A GIRL!"
    else:
        return "¡ITS A BOY!"

print(girl_or_boy("EricWithC04"))
print(girl_or_boy("ericwithc04"))
print(girl_or_boy("rodriasd"))
print(girl_or_boy("wiclock"))