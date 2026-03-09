import streamlit as st
import random
from livros import recomendar_livro, livros

st.set_page_config(
    page_title="Homenagem Dia das Mulheres",
    page_icon="🌸",
    layout="centered"
)

# contador
if "contador" not in st.session_state:
    st.session_state.contador = 0

st.title("🌸 Gerador de Homenagens")
st.caption("Crie uma homenagem especial para uma mulher importante no Dia Internacional da Mulher")

# métricas
col1, col2 = st.columns(2)

with col1:
    st.metric("🧸 Homenagens geradas", st.session_state.contador)

with col2:
    total_livros = sum(len(v) for v in livros.values())
    st.metric("📚 Livros recomendados", total_livros)

st.markdown("---")

nome = st.text_input("Nome da pessoa homenageada")

autor = st.text_input("Seu nome (quem envia a homenagem)")

relacao = st.selectbox(
    "Relação",
    [
        "Mãe",
        "Avó",
        "Tia",
        "Madrinha",
        "Madrasta",
        "Irmã",
        "Prima",
        "Amiga",
        "Professora",
        "Mentora",
        "Colega de trabalho",
        "Namorada",
        "Esposa",
        "Filha"
    ]
)

tom = st.selectbox(
    "Tom da mensagem",
    ["Inspirador", "Carinhoso", "Motivador"]
)

inicio = [
    "hoje celebramos uma mulher incrível.",
    "neste dia especial queremos reconhecer você.",
    "uma mulher forte merece todo reconhecimento."
]

inspirador = [
    "Sua coragem inspira todos ao seu redor.",
    "Você transforma desafios em conquistas.",
    "Sua história mostra o poder da determinação."
]

carinhoso = [
    "Seu carinho ilumina a vida das pessoas.",
    "Sua presença torna o mundo mais bonito.",
    "Seu cuidado faz diferença na vida de todos."
]

motivador = [
    "Continue acreditando no seu potencial.",
    "O mundo precisa da sua força.",
    "Seu caminho inspira outras mulheres."
]

final = [
    "Feliz Dia das Mulheres! 🌸",
    "Que seu dia seja cheio de alegria! 💜",
    "Você merece todo reconhecimento! ✨"
]

frases_relacao = {

    "Mãe": [
        "Seu amor é um exemplo todos os dias.",
        "Seu cuidado transforma a vida de todos."
    ],

    "Avó": [
        "Sua sabedoria ilumina toda a família.",
        "Seu carinho atravessa gerações."
    ],

    "Tia": [
        "Seu apoio e alegria fazem diferença na nossa vida.",
        "Você sempre esteve presente nos momentos importantes."
    ],

    "Madrinha": [
        "Seu apoio sempre guiou nossos caminhos.",
        "Sua presença traz segurança e carinho."
    ],

    "Madrasta": [
        "Seu cuidado demonstra que família é construída com amor.",
        "Seu carinho faz diferença na nossa vida."
    ],

    "Irmã": [
        "Crescer ao seu lado é um privilégio.",
        "Sua amizade é um presente para toda vida."
    ],

    "Prima": [
        "Nossa família é mais alegre com você.",
        "Sua companhia torna os momentos especiais."
    ],

    "Amiga": [
        "Sua amizade ilumina os dias mais difíceis.",
        "Você é uma presença especial na minha vida."
    ],

    "Professora": [
        "Seu ensino inspira novos caminhos.",
        "Seu conhecimento transforma vidas."
    ],

    "Mentora": [
        "Sua orientação ajuda a construir novos sonhos.",
        "Seu exemplo inspira crescimento."
    ],

    "Colega de trabalho": [
        "Seu profissionalismo inspira todos ao redor.",
        "Trabalhar ao seu lado é um privilégio."
    ],

    "Namorada": [
        "Seu amor torna a vida mais bonita.",
        "Cada momento ao seu lado é especial."
    ],

    "Esposa": [
        "Compartilhar a vida com você é uma alegria.",
        "Seu amor torna tudo mais significativo."
    ],

    "Filha": [
        "Seu brilho ilumina nosso caminho.",
        "Ver você crescer é uma alegria imensa."
    ]
}

if st.button("🌷 Gerar homenagem"):

    st.session_state.contador += 1

    if tom == "Inspirador":
        frase = random.choice(inspirador)
    elif tom == "Carinhoso":
        frase = random.choice(carinhoso)
    else:
        frase = random.choice(motivador)

    relacao_extra = random.choice(frases_relacao.get(relacao))

    mensagem = (
        f"{nome}, "
        + random.choice(inicio) + " "
        + frase + " "
        + relacao_extra + " "
        + random.choice(final)
    )

    if autor:
        mensagem += f"\n\nCom carinho,\n{autor}"

    livro = recomendar_livro(tom)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("💌 Mensagem")
        st.success(mensagem)

    with col2:
        st.subheader("📚 Livro recomendado")
        st.markdown(f"""
        **{livro['titulo']}**  
        Autora: *{livro['autora']}*
        """)

    st.subheader("✨ Frase do livro")
    st.info(f"“{livro['frase']}”")

    st.download_button(
        "📥 Baixar homenagem",
        mensagem,
        file_name="homenagem_dia_das_mulheres.txt"
    )