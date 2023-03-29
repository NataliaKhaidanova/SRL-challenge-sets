import json

caused_motion_examples = [['The', 'window', 'broke', '.'],
                          ['The', 'vase', 'shattered', '.'],
                          ['The', 'balloon', 'burst', '.'],
                          ['The', 'door', 'opened', '.'],
                          ['The','car','stopped', '.'],
                          ['The', 'glass', 'cracked', '.'],
                          ['The', 'bridge', 'collapsed', '.'],
                          ['The', 'boat', 'sank', '.'],
                          ['The', 'computer', 'crashed', '.'],
                          ['The', 'ice', 'melted', '.'],
                          ['The', 'knife', 'dropped', '.'],
                          ['The', 'airplane', 'crashed', '.'],
                          ['The', 'rock', 'rolled', '.'],
                          ['The', 'oil', 'spilled', '.'],
                          ['The', 'satellite', 'launched', '.'],
                          ['The', 'skateboard', 'rolled', '.'],
                          ['The', 'spaceship', 'landed', '.']]

caused_motion_labels = ['B-ARG1','I-ARG1','O','O']


polysemy_examples = [['I', 'saw', 'a', 'kid', 'with', 'a', 'cat', '.'],
                     ['He', 'saw', 'a', 'man', 'with', 'binoculars', '.']]             
                                         
polysemy_labels = [['B-ARG0', 'O', 'B-ARG1', 'I-ARG1', 'I-ARG1', 'I-ARG1', 'I-ARG1', 'O'],
                   ['B-ARG0', 'O', 'B-ARG1', 'I-ARG1', 'O', 'B-ARG2', 'O']]


idioms_examples = [['She', 'kicked', 'the', 'bucket', '.'], # to die 1
                   ['He', 'breathed', 'his', 'last', '.'], # to die 2
                   ['John', 'bit', 'the', 'dust', '.'], # to fail 3
                   ['She', 'popped', 'her', 'clogs', '.'], # to die 4
                   ['He', 'gave', 'the', 'slip', '.'], # to escape 5
                   ['Mary', 'spilled', 'the', 'beans', '.'], # to reveal a secret 6
                   ['They', 'broke', 'the', 'ice', '.'], # to ease tension in a social situation 7
                   ['He', 'hit', 'the', 'books', '.'], # to study 8
                   ['I', 'popped', 'the', 'question', '.'], # to propose marriage 9
                   ['They', 'spilled', 'their', 'guts', '.'], # to confess 10
                   ['They', 'pulled', 'the', 'plug', '.'], # to prevent something from happening 11
                   ['We', 'hit', 'the', 'jackpot', '.'], # to achieve great success 12
                   ['Michael', 'gave', 'a', 'start', '.'], # to jump from surprise 13
                   ['He', 'blew', 'his', 'top', '.'], # to become very angry 14
                   ['She', 'burned', 'her', 'bridges', '.'], # to continue 15
                   ['He', 'bit', 'the', 'bullet', '.'], # to endure something unpleasant or difficult 16
                   ['You', 'crossed', 'the', 'line', '.'], # to misbehave 17
                   ['Bill', 'pushed', 'the', 'envelope', '.'], # to extend the limits of what is possible 18 
                   ['They', 'rocked', 'the', 'boat', '.'], # to cause trouble 19
                   ['She', 'stirred', 'the', 'pot', '.'], # to cause trouble 20
                   ['You', 'saved', 'the', 'day', '.'], # to rescue a situation 21
                   ['Kate', 'stole', 'the', 'show', '.'], # to attract the most attention 22
                   ['He', 'took', 'the', 'plunge', '.'], # to take a risk 23
                   ['Scott', 'caught', 'his', 'breath', '.'], # to stop breathing for a moment 24
                   ['They', 'cracked', 'the', 'problem', '.'], # to solve the problem 25
                   ['She', 'made', 'her', 'mark', '.'], # to attain recognition or distinction 26 
                   ['You', 'missed', 'the', 'boat', '.'], # to be too slow to take advantage of an opportunity 27
                   ['I', 'paid', 'my', 'duties', '.'], # to fulfill one's obligations 28
                   ['He', 'struck', 'a', 'chord', '.'], # to cause someone to feel sympathy 29 
                   ['Emma', 'turned', 'the', 'tables', '.'], # reverse one's position relative to someone else 30
                   ['She', 'took', 'a', 'backseat', '.'], # be given a less important position or role 31
                   ['He', 'bared', 'his', 'soul', '.']] # to reveal one's most private thoughts 32
                   
