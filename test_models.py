from allennlp.predictors.predictor import Predictor
import allennlp_models.tagging
import os
import json


allenbert = Predictor.from_path('https://storage.googleapis.com/allennlp-public-models/structured-prediction-srl-bert.2020.12.15.tar.gz')
allenbilstm = Predictor.from_path('https://storage.googleapis.com/allennlp-public-models/openie-model.2020.03.26.tar.gz')
  
  
def clean_pred_labels(gold, pred):
    """
    Get rid of unnecessary labels.
    
    :param list gold: gold labels for one example
    :param list pred: predicted labels for one example
    :return list: clean predicted labels for one example 
    """
    
    pred_clean = []
    for i in range(len(gold)):
        if gold[i] == 'O' and pred[i][2:5] != 'ARG':
            pred_clean.append('O')
        else:
            pred_clean.append(pred[i])

    return pred_clean


def save_pred_to_json(example, gold, allenbert_pred, allenbilastm_pred, outputfile):
    """
    Save examples and gold labels in .json.
    
    :param list examples: lists of example tokens
    :param list gold: gold labels for one example 
    :param list allenbert_pred: allenBERT predictions for one example 
    :param list allenbert_pred: allenBiLSTM predictions for one example 
    :param str outputfile: path to output .json file
    :return: None
    """
    output_dict = {'example':example,                
                   'BIO':gold, 
                   'allenBERT_pred':allenbert_pred,
                   'allenBiLSTM_pred':allenbilastm_pred}
    with open(outputfile, 'a') as outfile:
        json.dump(output_dict, outfile)
        outfile.write('\n')
  
  
def get_nr_errors(y_test, y_pred):
    """
    :param list y_test: gold labels for one file
    :param list y_pred: predicted labels for one file
    :return int: number of incorrect predictions  
    """
    errors = []
    for gold, pred in zip(y_test, y_pred):
        if gold != pred:
            errors.append(pred)
            
    return len(errors)
  
  
def test_models(path, allenbert, allenbilstm):
    """
    Test allenBERT, allenBiLSTM pretrained models on .json test files,
    get error rate and number of fully correct predictions for each model for each test file,
    save example, gold labels, all models' predictions as .json for each test file.
  
    :param str path: directory to the folder with .json test files 
    :param allenbert: pretrained structured-prediction-srl-bert model
    :param allenbert: pretrained structured-prediction-srl model
    :return: None
    """
    for filename in os.listdir(path):
        if filename.endswith('.json'):
        
            y_test, allenbert_y_pred, allenbilstm_y_pred, allenbert_correct, allenbilstm_correct = [], [], [], [], []
                
            with open(f'{path}/{filename}') as infile:
                for line in infile.readlines():
                    line = line.strip('\n')
                    example_info = json.loads(line)       
                    gold = example_info['BIO']
                    for label in gold:
                        y_test.append(label)

                    # allenBERT and allenBiLSTM  
                    example = example_info['example']
                    example_untokenized = ' '.join(example[:-1]) + example[-1]
                    try:
                        allenbert_pred = allenbert.predict(example_untokenized)['verbs'][0]['tags']
                        allenbilstm_pred = allenbilstm.predict(example_untokenized)['verbs'][0]['tags']
                    except IndexError:
                        allenbert_pred = ['O'] * len(gold)
                        allenbilstm_pred = ['O'] * len(gold)

                    allenbert_pred = clean_pred_labels(gold, allenbert_pred)  
                    if allenbert_pred == gold:
                        allenbert_correct.append(allenbert_pred)
                        
                    allenbilstm_pred = clean_pred_labels(gold, allenbilstm_pred) 
                    if allenbilstm_pred == gold:
                        allenbilstm_correct.append(allenbilstm_pred)

                    for allenbert_label, allenbilstm_label in zip(allenbert_pred, allenbilstm_pred):
                        allenbert_y_pred.append(allenbert_label)
                        allenbilstm_y_pred.append(allenbilstm_label)

                    save_pred_to_json(example, gold, allenbert_pred, allenbilstm_pred, f'Output/pred_{filename}')

            allenbert_errors = get_nr_errors(y_test, allenbert_y_pred)
            allenbilstm_errors = get_nr_errors(y_test, allenbilstm_y_pred)

            print(f'allenBERT failure rate for {filename}: {round(((allenbert_errors/len(y_test))*100), 1)}')
            print(f'Number of allenBERT fully correct predictions for {filename}: {len(allenbert_correct)}')
            print(f'allenBiLSTM failure rate for {filename}: {round(((allenbilstm_errors/len(y_test))*100), 1)}')
            print(f'Number of allenBiLSTM fully correct predictions for {filename}: {len(allenbilstm_correct)}')
            print('-----------------------------')

        
if __name__ == '__main__':
    test_models(r'Data', allenbert, allenbilstm)
