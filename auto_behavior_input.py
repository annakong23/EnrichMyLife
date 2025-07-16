import pandas as pd

df = pd.read_excel('C:/Users/ssk07/.spyder-py3/XXXXXXXXXXXX.xlsx', skiprows=5, index_col=0)

df.drop(columns=['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3'], inplace=True)

df.index = pd.to_datetime(df.index, errors='coerce')

# 시작 및 종료 regdate 설정
start_date = '2024-05-18'
end_date = '2024-07-01'

# 행 데이터를 일렬로 나열, 결합
def flatten_and_concatenate(df, start_date, end_date):
    concatenated_list = []
    selected_rows = df.loc[start_date:end_date]
    for index, row in selected_rows.iterrows():
        for item in row:
            if isinstance(item, (list, tuple)):
                concatenated_list.extend(item)
            else:
                concatenated_list.append(item)
    return concatenated_list

result = flatten_and_concatenate(df, start_date, end_date)

result_df = pd.DataFrame(result)

output_file_path = 'C:/Users/ssk07/.spyder-py3/XXXX.xlsx'
result_df.to_excel(output_file_path, index=False)

print(f"Result saved to {output_file_path}")

len(result_df)
result_df.info()