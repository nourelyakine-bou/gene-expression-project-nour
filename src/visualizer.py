import arabic_reshaper
from bidi.algorithm import get_display

import seaborn as sns
import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self, data):
        self.data = data
    def plot_label_distribution(self, label_column):
        sns.countplot(data=self.data, x=label_column)
        title = "توزيع الحالات"
        reshaped_title = arabic_reshaper.reshape(title)
        bidi_title = get_display(reshaped_title)
        plt.title(bidi_title)
        plt.show()

