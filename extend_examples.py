import os
from utils import *


instrument_theme_examples = [['The','ball','broke','the','window','.'], 
                             ['The','hammer','smashed','the','vase','.'], 
                             ['The','knife','cut','the','bread','.'], 
                             ['The','scissors','shredded','the','paper','.'], 
                             ['The','axe','split','the','wood','.'], 
                             ['The','saw','sliced','the','metal','.'], 
                             ['The', 'key', 'unlocked', 'the', 'door', '.'], 
                             ['The','camera','captured','the','moment','.'], 
                             ['The','stapler','fastened','the','papers','.'], 
                             ['The', 'fork', 'speared', 'the', 'meat', '.'], 
                             ['The','blender','pureed','the','fruit','.'],
                             ['The','mixer','whipped','the','cream','.'], 
                             ['The','drill','bored','the','hole','.'], 
                             ['The','laser','cut','the','steel','.'], 
                             ['The','microphone','amplified','the','sound','.'], 
                             ['The','bullet','killed','the','man','.'], 
                             ['The','knife','sliced','the','tomato','.'], 
                             ['The','guitar','strummed','the','chords','.']] 

instrument_theme_labels = ['O','B-ARG2','O','O','B-ARG1','O']


caused_motion_examples = [['The','window','broke','.'],
                          ['The','vase','shattered','.'],
                          ['The','balloon','burst','.'],
                          ['The','door','opened','.'],
                          ['The','car','stopped', '.'],
                          ['The','glass','cracked','.'],
                          ['The','bridge','collapsed','.'],
                          ['The','boat','sank','.'],
                          ['The','computer','crashed','.'],
                          ['The','ice','melted','.'],
                          ['The','knife','dropped','.'],
                          ['The','airplane','crashed','.'],
                          ['The','rock','rolled','.'],
                          ['The','oil','spilled','.'],
                          ['The','satellite','launched','.'],
                          ['The','skateboard','rolled','.'],
                          ['The', 'spaceship', 'landed', '.']]

caused_motion_labels = ['O','B-ARG1','O','O']


benefactive_examples = [['She', 'lent', 'her', 'friend', 'a', 'book', '.'],
                        ['He', 'showed', 'his', 'wife', 'a', 'sunset', '.'],
                        ['She', 'sent', 'her', 'mother', 'a', 'bouquet', '.'],
                        ['She', 'cooked', 'her', 'grandmother', 'a', 'meal', '.'],
                        ['He', 'gave', 'his', 'boss', 'a', 'gift', '.'],
                        ['I', 'wrote', 'my', 'niece', 'a', 'letter', '.'],
                        ['John', 'bought', 'his', 'girlfriend', 'a', 'necklace', '.'],
                        ['Mary', 'emailed', 'her', 'boss', 'a', 'note', '.'],
                        ['They', 'offered', 'their', 'guests', 'a', 'snack', '.']]

benefactive_labels = ['B-ARG0','O','O','B-ARG2','O','B-ARG1','O']


unmask = create_pipeline()

if __name__ == '__main__':
    ### Instrument+Theme:   
    print('Extending Instrument+Theme examples ...')
    # save unmodified examples in .json
    save_to_json(instrument_theme_examples, instrument_theme_labels, 'Instrument+Theme.json')
    # mask the 5nd token, extend examples 
    instrument_theme_generated_examples = generate_examples(instrument_theme_examples, unmask, 4)
    # append new generated examples to .json 
    save_to_json(instrument_theme_generated_examples, instrument_theme_labels, 'Instrument+Theme.json')
    # clean examples from the ones that duplicate human examples 
    instrument_theme_clean_examples = delete_duplicates('Instrument+Theme.json')
    # delete the old .json file
    os.remove('Instrument+Theme.json')
    # get clean .json file 
    save_to_json(instrument_theme_clean_examples, instrument_theme_labels, 'Instrument+Theme.json')
    print('Instrument+Theme.json is saved')
                           
    ### Caused-motion:
    print('Extending caused-motion examples ...')
    save_to_json(caused_motion_examples, caused_motion_labels, 'Caused-motion.json')
    # mask the 2nd token, extend examples 
    caused_motion_generated_examples = generate_examples(caused_motion_examples, unmask, 1)
    save_to_json(caused_motion_generated_examples, caused_motion_labels, 'Caused-motion.json')
    caused_motion_clean_examples = delete_duplicates('Caused-motion.json')
    os.remove('Caused-motion.json')
    save_to_json(caused_motion_clean_examples, caused_motion_labels, 'Caused-motion.json')
    print('Caused-motion.json is saved')
    
    ### Benefactive:
    print('Extending benefactive examples ...')
    save_to_json(benefactive_examples, benefactive_labels, 'Benefactive.json')
    # mask the 4th and 6th tokens, extend examples 
    benefactive_generated_examples_first_iter = generate_examples(benefactive_examples, unmask, 3)
    benefactive_generated_examples_second_iter = generate_examples(benefactive_generated_examples_first_iter, unmask, 5)
    save_to_json(benefactive_generated_examples_second_iter, benefactive_labels, 'Benefactive.json')
    benefactive_clean_examples = delete_duplicates('Benefactive.json')
    os.remove('Benefactive.json')
    save_to_json(benefactive_clean_examples, benefactive_labels, 'Benefactive.json')
    print('Benefactive.json is saved')
