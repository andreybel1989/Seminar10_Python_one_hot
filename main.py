# first method

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)    
md = {"robot":[1, 0], "human":[0, 1]}
new_lst = []
for index, value in enumerate(lst):
    if value == "robot":
        new_lst.append(md["robot"])
    else:
        new_lst.append(md["human"])
print(f"Index Robot Human")
for index, (robot, human) in enumerate(new_lst):
    print(f"{index}\t{robot}\t{human}")

# second method

# import pandas as pd
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI': lst})
# one_hot_data = pd.get_dummies(data['whoAmI'],  dtype= int)
# print(one_hot_data.head(n = 20))

# third method

# import pandas as pd
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# dic_val = {"robot":[1, 0], "human":[0, 1]}
# new_lst = []
# for value in lst:
#     if value == "robot":
#         new_lst.append(dic_val["robot"])
#     else:
#         new_lst.append(dic_val["human"])
# new_data = pd.DataFrame({'robot':pd.DataFrame(new_lst)[0], 'human':pd.DataFrame(new_lst)[1]})
# print(new_data.head(n= 20))