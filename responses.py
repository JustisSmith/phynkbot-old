import random
import phynkblackjack

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        hello_responses = ["Hey there", "Ayo", "What's up", "Hello"]
        return random.choice(hello_responses)
    
    if p_message[0:6] == 'roll d':
        roll_num = int(p_message[6:])
        return str(random.randint(1,roll_num))
    
    if p_message == 'roll':
        return str(random.randint(1,6))
    
    if p_message == 'help':
        return "`Use '!' before a statement for public message \nUse '?' before a statement for private message \nCommands: \nhello\nroll d'#'`"
    
    if p_message == 'blackjack':
        start = "Starting Blackjack"

        def deal():
            card = random.randint(1,13)
            if card in range (11,13):
                card = 10

            if card == 1:
                card = 11

            return card

        player_card1 = deal()
        player_card2 = deal()
        dealer_card1 = deal()

        player_sum = (player_card1 + player_card2)

        p1 = (f'Player\'s Cards: {player_sum}')
        d1 = (f'Dealer\'s Card: {dealer_card1}')

        
            
        return (f'{start}\n\n {p1}\n {d1}')

    
