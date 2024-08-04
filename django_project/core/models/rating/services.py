from core.models.rating.models import Rating, NAME_COLOR_DELIMITER
import re


def get_rating(rating_or_id: int | Rating) -> Rating:
    if type(rating_or_id) is Rating:
        return rating_or_id
    return Rating.objects.get(id=rating_or_id)


def get_rating_color(rating: Rating) -> str:
    _, color = rating.name_and_color.split(NAME_COLOR_DELIMITER)
    return color


def get_rating_name(rating: Rating) -> str:
    name, _ = rating.name_and_color.split(NAME_COLOR_DELIMITER)
    return name


def create_new_rating(name: str, color: str, description: str, score: int) -> Rating:
    if NAME_COLOR_DELIMITER in name:
        raise ValueError(f"Rating name must not contain key delimiter '{NAME_COLOR_DELIMITER}'")
    if not re.match("^[0-9a-fA-F]{6}$", color):
        raise ValueError(f"Rating must have a valid 6-digit hex code; received {color}")
    name_and_color = name + NAME_COLOR_DELIMITER + color
    return Rating.objects.create(name_and_color=name_and_color, description=description, relative_score=score)
