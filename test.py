from flask import Flask, request, jsonify
import subprocess
import os
import threading
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import asyncio
import logging

app = Flask(__name__)

CUSTOM_LICENSE_PRIVATE_KEY = "9DBC845E9018537810FDAE62824322EEE1B12BAD81FCA28EC295FB397C61CE0B"
TELEGRAM_BOT_TOKEN = "8210884818:AAG_-nscDnTQzp3u920_m_mVPk5YaNj9ZrQ"  # Palitan ng actual bot token

# Telegram bot setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global variable para sa Telegram application
telegram_app = None

def generate_license(software_id, license_type):
    try:
        # Fixed license level - you can change this value as needed
        LICENSE_LEVEL = 6  # Change this to your desired fixed level
        
        if license_type == 'ros':
            cmd = ['python', 'license.py', 'licgenros', software_id, CUSTOM_LICENSE_PRIVATE_KEY]
        else:  # chr
            cmd = ['python', 'license.py', 'licgenchr', software_id, CUSTOM_LICENSE_PRIVATE_KEY]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Telegram command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    user = update.effective_user
    welcome_text = f"""
🤖 *MikroTik License Generator Bot*

Hello {user.mention_markdown_v2()}! I can generate MikroTik licenses for you\.

*Available Commands:*
/start \- Show this welcome message
/ros \[software\_id\] \- Generate RouterOS license
/chr \[software\_id\] \- Generate CHR license
/help \- Show help information

*Examples:*
`/ros 4JZ2-H049`
`/chr pjLQ21gHzfI`

*Note:* All licenses are generated with Level 6 \(extra\-channels\)
    """
    await update.message.reply_markdown_v2(welcome_text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /help is issued."""
    help_text = """
📖 *How to use this bot:*

1\. *For RouterOS License:*
   Send: `/ros YOUR_SOFTWARE_ID`
   Example: `/ros 4JZ2-H049`

2\. *For CHR License:*
   Send: `/chr YOUR_SOFTWARE_ID`
   Example: `/chr pjLQ21gHzfI`

📍 *Where to find Software ID:*
• RouterOS: System > License > click on "System ID"
• CHR: Type `system license print` in terminal

⚠️ *Important:*
• All licenses are Level 6
• Make sure Software ID is correct
• This is for educational purposes
    """
    await update.message.reply_markdown_v2(help_text)

async def generate_ros_license(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Generate RouterOS license."""
    if not context.args:
        await update.message.reply_text("❌ Please provide Software ID\nExample: `/ros 4JZ2-H049`", parse_mode='Markdown')
        return
    
    software_id = context.args[0]
    await generate_and_send_license(update, software_id, 'ros')

async def generate_chr_license(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Generate CHR license."""
    if not context.args:
        await update.message.reply_text("❌ Please provide Software ID\nExample: `/chr pjLQ21gHzfI`", parse_mode='Markdown')
        return
    
    software_id = context.args[0]
    await generate_and_send_license(update, software_id, 'chr')

async def generate_and_send_license(update: Update, software_id: str, license_type: str):
    """Generate license and send to user."""
    try:
        # Send "generating" message
        generating_msg = await update.message.reply_text("⏳ Generating license...")
        
        # Generate license (sync function, so we run it in thread)
        loop = asyncio.get_event_loop()
        license_key = await loop.run_in_executor(None, generate_license, software_id, license_type)
        
        # Delete generating message
        await context.bot.delete_message(chat_id=generating_msg.chat_id, message_id=generating_msg.message_id)
        
        if license_key.startswith("Error:"):
            await update.message.reply_text(f"❌ {license_key}")
        else:
            license_type_name = "RouterOS" if license_type == 'ros' else "CHR"
            response_text = f"""
✅ *{license_type_name} License Generated*

📋 *Software ID:* `{software_id}`
🔑 *License Level:* 6 \(extra\-channels\)

📜 *License Key:*
