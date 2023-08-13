from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def resume():
    resume_template = """

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Daniel Dávila Resume</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                font-weight: bold;
                text-transform: uppercase;
                background: black;
                color: #fff;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
                overflow: hidden;
            }

            .card {
                background: rgba(255, 255, 255, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.3);
                border-radius: 10px;
                padding: 25px;
                width: 350px;
                max-height: 400px;
                box-shadow: 0 8px 32px 0 rgb(29, 28, 28);
                backdrop-filter: blur(10px);
                cursor: pointer;
                transform: scale(1);
                transition: transform 0.2s, box-shadow 0.2s;
                margin: 20px;
                text-align: center;
                overflow: auto;
            }

            .card:hover {
                transform: scale(1.05);
                box-shadow: 0 12px 36px 0 rgb(29, 28, 28);
            }

            .card-container {
                display: none;
            }

            .card-container.active {
                display: block;
            }
        </style>
        <script>
            let currentCard = 0;

            function nextCard() {
                const cards = document.querySelectorAll('.card-container');
                cards[currentCard].classList.remove('active');
                currentCard = (currentCard + 1) % cards.length;
                cards[currentCard].classList.add('active');
            }
        </script>
    </head>
    <body>

        <div class="card-container active" onclick="nextCard()">
            <div class="card">
                DANIEL DÁVILA
            </div>
        </div>
        <div class="card-container" onclick="nextCard()">
            <div class="card">
                Pensador crítico automotivado, letrado em filosofia e diletante em biologia, com excelentes habilidades de comunicação. Aprende rápido. Atualmente cursando Engenharia da Computação no Inteli.
            </div>
        </div>
        <div class="card-container" onclick="nextCard()">
            <div class="card">
                Possui como principais habilidades programação, design, produção textual, e prompt engineering. Fluente em inglês e espanhol.
            </div>
        </div>
        <div class="card-container" onclick="nextCard()">
            <div class="card">
                Histórico de Trabalho:
            </div>
        </div>
        <div class="card-container" onclick="nextCard()">
            <div class="card">
                BTG Pactual, Jul 2022:<br><br>Summer Job no setor de Automation. Contribuição para o desenvolvimento de projetos.
            </div>
        </div>
        <div class="card-container" onclick="nextCard()">
            <div class="card">
                Dávila Arquitetura, Dez 2019:<br><br>Colaboração na organização de dados (em planilhas e relatórios) atrelados a processos administrativos e organizacionais, inclusive associados à Gestão da Qualidade (ISO 9001).
            </div>
        </div>
        <div class="card-container" onclick="nextCard()">
            <div class="card">
                daniel@sirionpar.com.br
            </div>
        </div>
        </div>

    </body>
    </html>
    """
    return render_template_string(resume_template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
