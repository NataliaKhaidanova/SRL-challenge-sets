from nltk.tokenize import word_tokenize
from transformers import pipeline
import json

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

def generate_examples(examples):
    """
    Extend examples using transformers fill-mask pipeline.
    
    :param list examples: lists of example tokens
    :return: extended list of examples
    """
    print('Creating pipeline ...')
    unmask = pipeline('fill-mask')
    unmask.tokenizer.mask_token
    print('Pipeline created.')
    
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

def save_to_json(examples, labels):
    """
    Save examples and gold labels in .json:
    
    :param list extended_examples: extended list of examples (output of extend_examples)
    :param list labels: gold labels 
    :return: None
    """
    for i in range(len(examples)):
        output_dict = {'example': examples[i], 'BIO': labels}
        with open('Caused_motion.json', 'a') as outfile:
            json.dump(output_dict, outfile)
            outfile.write('\n')

if __name__ == '__main__':
    # save unmodified examples
    save_to_json(examples, labels)
    generated_examples = generate_examples(examples)
    # append new generated examples
    save_to_json(generated_examples, labels)
