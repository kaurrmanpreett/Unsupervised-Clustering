from .imports import *

def load_data(file_path):
    # Loads data from a CSV file.
    df = pd.read_csv(file_path)
    return df

def check_data(df): 
    # Check data and plot.
    df.head()
    df.describe()
    df.shape
    sns.pairplot(df[['Age','Annual_Income','Spending_Score']])
    plt.show()
    