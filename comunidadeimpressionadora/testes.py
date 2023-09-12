from comunidadeimpressionadora import app, database
from comunidadeimpressionadora.models import Post
#with app.app_context():
#    database.create_all()

#with app.app_context():
#    usuario = Usuario(username='Lucas', email='teste@gmail.com',senha='123456')

#    usuario2 = Usuario(username='Lucas2', email='teste2@gmail.com',senha='123456')

#    database.session.add(usuario)
#    database.session.add(usuario2)
#    database.session.commit()

#with app.app_context():
#    meus_usuarios = Usuario.query.all()
#    print(meus_usuarios)

#    primeiro_usuario = Usuario.query.first()
#    print(primeiro_usuario.email)

#    usuario_teste = Usuario.query.filter_by(id=2).first()
#    print(usuario_teste.email)

#with app.app_context():

#    meu_post = Post(id_usuario=1,titulo='primeiro post',corpo='Teste de post')
#    database.session.add(meu_post)
#    database.session.commit()

# with app.app_context():
#     post = Post.query.first()
#     print(post.corpo)
#     print(post.autor.email)

with app.app_context():
    post = Post.query.first()
    print(post.corpo)