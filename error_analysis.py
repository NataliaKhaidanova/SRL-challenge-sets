import json
import os


def get_correct_predictions(path):
    """
    Print name of .json test file, example of gold labels, all correctly resolved examples for each model. 

    :param str path: directory to the folder with .json test files with models' predictions
    :return: None
    """
    for filename in os.listdir(path):
        if filename.endswith('.json'):

            y_test, allenbert_correct, allenbilstm_correct = [], [], []

            print(filename)

            with open(f'{path}/{filename}') as infile:
                for line in infile.readlines():
                    line = line.strip('\n')
                    example_info = json.loads(line) 
                    example = example_info['example']
                    example = ' '.join(example[:-1]) + example[-1]
                    gold = example_info['BIO']
                    y_test.append(gold)
                    allenbert_pred = example_info['allenBERT_pred']
                    allenbilstm_pred = example_info['allenBiLSTM_pred']
                    if allenbert_pred == gold:
                        allenbert_correct.append(example)
                    if allenbilstm_pred == gold:
                        allenbilstm_correct.append(example)

            print(f'gold: {y_test[0]}')
            print(f'''allenBERT correct: 
    {allenbert_correct}''')
            print('-----------------------------')
            print(f'''allenBiLSTM correct: 
    {allenbilstm_correct}''')
            print('=============================')


def get_mistakes_in_Benefactive(path):
    """
    Print all incorrectly resolved examples and predictions for each model for Benefactive.

    :param str path: directory to the folder with .json test files with models' predictions
    :return: None
    """

    for filename in os.listdir(path):
        if filename == 'pred_Benefactive.json':

            allenbert_examples, allenbert_incorrect_pred, allenbilstm_examples, allenbilstm_incorrect_pred = [], [], [], []

            with open(f'{path}/{filename}') as infile:
                for line in infile.readlines():
                    line = line.strip('\n')
                    example_info = json.loads(line) 
                    example = example_info['example']
                    example = ' '.join(example[:-1]) + example[-1]
                    gold = example_info['BIO']
                    allenbert_pred = example_info['allenBERT_pred']
                    allenbilstm_pred = example_info['allenBiLSTM_pred']

                    if allenbert_pred != gold:
                        allenbert_examples.append(example)
                        allenbert_incorrect_pred.append(allenbert_pred)
                    if allenbilstm_pred != gold:
                        allenbilstm_examples.append(example)
                        allenbilstm_incorrect_pred.append(allenbilstm_pred)

            print(f'allenBERT mistakes in {filename}:')
            for example, pred in zip(allenbert_examples, allenbert_incorrect_pred):
                print(example) 
                print(pred)
                print('-----------------------------')
            print('=============================')
            print(f'allenBiLSTM mistakes in {filename}:')
            for example, pred in zip(allenbilstm_examples, allenbilstm_incorrect_pred):
                print(example) 
                print(pred)
                print('-----------------------------') 
                
                
def get_mistakes_in_Passive_voice(path):
    """
    Print all incorrectly resolved examples and predictions for each model for Passive voice.

    :param str path: directory to the folder with .json test files with models' predictions
    :return: None
    """
    for filename in os.listdir(path):
      if filename == 'pred_Passive voice.json':

          allenbert_examples, allenbert_preds, allenbilstm_examples, allenbilstm_preds = [], [], [], []
          with open(f'{path}/{filename}') as infile:
              for line in infile.readlines():
                  line = line.strip('\n')
                  example_info = json.loads(line) 
                  example = example_info['example']
                  example = ' '.join(example[:-1]) + example[-1]
                  gold = example_info['BIO']
                  allenbert_pred = example_info['allenBERT_pred']
                  allenbilstm_pred = example_info['allenBiLSTM_pred']

                  if allenbert_pred != ["O", "O", "O", "O", "O", "O", "O", "O"]:
                      allenbert_examples.append(example)
                      allenbert_preds.append(allenbert_pred)
                  if allenbilstm_pred != ["O", "O", "O", "O", "O", "O", "O", "O"]:
                      allenbilstm_examples.append(example)
                      allenbilstm_preds.append(allenbilstm_pred)

          print(f'allenBERT nonzero predictions for {filename}:')            
          for example, pred in zip(allenbert_examples, allenbert_preds):
              print(example) 
              print(pred)
              print('-----------------------------')
          print('=============================')
          print(f'allenBiLSTM nonzero predictions for {filename}:')   
          for example, pred in zip(allenbilstm_examples, allenbilstm_preds):
              print(example) 
              print(pred)
              print('-----------------------------')  
              
              
 if __name__ == '__main__':
    path = r'Output'
    get_correct_predictions(path)
    print('=============================')
    print('=============================')
    print('=============================')
    get_mistakes_in_Benefactive(path)
    print('=============================')
    print('=============================')
    print('=============================')
    get_mistakes_in_Passive_voice(path)
