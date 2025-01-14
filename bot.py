import discord
import json
import requests
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os

# Carregar as variáveis do .env
load_dotenv()

# Configurações
TOKEN = os.getenv("DISCORD_TOKEN")
SERP_API_KEY = os.getenv("SERP_API_KEY")

# Configurações
CANAL_ID = 1328473388783632507  # Substitua pelo ID do canal

# Intents para o bot
intents = discord.Intents.default()
intents.message_content = True  # Habilitar o acesso ao conteúdo das mensagens

bot = commands.Bot(command_prefix="/", intents=intents)

ARQUIVO_NOTICIAS = "noticias_enviadas.json"

# Funções para persistência
def carregar_noticias():
    try:
        with open(ARQUIVO_NOTICIAS, "r") as f:
            return set(json.load(f))
    except FileNotFoundError:
        return set()

def salvar_noticias():
    with open(ARQUIVO_NOTICIAS, "w") as f:
        json.dump(list(noticias_enviadas), f)

# Histórico de notícias enviadas
noticias_enviadas = carregar_noticias()

# Comando /j para buscar notícias específicas
@bot.command(name="j")
async def buscar_noticias(ctx, *, termo: str):
    """Comando para buscar notícias específicas com base no termo fornecido."""
    await ctx.send(f"🔍 Buscando notícias sobre: **{termo}**...")

    # Fazendo a requisição para a API do SerpApi com a palavra-chave fornecida
    url = f"https://serpapi.com/search.json?q={termo}&tbm=nws&tbs=qdr:d&api_key={SERP_API_KEY}"
    response = requests.get(url)
    
    # Log da resposta para depuração
    print(f"Resposta da API: {response.text}")  # Verifique o conteúdo completo da resposta

    if response.status_code == 200:
        resultados = response.json().get("news_results", [])
        if resultados:
            # Enviar a primeira notícia encontrada
            noticia = resultados[0]  # A primeira notícia
            titulo = noticia.get("title")
            link = noticia.get("link")
            if link not in noticias_enviadas:
                noticias_enviadas.add(link)
                salvar_noticias()
                await ctx.send(f"**{titulo}**\n[Leia mais]({link})")
        else:
            await ctx.send("⚠️ Nenhuma notícia encontrada para o termo especificado.")
    else:
        await ctx.send(f"❌ Erro ao buscar notícias: {response.status_code}")

# Função que é chamada quando o bot estiver pronto
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")
    verificar_noticias.start()

@tasks.loop(minutes=10)
async def verificar_noticias():
    """Busca por notícias das últimas 24 horas relacionadas às cidades e envia ao canal."""
    canal = bot.get_channel(CANAL_ID)
    if not canal:
        print("Canal não encontrado! Verifique o ID do canal.")
        return

    # Definindo os termos de busca
    termos = "Aparecida de Goiânia OR Goiânia"
    url = f"https://serpapi.com/search.json?q={termos}&tbm=nws&tbs=qdr:d&api_key={SERP_API_KEY}"

    # Verificar a resposta da API
    response = requests.get(url)
    print(f"Resposta da API (verificando notícias): {response.text}")  # Log de resposta

    if response.status_code == 200:
        resultados = response.json().get("news_results", [])
        if resultados:
            for noticia in resultados:
                titulo = noticia.get("title")
                link = noticia.get("link")
                # Verificar se a notícia já foi enviada
                if link not in noticias_enviadas:
                    # Adicionar ao conjunto de notícias enviadas
                    noticias_enviadas.add(link)
                    salvar_noticias()
                    # Enviar a notícia para o canal
                    await canal.send(f"**{titulo}**\n[Leia mais]({link})")
        else:
            print("Nenhuma notícia encontrada nas últimas 24 horas.")
    else:
        print(f"Erro ao buscar notícias: {response.status_code}")

# Iniciar o bot
bot.run(TOKEN)
