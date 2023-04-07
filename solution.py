import pandas as pd
import numpy as np

from scipy.stats import norm, chi2


chat_id = 201321241 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    s = np.std(x/47)
    
    chi2_left = chi2.ppf(alpha/2, n-2)
    chi2_right = chi2.ppf(1 - alpha/2, n-2)
    sigma_left = np.sqrt((n-2) * s**2 / chi2_right)
    sigma_right = np.sqrt((n-2) * s**2 / chi2_left)
    
    alpha = 1 - p
    loc = x.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return sigma_left, sigma_right
