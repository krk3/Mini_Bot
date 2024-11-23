# Mini Bot de Discord

![2y94rgbqas691](https://github.com/user-attachments/assets/c4aa86c7-5ac4-4b9e-b8bd-fce79634a689)


Un bot simple para Discord desarrollado en Python que responde a comandos básicos como saludos y genera memes. Este bot está diseñado para ser fácil de configurar, personalizar y expandir, ideal para proyectos pequeños o como base para aprender más sobre bots de Discord.

## Comandos disponibles:
- `!hola`: El bot saluda al usuario.
- `!meme`: El bot responde con un meme aleatorio usando una API externa.
- `!adios`: El bot se despide del usuario.

## Funcionalidades:
- Saludos personalizados.
- Generación de memes aleatorios a través de una API.
- Despedidas amigables.

## Requisitos:
- Python 3.11 o superior.
- Librería `discord.py` (v2.0 o superior).
- Librería `requests` para obtener memes.

## Cómo instalar y usar el bot:

### 1. Clonar este repositorio:
Abre una terminal y clona el repositorio a tu máquina local:

```bash
git clone https://github.com/tu-usuario/mini-bot-discord.git
cd mini-bot-discord
```
### 2. Instalar dependencias:
Asegúrate de tener Python 3.11 o superior instalado en tu sistema. Luego, instala las dependencias necesarias con pip:

```bash
pip install discord requests
```

### 3. Configurar el token de tu bot:
En el archivo Bot.py, reemplaza el valor de TOKEN con el token de tu bot de Discord:

```bash
TOKEN = 'tu-token-de-bot-aqui'
```
### 4. Ejecutar el bot:
Para correr el bot, simplemente ejecuta el archivo Bot.py:

```bash
python Bot.py
```

### 5. Agregar el bot a tu servidor de Discord:
Ve a Discord Developer Portal.
Crea una nueva aplicación si no tienes una.
En la sección de "Bot", habilita el bot.
Copia el token del bot y pégalo en tu archivo Bot.py.
En la sección de "OAuth2" selecciona "bot" como el alcance y los permisos que deseas para tu bot.
Genera el enlace de invitación y agrégalo a tu servidor de Discord.


## Capturas del funcionamiento:
- `!hola`: El bot saluda al usuario.
 
![Captura de pantalla 2024-11-23 194656](https://github.com/user-attachments/assets/6075c4c9-faa8-4015-9d56-f22a2a907e71)

- `!meme`: El bot responde con un meme aleatorio usando una API externa.

![Captura de pantalla 2024-11-23 194708](https://github.com/user-attachments/assets/a1f4c516-4ace-431b-a0fb-3519afd02ba9)

- `!adios`: El bot se despide del usuario.

![Captura de pantalla 2024-11-23 194720](https://github.com/user-attachments/assets/90d42c00-8587-498f-8e33-761993d96268)
