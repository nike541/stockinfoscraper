import requests
import pandas as pd

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
    df_filtered = df[df['newName1'].str.contains(' IST', regex=True, na=False)]
    df_filtered.loc[:, 'datetime'] = df_filtered['newName1'].str.extract(r'<span>(.*?) IST</span>')
    df_filtered.loc[:, 'title'] = df_filtered['newName1'].str.extract(r'title="(.*?)"')
    df_filtered.loc[:, 'paragraph'] = df_filtered['newName1'].str.extract(r'</a></h2><p>(.*?)</p>')
    df_filtered.loc[:, 'company'] = df_filtered['title'].str.extract(r': (.*)')
    df_filtered.loc[:, 'company_c'] = df_filtered['company'].str.count(' ')

    return df_filtered[df_filtered['company_c'] < 5]

# Iterate over the pages and append the results
result_df = pd.DataFrame()

for x in range(1, 30):  # Modify the range as needed
    page_data = extract_data(x)
    result_df = pd.concat([result_df, page_data])

# Save the results to a CSV file
result_df.to_csv('money_control.csv', sep='|', encoding='utf-8', index=False)

# Display the top rows of the resulting DataFrame
result_df.head(2500)
