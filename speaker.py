import pdfplumber
import pyttsx3

# Inicializando a engine de NLP
engine = pyttsx3.init()

# Lendo o arquivo PDF
pdf = pdfplumber.open("O elefante em apuros.pdf")
nome_livro = "O Elefante em Apuros"

# Gerando lista de páginas de texto da página 3 a 26
paginas = pdf.pages[2:-3]

texto_livro = ''
for pagina in paginas:
    texto_livro += pagina.extract_text()

texto_final = texto_livro.replace(".", ". ").replace(",", ", ").replace(";", "; ")

engine.save_to_file(texto_final, f"{nome_livro}.mp3", 150)
engine.runAndWait()