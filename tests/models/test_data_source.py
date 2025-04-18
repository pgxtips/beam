from src.models.data_source import DataSource

def test_datasource():
    data_source  = DataSource("file", "./data/youtube_data.json")
    
    expected = [
        'kind',
        'etag',
        'id',
        'snippet_publishedAt',
        'snippet_channelId',
        'snippet_title',
        'snippet_description',
        'snippet_thumbnails_default_url',
        'snippet_thumbnails_default_width',
        'snippet_thumbnails_default_height',
        'snippet_thumbnails_medium_url',
        'snippet_thumbnails_medium_width',
        'snippet_thumbnails_medium_height',
        'snippet_thumbnails_high_url',
        'snippet_thumbnails_high_width',
        'snippet_thumbnails_high_height',
        'snippet_thumbnails_standard_url',
        'snippet_thumbnails_standard_width',
        'snippet_thumbnails_standard_height',
        'snippet_thumbnails_maxres_url',
        'snippet_thumbnails_maxres_width',
        'snippet_thumbnails_maxres_height',
        'snippet_channelTitle',
        'snippet_tags',
        'snippet_categoryId',
        'snippet_liveBroadcastContent',
        'snippet_defaultLanguage',
        'snippet_localized_title',
        'snippet_localized_description',
        'snippet_defaultAudioLanguage',
        'contentDetails_duration',
        'contentDetails_dimension',
        'contentDetails_definition',
        'contentDetails_caption',
        'contentDetails_licensedContent',
        'contentDetails_projection',
        'statistics_viewCount',
        'statistics_likeCount',
        'statistics_favoriteCount',
        'statistics_commentCount'
    ]

    assert data_source.get_features() == expected
