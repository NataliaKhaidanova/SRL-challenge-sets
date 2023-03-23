from nltk.tokenize import word_tokenize
import os
from utils import *


examples = [['She', 'lent', 'her', 'friend', 'a', 'book', '.'],
            ['He', 'showed', 'his', 'wife', 'a', 'sunset', '.'],
            ['She', 'sent', 'her', 'mother', 'a', 'bouquet', '.'],
            ['She', 'cooked', 'her', 'grandmother', 'a', 'meal', '.'],
            ['He', 'gave', 'his', 'boss', 'a', 'gift', '.'],
            ['I', 'wrote', 'my', 'niece', 'a', 'letter', '.'],
            ['John', 'bought', 'his', 'girlfriend', 'a', 'necklace', '.'],
            ['Mary', 'emailed', 'her', 'boss', 'a', 'note', '.'],
            ['They', 'offered', 'their', 'guests', 'a', 'snack', '.']]

labels = ['B-ARG0','O','O','B-ARG2','O','B-ARG1','O']


unmask = create_pipeline()

def generate_examples(examples):
    """
    Extend examples using transformers fill-mask pipeline.
    
    :param list examples: lists of example tokens
    :return: extended list of examples
    """ 
    generated_examples_first_iter, generated_examples_second_iter = [], []
    
    ### transformers do not support masking two tokens at ones
    ### for this reason we perform masking in two iterations  
    # mask the forth word
    print('Performing the first iteration ...')
    for example in examples:
        example[3] = '<mask>'
        example = ' '.join(example[:-1]) + example[-1]
        predictions = unmask(example)
        # get new examples
        for prediction in predictions:
            prediction = prediction['sequence'].strip('<s>').strip('</s>')
            prediction = word_tokenize(prediction)         
            if prediction not in generated_examples_first_iter:
                generated_examples_first_iter.append(prediction)
                
    print('Performing the second iteration ...')            
    # mask the sixth word
    for example in generated_examples_first_iter:
        example[5] = '<mask>'
        example = ' '.join(example[:-1]) + example[-1]      
        predictions = unmask(example)
        for prediction in predictions:
            prediction = prediction['sequence'].strip('<s>').strip('</s>')
            prediction = word_tokenize(prediction)            
            if prediction not in generated_examples_second_iter:
                generated_examples_second_iter.append(prediction)
    
    return generated_examples_second_iter
            

if __name__ == '__main__':
    # save unmodified examples
    save_to_json(examples, labels)
    generated_examples = generate_examples(examples)
    # append new generated examples
    save_to_json(generated_examples, labels)
    clean_examples = delete_duplicates('Benefactive.json')
    # delete the old file
    os.remove('Benefactive.json')
    # get clean file 
    save_to_json(clean_examples, labels)
