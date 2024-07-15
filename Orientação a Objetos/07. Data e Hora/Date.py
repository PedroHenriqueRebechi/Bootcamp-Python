# Módulo datetime
import datetime

print(datetime.date(2024, 4, 19))

print(datetime.date.today())

print(datetime.datetime(2024, 4, 19, 10, 30, 2))

print(datetime.time(10,20))

print("-" * 50)

# Criando data e hora 
d = datetime.datetime(2023, 7, 19, 13, 45)
print(d)

# Adicionando uma semana 
d = d + datetime.timedelta(weeks=1)
print(d)

print("-" * 50)

# Formatando data e hora
print(datetime.datetime.today().strftime("%d/%m/%Y %H:%M"))

data = "20/07/2023 15:39"
converter_data = datetime.datetime.strptime(data, "%d/%m/%Y %H:%M")
print(converter_data)


print("-" * 50)
# Trabalhando com fuso horario
# Módulo pytz
import pytz

timezone = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))
print(timezone)

timezone2 = datetime.datetime.now(pytz.timezone("Europe/Oslo"))
print(timezone2)
