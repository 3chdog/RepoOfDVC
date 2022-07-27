from operator import index
import os
import pandas as pd

imgFolderName = 'img'

initDic = {'name': os.listdir(imgFolderName)}
df = pd.DataFrame.from_dict(initDic)
df['random']=list([i*100 for i in range(len(initDic['name']))])
df['path']=list([os.path.join(imgFolderName, n) for n in initDic['name']])
print(df)
df.to_csv('mydf.csv', index=False)
