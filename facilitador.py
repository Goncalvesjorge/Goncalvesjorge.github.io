import os
from google import genai
from google.colab import userdata

# 1. Configurar o Cliente Gemini utilizando a chave salva nos segredos do Colab
try:
    api_key = userdata.get('API_KEY')
    client = genai.Client(api_key=api_key)
    print("Cliente inicializado com sucesso!")
except Exception as e:
    print(f"Erro ao obter a chave API ou inicializar o cliente. Verifique se configurou 'GEMINI_API_KEY' nos segredos do Colab: {e}")

# 2. Exemplo de manipulação de arquivo local
nome_arquivo = "tarefas_pendentes.txt"
conteudo_tarefas = """- Corrigir bugs no script de processamento de dados
- Gerar relatório mensal em formato PDF
- Enviar e-mail de acompanhamento para os clientes cadastrados"""

with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write(conteudo_tarefas)
print(f"\nArquivo '{nome_arquivo}' criado com sucesso para processamento.")

# 3. Ler o arquivo e enviar para o Gemini processar
if 'client' in locals():
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        dados = arquivo.read()
    
    print("\nEnviando o conteúdo do arquivo para análise do Gemini...")
    
    response = client.models.generate_content(
        model='gemini-2.5-flash-lite',
        contents=f"Abaixo está uma lista de tarefas extraída de um arquivo de texto. Crie um plano de ação em Python com prioridades para realizá-las:\n\n{dados}",
    )
    
    print("\n--- Resposta do Gemini ---")
    print(response.text)
