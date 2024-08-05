import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from .imports import *
from .data_loading import *
from .model_training import *

def evaluate_clusters_kmeanswith2features(df):
    sns.scatterplot(x='Annual_Income', y = 'Spending_Score', data=df, hue='Cluster', palette='colorblind')
    plt.title("CLUSTER WITH 2 FEATURES")
    plt.show()

def evaluate_clusters_elbowmethod(wss):
    wss.plot(x='cluster', y = 'WSS_Score')
    plt.xlabel('No. of clusters')
    plt.ylabel('WSS Score')
    plt.title('Elbow Plot cluster with 2 features')
    plt.show()
def evaluate_clusters_silhouettemethod(wss):  
    wss.plot(x='cluster', y='Silhouette_Score')
    plt.xlabel('No. of clusters')
    plt.ylabel('Silhouette Score')
    plt.title('Silhouette Plot for cluster with 2 features')
    plt.show()
    
def evaluate_clusters_kmeanswith3features(Variables3):
    Variables3.plot(x='cluster', y='Silhouette_Score')
    plt.title("Silhouette plot Cluster with 3 features")
    plt.show()