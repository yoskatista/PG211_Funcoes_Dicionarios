def itens(*sanduiche):

    print("Seu Sanduiche é de ")
    print(sanduiche)


print(itens("pao","hamburguer","salada"))
print(itens("pao","manteiga"))
print(itens("pao","salsicha","purê"))

"""def dic(first, last, **user):
    perfil = {}
    perfil["first_name"] = first
    perfil["last_name"] = last
    for key, value in user.items():
        perfil[key] = value
    return perfil

print(dic('cu','cuu'))"""""

def builf_profile(nome, sobrenome, **usuario):
    lista = {}
    lista["Seu nome:"] = nome
    lista["Seu sobrenome"] = sobrenome
    for key, value in usuario.items():
        print(key + value)
    return lista

print(builf_profile("Miquel","Casemiro"))
print(builf_profile("Michael","Cassiano"))
print(builf_profile("Mikael","Cassino"))


def carros(fabricante, modelo, cor, **adicional):
    car = {}
    car["Seu fabricante é"] = fabricante
    car["Seu modelo é"] = modelo
    car["Sua cor é"] = cor
    for value, key in adicional:
        print(value, key)
    return car

print(carros("Volkswagen ","Gol", "Branco"))