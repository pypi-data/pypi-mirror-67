import numpy as np
import logging
import zipfile
import os
import shutil
from sentence_transformers import SentenceTransformer, LoggingHandler
from sys import exit

class TrainSentences:

    def __init__(self, txt_file):
        dir_path = os.getcwd() + '/'
        file_path = dir_path + txt_file
        print('\n')
        print('Scanning the path '+file_path+ ' ...')
        self.predtrained_model = 'bert-base-nli-mean-tokens'
        print('Pretrained model is set to '+self.predtrained_model+ ' ...')
        if(os.path.isfile(file_path) and self.get_file_extension(file_path) == ".txt"):
            print('Training file validation OK...')
            self.train_file_path = file_path
            if not os.path.exists(dir_path+'trained_model'):
                os.makedirs(dir_path+'trained_model')
            self.model_save_path = dir_path+'trained_model/'
            self.zip_save_path = dir_path+'/'
        else:
            exit('Training file is not valid... exiting...')
    
    def pretrained_model(self,model_name)
        self.predtrained_model = model_name
        print('Pretrained model is reset to '+model_name+ ' ...')

    def get_file_extension(self,src):
        return os.path.splitext(src)[-1].lower()

    def get_path(self):
        _vector_file = 'vector.npy'
        _train_file = 'train.txt'
        _files = {
            'model': self.model_save_path,
            'vector': self.model_save_path + _vector_file,
            'training_set': self.train_file_path,
            'zip_path' : self.zip_save_path+'model.zip',
            'train_file' : self.model_save_path + _train_file,
        }
        return _files

    def train(self):
        path = self.get_path()
        np.set_printoptions(threshold=100)
        logging.basicConfig(format='%(asctime)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            level=logging.ERROR,
                            handlers=[LoggingHandler()])
        model = SentenceTransformer(self.predtrained_model)
        sentences = open(path.get('training_set')).read().splitlines()
        sentence_embeddings = model.encode(sentences)
        vecs = np.stack(sentence_embeddings)
        model.save(path.get('model'))
        print('Saving the model to '+path.get('model')+'...')
        np.save(path.get('vector'), sentence_embeddings)
        print('Saving the vector to '+path.get('vector')+'...')
        print('Initiating model compression(.zip) ...')
        os.rename(path.get('training_set'), path.get('train_file'))
        self.compress_file(path.get('model'),path.get('zip_path'))
        print('→ Download "model.zip" and use it for prediction ...')
       
    def compress_file(self,dirpath, zippath):
        fzip = zipfile.ZipFile(zippath, 'w', zipfile.ZIP_DEFLATED)
        basedir = os.path.dirname(dirpath) + '/' 
        for root, dirs, files in os.walk(dirpath):
            dirname = root.replace(basedir, '')
            for f in files:
                fzip.write(root + '/' + f, dirname + '/' + f)
        fzip.close()
        shutil.rmtree(self.model_save_path)