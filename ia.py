from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

frases = [
    # saudação
    "oi", "olá", "bom dia", "boa tarde",

    # matrícula
    "como faço a matrícula", "quero me matricular", "matrícula", "documentos matrícula",

    # notas
    "como ver minhas notas", "consultar notas", "boletim", "notas",

    # horário
    "qual o horário das aulas", "horário", "que horas são as aulas", "turnos",

    # contato
    "como entro em contato", "telefone da escola", "secretaria", "contato",

    # desconhecido (não precisa treinar muito aqui)
    "teste"
]

intencoes = [
    "saudacao", "saudacao", "saudacao", "saudacao",

    "matricula", "matricula", "matricula", "matricula",

    "notas", "notas", "notas", "notas",

    "horario", "horario", "horario", "horario",

    "contato", "contato", "contato", "contato",

    "desconhecido"
]

# modelo de treinamento
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(frases)

modelo = MultinomialNB()
modelo.fit(x, intencoes)

# função de resposta
def responder(intencao):
    if intencao == "saudacao":
        return "Olá! Bem-vindo à escola. Como posso ajudar?"
    
    elif intencao == "matricula":
        return "As matrículas podem ser feitas na secretaria. É necessário RG, CPF e comprovante de residência."
    
    elif intencao == "notas":
        return "Você pode consultar suas notas pelo portal do aluno ou na secretaria."
    
    elif intencao == "horario":
        return "As aulas acontecem nos turnos manhã, tarde e noite, conforme a turma."
    
    elif intencao == "contato":
        return "Você pode entrar em contato pelo telefone ou diretamente na secretaria da escola."
    
    else:
        return "Desculpe, não entendi sua dúvida."

# função do chatbot
def chatbot(mensagem):
    mensagem_vetorizada = vectorizer.transform([mensagem])
    intencao = modelo.predict(mensagem_vetorizada)[0]
    return responder(intencao)