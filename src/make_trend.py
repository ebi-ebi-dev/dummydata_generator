import pandas as pd
import io, csv, pprint
import numpy as np


class makeTrend():

    def __init__(self):
        self.error_code = 0
        self.error_msg_dict = {
        }
    
    def read_from_csvtext(self, csv_text):

        with io.StringIO() as f:
            f.write(csv_text)
            f.seek(0)
            csv_reader = csv.reader(f)
            csv_list = [row for row in csv_reader]

            header = csv_list[0]
            csv_list = list(zip(*csv_list[1:])) # 転置: [[row1], [row2], ... ] -> [[col1], [col2],...]

        csv_dict = {}
        for h, idx in zip(header, range(len(header))):
            csv_dict[h] = list(csv_list[idx])

        self.output_df = pd.DataFrame(csv_dict)
        
    def trend_x(self, sort_column, target_column, max_scale = 1):
        if sort_column not in self.output_df.columns or target_column not in self.output_df.columns:
            print(f"CSVに「{target_column}」という項目はありません。確認してください。")
            self.error_msg_dict["error_msg"] = f"CSVに「{target_column}」という項目はありません。確認してください。"
            self.error_code = 1
            return

        self.output_df = self.output_df.sort_values(sort_column)
        coef = np.linspace(1, max_scale, len(self.output_df[target_column]))

        tmp_arr = np.array(self.output_df[target_column], dtype=np.float32) # デフォでintのカラムにはfloatと掛け算できないので、一度キャスト
        tmp_arr *= coef
        self.output_df[target_column] = np.array(tmp_arr, dtype=np.int32)
    
    def trend_sinx(self, sort_column, target_column, amp = 1, freq = 32):
        if sort_column not in self.output_df.columns or target_column not in self.output_df.columns:
            print(f"CSVに「{target_column}」という項目はありません。確認してください。")
            self.error_msg_dict["error_msg"] = f"CSVに「{target_column}」という項目はありません。確認してください。"
            self.error_code = 1
            return
        
        self.output_df = self.output_df.sort_values(sort_column)
        coef = amp * (0.5 * np.sin(np.pi * np.arange(0, len(self.output_df)) / freq) + 1)

        tmp_arr = np.array(self.output_df[target_column], dtype=np.float32) # デフォでintのカラムにはfloatと掛け算できないので、一度キャスト
        tmp_arr *= coef
        self.output_df[target_column] = np.array(tmp_arr, dtype=np.int32)


    def output_csv(self, output_path):
        self.output_df.to_csv(output_path, index = False, encoding = "utf-8")
    
    



