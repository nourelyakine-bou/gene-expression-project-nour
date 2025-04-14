from src.gene_data import GeneExpressionData
from src.data_explorer import DataExplorer
from src.visualizer import Visualizer

# تحميل البيانات
data_handler = GeneExpressionData("data/gene_expression.csv")
data_handler.load_data()
data_handler.preview()
data_handler.shape()
data_handler.info()

# تحليل البيانات
explorer = DataExplorer(data_handler.data)
explorer.missing_values()
explorer.describe_data()

# رسوم بيانية
visuals = Visualizer(data_handler.data)
visuals.plot_label_distribution("Label")