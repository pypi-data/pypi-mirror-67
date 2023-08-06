import os
import numpy as np
import argparse
import librosa
import matplotlib.pyplot as plt
import torch
from pathlib import Path

from .pytorch_utils import move_data_to_device
from .models import Cnn14, Cnn14_DecisionLevelMax
from .config import labels, classes_num


def create_folder(fd):
    if not os.path.exists(fd):
        os.makedirs(fd)
        
        
def get_filename(path):
    path = os.path.realpath(path)
    na_ext = path.split('/')[-1]
    na = os.path.splitext(na_ext)[0]
    return na


class AudioTagging(object):
    def __init__(self, model_type='Cnn14', device='cuda', checkpoint_path=None):
        """Audio tagging inference wrapper.
        """
        if not checkpoint_path:
            checkpoint_path='{}/panns_data/Cnn14_mAP=0.431.pth'.format(str(Path.home()))
        print('Checkpoint path: {}'.format(checkpoint_path))

        if not os.path.exists(checkpoint_path):
            create_folder(os.path.dirname(checkpoint_path))
            os.system('wget -O "{}" https://zenodo.org/record/3576403/files/Cnn14_mAP%3D0.431.pth?download=1'.format(checkpoint_path))

        if device == 'cuda' and torch.cuda.is_available():
            self.device = 'cuda'
        else:
            self.device = 'cpu'
        
        self.labels = labels
        self.classes_num = classes_num

        # Model
        Model = eval(model_type)
        self.model = Model(sample_rate=32000, window_size=1024, 
            hop_size=320, mel_bins=64, fmin=50, fmax=14000, 
            classes_num=self.classes_num)

        checkpoint = torch.load(checkpoint_path, map_location=self.device)
        self.model.load_state_dict(checkpoint['model'])

        # Parallel
        print('GPU number: {}'.format(torch.cuda.device_count()))
        self.model = torch.nn.DataParallel(self.model)

        if 'cuda' in str(self.device):
            self.model.to(self.device)

    def inference(self, audio):
        audio = move_data_to_device(audio, self.device)

        with torch.no_grad():
            self.model.eval()
            output_dict = self.model(audio, None)

        clipwise_output = output_dict['clipwise_output'].data.cpu().numpy()
        embedding = output_dict['embedding'].data.cpu().numpy()

        return clipwise_output, embedding


class SoundEventDetection(object):
    def __init__(self, model_type='Cnn14_DecisionLevelMax', device='cuda', checkpoint_path=None):
        """Sound event detection inference wrapper.
        """
        if not checkpoint_path:
            checkpoint_path='{}/panns_data/Cnn14_DecisionLevelMax'.format(str(Path.home()))
        print('Checkpoint path: {}'.format(checkpoint_path))

        if not os.path.exists(checkpoint_path):
            create_folder(os.path.dirname(checkpoint_path))
            os.system('wget -O "{}" https://zenodo.org/record/3576403/files/Cnn14_DecisionLevelMax_mAP%3D0.385.pth?download=1'.format(checkpoint_path))

        if device == 'cuda' and torch.cuda.is_available():
            self.device = 'cuda'
        else:
            self.device = 'cpu'
        
        self.labels = labels
        self.classes_num = classes_num

        # Model
        Model = eval(model_type)
        self.model = Model(sample_rate=32000, window_size=1024, 
            hop_size=320, mel_bins=64, fmin=50, fmax=14000, 
            classes_num=self.classes_num)
        
        checkpoint = torch.load(checkpoint_path, map_location=self.device)
        self.model.load_state_dict(checkpoint['model'])

        # Parallel
        print('GPU number: {}'.format(torch.cuda.device_count()))
        self.model = torch.nn.DataParallel(self.model)

        if 'cuda' in str(self.device):
            self.model.to(self.device)

    def inference(self, audio):
        audio = move_data_to_device(audio, self.device)

        with torch.no_grad():
            self.model.eval()
            output_dict = self.model(audio, None)

        framewise_output = output_dict['framewise_output'].data.cpu().numpy()

        return framewise_output