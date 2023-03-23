from nltk.tokenize import word_tokenize
import os
from utils import *

examples = [['The','window','broke','.'],
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

labels = ['O','B-ARG1','O','O']


unmask = create_pipeline()

def generate_examples(examples):
    """
    Extend examples using transformers fill-mask pipeline.
    
    :param list examples: lists of example tokens
    :return: extended list of examples
    """    
    generated_examples = []
    
    for example in examples:
        # mask the second word
        example[1] = '<mask>'
        example = ' '.join(example[:-1]) + example[-1]
        predictions = unmask(example)
        # get new examples
        for prediction in predictions:
            prediction = prediction['sequence'].strip('<s>').strip('</s>')
            prediction = word_tokenize(prediction)
            if prediction not in generated_examples:
                generated_examples.append(prediction)
    
    return generated_examples


if __name__ == '__main__':
    # save unmodified examples
    save_to_json(examples, labels, 'Caused-motion.json')
    generated_examples = generate_examples(examples)
    # append new generated examples
    save_to_json(generated_examples, labels, 'Caused-motion.json')
    clean_examples = delete_duplicates('Caused-motion.json')
    # delete the old file
    os.remove('Caused-motion.json')
    # get clean file 
    save_to_json(clean_examples, labels, 'Caused-motion.json')
    print('The file is saved.')
