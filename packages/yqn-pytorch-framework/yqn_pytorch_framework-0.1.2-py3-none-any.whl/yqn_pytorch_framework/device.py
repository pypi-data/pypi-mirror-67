import torch

cpu_device = "cpu"


def get_cpu_device():
    device = torch.device("cpu")
    return device


def get_device(verbose=False):
    train_on_gpu = torch.cuda.is_available()
    if verbose:
        if not train_on_gpu:
            print('CUDA is not available. Run on CPU')
        else:
            print('CUDA is available. Run on GPU')

    device = torch.device("cuda:0" if train_on_gpu else "cpu")
    return device
