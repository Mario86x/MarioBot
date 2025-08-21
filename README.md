# README.md

# MarioBot

MarioBot is a Telegram chatbot that interacts with a language model to provide responses to user messages. This project is structured to allow easy expansion and maintenance of functionalities.

## Features

- Responds to user messages with predefined commands.
- Integrates with a language model for dynamic responses.
- Modular architecture for easy addition of new features.

## Project Structure

```
mariobot
├── src
│   ├── bot
│   │   ├── __init__.py
│   │   └── telegram_bot.py
│   ├── llm
│   │   ├── __init__.py
│   │   └── model.py
│   ├── handlers
│   │   ├── __init__.py
│   │   └── message_handler.py
│   ├── config
│   │   ├── __init__.py
│   │   └── settings.py
│   └── utils
│       ├── __init__.py
│       └── helpers.py
├── tests
│   ├── __init__.py
│   ├── test_bot.py
│   └── test_llm.py
├── .env
├── requirements.txt
├── main.py
└── README.md
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd mariobot
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up your environment variables in the `.env` file.

## Usage

To run the bot, execute the following command:

```bash
python main.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.