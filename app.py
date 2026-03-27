from flask import Flask, render_template, request
from ia import chatbot

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resposta = ""
    mensagem_usuario = ""

    if request.method == 'POST':
        mensagem_usuario = request.form.get("mensagem", "").strip()

        if mensagem_usuario:
            resposta = chatbot(mensagem_usuario)
        else:
            resposta = "Por favor, digite uma pergunta."

    return render_template(
        'index.html',
        resposta=resposta,
        mensagem_usuario=mensagem_usuario
    )

if __name__ == "__main__":
    app.run(debug=True)