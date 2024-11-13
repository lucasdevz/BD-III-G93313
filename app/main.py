from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session
import os

session = Session()
repository = UsuarioRepository(session)
service = UsuarioService(repository)

#Solicitando dados para o usuário.
print("\nCadastrando usuário: ")
nome = input("digite seu nome: ")
email = input("digite seu email: ")
senha = input("digite sua senha: ")

service.criar_usuario(nome, email, senha)

#Exibindo todos os registros na tabela "usuarios" do banco de dados.
print("\n=== Listando usuários cadastrados ===")
lista_usuarios = service.listar_todos_usuarios()
for usuario in lista_usuarios:
    print(f"Nome: {usuario.nome} \nE-mail: {usuario.email}")
