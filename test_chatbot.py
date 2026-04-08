def chatbot(mensagem):
    mensagem = mensagem.lower().strip()

    # regra simples para detectar desconhecido
    if mensagem not in [
        "oi", "olá", "bom dia", "boa tarde",
        "como faço a matrícula", "quero me matricular", "matrícula", "matricula", "documentos matrícula",
        "como ver minhas notas", "consultar notas", "boletim", "notas",
        "qual o horário das aulas", "horário", "horario", "que horas são as aulas", "turnos",
        "como entro em contato", "telefone da escola", "secretaria", "contato"
    ]:
        return responder("desconhecido")

    x_input = vectorizer.transform([mensagem])
    intencao = modelo.predict(x_input)[0]

    return responder(intencao)