from src.recommender.data_processing import prepare_data
from src.models.data_source import DataSource

def test_prepare_data():
    data_source  = DataSource("file", "./data/youtube_data.json")
    data_source.set_content_id_column("id")
    data_source.set_tag_column("snippet_tags")

    ids, vectoriser, X = prepare_data(data_source)

    assert ids is not None
    assert vectoriser is not None
    assert X is not None
