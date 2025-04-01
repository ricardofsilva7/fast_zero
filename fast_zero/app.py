from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import Message, UserSchema, UserPublic

from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return "{'message': 'Olá mundo!'}"

@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    return user

@app.get('/exercio-html', response_class=HTMLResponse)
def exercicio_aula_02():
    return """
        <html>
            <head>
                <title> Olá Mundo!</title>
            </head>          
            <body>
                <h1>Olá Mundo!</h1>
            </body>
        </html>"""