# Take Home Exam
TM Natalia Khaidanova (2778662)

- save_munual_examples.py contains code for saving test instances defined in the file and their gold labels as .json files. The output is four .json test files: 
Caused-motion.json,
Polysemy.json, 
B-ARG0 idioms.json, and
B-ARG1 idioms.json.
Note! The files are saved to the Data folder. So make sure you have it, otherwise you need to adapt the code. 

- extend_some_examples.py contains code for extending test instances defined in the file using Transformers fill-mask pipeline, and saving unique extended instances and their gold labels as .json files. The output is five .json test files: 
Instrument+Theme.json,
Benefactive.json,
Passive voice.json,
Left-out predicate.json, and
Left-out Theme.json.
Note! The files are saved to the Data folder. So make sure you have it, otherwise you need to adapt the code. 

- utils.py contains the code necessary to run save_munual_examples.py and extend_some_examples.py.

- test_models.py contains the code for evaluating the pretrained structured-prediction-srl-bert and structured-prediction-srl models on the defined .json test files. The output is the failure rate of each model for each .json test file, the number of fully correct predictions per .json test file. The test instances, gold labels, and predictions of each model are saved as new .json files. 
Note! The files are saved to the Output folder. So make sure you have it, otherwise you need to adapt the code. 

- Data folder contains .json test files that are outputs of the code defined in save_munual_examples.py and extend_some_examples.py. 

- Output folder contains .json test files with the predictions of the pretrained structured-prediction-srl-bert and structured-prediction-srl models.

If you want to replicate the results, run test_models.py. 

If you want to test the code, delete all files in the Data and Output folders, then run save_munual_examples.py, extend_some_examples.py, and test_models.py in the specified order. Note! The results will not to replicated as some .json test files in the Data folder were manually reduced before running test_models.py.  
