import random
import phynkbot2
import discord
import os

async def send_message(message, is_private):
    try:
        await message.author.send(message) if is_private else await message.channel.send(message)

    except Exception as e:
        print(e)

class bj:
    def play_bj(test):
            test.start = "Starting Blackjack"

            player_card1 = random.randint(1,13)
            player_card2 = random.randint(1,13)
            dealer_card1 = random.randint(1,13)
            player_sum = sum(player_card1,player_card2)

            test.p1 = (f'Player\'s Cards: {player_sum}')
            test.p2 = (f'Dealer\'s Card: {dealer_card1}')

def fun():
     return bj()


