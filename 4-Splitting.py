
pip  install split-folders

import splitfolders

input_folder = 'Tomato_Dataset'

splitfolders.ratio(input_folder, output = "Final_Dataset_1" ,
                   seed =42 ,ratio = (.6,.2,.2),
                   group_prefix = None)
