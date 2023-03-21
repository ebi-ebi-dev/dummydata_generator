import pandas as pd
import io, csv, pprint
import numpy as np


class makeTrend():

    def __init__(self):
        self.error_code = 0
        self.error_msg_dict = {
        }
    
    def is_number(self, str):
        try:
            float(str)
        except:
            return False
        else:
            return True
    
    def is_int(self, n: float):
        if n.is_integer(): return True
        else: return False

    def get_list_type(self, in_list):
        tmp = [self.is_number(x) for x in in_list]
        # 数値でない要素が1つでもあればstr
        if (all(tmp) is not True): return "str" 
        else:
            tmp = [self.is_int(float(x)) for x in in_list]
            # 整数でない要素が1つでもあればfloat
            if (all(tmp) is not True): return "float" 
            else: return "int"


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
            tmp = map(eval(self.get_list_type(list(csv_list[idx]))), list(csv_list[idx]))
            csv_dict[h] = list(tmp)

        self.input_df = pd.DataFrame(csv_dict)
        self.output_df = pd.DataFrame(csv_dict)
        
    def trend_x(self, sort_column, target_column, max_scale = 1):
        if sort_column not in self.output_df.columns:
            print(f"CSVに「{sort_column}」という項目はありません。確認してください。")
            self.error_msg_dict["error_msg"] = f"CSVに「{sort_column}」という項目はありません。確認してください。"
            self.error_code = 1
            return
        if target_column not in self.output_df.columns:
            print(f"CSVに「{target_column}」という項目はありません。確認してください。")
            self.error_msg_dict["error_msg"] = f"CSVに「{target_column}」という項目はありません。確認してください。"
            self.error_code = 1
            return
        if self.get_list_type(self.output_df[target_column].to_list()) == "str":
            print(f"「{target_column}」項目は数値型ではありません。確認してください。")
            self.error_msg_dict["error_msg"] = f"「{target_column}」項目は数値型ではありません。確認してください。"
            self.error_code = 1
            return

        self.output_df = self.output_df.sort_values(sort_column)
        coef = np.linspace(1, max_scale, len(self.output_df[target_column]))

        target_column_type = self.get_list_type(self.output_df[target_column].to_list())
        self.output_df[target_column] = np.array(self.output_df[target_column] * coef, dtype = target_column_type)
    
    def trend_sinx(self, sort_column, target_column, amp = 1, freq = 32):
        if sort_column not in self.output_df.columns:
            print(f"CSVに「{sort_column}」という項目はありません。確認してください。")
            self.error_msg_dict["error_msg"] = f"CSVに「{sort_column}」という項目はありません。確認してください。"
            self.error_code = 1
            return
        if target_column not in self.output_df.columns:
            print(f"CSVに「{target_column}」という項目はありません。確認してください。")
            self.error_msg_dict["error_msg"] = f"CSVに「{target_column}」という項目はありません。確認してください。"
            self.error_code = 1
            return
        if self.get_list_type(self.output_df[target_column].to_list()) == "str":
            print(f"「{target_column}」項目は数値型ではありません。確認してください。")
            self.error_msg_dict["error_msg"] = f"「{target_column}」項目は数値型ではありません。確認してください。"
            self.error_code = 1
            return
        
        self.output_df = self.output_df.sort_values(sort_column)
        if (amp == 0):
            coef = np.ones(len(self.output_df))
        else:
            coef = amp * (0.5 * np.sin(np.pi * np.arange(0, len(self.output_df)) / freq) + 1)

        target_column_type = self.get_list_type(self.output_df[target_column].to_list())
        self.output_df[target_column] = np.array(self.output_df[target_column] * coef, dtype = target_column_type)


    def output_csv(self, output_path):
        self.output_df.to_csv(output_path, index = False, encoding = "utf-8")
    
    



