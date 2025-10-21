"""
PREGUNTAS_AIKEN
"""

#!/usr/bin/env python
# coding: utf-8

# In[5]:


from dotenv import load_dotenv
load_dotenv()
import os
import openai
from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI
import docx

from langchain_openai import ChatOpenAI


# Configura tu API key de OpenAI
openai.api_key = "YOUR_API_KEY_HERE"

# Define la ruta de los documentos
path_in = "C:\\Users\\HP\\Desktop\\CATO CURSOS-1-2024\\GER-TI CATO1-2024\\Cursos\\EXAMEN FINAL\\textos y preguntas\\"
path_out = "C:\\Users\\HP\\Desktop\\CATO CURSOS-1-2024\\GER-TI CATO1-2024\\Cursos\\EXAMEN FINAL\\textos y preguntas\\preguntas\\"
# Función para leer contenido de archivos docx
def read_docx(path_in):
    doc = docx.Document(path_in)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

# Prompt para generar preguntas AIKEN
prompt_template = """Elabora VEINTE preguntas en formato AIKEN del texto que te copio en adjunto.  
      Las preguntas deben ser principalmente del tema abordado en el texto.
      NUNCA das citaciones ni fuentes
      NUNCA das un texto de introduccion , ni de despedida 
      UNICAMENTE respondes con las preguntas solictadas haciendo como en el ejemplo, no mas y no menos
      El ejemplo de preguntas que debes generar son así:”
Según el texto de título: Business Storytelling Masterclass with Matteo Cassese, ¿qué es esencial para captar la atención del público en storytelling?
A) Utilizar terminología complicada
B) Hablar en un tono monótono
C) Empezar con una anécdota interesante
D) Presentar gráficos complejos
ANSWER: C
"""

# Inicializa el modelo de lenguaje
llm = ChatOpenAI(model = "gpt-4o",
                 temperature = 0.7, # mas cerca de 0 mas concreto mas cerca de 1 mas creativo
                 verbose = True                
                )

# Procesa cada archivo en la carpeta
for filename in os.listdir(path_in):
    if filename.endswith(".txt"):
        file_path = os.path.join(path_in, filename)
        content = read_docx(file_path)

        # Prepara el prompt
        prompt = prompt_template.format(content=content)

        # Genera las preguntas
        response = llm.invoke(prompt_template) # con temaplte haremos que gallina sea una replazada por una variable
        print(response.content)

        questions = response.choices[0].text.strip()

        # Guarda las preguntas en un archivo .txt
        output_file = os.path.join(path_out, f"questions_{filename.split('.')[0]}.txt")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(questions)

print("Preguntas generadas y guardadas exitosamente.")


# In[18]:


from langchain_core.prompts import ChatPromptTemplate

# path_out = "C:\\Users\\HP\\Desktop\\CATO CURSOS-1-2024\\GER-TI CATO1-2024\\Cursos\\EXAMEN FINAL\\textos y preguntas\\preguntas\\"



# path_in=r"C:\Users\HP\Desktop\CATO CURSOS-1-2024\GER-TI CATO1-2024\Cursos\EXAMEN FINAL\textos y preguntas\Charlavirtual10estrategiasdeMarketingDigitalparapotenciartuemprendimiento.txt"
# # Aqui creamos el template
prompt = ChatPromptTemplate.from_template("""Elabora VEINTE preguntas en formato AIKEN del siguiente texto {texto}.  
      Las preguntas deben ser principalmente del tema abordado en el texto.
      NUNCA das citaciones ni fuentes
      NUNCA das un texto de introduccion , ni de despedida 
      UNICAMENTE respondes con las preguntas solictadas haciendo como en el ejemplo, no mas y no menos
      El ejemplo de preguntas que debes generar son así:”
Según el texto de título: Business Storytelling Masterclass with Matteo Cassese, ¿qué es esencial para captar la atención del público en storytelling?
A) Utilizar terminología complicada
B) Hablar en un tono monótono
C) Empezar con una anécdota interesante
D) Presentar gráficos complejos
ANSWER: C
""")



chain = prompt | llm # hacemos que el pormpt sea pasado a la instacia LLM

title = "Prueba1"

# def leer_archivo_txt(path_in, path_out):
#     with open(path_in, 'r', encoding='utf-8') as archivo:
#         contenido = archivo.read()
#         response = chain.invoke({"texto":contenido})
#         text= response.content
#     file_path = os.path.join(path_out, f"{title}.txt")
#     with open(file_path, 'w', encoding='utf-8') as file:
#         file.write(text)

# leer_archivo_txt(path_in, path_out)


import os

def leer_archivo_txt(path_in, path_out):
    # Iterar sobre todos los archivos en la carpeta de entrada
    for filename in os.listdir(path_in):
        if filename.endswith(".txt"):
            file_path_in = os.path.join(path_in, filename)

            with open(file_path_in, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                response = chain.invoke({"texto": contenido})
                text = response.content

            # Obtener el título sin la extensión .txt
            title = os.path.splitext(filename)[0]

            # Construir la ruta de salida completa
            file_path_out = os.path.join(path_out, f"{title}.txt")

            with open(file_path_out, 'w', encoding='utf-8') as file:
                file.write(text)

            print(f"Archivo procesado y guardado en: {file_path_out}")

# Ejemplo de uso
path_out = "C:\\Users\\HP\\Desktop\\CATO CURSOS-1-2024\\GER-TI CATO1-2024\\Cursos\\EXAMEN FINAL\\textos y preguntas\\preguntas\\"
path_in = "C:\\Users\\HP\\Desktop\CATO CURSOS-1-2024\\GER-TI CATO1-2024\\Cursos\\EXAMEN FINAL\\textos y preguntas\\textos\\"
# Aqui creamos el template

# Suponiendo que tienes un objeto 'chain' ya definido para invocar la cadena de procesamiento
# chain = ...

leer_archivo_txt(path_in, path_out)




# In[ ]:






if __name__ == "__main__":
    pass
