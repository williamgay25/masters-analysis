import pdfplumber
import pandas as pd

BASE_DIR = "2024/"

def convert_last_year_to_csv():
    pdf = pdfplumber.open(BASE_DIR + "results.pdf")

    tables = []
    for page in pdf.pages:
        table = page.extract_tables()

        if table:
            tables.extend(table)

    dfs = []
    for table in tables:
        df = pd.DataFrame(table[1:], columns=tables[0][0])
        dfs.append(df)

    output_df = pd.concat(dfs).drop(["Pot", "$1,810.00"], axis=1)
    output_df.to_csv(BASE_DIR + 'stats.csv')

def compute_distribution(df, column):
    distribution = df[column].value_counts()
    output = pd.DataFrame({
        'Count': distribution,
        'Percentage': distribution / len(df) * 100
    })
    return output

def compute_distinct_picks(df, columns = ['Group A', 'Group B', 'Group C']):
    total_unique = 0
    for column in columns:
        total_unique += df[column].nunique()
    return total_unique

def main():
    results = BASE_DIR + 'stats.csv'
    df = pd.read_csv(results)

    print(f"Last years competition contained a total of {len(df)} groups")
    print(f"There was a total of {compute_distinct_picks(df)} distinct players picked out of 89 in the field")
    
    #print(compute_distribution(df, 'Group A'))
    #print(compute_distribution(df, 'Group B'))
    print(compute_distribution(df, 'Group C'))

if __name__ == "__main__":
    main()