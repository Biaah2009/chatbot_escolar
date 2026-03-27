from ia import chatbot

def test_saudacao():
    resposta = chatbot("oi")
    assert resposta == "Olá! Bem-vindo à escola. Como posso ajudar?"

def test_matricula():
    resposta = chatbot("como faço a matrícula")
    assert resposta == "As matrículas podem ser feitas na secretaria. É necessário RG, CPF e comprovante de residência."

def test_notas():
    resposta = chatbot("como ver minhas notas")
    assert resposta == "Você pode consultar suas notas pelo portal do aluno ou na secretaria."

def test_horario():
    resposta = chatbot("qual o horário das aulas")
    assert resposta == "As aulas acontecem nos turnos manhã, tarde e noite, conforme a turma."

def test_contato():
    resposta = chatbot("como entro em contato")
    assert resposta == "Você pode entrar em contato pelo telefone ou diretamente na secretaria da escola."

def test_frase_desconhecida():
    resposta = chatbot("teste de erro")
    assert resposta == "Desculpe, não entendi sua dúvida."