from allennlp.predictors.predictor import Predictor
import allennlp_models.tagging
import os
import json


allenbert = Predictor.from_path('https://storage.googleapis.com/allennlp-public-models/structured-prediction-srl-bert.2020.12.15.tar.gz')
allenbilstm = Predictor.from_path('https://storage.googleapis.com/allennlp-public-models/openie-model.2020.03.26.tar.gz')


def clean_gold_labels(filename, gold):
    """
    Adapt gold labels for allenBERT and allenBiLSTM.
    
    :param str filename: name of .json file
    :param list gold: gold labels for one example
    :return: list of atapted gold labels for one example 
    """
    for index, label in enumerate(gold):
        if filename not in ['Left-out Theme.json', 'Left-out predicate.json']:
            if label == 'B-ARG0' and gold[index-1] != 'and' and index != 0:
                gold[index-1] = 'B-ARG0'
                gold[index] = 'I-ARG0'
            if label == 'B-ARG1' and index != 0:
                gold[index-1] = f'B-ARG{label[-1]}'
                gold[index] = f'I-ARG{label[-1]}'
        
        if filename == 'Left-out Theme.json':
            if label == 'B-ARG0' and index != 0:
                gold[index-1] = 'B-ARG0'
                gold[index] = 'I-ARG0'
                    
    return gold
  
  
def clean_pred_labels(gold, pred):
    """
    Get rid of unnecessary labels.
    
    :param list gold: gold labels for one example
    :param list pred: predicted labels for one example
    :return: list of atapted predicted labels for one example 
    """
    
    pred_clean = []
    for i in range(len(gold)):
        if gold[i] == 'O' and pred[i][2:5] != 'ARG':
            pred_clean.append('O')
        else:
            pred_clean.append(pred[i])

    return pred_clean
  
  
def get_nr_errors(y_test, y_pred):
    """
    :param list y_test: gold labels for one file
    :param list y_pred: predicted labels for one file
    :return: number of incorrect predictions  
    """
    errors = []
    for gold, pred in zip(y_test, y_pred):
        if gold != pred:
            errors.append(pred)
            
    return len(errors)
  
  
def test_models(path, allenbert, allenbilstm):
  """
  Test allenBERT, allenBiLSTM pretrained models on .json test files,
  get error rate for each model for each test file,
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
                # get gold labels 
                gold = example_info['BIO']
                gold = clean_gold_labels(filename, gold) 
                for label in gold:
                    y_test.append(label)
                    
                # allenBERT and allenBiLSTM  
                example = example_info['example']
                example = ' '.join(example[:-1]) + example[-1]
                try:
                    allenbert_pred = allenbert.predict(example)['verbs'][0]['tags']
                    if allenbert_pred == gold:
                        allenbert_correct.append(allenbert_pred)
                    allenbilstm_pred = allenbilstm.predict(example)['verbs'][0]['tags']
                    if allenbilstm_pred == gold:
                        allenbilstm_correct.append(allenbilstm_pred)
                except IndexError:
                    allenbert_pred = ['O'] * len(gold)
                    allenbilstm_pred = ['O'] * len(gold)
                
                allenbert_pred = clean_pred_labels(gold, allenbert_pred)  
                allenbilstm_pred = clean_pred_labels(gold, allenbilstm_pred) 
        
                for allenbert_label, allenbilstm_label in zip(allenbert_pred, allenbilstm_pred):
                    allenbert_y_pred.append(allenbert_label)
                    allenbilstm_y_pred.append(allenbilstm_label)
                    
                #save_pred_to_json(example, gold, pred, f'pred_{file}')
    
        allenbert_errors = get_nr_errors(y_test, allenbert_y_pred)
        allenbilstm_errors = get_nr_errors(y_test, allenbilstm_y_pred)

        print(f'allenBERT error rate for {filename}: {round(((allenbert_errors/len(y_test))*100), 1)}')
        print(f'Number of allenBERT correct predictions for {filename}: {len(allenbert_correct)}')
        print(f'allenBiLSTM error rate for {filename}: {round(((allenbilstm_errors/len(y_test))*100), 1)}')
        print(f'Number of allenBiLSTM correct predictions for {filename}: {len(allenbilstm_correct)}')
        print('-----------------------------')

        
 if __name__ == '__main__':
    test_models(r'Data', allenbert, allenbilstm)
