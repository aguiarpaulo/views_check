import pandas as pd 

# Funtion to read Excel file and count characters
def count_view_characters(excel_file):
    df = pd.read_excel(excel_file)

    # Check if the required columns are present
    if not all(col in df.columns for col in ['schema', 'table_name', 'definition']):
        print('Does not contain the required columns.')
        return

        # Create a dictionary to store the view name and character count
    results = {}

    # Iterate over each row in the Dataframe
    for index, row in df.iterrows():
        view_name = f"{row['schema']}.{row['table_name']}"
        character_count = len(str(row['definition']))

        # Store the result
        results[view_name] = character_count

    #Display the results
    for view_name, count in results.items():
        print(f'View: {view_name} - Character count: {count}')

excel_file = 'C:/Users/paulo_aguiar/py_projects/data/view_def.xlsx'

count_view_characters(excel_file)