from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
#Campos de preenchimento(Field) - para texto, senha e envio(botao)
from wtforms.validators import DataRequired, Length, Email,EqualTo, ValidationError
from comunidadeimpressionadora.models import Usuario
from flask_login import current_user
#validadores de informações:
#DataRequired: torna o campo obrigatório
#length: valida por tamanho (tamanho senha)
#Email: verificar se o email é valido
#equal_to: verificar se o campo é igual a outro(confirmação de senha)

class FormCriarConta(FlaskForm):
    username = StringField('Nome de usuário',validators=[DataRequired()])
    email = StringField('E-mail',validators=[DataRequired(),Email()])
    senha = PasswordField('senha',validators=[DataRequired(),Length(6,20)])
    confirmacao_senha = PasswordField('Confirmação da senha',validators=[DataRequired(),EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado, use outro email ou faça login para continuar')


class FormLogin(FlaskForm):
    email = StringField('E-mail',validators=[DataRequired(),Email()])
    senha = PasswordField('senha',validators=[DataRequired(),Length(6,20)])
    lembrar_dados = BooleanField('Lembrar dados de Acesso')
    botao_submit_login = SubmitField('Fazer Login')


class formEditarPerfil(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizer foto de perfil', validators=[FileAllowed(['jpg','png'])])
    curso_excel = BooleanField('Excel impressionador')
    curso_vba = BooleanField('VBA impressionador')
    curso_powerbi = BooleanField('Power BI impressionador')
    curso_python = BooleanField('Python impressionador')
    curso_ppt = BooleanField('Power Point impressionador')
    curso_sql = BooleanField('SQL impressionador')
    botao_submit_editarperfil = SubmitField('Confirmar Edição')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Já existe um usuário com esse email')


class FormCriarPost(FlaskForm):
    titulo = StringField ('Ttitulo do Posto',validators=[DataRequired(), Length(2,140)])
    corpo = TextAreaField ('Escreva seu post aqui', validators=[DataRequired()])
    botao_submit = SubmitField('Criar Post')