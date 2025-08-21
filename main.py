import logging
import os
from dotenv import load_dotenv
from src.bot.telegram_bot import TelegramBot
from src.llm.model import init_llm, init_local_llm

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    try:
        # Load environment variables
        load_dotenv()
        
        # Get Telegram token
        telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")
        if not telegram_token:
            raise ValueError("TELEGRAM_BOT_TOKEN environment variable is not set")
        
        # Initialize LLM (choose one)
        use_local = os.getenv("USE_LOCAL_LLM", "false").lower() == "true"
        if use_local:
            llm = init_local_llm()
        else:
            api_key = os.getenv("GOOGLE_API_KEY")
            if not api_key:
                raise ValueError("GOOGLE_API_KEY environment variable is not set")
            llm = init_llm(api_key)
        
        # Create and start the bot
        bot = TelegramBot(telegram_token, llm)
        bot.start()
        
    except Exception as e:
        logger.error(f"Error in main: {str(e)}")
        raise

if __name__ == "__main__":
    main()