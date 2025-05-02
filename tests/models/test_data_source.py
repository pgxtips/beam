from src.models.data_source import DataSource

def test_get_keys():
    data_source  = DataSource("file", "./data/youtube_data.json")
    attr = data_source.get_keys()

    assert attr is not None, "get_all_features() returned None"
    assert len(attr) > 0
    attr.sort()

    expected = ['contentDetails_caption', 'contentDetails_contentRating_ytRating', 'contentDetails_definition', 'contentDetails_dimension', 'contentDetails_duration', 'contentDetails_licensedContent', 'contentDetails_projection', 'contentDetails_regionRestriction_allowed', 'contentDetails_regionRestriction_blocked', 'etag', 'id', 'kind', 'snippet_categoryId', 'snippet_channelId', 'snippet_channelTitle', 'snippet_defaultAudioLanguage', 'snippet_defaultLanguage', 'snippet_description', 'snippet_liveBroadcastContent', 'snippet_localized_description', 'snippet_localized_title', 'snippet_publishedAt', 'snippet_tags', 'snippet_thumbnails_default_height', 'snippet_thumbnails_default_url', 'snippet_thumbnails_default_width', 'snippet_thumbnails_high_height', 'snippet_thumbnails_high_url', 'snippet_thumbnails_high_width', 'snippet_thumbnails_maxres_height', 'snippet_thumbnails_maxres_url', 'snippet_thumbnails_maxres_width', 'snippet_thumbnails_medium_height', 'snippet_thumbnails_medium_url', 'snippet_thumbnails_medium_width', 'snippet_thumbnails_standard_height', 'snippet_thumbnails_standard_url', 'snippet_thumbnails_standard_width', 'snippet_title', 'statistics_commentCount', 'statistics_favoriteCount', 'statistics_likeCount', 'statistics_viewCount']
    assert attr == expected

def test_get_col():
    data_source  = DataSource("file", "./data/youtube_data.json")
    data = data_source.get_col_data("snippet_tags")

    assert data is not None

    expected = ['cat meowing to attract cats,cats meowing,cats meowing to attract cats,cat sounds to attract cats,sounds to attract cats,kittens meowing,kitten meowing,cats meowing loudly,cats and kittens meowing,cat meowing,meowing cats,kittens and cats meowing,meowing kittens,audio to attract cats,sounds that attract cats,meowing,cats,kittens meowing to attract cats,cat sounds to attract kittens,meows to attract cats,basket of meowing kittens']

    # MATCH FOUND   
    assert data[0] == expected

def test_get_tags():
    data_source  = DataSource("file", "./data/youtube_data.json")
    data_source.set_tag_column("snippet_tags")
    data = data_source.get_tags()

    assert data is not None
    data.sort()

    print("tag count:", len(data))

    expected = ['"Jamuna International', '"भविष्य की टेक्नोलॉजी Future technology', '#10hometips', '#11dailyusefulhometips', '#1Trending', '#8amazinghometips&hacks', '#8newhometips', '#ABS WORKOUT', '#ABS-CBNNews_Exclusive', '#ABS-CBNNews_Highlight', '#ABS-CBNNews_Livestream', '#ABSCBNNewsExclusive', '#ABSCBNNewsExclusive_HLS', '#AI Technology', '#Abisko', '#Adventure', '#AdventureSweden', '#AfricanTravel', '#AfroTrap', '#Agadir', '#Agra', '#AtlasMountains', '#Banaue', '#BavarianAlps', '#BeachVibes', '#BeautifulDestinations', '#BeautifulPlaces', '#BeautifulSweden', '#Berlin', '#BeyondTheHeadlines', '#BigFiveSafari', '#Bohol', '#Bollywood music', '#Bollywood song', '#Boracay', '#BouldersBeach', '#BreakingNews', '#BucketList', '#CARDIO', '#CampsBay', '#CapeOfGoodHope', '#CapeTown', '#CapeWinelands', '#Casablanca', '#CatLovers', '#CatOfTheDay', '#CatTikTok', '#CatVibes', '#CatVideos', '#Cats']

    assert data[:50] == expected

# def test_feature_selection():
#     data_source  = DataSource("file", "./data/youtube_data.json")
#
#     data_source.set_selected([
#         'contentDetails_caption',
#         'contentDetails_contentRating_ytRating',
#         'contentDetails_definition',
#     ])
#     data = data_source.get_data()
#     assert data is not None, "get_data() returned None"
#
#     test_el = data[0]
#     expected = {'contentDetails_caption': 'false', 'contentDetails_contentRating_ytRating': None, 'contentDetails_definition': 'hd'}
#
#     assert test_el == expected
