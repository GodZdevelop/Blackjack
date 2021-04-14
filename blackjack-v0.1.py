import random, time

cardA = 1
card2 = 2
card3 = 3
card4 = 4
card5 = 5
card6 = 6
card7 = 7
card8 = 8
card9 = 9
card10 = 10
cardJ = 10
cardQ = 10
cardK = 10

cards = [cardA, card2, card3, card4, card5, card6, card7, card8, card9, card10, cardJ, cardQ,cardK]

player = 0
bot = 0

player_cards = []
bot_cards = []

player_turn = True

player_stand = False
bot_stand = False

while True:
  
  if player_stand == True:
    player_turn = False
  
  if player_turn == True and player_stand == False:
    answer = input('      [hit] [stand] ')
  
  if answer == 'hit' and player_turn == True and player_stand == False:
    selected_card = random.choice(cards)
    player += selected_card
    player_cards.append(selected_card)
    player_turn = False
    
  if answer == 'stand' and player_turn == True and player_stand == False:
    player_stand = True
    player_turn = False
    
    
  print('\n————————————')
  print(f'Player: {player}')
  print(f'Your cards: {player_cards}\n')
  print(f'Bot: {bot}')
  print(f'Bot cards: {bot_cards}')
  print('————————————\n')
  
  if player >= 21:
    break
  
  
  print('      Bot\'s turn...')
  time.sleep(2)
  
  if player_stand == True:
    player_turn = False
  
#If player used stand and bot have the same as the player, and the value is +11: Stand
  if player_stand == True and player == bot and bot > 11 and bot_stand == False and player_turn == False:
    print('      Bot choose... [stand]')
    bot_stand = True
    player_turn = True
    
#If player used stand and bot have more than the player: Stand
  elif player_stand == True and bot > player and player_turn == False and bot_stand == False:
    print('      Bot choose... [stand]')
    bot_stand = True
    player_turn = True
  
#If bot = 18 -> 21: Stand   
  elif bot > 18 and bot < 21 and player_turn == False and bot_stand == False:
    print('      Bot choose... [stand]')
    bot_stand = True
    player_turn = True
    
  

    
#If bot have 15 or less: Hit
  elif bot <= 15 and player_turn == False and bot_stand == False:
    print('      Bot choose... [hit]')
    selected_card = random.choice(cards)
    bot_cards.append(selected_card)
    bot += selected_card
    player_turn = True
    
#If player used stand and bot have the same as the player, and the value is -=11: Hit
  if player_stand == True and player == bot and bot <= 11 and bot_stand == False and player_turn == False:
    print('      Bot choose... [hit]')
    selected_card = random.choice(cards)
    bot_cards.append(selected_card)
    bot += selected_card
    player_turn = True
    
#If player used Stand and bot value is less than the player: Hit
  elif player_stand == True and player > bot and bot_stand == False and player_turn == False:
    print('      Bot choose... [hit]')
    selected_card = random.choice(cards)
    bot_cards.append(selected_card)
    bot += selected_card
    player_turn = True
    
#If bot have less than 15: Hit
  elif bot < 16 and player_turn == False and bot_stand == False:
    print('      Bot choose... [hit]')
    selected_card = random.choice(cards)
    bot_cards.append(selected_card)
    bot += selected_card
    player_turn = True
    
    
  print('\n————————————')
  print(f'Player: {player}')
  print(f'Your cards: {player_cards}\n')
  print(f'Bot: {bot}')
  print(f'Bot cards: {bot_cards}')
  print('————————————\n')
  
  if bot >= 21:
    break
  
  if player_stand == True and bot_stand == True:
    break