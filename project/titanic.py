import numpy as np # 행렬 연산을 위한 핵심 라이브러리
import pandas as pd # 데이터값
import matplotlib.pyplot as plt # 자료를 차트나 플롯으로 시각화 
import seaborn as sns

plt.style.use('seaborn')
sns.set(font_scale = 2.5)

import missingno as msno

# ignore warnings
import warnings
warnings.filterwarnings('ignore')




df_train = pd.read_csv('../input/train.csv')
df_test = pd.read_csv('../input/test.csv')


f, ax = plt.subplots(1, 2, figsize = (18,8)) #1,2 일행 이열

df_train['Survived'].value_counts().plot.pie(explode =[0, 0.1], autopct = '%1.1f%%' , ax=ax[0], shadow = True)
ax[0].set_title('Pie plot - Survived')
ax[0].set_ylabel('')
sns.countplot('Survived' , data = df_train, ax = ax[1])
ax[1].set_title('Count plot - Survived')
plt.show()