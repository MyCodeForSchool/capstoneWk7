# import bot, user_input
#
# print('Welcome to ' + bot.program_name)
#
# print('Type stop to end.')
#
# user_input.ask_question('How was your day?')
#
# while True:
#     bot_response =bot.generate_computer_response()
#     response = user_input.ask_question(bot_response)
#     if response.upper() == 'STOP':
#         break
#
# print('Thanks for the interesting conversation!')

from bot import program_name, generate_computer_response
from user_input import ask_question
# from bot import *  #not recommended to use "*" as modules might have same names
# from user_input import *

print('Welcome to ' + program_name)

print('Type stop to end.')

ask_question('How was your day?')

while True:
    bot_response =generate_computer_response()
    response = ask_question(bot_response)
    if response.upper() == 'STOP':
        break

print('Thanks for the interesting conversation!')
