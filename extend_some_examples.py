import os
from utils import *


instrument_theme_examples = [['The', 'ball', 'broke', 'the', 'window', '.'], 
                             ['The', 'hammer', 'smashed', 'the', 'vase', '.'], 
                             ['The', 'knife', 'cut', 'the', 'bread', '.'], 
                             ['The', 'scissors', 'shredded','the','paper','.'], 
                             ['The', 'axe', 'split', 'the', 'wood', '.'], 
                             ['The', 'saw', 'sliced', 'the', 'metal', '.'], 
                             ['The', 'key', 'unlocked', 'the', 'door', '.'], 
                             ['The', 'camera', 'captured', 'the', 'moment', '.'], 
                             ['The', 'stapler', 'fastened', 'the', 'papers', '.'], 
                             ['The', 'fork', 'speared', 'the', 'meat', '.'], 
                             ['The', 'blender', 'pureed', 'the', 'fruit', '.'],
                             ['The', 'mixer', 'whipped', 'the', 'cream', '.'], 
                             ['The', 'drill', 'bored', 'the', 'hole', '.'], 
                             ['The', 'laser', 'cut', 'the', 'steel', '.'], 
                             ['The', 'microphone', 'amplified', 'the', 'sound', '.'], 
                             ['The', 'bullet', 'killed', 'the', 'man', '.'], 
                             ['The', 'knife', 'sliced', 'the', 'tomato', '.'], 
                             ['The', 'guitar', 'strummed', 'the', 'chords', '.']] 

instrument_theme_labels = ['B-ARG2','I-ARG2','O','B-ARG1','I-ARG1','O']


benefactive_examples = [['She', 'lent', 'her', 'friend', 'a', 'book', '.'],
                        ['He', 'showed', 'his', 'wife', 'a', 'sunset', '.'],
                        ['She', 'sent', 'her', 'mother', 'a', 'bouquet', '.'],
                        ['She', 'cooked', 'her', 'grandmother', 'a', 'meal', '.'],
                        ['He', 'gave', 'his', 'boss', 'a', 'gift', '.'],
                        ['I', 'wrote', 'my', 'niece', 'a', 'letter', '.'],
                        ['John', 'bought', 'his', 'girlfriend', 'a', 'necklace', '.'],
                        ['Mary', 'emailed', 'her', 'boss', 'a', 'note', '.'],
                        ['They', 'offered', 'their', 'guests', 'a', 'snack', '.']]

benefactive_labels = ['B-ARG0','O','B-ARG2','I-ARG2','B-ARG1','I-ARG1','O']


passive_voice_examples = [['The', 'car', 'was', 'repaired', 'by', 'the', 'mechanic', '.'],
                          ['The', 'picture', 'was', 'painted', 'by', 'the', 'artist', '.'],
                          ['The', 'problem', 'was', 'solved', 'by', 'the', 'team', '.'],
                          ['The', 'letter', 'was', 'typed', 'by', 'the', 'secretary', '.'],
                          ['The', 'house', 'was', 'built', 'by', 'the', 'contractor', '.'],
                          ['The', 'song', 'was', 'composed', 'by', 'the', 'musician', '.'],
                          ['The', 'essay', 'was', 'graded', 'by', 'the', 'teacher', '.'],
                          ['The', 'project', 'was', 'completed', 'by', 'the', 'team', '.'],
                          ['The', 'speech', 'was', 'delivered', 'by', 'the', 'politician', '.'],
                          ['The', 'movie', 'was', 'directed', 'by', 'the', 'filmmaker', '.'],
                          ['The', 'bridge', 'was', 'constructed', 'by', 'the', 'engineer', '.'],
                          ['The', 'garden', 'was', 'tended', 'by', 'the', 'gardener', '.'],
                          ['The', 'experiment', 'was', 'conducted', 'by', 'the', 'scientist', '.'],
                          ['The', 'website', 'was', 'designed', 'by', 'the', 'developer', '.'],
                          ['The', 'meal', 'was', 'prepared', 'by', 'the', 'chef', '.'],
                          ['The', 'presentation', 'was', 'given', 'by', 'the', 'speaker', '.']]

passive_voice_labels = ['B-ARG1','I-ARG1','O','O','O','B-ARG0','I-ARG0','O']


left_out_predicate_examples = [['John', 'likes', 'coffee', ',', 'and', 'Mary', 'tea', '.'],
                               ['Sarah', 'enjoys', 'swimming', ',', 'and', 'Mark', 'running', '.'],
                               ['She', 'prefers', 'books', ',', 'and', 'he', 'movies', '.'],
                               ['He', 'loves', 'hiking', ',', 'and', 'she', 'camping', '.'],
                               ['He', 'enjoys', 'classics', ',', 'and', 'she', 'jazz', '.'],
                               ['John', 'plays', 'basketball', ',', 'and', 'Bill', 'soccer', '.'],
                               ['They', 'enjoy', 'skiing', ',', 'and', 'we', 'snowboarding', '.'],
                               ['He', 'drinks', 'beer', ',', 'and', 'she', 'wine', '.'],
                               ['You', 'study', 'math', ',', 'and', 'I', 'physics', '.'],
                               ['I', 'prefer', 'dogs', ',', 'and', 'Emma', 'cats', '.'],
                               ['He', 'enjoys', 'gardening', ',', 'and', 'she', 'cooking', '.'],
                               ['She', 'likes', 'dancing', ',', 'and', 'he', 'singing', '.']]
                           
left_out_predicate_labels = ['B-ARG0','O','B-ARG1','O','O','B-ARG0','B-ARG1','O']


