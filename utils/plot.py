import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def plot_data(features, labels):
    x, y, z, p = features['income'], features['age'], features['loan'], labels
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    img = ax.scatter(x, y, z, c=p)
    ax.set_xlabel('Income', fontsize=14)
    ax.set_ylabel('Age', fontsize=14)
    ax.set_zlabel('Loan', fontsize=14)
    fig.colorbar(img)
    plt.show()


def plot_cm(cm):
    sns.heatmap(cm / np.sum(cm), annot=True, fmt='.2%', cmap='Blues')
    plt.show()
