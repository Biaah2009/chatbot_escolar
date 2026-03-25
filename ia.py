from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


frases = [
    "oi", "olá", "bom dia", "boa tarde",
    "quais produtos vocês têm", "o que vocês vendem", "tem camiseta", "tem tênis",
    "qual o preço", "quanto custa", "preço",
    "horário", "que horas abre", "que horas fecha",
    "tchau", "até mais"
]

intencoes = [
    "saudacao", "saudacao", "saudacao", "saudacao",
    "produtos", "produtos", "produtos", "produtos",
    "preco", "preco", "preco",
    "horario", "horario", "horario",
    "despedida", "despedida"
]

#modelo de treinamento
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(frases)
modelo = MultinomialNB()
modelo.fit(x, intencoes)

#função de resposta
def responder(intencao):
    if intencao == "saudacao":
        return "Olá! Bem-vindo à nossa loja "
    elif intencao == "produtos":
        return "Temos camisetas, tênis e acessórios!"
    elif intencao == "preco":
        return "Camisetas a partir de R$50 e tênis a partir de R$120."
    elif intencao == "horario":
        return "Funcionamos das 08h às 18h."
    elif intencao == "despedida":
        return "Obrigado pela visita!"
    else:
        return "Desculpe, não entendi."

#função do chatbot
def chatbot(mensagem):
    mensagem_vetorizada = vectorizer.transform([mensagem])
    intencao = modelo.predict(mensagem_vetorizada)[0]
    return responder(intencao)