idioms_labels = [['B-ARG1', 'O', 'O', 'O', 'O'], # 1
                 ['B-ARG1', 'O', 'O', 'O', 'O'], # 2
                 ['B-ARG1', 'O', 'O', 'O', 'O'], # 3
                 ['B-ARG1', 'O', 'O', 'O', 'O'], # 4
                 ['B-ARG0', 'O', 'O', 'O', 'O'], # 5
                 ['B-ARG0', 'O', 'O', 'O', 'O'], # 6
                 ['B-ARG0', 'O', 'O', 'O', 'O'], # 7
                 ['B-ARG0', 'O', 'O', 'O', 'O'], # 8
                 ['B-ARG0', 'O', 'O', 'O', 'O'], # 9
                 ['B-ARG0', 'O', 'O', 'O', 'O'], # 10
                 ['B-ARG0', 'O', 'O', 'O', 'O'], # 11
                 ['B-ARG0', 'O', 'O', 'O', 'O'], # 12
                 ['B-ARG1', 'O', 'O', 'O', 'O'], # 13
                 ['B-ARG1', 'O', 'O', 'O', 'O'], # 14
                 ['B-ARG0', 'O', 'O', 'O', 'O'], # 15
                 ['B-ARG1', 'O', 'O', 'O', 'O'], # 16
                 ['B-ARG0', 'O', 'O', 'O', 'O'], # 17
                 ['B-ARG0', 'O', 'O', 'O', 'O'], # 18
                 ['B-ARG0', 'O', 'O', 'O', 'O'], # 19
                 ['B-ARG0', 'O', 'O', 'O', 'O'], # 20
                 ['B-ARG0', 'O', 'O', 'O', 'O'], # 21
                 ['B-ARG0', 'O', 'O', 'O', 'O'], # 22
                 ['B-ARG0', 'O', 'O', 'O', 'O'], # 23
                 ['B-ARG0', 'O', 'O', 'O', 'O'], # 24
                 ['B-ARG0', 'O', 'O', 'O', 'O'], # 25
                 ['B-ARG0', 'O', 'O', 'O', 'O'], # 26
                 ['B-ARG1', 'O', 'O', 'O', 'O'], # 27
                 ['B-ARG0', 'O', 'O', 'O', 'O'], # 28
                 ['B-ARG0', 'O', 'O', 'O', 'O'], # 29
                 ['B-ARG0', 'O', 'O', 'O', 'O'], # 30
                 ['B-ARG1', 'O', 'O', 'O', 'O'], # 31
                 ['B-ARG0', 'O', 'O', 'O', 'O']] # 32
                     
                     
if __name__ == '__main__':
    # Save caused-motion examples
    for i in range(len(caused_motion_examples)):
        caused_motion_output_dict = {'example': caused_motion_examples[i], 'BIO': caused_motion_labels}
        with open('Data/Caused-motion.json', 'a') as outfile:
            json.dump(caused_motion_output_dict, outfile)
            outfile.write('\n')
    print('Caused-motion.json is saved')
    # Save polysemy examples
    for i in range(len(polysemy_examples)):
        polysemy_output_dict = {'example': polysemy_examples[i], 'BIO': polysemy_labels[i]}
        with open('Data/Polysemy.json', 'a') as outfile:
            json.dump(polysemy_output_dict, outfile)
            outfile.write('\n')
    print('Polysemy.json is saved')
    # Save idioms 
    for i in range(len(idioms_examples)):
        # Save ARG0 idioms 
        if idioms_labels[i][0] == 'B-ARG0':
            ARG0_output_dict = {'example': idioms_examples[i], 'BIO': idioms_labels[i]}
            with open('Data/ARG0 idioms.json', 'a') as outfile:
                json.dump(ARG0_output_dict, outfile)
                outfile.write('\n')
        print('B-ARG0 idioms.json is saved')
        # Save ARG1 idioms 
        else:
            ARG1_output_dict = {'example': idioms_examples[i], 'BIO': idioms_labels[i]}
            with open('Data/ARG1 idioms.json', 'a') as outfile:
                json.dump(ARG1_output_dict, outfile)
                outfile.write('\n')
        print('B-ARG1 idioms.json is saved')
