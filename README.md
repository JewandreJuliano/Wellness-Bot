# Wellness-Bot
This Bot was made to aid the overall wellness of humans.

## Description
This bot provides personalized wellness advice based on user input. It can respond to queries about stress, energy levels, diet, and more.

## Installation
1. Clone the repository.
2. Set up a virtual environment:
   - python -m venv venv
   
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On Mac/Linux: `source venv/bin/activate`
4. Install dependencies:
   - pip install -r requirements.txt

## Running the Bot
1. Replace `"7168442396:AAEyMOGGq8568GwauU8rhpoSVNe1SLRnOdo"` in `bot.py` with your actual Telegram bot token.
2. Run the bot:
   - python bot.py

## Verifying the Solution
Start a conversation with your bot on Telegram and ask it for wellness advice. The bot should respond with appropriate tips.

## Limitations
- The bot may not handle complex or ambiguous queries well.
- It provides general advice and should not be considered a substitute for professional medical guidance.
- When the user queries a response out of the bots controll it tells the user that it is not inclined to respond to all queries as of yet.