left_out_theme_examples = [['John', 'enjoys', 'swimming', ',', 'and', 'so', 'does', 'his', 'brother', '.'],
                           ['I', 'love', 'coffee', ',', 'and', 'so', 'does', 'my', 'roommate', '.'],
                           ['He', 'speaks', 'French', ',', 'and', 'so', 'does', 'his', 'wife', '.'],
                           ['Jane', 'loves', 'books', ',', 'and', 'so', 'does', 'her', 'sister', '.'],
                           ['They', 'prefer', 'tea', ',', 'and', 'so', 'do', 'their', 'parents', '.'],
                           ['She', 'hates', 'cold', ',', 'and', 'so', 'does', 'her', 'boyfriend', '.'],
                           ['He', 'enjoys', 'games', ',', 'and', 'so', 'do', 'his', 'friends', '.'],           
                           ['She', 'loves', 'danceing', ',', 'and', 'so', 'does', 'her', 'daughter', '.'],
                           ['He', 'enjoys', 'hiking', ',', 'and', 'so', 'does', 'his', 'girlfriend', '.']]
    
left_out_theme_labels = ['B-ARG0','O','B-ARG1','O','O','O','O','B-ARG0','I-ARG0','O']


unmask = create_pipeline()

if __name__ == '__main__':
    ### Instrument+Theme:   
    print('Extending Instrument+Theme examples ...')
    # save unmodified examples in .json
    save_to_json(instrument_theme_examples, instrument_theme_labels, 'Data/Instrument+Theme.json')
    # mask the 3rd token, extend examples 
    instrument_theme_generated_examples = generate_examples(instrument_theme_generated_examples_first_iter, unmask, 2)
    # append new generated examples to .json 
    save_to_json(instrument_theme_generated_examples, instrument_theme_labels, 'Data/Instrument+Theme.json')
    # clean examples from the ones that duplicate human examples 
    instrument_theme_clean_examples = delete_duplicates('Data/Instrument+Theme.json')
    # delete the old .json file
    os.remove('Data/Instrument+Theme.json')
    # get clean .json file 
    save_to_json(instrument_theme_clean_examples, instrument_theme_labels, 'Data/Instrument+Theme.json')
    print('Instrument+Theme.json is saved')
                           
    ### Benefactive:
    print('Extending benefactive examples ...')
    save_to_json(benefactive_examples, benefactive_labels, 'Data/Benefactive.json')
    # mask the 2nd and 6th token
    benefactive_generated_examples_first_iter = generate_examples(benefactive_examples, unmask, 5)
    benefactive_generated_examples_second_iter = generate_examples(benefactive_generated_examples_first_iter, unmask, 1)
    save_to_json(benefactive_generated_examples_second_iter, benefactive_labels, 'Data/Benefactive.json')
    benefactive_clean_examples = delete_duplicates('Data/Benefactive.json')
    os.remove('Data/Benefactive.json')
    save_to_json(benefactive_clean_examples, benefactive_labels, 'Data/Benefactive.json')
    print('Benefactive.json is saved')
    
    ### Passive voice:
    print('Extending passive voice examples ...')
    save_to_json(passive_voice_examples, passive_voice_labels, 'Data/Passive voice.json')
    # mask the 2nd and 4th token
    passive_voice_generated_examples_first_iter = generate_examples(passive_voice_examples, unmask, 1)
    passive_voice_generated_examples_second_iter = generate_examples(passive_voice_generated_examples_first_iter, unmask, 3)
    save_to_json(passive_voice_generated_examples_second_iter, passive_voice_labels, 'Data/Passive voice.json')
    passive_voice_clean_examples = delete_duplicates('Data/Passive voice.json')
    os.remove('Data/Passive voice.json')
    save_to_json(passive_voice_clean_examples, passive_voice_labels, 'Data/Passive voice.json')
    print('Passive voice.json is saved')
    
    ### Left-out predicate:
    print('Extending left-out predicate examples ...')
    save_to_json(left_out_predicate_examples, left_out_predicate_labels, 'Data/Left-out predicate.json')
    # mask the 2nd token
    left_out_predicate_generated_examples = generate_examples(left_out_predicate_examples, unmask, 1)
    save_to_json(left_out_predicate_generated_examples, left_out_predicate_labels, 'Data/Left-out predicate.json')
    left_out_predicate_clean_examples = delete_duplicates('Data/Left-out predicate.json')
    os.remove('Data/Left-out predicate.json')
    save_to_json(left_out_verb_clean_examples, left_out_verb_labels, 'Data/Left-out predicate.json')
    print('Left-out predicate.json is saved')
    
    ### Left-out Theme:
    print('Extending left-out Theme examples ...')
    save_to_json(left_out_theme_examples, left_out_theme_labels, 'Data/Left-out Theme.json')
    # mask the 2nd and 3rd token
    left_out_theme_generated_examples_first_iter = generate_examples(left_out_theme_examples, unmask, 2)
    left_out_theme_generated_examples_second_iter = generate_examples(left_out_theme_generated_examples_first_iter, unmask, 1)
    save_to_json(left_out_theme_generated_examples_second_iter, left_out_theme_labels, 'Data/Left-out Theme.json')
    left_out_theme_clean_examples = delete_duplicates('Data/Left-out Theme.json')
    os.remove('Data/Left-out Theme.json')
    save_to_json(left_out_theme_clean_examples, left_out_theme_labels, 'Data/Left-out Theme.json')
    print('Left-out Theme.json is saved')
