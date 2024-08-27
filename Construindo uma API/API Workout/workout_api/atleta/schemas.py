from pydantic import Field, PositiveFloat
from typing import Annotated
from workout_api.contrib.schemas import BaseSchema


class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', example='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', example='12345678901', max_length=11)]
    idade : Annotated[int, Field(description='Idade do atleta', example='23')]
    peso : Annotated[PositiveFloat, Field(description='Peso do atleta', example='78.5')]
    altura : Annotated[PositiveFloat, Field(description='Altura do atleta', example='1.79')]
    sexo: Annotated[str, Field(description='Sexo do atleta', example='M', max_length=1)]