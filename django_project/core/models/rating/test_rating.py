import pytest
from core.models.rating.models import Rating, NAME_COLOR_DELIMITER
import core.models.rating.services as rating_services


TEST_NAME = "Test"
TEST_COLOR = "ff00ff"
TEST_NAME_AND_COLOR = TEST_NAME + NAME_COLOR_DELIMITER + TEST_COLOR

TEST_DESCRIPTION = "Test description"
SCORE = 1


class TestGetRating:
    @pytest.mark.django_db
    def test_get_rating_matching_id(self):
        rating = Rating.objects.create(name_and_color=TEST_NAME_AND_COLOR, description=TEST_DESCRIPTION, relative_score=SCORE)
        get_rating = rating_services.get_rating(rating.id)
        assert rating == get_rating

    def test_return_rating_if_provided(self):
        rating = Rating(name_and_color=TEST_NAME_AND_COLOR, description=TEST_DESCRIPTION, relative_score=SCORE)
        assert rating_services.get_rating(rating) == rating


class TestGetName:
    def test_get_name(self):
        rating = Rating(name_and_color=TEST_NAME_AND_COLOR, description=TEST_DESCRIPTION, relative_score=SCORE)
        name = rating_services.get_rating_name(rating)
        assert name == TEST_NAME


class TestGetColor:
    def test_get_color(self):
        rating = Rating(name_and_color=TEST_NAME_AND_COLOR, description=TEST_DESCRIPTION, relative_score=SCORE)
        color = rating_services.get_rating_color(rating)
        assert color == TEST_COLOR


class TestCreateRating:
    def test_raises_error_if_name_has_delimiter(self):
        with pytest.raises(ValueError):
            rating_services.create_new_rating(TEST_NAME + NAME_COLOR_DELIMITER, TEST_COLOR, TEST_DESCRIPTION, SCORE)

    def test_raises_error_if_invalid_hex_characters_provided(self):
        with pytest.raises(ValueError):
            rating_services.create_new_rating(TEST_NAME, 'ffxxff', TEST_DESCRIPTION, SCORE)

    def test_raises_error_if_invalid_hex_length_provided(self):
        with pytest.raises(ValueError):
            rating_services.create_new_rating(TEST_NAME, 'ff00ffaa', TEST_DESCRIPTION, SCORE)

    @pytest.mark.django_db
    def test_rating_created_successfully(self):
        new_rating = rating_services.create_new_rating(TEST_NAME, TEST_COLOR, TEST_DESCRIPTION, SCORE)
        assert new_rating.name_and_color == TEST_NAME_AND_COLOR
        assert new_rating.description == TEST_DESCRIPTION
        assert new_rating.relative_score == SCORE
