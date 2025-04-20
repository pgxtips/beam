from src.recommender.logistic_recommender import LogisticRecommender
from src.recommender.data_processing import prepare_data
from src.models.data_source import DataSource

def test_logistic_recommender():
    data_source  = DataSource("file", "./data/youtube_data.json")
    data_source.set_content_id_column("id")
    data_source.set_tag_column("snippet_tags")

    ids, vectoriser, X = prepare_data(data_source)

    recommender = LogisticRecommender(X, ids, vectoriser) 

    prefs = {"coding", "animal"}
    session_id = "1jf8"
    
    recommender.add_user_preferences(session_id, prefs)
    # recommender.train(session_id, [["NsMKvVdEPkw", 0]])

    recs = recommender.recommend(session_id, 10)

    print(recs)
