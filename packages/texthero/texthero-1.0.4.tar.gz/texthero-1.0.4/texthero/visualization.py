"""
Visualize insights and statistics of a text-based Pandas DataFrame.
"""


import pandas as pd
import plotly.express as px

def scatterplot(df: pd.DataFrame , col: str, color: str = None, hover_data: [] = None, title="") -> None:
    """
    Show scatterplot using python plotly scatter.

    Parameters
    ----------
    df
    col
        The name of the column of the DataFrame used for x and y axis.


    Examples
    --------

    >>> import texthero
    >>> df = pd.DataFrame([(0,1), (1,0)], columns='pca')
    >>> texthero.visualization.scatterplot(df, 'pca')

    """

    pca0 = df[col].apply(lambda x: x[0])
    pca1 = df[col].apply(lambda x: x[1])

    fig = px.scatter(df,
                     x=pca0,
                     y=pca1,
                     color=color,
                     hover_data=hover_data,
                     title=title
                    )
    fig.show(config={'displayModeBar': False})

def top_words(s: pd.Series,  normalize=False) -> pd.Series:
    """
    Return most common words.

    Parameters
    ----------

    s
    normalize :
        Default is False. If set to True, returns normalized values.

    """
    WHITESPACE_SPLITTER = r"\W+"
    return s.str.split(WHITESPACE_SPLITTER).explode().value_counts(normalize=normalize)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
