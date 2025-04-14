import pandas as pd

class GeneExpressionData:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None

    def load_data(self):
        try:
            self.data = pd.read_csv(self.filepath)
            print("✔️ تم تحميل البيانات.")
        except Exception as e:
            print(f"❌ خطأ: {e}")

    def preview(self):
        print("أول 5 صفوف من البيانات:")
        print(self.data.head())

    def shape(self):
        print(f"البيانات تحتوي على {self.data.shape[0]} صفوف و {self.data.shape[1]} أعمدة.")

    def info(self):
        print(self.data.info())