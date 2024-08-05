from modules.imports import *
from modules.data_loading import *
from modules.model_training import *
from modules.model_evaluation import *

def set_random_seed(seed):
    np.random.seed(seed)
    random.seed(seed)

set_random_seed(10)
file_path = 'C:\\Users\\kaurr\\OneDrive\\Desktop\\BISI\\2208\\Unsupervised clustering solution\\data\\mall_customers.csv'
df = load_data(file_path)
# check_data(df) Optional
df = train_KmeansModel_with_2features(df)
evaluate_clusters_kmeanswith2features(df)
wss = elbowmethod_to_checkclusters(df)
evaluate_clusters_elbowmethod(wss)
wss = silhouttemethod_to_checkclusters(df,wss) 
evaluate_clusters_silhouettemethod(wss)
Variables3 = train_KmeansModel_with_3features(df)
evaluate_clusters_kmeanswith3features(Variables3)