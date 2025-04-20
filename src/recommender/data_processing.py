from src.models.data_source import DataSource 

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from scipy.sparse import lil_matrix, csr_matrix
from sklearn.metrics.pairwise import cosine_similarity

def data_extraction(ds: DataSource):
    data = ds.dso.get_data()

    if data is None:
        print("Error: Data Unavailable")
        return []

    if ds.dso.tag_column is None:
        print("Error: Tag Column ID not set")
        return []

    if ds.dso.content_id_column is None:
        print("Error: Content Column ID not set")
        return []

    ids = []
    tag_strings = []
    tag_count = 0

    for dp in data:

        id_data = dp.get(ds.dso.content_id_column)
        tag_data = dp.get(ds.dso.tag_column);
        
        ids.append(id_data)

        if tag_data is not None:
            tag_strings.append(" ".join(tag_data))
            tag_count += len(tag_data)
        else:
            tag_strings.append(" ")

    return ids, tag_strings, tag_count

def prepare_data(ds: DataSource):
    [ids, tags, tag_count] = data_extraction(ds)

    # build sparse CountVectorizer
    vectoriser = CountVectorizer(
        tokenizer=lambda x: x.split(),
        max_features=tag_count
    )
    X = vectoriser.fit_transform(tags)  # X is sparse (n_videos x n_tags)

    return ids, vectoriser, X
