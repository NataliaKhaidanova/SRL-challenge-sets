from transformers import pipeline
from nltk.tokenize import word_tokenize
import json


def create_pipeline():
    """
    Create transformers fill-mask pipeline.
    :return: transformers.pipelines.fill_mask.FillMaskPipeline
    """
    print('Creating pipeline ...')
    unmask = pipeline('fill-mask')
    unmask.tokenizer.mask_token
    
    return unmask
    
    
def generate_examples(examples, unmask, mask_index):
    """
    Extend examples using transformers fill-mask pipeline.

    :param list examples: lists of example tokens
    :param transformers.pipelines.fill_mask.FillMaskPipeline unmask: transformers fill-mask pipeline
    :param int mask_index: index of the token to mask
    :return: extended list of examples
    """
    generated_examples = []

    for example in examples:
        # mask n token
        example[mask_index] = '<mask>'
        example = ' '.join(example[:-1]) + example[-1]
        predictions = unmask(example)
        # get new examples
        for prediction in predictions:
            prediction = prediction['sequence'].strip('<s>').strip('</s>')
            prediction = word_tokenize(prediction)
            if prediction not in generated_examples:
                generated_examples.append(prediction)
                
    return generated_examples


def save_to_json(examples, labels, outputfile):
    """
    Save examples and gold labels in .json.
    
    :param list examples: lists of example tokens
    :param list labels: gold labels 
    :param str outputfile: path to output .json file
    :return: None
    """
    for i in range(len(examples)):
        output_dict = {'example': examples[i], 'BIO': labels}
        with open(outputfile, 'a') as outfile:
            json.dump(output_dict, outfile)
            outfile.write('\n')
            
            
def delete_duplicates(json_file):
    """
    Read in .json, get none-duplicating examples.
    
    :param str json_file: path to .json file
    :return: a list with none-duplicating examples
    """
    all_examples, clean_examples = [], []
    
    with open(json_file) as infile:
        for line in infile.readlines():
            line = line.strip('\n')
            example_information = json.loads(line)
            example = example_information['example']
            all_examples.append(example)
            
    for example in all_examples:
        if example not in clean_examples:
            clean_examples.append(example)
            
    return clean_examples  
