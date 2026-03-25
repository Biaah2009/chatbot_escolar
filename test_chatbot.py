from ia import chatbot

def test_saudacao():
    resposta = chatbot("oi")
    assert resposta == "ola! Bem-vindo a nossa loja "

def test_produtos():
    resposta = chatbot("quais produtos voces tem")
    assert resposta == "Temos camisetas, tenis e acessorios!"

def test_preco():
    resposta = chatbot("qual o preço da camiseta")
    assert resposta == "Camisetas a partir de R$50 e tenis a partir de R$120."

def test_horario():
    resposta = chatbot("que horas abre")
    assert resposta == "Funcionamos das 08h as 18h."

def test_despedida():
    resposta = chatbot("tchau")
    assert resposta == "Obrigado pela visita!"

def test_frase_desconhecida():
    resposta = chatbot("teste de erro")
    assert resposta == "Desculpe, nao entendi."