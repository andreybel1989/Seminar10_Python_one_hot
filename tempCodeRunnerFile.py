import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
one_hot_data = pd.get_dummies(data['whoAmI'],  dtype= int)
print(one_hot_data.head(n = 20))