import discord
import os
from discord.ext import commands
import random

# Configuración de intents
intents = discord.Intents.default()
intents.message_content = True

# Creación del bot
botsito = commands.Bot(command_prefix="/", intents=intents)

# Evento al iniciar el bot
@botsito.event
async def on_ready():
    print("El bot está en línea y listo para promover el reciclaje.")

# Lista de consejos sobre reciclaje
formas_reciclaje = [
    "1. Separa la basura en orgánica e inorgánica para facilitar el reciclaje.",
    "2. Limpia los envases antes de reciclarlos para evitar contaminación.",
    "3. Reutiliza frascos de vidrio como recipientes o decoración.",
    "4. Lleva tus botellas de plástico a centros de acopio locales.",
    "5. Usa bolsas reutilizables en lugar de bolsas de plástico desechables.",
    "6. Convierte restos de comida en compost para tus plantas.",
    "7. Dona ropa y artículos que ya no uses en lugar de tirarlos.",
    "8. Recicla baterías, pilas y electrónicos en puntos de recolección especializados.",
]

# Comando para enviar información aleatoria sobre reciclaje
@botsito.command()
async def reciclaje(ctx):
    consejo = random.choice(formas_reciclaje)  # Selecciona un consejo aleatorio
    await ctx.send(f"🌱 **Consejo de reciclaje:** {consejo}")

# Comando para listar todas las formas de reciclaje
@botsito.command()
async def formas(ctx):
    consejos = "\n".join(formas_reciclaje)  # Combina todos los consejos en un texto
    await ctx.send(f"♻️ **Formas de reciclaje:**\n{consejos}")




botsito.run("MTMwNzExNDIwNTU5NzQwMTE0OA.Gd0C6Q.dd4k4HVPCsFSL2LDyL_ORNmHNytyRLSgZut5_8")  
 
