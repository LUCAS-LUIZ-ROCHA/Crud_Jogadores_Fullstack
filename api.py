from fastapi import FastAPI
from routes.jogador import jogador_router
from fastapi.middleware.cors import CORSMiddleware

# Informando o cliente que irá consumir a API, neste caso React.js na porta 3000
cliente_app= [
    "http://localhost:3000"
]


# Iniciando a API de forma modularizada 
app= FastAPI()

app.include_router(jogador_router)


# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins= cliente_app,
    allow_credentials= True,
    allow_methods= ["*"],
    allow_headers= ["*"]
)


