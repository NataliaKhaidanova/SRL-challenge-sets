from transformers import pipeline
import json


def create_pipeline():
    """
    Create transformers fill-mask pipeline.
    :return: unmask
    """
    print('Creating pipeline ...')
    unmask = pipeline('fill-mask')
    unmask.tokenizer.mask_token
    print('Pipeline created.')
    
    return unmask


def save_to_json(examples, labels):
    """
    Save examples and gold labels in .json.
    
    :param list examples: lists of example tokens
    :param list labels: gold labels 
    :return: None
    """
    for i in range(len(examples)):
        output_dict = {'example': examples[i], 'BIO': labels}
        with open('Benefactive.json', 'a') as outfile:
            json.dump(output_dict, outfile)
            outfile.write('\n')
            
            
def delete_duplicates(json_file):
    """
    Read in .json, get none-duplicating examples 
    
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
