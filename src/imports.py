# АВТОМАТИЧЕСКАЯ НАСТРОЙКА (не удалять!)
import sys
import os
venv_path = '/Users/anthony/My drive/Work/Webmasteranton/Veterinary/ecovetnadom-growth-analysis/venv/lib/python3.8/site-packages'
if venv_path not in sys.path:
    sys.path.insert(0, venv_path)

# Импорты
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import poisson
import statsmodels.api as sm
import statsmodels.formula.api as smf

print("✅ Окружение готово!")