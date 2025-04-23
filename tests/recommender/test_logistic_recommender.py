from src.recommender.logistic_recommender import LogisticRecommender
from src.recommender.data_processing import prepare_data
from src.models.data_source import DataSource
from src.models.app_data import AppData 

from src.globals import app_data 

def test_logistic_recommender():
    data_source  = DataSource("file", "./data/youtube_data.json")
    data_source.set_content_id_column("id")
    data_source.set_tag_column("snippet_tags")

    # all of these should be able to exist without any 
    # data from a session
    ids, vectoriser, X = prepare_data(data_source)
    recommender = LogisticRecommender(X, ids, vectoriser) 
    
    session_id = app_data.create_new_session()
    app_data.set_session_preferences(session_id, {"coding", "technology"})
    
    recommender.add_user_preferences(session_id)
    # recommender.train(session_id, [["NsMKvVdEPkw", 0]])

    recs = recommender.recommend(session_id, 10)

    print(recs)
