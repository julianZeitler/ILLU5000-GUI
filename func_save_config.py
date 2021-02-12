from scipy.io import savemat


def save_config(name, config):
    savemat(name, {'config': config})
