import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from llama_index.core.llms import LLM

logger = logging.getLogger(__name__)

class TelegramBot:
    def __init__(self, token: str, llm: LLM):
        """Initialize the bot with token and LLM model."""
        self.token = token
        self.llm = llm
        # Modified initialization to avoid proxy issues
        self.app = Application.builder().token(self.token).connect_timeout(30.0).read_timeout(30.0).build()
        self._setup_handlers()

    def _setup_handlers(self):
        """Setup command and message handlers."""
        self.app.add_handler(CommandHandler("start", self._start_command))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self._handle_message))

    async def _start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle the /start command."""
        await update.message.reply_text("Ciao! Sono il tuo chatbot AI 🤖\nPuoi chiedermi qualsiasi cosa!")

    async def _handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle incoming messages using the LLM."""
        try:
            user_message = update.message.text
            # Send "typing" action while processing
            await update.message.chat.send_action(action="typing")
            
            # Get response from LLM
            response = self.llm.complete(user_message)
            
            await update.message.reply_text(response.text)
            
        except Exception as e:
            logger.error(f"Error processing message: {str(e)}")
            await update.message.reply_text("Mi dispiace, si è verificato un errore durante l'elaborazione del messaggio.")

    def start(self):
        """Start the bot."""
        logger.info("Bot starting... 🚀")
        self.app.run_polling()