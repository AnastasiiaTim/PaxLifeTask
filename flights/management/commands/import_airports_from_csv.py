from __future__ import unicode_literals
import csv
from django.core.management.base import BaseCommand
from flights.models import Airport

SILENT, NORMAL, VERBOSE, VERY_VERBOSE = 0, 1, 2, 3


class Command(BaseCommand):
    help = (
        "Imports airports from a local CSV file. "
        "Expects title, URL, and release year."
    )

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument(
            "file_path",
            nargs=1,
            # type=unicode,
        )

    def handle(self, *args, **options):
        verbosity = options.get("verbosity", NORMAL)
        file_path = options["file_path"][0]

        if verbosity >= NORMAL:
            self.stdout.write("=== Airports imported ===")

        with open(file_path) as f:
            reader = csv.reader(f)
            for rownum, (_, ident, type, name, latitude_deg, longitude_deg, elevation_ft, continent, iso_country,
                         iso_region, municipality, scheduled_service, gps_code, iata_code, local_code, home_link,
                         wikipedia_link, keywords) in enumerate(reader):
                if rownum == 0:
                    # let's skip the column captions
                    continue
                if len(iata_code) == 0:
                    # skip all aiports with no IATA code
                    continue
                if not elevation_ft:
                    elevation_ft = 0
                airport, created = Airport.objects.get_or_create(
                    ident=ident,
                    type=type,
                    name=name,
                    latitude_deg=latitude_deg,
                    longitude_deg=longitude_deg,
                    elevation_ft=elevation_ft,
                    continent=continent,
                    iso_country=iso_country,
                    iso_region=iso_region,
                    municipality=municipality,
                    scheduled_service=scheduled_service,
                    gps_code=gps_code,
                    iata_code=iata_code,
                    local_code=local_code,
                    home_link=home_link,
                    wikipedia_link=wikipedia_link,
                    keywords=keywords,
                )
                if verbosity >= NORMAL:
                    self.stdout.write("{}. {}".format(
                        rownum, airport.iata_code
                    ))
