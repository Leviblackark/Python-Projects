print('''
              .-.
              | |____________________________________________________
 _ _ _ _ _ _ _| |                                                  .'`.
|_|_|_|_|_|_|_| |-mbfh-------------------------------------------.'****>
`.            | |_______________________________________________.'***.'
  `.        .'| |                                               `**'
    `-.___.'  `-'                                               .'*`.
             ,.  ,.                                             `._.' 
             ||  ||                                                 .'*`.
            ,''--''.                                                `._.'
           : (.)(.) :                                           .'*`.
          ,'        `.                                          `._.'       .'*`.
          :          :                                                 .'*`.`._.' 
          :          :                                                 `._.'
    -ctr- `._m____m_,'                                                    
                                                                   .'*`.
                                                                   `._.'           
''')
print("Welcome to Treasure Island!\n")
print("Find The Treasure in hearts of two✖️\nLost in riddle✖️\nAnd two parts of gold✖️")
print("Your only clue is you✖️\nFor those with val and true✖️\nWill pass through✖️️\n")

answer_1 = input('When the oceans red and the wind runs cherry blue,\nType “Left”, the seeds of life turn red in '
                 'summers bloom,'
                 '\nType “Right” We envy seasons doubt with only two heads, one is true\n').lower()

if answer_1 == "left" or answer_1 == "right":
    if answer_1 == "left":
        answer_2 = input('You have reached a point, for you could return.'
                         '\nOne blessing, one curse, knowledge of fruit and the others of rebirth'
                         '\nType “Human”: The stars grander than oceans and we dream of more, strive for greatness '
                         'to seek peace and come for circle once more'
                         '\nType “Burn”: leave behind to save oneself, to journey alone, '
                         'to feel safe in one\'s home.\n').lower()
        if answer_2 == "human":
            answer_3 = input('You see three rocks,'
                             '\nThe first is brittle and would fall apart and at a single touch'
                             '\nThe second is strong and unmoving, impossible to break '
                             '\nThe thread reflects the pain and love with in ones heart\n'
                             '\nWhich one defines human best'
                             '\nType: First Second Third or Neither\n').lower()
            if answer_3 == "first":
                print("We are all neither and all three at the same time, "
                      "humans can evolve and they change shape over time."
                      "\n️✖️️️✖️✖️️✖️✖️️️✖️️️️✖️✖️️✖️️️️️✖️✖️✖️️✖️GAMEOVER️✖️️️✖️✖️️✖️️✖️✖️️️✖️✖️️✖️️✖️️️✖️✖️"
                      "️✖️️️✖️️️✖️️️")
            elif answer_3 == "Second":
                print("Strength comes from weakness, rocks never began strong "
                      "but form over countless life times"
                      "\n ️✖️️️✖️✖️️✖️✖️️️✖️️️️✖️✖️️✖️️️️️✖️✖️✖️️✖️GAMEOVER️✖️️️✖️✖️️✖️️✖️✖️️️✖️✖️️✖️️✖️️️✖️✖️"
                      "️✖️️️✖️️️✖️️️")
            elif answer_3 == "third":
                print("To have peace, you must have known pain. Harmony is a "
                      "price paved in sorrow and hardship"
                      "\n️✖️️️✖️✖️️✖️✖️️️✖️️️️✖️✖️️✖️️️️️✖️✖️✖️️✖️GAMEOVER️✖️️️✖️✖️️✖️️✖️✖️️️✖️✖️️✖️️✖️️️✖️✖️"
                      "️✖️️️✖️️️✖️️️")
            elif answer_3 == "neither":
                print('You Win, we are all three'
                      '\nHumans are not created equal'
                      '\nTo be strong you must know weakness'
                      '\nAnd to know peace you must know pain')
            else:
                print("✖️✖️✖️ERROR INCORRECT ENTRY✖️✖️✖️️️")
                print("️✖️️✖️✖️️✖️✖️️✖️GAMEOVER️✖️️️✖️✖️️✖️️✖️️✖️")
                print("✖️✖️✖️ERROR INCORRECT ENTRY✖️✖️✖️️")
        elif answer_2 == "burn":
            print('We can not predict ones path but to journey alone is to be the last'
                  '\n️✖️️️✖️✖️️✖️✖️️️✖️️️️✖️✖️️✖️️️️️✖️✖️✖️️✖️GAMEOVER️✖️️️✖️✖️️✖️️✖️✖️️️✖️✖️️✖️️✖️️️✖️✖️️✖️️️✖️️️✖️️️')
        else:
            print("✖️✖️✖️ERROR INCORRECT ENTRY✖️✖️✖️️️")
            print("️✖️️✖️✖️️✖️✖️️✖️GAMEOVER️✖️️️✖️✖️️✖️️✖️✖️️")
            print("✖️✖️✖️ERROR INCORRECT ENTRY✖️✖️✖️️")
    else:
        print('The plants are Poppies and envy is the root of all demise'
              '\n️✖️️✖️✖️️️✖️️️️✖️✖️️✖️️️️️✖️✖️✖️️✖️GAMEOVER✖️️️✖️✖️️✖️️✖️✖️️️✖️✖️️✖️️✖️️️✖️✖️️✖️️️')
else:
    print("✖️✖️✖️ERROR INCORRECT ENTRY✖️✖️✖️️️")
    print("️✖️️✖️✖️️✖️✖️️✖️GAMEOVER️✖️️️✖️✖️️✖️️✖️️✖️")
    print("✖️✖️✖️ERROR INCORRECT ENTRY✖️✖️✖️️")
