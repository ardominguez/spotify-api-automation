def validated_artist_information(context, artist_information, artist_value):
    current_artist = context.response_body[artist_information]
    expected_artist_information = str(artist_value)
    return current_artist == expected_artist_information
