import functools

def duplicar(func):
    @functools.wraps(func)
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return envelope

@duplicar # Decoradores com parametros
def aprender(tecnologia):
    print(f"Estou aprendendo {tecnologia}")
    return tecnologia.upper()

aprender('Python')
print(aprender('Python'))

# Introspecção 
# Importar functools
print(aprender.__name__) 