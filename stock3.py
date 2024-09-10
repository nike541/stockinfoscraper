import requests
import pandas as pd
import re

def clean_html_and_whitespace(text):

    text = re.sub(r'<.*?>','',text)


    text = text.strip()
    return text
# Function to extract data from each page
def extract_data(page_num):
    url = f"https://www.moneycontrol.com/news/business/stocks/page-{page_num}/"
    response = requests.get(url)
    content = response.text
    
    # Split the content into lines
    lines = content.splitlines()
    
    # Convert the lines into a DataFrame
    df = pd.DataFrame(lines, columns=['newName1'])  
    # Process the DataFrame to extract relevant information
  # Assuming df is your original DataFrame
    df_filtered = df[df['newName1'].str.contains(' IST', regex=True, na=True)].copy()
    df_filtered['title'] = df_filtered['newName1'].str.extract(r'title="(.*?)"')[0]
    #print(df_filtered['title'])
    df_filtered['paragraph'] = df_filtered['newName1'].str.extract(r'</a></h2><p>(.*?)</p>')[0]
    #print(df_filtered['paragraph'])
    df_filtered['company'] = df_filtered['title'].str.extract(r': (.*)')[0]
    df_filtered['company_c'] = df_filtered['company'].str.count(' ')
    df_filtered['newName1'] = df_filtered['newName1'].apply(lambda x: clean_html_and_whitespace(x))
 
# Print the full cleaned DataFrame with all columns
    print(df_filtered)

    return df_filtered[df_filtered['company_c'] < 5]

# Iterate over the pages and append the results
result_df = pd.DataFrame()


for x in range(1, 5):  # Modify the range as needed
    page_data = extract_data(x)
    print(page_data)
    result_df = pd.concat([result_df, page_data])
   # print(result_df)
# Save the results to a CSV file
result_df.to_csv('money_control.csv', sep='|', encoding='utf-8', index=False)

# Display the top rows of the resulting DataFrame
#result_df.head(2500)
