
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


for x in range(1, 30): # 1 is 1st page to 30 is last page (modify this numbers according to ur requirement)
# for x in range(1, 6):
  #url="https://www.moneycontrol.com/news/business/stocks/%d"
  url2 = "https://www.moneycontrol.com/news/business/stocks/page-%d/" % (x)
  c=pd.read_csv(url2,sep='\n',header=1)
  c.rename(columns={'            "@context": "https://schema.org",': 'newName1'}, inplace=True)
  xyx = c[c.newName1.str.contains(' IST', regex= True, na=False)]
  pd.set_option('display.max_colwidth', None)
  xyx.loc[:,'datetime'] = xyx['newName1'].str.replace('(.*)(<span>)(.*)(IST)(</span>)(.*)',r'\3\4')
  xyx.loc[:,'title'] = xyx['newName1'].str.replace('(.*)(title=\")(.*)(</a></h2>)(.*)',r'\3')
  xyx.loc[:,'title'] = xyx['title'].str.replace('(.*)(\" >)(.*)',r'\1')
  xyx.loc[:,'paragraph'] = xyx['newName1'].str.replace('(.*)(</a></h2>)(.*)(</p>)(.*)',r'\3')
  xyx.loc[:,'paragraph'] = xyx['paragraph'].str.replace('<p>','')
  xyx.loc[:,'company'] = xyx['title'].str.replace('(.*)(:)(.*)',r'\3')
  xyx.loc[:,'company_c'] = xyx['company'].str.count(' ')
  del xyx['newName1']
  if x==1:
    xyx[xyx.company_c < 5].to_csv('money_control.csv', sep='|',header=True, encoding='utf-8', index=False)
  else:    
    xyx[xyx.company_c < 5].to_csv('money_control.csv', sep='|',mode='a', header=False, encoding='utf-8', index=False)
pd.read_csv('money_control.csv', sep='|').head(2500)

