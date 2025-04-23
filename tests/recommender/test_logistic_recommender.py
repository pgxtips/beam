from src.recommender.logistic_recommender import LogisticRecommender
from src.recommender.data_processing import prepare_data
from src.models.data_source import DataSource

from src.globals import session_handler 

def test_lr_user_pref():
    data_source  = DataSource("file", "./data/youtube_data.json")
    data_source.set_content_id_column("id")
    data_source.set_tag_column("snippet_tags")

    # all of these should be able to exist without any 
    # data from a session
    ids, vectoriser, X = prepare_data(data_source)
    recommender = LogisticRecommender(X, ids, vectoriser) 

    session_id = session_handler.create_new()
    recs1 = recommender.recommend(session_id, 10)

    session_handler.set_preferences(session_id, ["coding", "technology"])
    recs2 = recommender.recommend(session_id, 10)

    assert recs1 != recs2


def test_lr_likes_content():
    data_source  = DataSource("file", "./data/youtube_data.json")
    data_source.set_content_id_column("id")
    data_source.set_tag_column("snippet_tags")

    # all of these should be able to exist without any 
    # data from a session
    ids, vectoriser, X = prepare_data(data_source)
    recommender = LogisticRecommender(X, ids, vectoriser) 

    session_id = session_handler.create_new()
    session_handler.set_preferences(session_id, ["coding", "technology"])

    recs1 = recommender.recommend(session_id, 10)

    # video with tags: cat meowing to attract cats, cats meowing, cats meowing to attract cats, cat sounds to attract cats, sounds to attract cats, kittens meowing, kitten meowing, cats meowing loudly, cats and kittens meowing, cat meowing, meowing cats, kittens and cats meowing, meowing kittens, audio to attract cats, sounds that attract cats, meowing, cats, kittens meowing to attract cats, cat sounds to attract kittens, meows to attract cats, basket of meowing kittens
    session_handler.like_content(session_id, "NsMKvVdEPkw")

    recs2 = recommender.recommend(session_id, 10)

    assert recs2 != recs1 


def test_lr_dislike_content():
    data_source  = DataSource("file", "./data/youtube_data.json")
    data_source.set_content_id_column("id")
    data_source.set_tag_column("snippet_tags")

    # all of these should be able to exist without any 
    # data from a session
    ids, vectoriser, X = prepare_data(data_source)
    recommender = LogisticRecommender(X, ids, vectoriser) 

    session_id = session_handler.create_new()
    recs1 = recommender.recommend(session_id, 10)

    session_handler.dislike_content(session_id, "XZrckLYqdys")
    session_handler.dislike_content(session_id, "FcbP--wmgO4")
    session_handler.dislike_content(session_id, "z7do1hhb6fE")

    recs2 = recommender.recommend(session_id, 10)

    assert recs1 != recs2
