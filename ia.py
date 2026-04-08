from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

frases = [
    "oi", "olá", "bom dia", "boa tarde",

    "como faço a matrícula", "quero me matricular", "matrícula", "matricula", "documentos matrícula",

    "como ver minhas notas", "consultar notas", "boletim", "notas",

    "qual o horário das aulas", "horário", "horario", "que horas são as aulas", "turnos",

    "como entro em contato", "telefone da escola", "secretaria", "contato",

    "teste"
]

intencoes = [
    "saudacao", "saudacao", "saudacao", "saudacao",

    "matricula", "matricula", "matricula", "matricula", "matricula",

    "notas", "notas", "notas", "notas",

    "horario", "horario", "horario", "horario", "horario",

    "contato", "contato", "contato", "contato",

    "desconhecido"
]

vectorizer = CountVectorizer(lowercase=True)
x = vectorizer.fit_transform(frases)

modelo = MultinomialNB()
modelo.fit(x, intencoes)

def responder(intencao):
    respostas = {
        "saudacao": "Olá! Bem-vindo à escola. Como posso ajudar?",
        "matricula": "As matrículas podem ser feitas na secretaria. É necessário RG, CPF e comprovante de residência.",
        "notas": "Você pode consultar suas notas pelo portal do aluno ou na secretaria.",
        "horario": "As aulas acontecem nos turnos manhã, tarde e noite, conforme a turma.",
        "contato": "Você pode entrar em contato pelo telefone ou diretamente na secretaria da escola.",
        "desconhecido": "Desculpe, não entendi sua dúvida."
    }
    return respostas.get(intencao, respostas["desconhecido"])

def chatbot(mensagem):
    mensagem = mensagem.lower().strip()

    x_input = vectorizer.transform([mensagem])
    probs = modelo.predict_proba(x_input)[0]

    # evita respostas erradas com baixa confiança
    def chatbot(mensagem):
        mensagem = mensagem.lower().strip()

    x_input = vectorizer.transform([mensagem])
    intencao = modelo.predict(x_input)[0]

    return responder(intencao)

    intencao = modelo.predict(x_input)[0]
    return responder(intencao)