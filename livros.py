import random

livros = {
    "Inspirador": [
        {
            "titulo": "Sejamos Todos Feministas",
            "autora": "Chimamanda Ngozi Adichie",
            "frase": "A cultura não faz as pessoas. As pessoas fazem a cultura."
        },
        {
            "titulo": "I Know Why the Caged Bird Sings",
            "autora": "Maya Angelou",
            "frase": "Ainda assim, eu me levanto."
        },
        {
            "titulo": "O Segundo Sexo",
            "autora": "Simone de Beauvoir",
            "frase": "Não se nasce mulher: torna-se."
        },
        {
            "titulo": "Um Teto Todo Seu",
            "autora": "Virginia Woolf",
            "frase": "Uma mulher precisa de dinheiro e um teto todo seu."
        },
        {
            "titulo": "Americanah",
            "autora": "Chimamanda Ngozi Adichie",
            "frase": "A raça não existe biologicamente, mas existe socialmente."
        }
    ],

    "Carinhoso": [
        {
            "titulo": "Orgulho e Preconceito",
            "autora": "Jane Austen",
            "frase": "Não há encanto igual à ternura do coração."
        },
        {
            "titulo": "A Hora da Estrela",
            "autora": "Clarice Lispector",
            "frase": "Ela acreditava nos pequenos instantes da vida."
        },
        {
            "titulo": "A Amiga Genial",
            "autora": "Elena Ferrante",
            "frase": "A amizade pode transformar destinos."
        },
        {
            "titulo": "Pequenos Incêndios por Toda Parte",
            "autora": "Celeste Ng",
            "frase": "Às vezes é preciso destruir algo para reconstruir."
        },
        {
            "titulo": "Circe",
            "autora": "Madeline Miller",
            "frase": "Eu descobri que podia moldar meu próprio destino."
        }
    ],

    "Motivador": [
        {
            "titulo": "Beloved",
            "autora": "Toni Morrison",
            "frase": "Você é sua melhor coisa."
        },
        {
            "titulo": "Frankenstein",
            "autora": "Mary Shelley",
            "frase": "Nada é tão doloroso quanto o pensamento não realizado."
        },
        {
            "titulo": "Jane Eyre",
            "autora": "Charlotte Brontë",
            "frase": "Eu não sou um pássaro; nenhuma rede me prende."
        },
        {
            "titulo": "Quarto de Despejo",
            "autora": "Carolina Maria de Jesus",
            "frase": "O Brasil precisa ser dirigido por quem já passou fome."
        },
        {
            "titulo": "O Conto da Aia",
            "autora": "Margaret Atwood",
            "frase": "Não deixe que os bastardos te oprimam."
        }
    ]
}

def recomendar_livro(tom):
    return random.choice(livros[tom])