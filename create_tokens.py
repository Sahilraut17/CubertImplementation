import python_tokenizer
import unified_tokenizer
import os


data_folder = "/common/home/rru9/Desktop/NeuralCodeSum/data/python/"

for root, subdirs, files in os.walk(data_folder):
    for subdir in subdirs:
        code_file = open(data_folder+subdir+'//code.original', 'r')
        lines = code_file.readlines()
        subtokens = []
        tokenizer = python_tokenizer.PythonTokenizer()

        for line in lines:
            subtokens.append(" ".join(tokenizer.tokenize(line))+"\n")

        code_subtokens = open(data_folder+subdir+'//code.original_subtoken', 'w')
        code_subtokens.writelines(subtokens)
        code_subtokens.close()