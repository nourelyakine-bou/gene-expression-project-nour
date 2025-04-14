class DataExplorer:
    def __init__(self, data):
        self.data = data

    def missing_values(self):
        print("🔍 القيم المفقودة في كل عمود:")
        print(self.data.isnull().sum())

    def describe_data(self):
        print("📊 ملخص إحصائي:")
        print(self.data.describe())