# Take Home Exam
TM Natalia Khaidanova (2778662)

- save_munual_examples.py contains code for saving test instances defined in the file and their gold labels as .json files. The output is four .json test files: 
Caused-motion.json
Polysemy.json 
B-ARG0 idioms.json
B-ARG1 idioms.json
Note! The files are saved to the Data folder. So make sure you have it, otherwise you need to adapt the code. 

- extend_some_examples.py contains code for extending test instances defined in the file using Transformers fill-mask pipeline, and saving unique extended instances and their gold labels as .json files. The output is five .json test files: 
Instrument+Theme.json
Benefactive.json
Passive voice.json
Left-out predicate.json
Left-out Theme.json
Note! The files are saved to the Data folder. So make sure you have it, otherwise you need to adapt the code. 

- utils.py contains the code necessary to run save_munual_examples.py and extend_some_examples.py.

- test_models.py contains the code for evaluating the pretrained structured-prediction-srl-bert and structured-prediction-srl models on the defined .json test files. The output is the failure rate of each model for each .json test file, the number of fully correct predictions per .json test file. The test instances, gold labels, and predictions of each model are saved as new .json files. 
Note! The files are saved to the Output folder. So make sure you have it, otherwise you need to adapt the code. 
