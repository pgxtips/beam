from src.models.data_source import DataSource

def test_get_features():
    data_source  = DataSource("file", "./data/youtube_data.json")
    attr = data_source.get_all_features()

    assert attr is not None, "get_all_features() returned None"
    assert len(attr) > 0
    attr.sort()

    expected = ['contentDetails_caption', 'contentDetails_contentRating_ytRating', 'contentDetails_definition', 'contentDetails_dimension', 'contentDetails_duration', 'contentDetails_licensedContent', 'contentDetails_projection', 'contentDetails_regionRestriction_allowed', 'contentDetails_regionRestriction_blocked', 'etag', 'id', 'kind', 'snippet_categoryId', 'snippet_channelId', 'snippet_channelTitle', 'snippet_defaultAudioLanguage', 'snippet_defaultLanguage', 'snippet_description', 'snippet_liveBroadcastContent', 'snippet_localized_description', 'snippet_localized_title', 'snippet_publishedAt', 'snippet_tags', 'snippet_thumbnails_default_height', 'snippet_thumbnails_default_url', 'snippet_thumbnails_default_width', 'snippet_thumbnails_high_height', 'snippet_thumbnails_high_url', 'snippet_thumbnails_high_width', 'snippet_thumbnails_maxres_height', 'snippet_thumbnails_maxres_url', 'snippet_thumbnails_maxres_width', 'snippet_thumbnails_medium_height', 'snippet_thumbnails_medium_url', 'snippet_thumbnails_medium_width', 'snippet_thumbnails_standard_height', 'snippet_thumbnails_standard_url', 'snippet_thumbnails_standard_width', 'snippet_title', 'statistics_commentCount', 'statistics_favoriteCount', 'statistics_likeCount', 'statistics_viewCount']
    assert attr == expected

def test_feature_selection():
    data_source  = DataSource("file", "./data/youtube_data.json")

    data_source.set_selected([
        'contentDetails_caption',
        'contentDetails_contentRating_ytRating',
        'contentDetails_definition',
    ])
    data = data_source.get_data()
    assert data is not None, "get_data() returned None"

    test_el = data[0]
    expected = {'contentDetails_caption': 'false', 'contentDetails_contentRating_ytRating': None, 'contentDetails_definition': 'hd'}

    assert test_el == expected
