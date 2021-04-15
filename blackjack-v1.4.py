import random, time

cardA = 'A'
card2 = 2
card3 = 3
card4 = 4
card5 = 5
card6 = 6
card7 = 7
card8 = 8
card9 = 9
card10 = 10
cardJ = 'J'
cardQ = 'Q'
cardK = 'K'

cards = [cardA, card2, card3, card4, card5, card6, card7, card8, card9, card10, cardJ, cardQ,cardK]
cards_icon = ['♥️', '♠️', '♦️', '♣️']

player = 0
bot = 0

player_cards = []
bot_cards = []

player_turn = True

player_stand = False
bot_stand = False

enemy_list = ['Dragon', 'God', 'GodZ!', 'Bot', 'Tryhard', 'Donald Trump', 'Elon Musk', 'Grandpa']

enemy = random.choice(enemy_list)

player_text_visibility = True


while True:
  
  if player_stand == True:
     player_text_visibility = False
  
  if player_turn == True and player_stand == False:
    answer = input('      [hit] [stand] ')
  
  if answer == 'hit' and player_turn == True and player_stand == False:
    selected_card = random.choice(cards)
    
    if selected_card == 'J':
      selected_card_icon = 'J' + random.choice(cards_icon)
      selected_card = 10
    elif selected_card == 'Q':
      selected_card_icon = 'Q' + random.choice(cards_icon)
      selected_card = 10
    elif selected_card == 'K':
      selected_card_icon = 'K' + random.choice(cards_icon)
      selected_card = 10
    elif selected_card == 'A':
      selected_card_icon = 'A' + random.choice(cards_icon)
      selected_card = 1
    else:
      selected_card_icon = str(selected_card) + random.choice(cards_icon)
    
    player += selected_card
    player_cards.append(selected_card_icon)
    player_turn = False
    
  if answer == 'stand' and player_turn == True and player_stand == False:
    player_stand = True
    player_turn = False
    
  if player_text_visibility == True:
    print('\n————————————')
    print(f'Player: {player}')
    print(f'Your cards: {player_cards}\n')
    print(f'{enemy}: {bot}')
    print(f'{enemy} cards: {bot_cards}')
    print('————————————\n')
  
  if player >= 21:
    break
  
  if len(player_cards) > 4 and player <= 21:
    break
  
  
  
  
  print(f'      {enemy}\'s turn...')
  time.sleep(1)
  
  if player_stand == True:
    player_turn = False
    
#If player used Stand and bot value is less than the player: Hit
  if player_stand == True and player > bot and bot_stand == False and player_turn == False:
    print(f'      {enemy} choosed... [hit]')
    selected_card = random.choice(cards)
    
    if selected_card == 'J':
      selected_card_icon = 'J' + random.choice(cards_icon)
      selected_card = 10
    elif selected_card == 'Q':
      selected_card_icon = 'Q' + random.choice(cards_icon)
      selected_card = 10
    elif selected_card == 'K':
      selected_card_icon = 'K' + random.choice(cards_icon)
      selected_card = 10
    elif selected_card == 'A':
      selected_card_icon = 'A' + random.choice(cards_icon)
      selected_card = 1
    else:
      selected_card_icon = str(selected_card) + random.choice(cards_icon)
      
    bot_cards.append(selected_card_icon)
    bot += selected_card
    player_turn = True
  
#If player used stand and bot have the same as the player, and the value is +11: Stand
  if player_stand == True and player == bot and bot > 11 and bot_stand == False and player_turn == False:
    print(f'      {enemy} choosed... [stand]')
    bot_stand = True
    player_turn = True
    
#If player used stand and bot have more than the player: Stand
  elif player_stand == True and bot > player and player_turn == False and bot_stand == False:
    print(f'      {enemy} choosed... [stand]')
    bot_stand = True
    player_turn = True
  
#If bot = 16 -> 21: Stand   
  elif bot >= 16 and bot < 21 and player_turn == False and bot_stand == False:
    print(f'      {enemy} choosed... [stand]')
    bot_stand = True
    player_turn = True
    

    
#If bot have 15 or less: Hit
  elif bot <= 15 and player_turn == False and bot_stand == False:
    print(f'      {enemy} choosed... [hit]')
    selected_card = random.choice(cards)
    
    if selected_card == 'J':
      selected_card_icon = 'J' + random.choice(cards_icon)
      selected_card = 10
    elif selected_card == 'Q':
      selected_card_icon = 'Q' + random.choice(cards_icon)
      selected_card = 10
    elif selected_card == 'K':
      selected_card_icon = 'K' + random.choice(cards_icon)
      selected_card = 10
    elif selected_card == 'A':
      selected_card_icon = 'A' + random.choice(cards_icon)
      selected_card = 1
    else:
      selected_card_icon = str(selected_card) + random.choice(cards_icon)
      
    bot_cards.append(selected_card_icon)
    bot += selected_card
    player_turn = True
    
#If player used stand and bot have the same as the player, and the value is -=11: Hit
  if player_stand == True and player == bot and bot <= 11 and bot_stand == False and player_turn == False:
    print(f'      {enemy} choosed... [hit]')
    selected_card = random.choice(cards)
    
    if selected_card == 'J':
      selected_card_icon = 'J' + random.choice(cards_icon)
      selected_card = 10
    elif selected_card == 'Q':
      selected_card_icon = 'Q' + random.choice(cards_icon)
      selected_card = 10
    elif selected_card == 'K':
      selected_card_icon = 'K' + random.choice(cards_icon)
      selected_card = 10
    elif selected_card == 'A':
      selected_card_icon = 'A' + random.choice(cards_icon)
      selected_card = 1
    else:
      selected_card_icon = str(selected_card) + random.choice(cards_icon)
      
    bot_cards.append(selected_card_icon)
    bot += selected_card
    player_turn = True
    
    
    
  print('\n————————————')
  print(f'Player: {player}')
  print(f'Your cards: {player_cards}\n')
  print(f'{enemy}: {bot}')
  print(f'{enemy} cards: {bot_cards}')
  print('————————————\n')
  
  
  if bot >= 21:
    break
  
  if len(bot_cards) > 4 and bot <= 21:
    break
  
  if player_stand == True and bot_stand == True:
    break
  
  
  
  
if player == 21:
  print('You win! You reached 21 first')
  
elif bot == 21:
  print('You lost! The dealer reached 21 first')
  
elif player > 21:
  print('You lost! You bypassed 21')

elif bot > 21:
  print('You win! The dealer bypassed 21')
  
elif len(player_cards) > 4 and player <= 21:
  print('You win! You took 5 cards without getting 21')
  
elif len(bot_cards) > 4 and bot <= 21:
  print('You lost! The dealer took 5 cards without getting 21')
  
elif player > bot:
  print(f'You win! Your cards: {player} | Dealer cards: {bot}')
  
elif player < bot:
  print(f'You lost! Your cards: {player} | Dealer cards: {bot}')
  
elif player == bot:
  print('Draw')