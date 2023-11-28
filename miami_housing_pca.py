import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def load_data() -> pd.DataFrame:
    """ Load and preprocess the Miami housing dataset.

    Reads the dataset from 'data/miami-housing.csv', selects specific columns relevant for analysis,
    and returns the resulting DataFrame.

    Returns:
    --------
        df: The processed DataFrame with selected columns.
    """
    df = pd.read_csv('data/miami-housing.csv')
    df = df[['SALE_PRC','LND_SQFOOT','TOT_LVG_AREA','SPEC_FEAT_VAL','WATER_DIST','CNTR_DIST','age']]

    return df

def fit_PCA(df:pd.DataFrame) -> PCA:
    """ Fit PCA to the provided DataFrame.

    Standardizes the data using StandardScaler and fits PCA to the standardized data.

    Parameters:
    -----------
        df: The DataFrame on which PCA is to be fitted.

    Returns:
    --------
        PCA: The PCA model fitted to the standardized data.
    """
    # Standardize the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)

    pca = PCA()
    pca.fit(scaled_data)

    return pca

def PCA_results(pca:PCA, columns:list[str]) -> None:
    """ Print the PCA loadings for each principal component.

    Parameters:
    -----------
        pca: The fitted PCA model.
        columns: List of column names of the original data.
    """
    # Get the loading data for all principal components
    loadings = pca.components_
    loadings_df = pd.DataFrame(loadings.T, columns=['PC{}'.format(i+1) for i in range(pca.n_components_)], index=columns)
    print(loadings_df)

def main():
    """ Main function to run the PCA analysis on the Miami housing dataset.

    This function will load the data, preprocess it, fit PCA and display the PCA results.
    """

    # Load the Miami housing dataset
    df = load_data()
    
    # Drop sale price column from data
    X = df.drop(columns='SALE_PRC',inplace=False)

    pca = fit_PCA(df=X)

    # Results of PCA
    PCA_results(pca=pca, columns=X.columns)

if __name__=="__main__":
    main()