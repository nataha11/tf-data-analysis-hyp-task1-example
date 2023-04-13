import pandas as pd
import numpy as np


chat_id = 1283808304 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    
    return (y_success/y_cnt - x_success/x_cnt < 0.1)
