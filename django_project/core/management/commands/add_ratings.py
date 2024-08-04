from django.core.management.base import BaseCommand, CommandError
import core.models.rating.services as rating_services
from core.models.rating.models import Rating, NAME_COLOR_DELIMITER
import csv
import core.management.commands._utils as command_utils


class CsvHeaders:
    RatingName = "Name"
    Color = "Color"
    Description = "Description"
    RelativeScore = "Relative Score"


class Command(BaseCommand):
    help = "Imports ratings from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument("csv_filename", type=open)

    def handle(self, *args, **options):
        csv_file = options["csv_filename"]
        reader = csv.DictReader(csv_file)
        for row in reader:
            name = row[CsvHeaders.RatingName]
            color = row[CsvHeaders.Color]
            description = row[CsvHeaders.Description]
            score = row[CsvHeaders.RelativeScore]
            try:
                existing_rating = Rating.objects.get(relative_score=score)
            except Rating.DoesNotExist:
                try:
                    rating_services.create_new_rating(name=name, color=color, description=description, score=score)
                except Exception as e:
                    command_utils.print_error(self, f"Failed to create new rating '{name}' with exception: {e}")
                else:
                    command_utils.print_success(self, f"Created new rating '{name}', rating: {score}")
            else:
                existing_name = rating_services.get_rating_name(existing_rating)
                command_utils.print_warning(self, f"Rating already exists with score '{existing_rating.relative_score}' ('{existing_name}')")
                print(f"Replace with '{name}'? y/n (leave blank defaults to no)")
                if command_utils.get_user_agrees():
                    existing_rating.name_and_color = name + NAME_COLOR_DELIMITER + color
                    existing_rating.description = description
                    try:
                        existing_rating.save()
                    except Exception as e:
                        command_utils.print_error(self, f"Failed to create new rating '{name}' with exception: {e}")
                    else:
                        command_utils.print_success(self, f"Updated rating: {score} to '{name}'")
