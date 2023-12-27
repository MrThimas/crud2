from database import db, Usuario, Anuncio

db.connect()


db.create_tables([Usuario, Anuncio])

Usuario.create(nome = 'Roberto', email = 'teste@gmail.com', senha= '123456')
Usuario.create(nome = 'Bruno', email = 'teste02@gmail.com', senha = 'Philos')
Usuario.create(nome = 'Johnny', email = 'teste03@gmail.com', senha = 'SM12345')

lista_usuario = Usuario.select()
print('Listando usuarios:')

for u in lista_usuario:
    print('-', u.id, u.nome, u.email, u.senha)

roberto = Usuario.get(Usuario.nome == 'Roberto')
anuncio = Anuncio.create(
    usuario = roberto,
    titulo = "Video banco de dados",
    descricao = 'Fazer um video descritivo sobre banco de dados',
    valor = 500.0
)

print('Novo anuncio:', anuncio.id, anuncio.titulo)