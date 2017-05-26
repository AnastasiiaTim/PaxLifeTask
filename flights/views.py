from flights.models import Airport
from django.http import JsonResponse


# Create your views here.
def iata_code_search_view(request):
    code = request.GET.get('iata_code')
    if code:
        airport = Airport.objects.values(
            'name', 'iata_code', 'gps_code', 'municipality', 'iso_country', 'latitude_deg', 'longitude_deg'
        ).filter(iata_code__icontains=code).first()
        print(airport)
        if airport:
            # return JsonResponse(airport)
            return JsonResponse(get_json_data(
                    airport.get('name'),
                    airport.get('iata_code'),
                    airport.get('gps_code'),
                    airport.get('municipality'),
                    airport.get('iso_country'),
                    airport.get('latitude_deg'),
                    airport.get('longitude_deg')
                ))
        return JsonResponse(status=404, data={'status': 'false', 'message': "No airports with iata_code %s" % code})
    return JsonResponse(status=404, data={'status': 'false', 'message': "Input iata_code is not specified"})


def name_search_view(request):
    name = request.GET.get('name')
    response_data = list()
    if name:
        airports = Airport.objects.values(
                'name', 'iata_code', 'gps_code', 'municipality', 'iso_country', 'latitude_deg', 'longitude_deg'
            ).filter(name__icontains=name)
        print(airports)
        if airports:
            for airport in airports.values():
                response_data.append(get_json_data(
                    airport.get('name'),
                    airport.get('iata_code'),
                    airport.get('gps_code'),
                    airport.get('municipality'),
                    airport.get('iso_country'),
                    airport.get('latitude_deg'),
                    airport.get('longitude_deg')
                ))
            return JsonResponse(response_data, safe=False)
        return JsonResponse(status=404, data={'status': 'false', 'message': "No airports with name found"})
    return JsonResponse(status=404, data={'status': 'false', 'message': "Input name is not specified"})


def get_json_data(name, iata_code, gps_code, municipality, iso_country, latitude_deg, longitude_deg):
    return {
        "name": name,
        "iata": iata_code,
        "icao": gps_code,
        "city": municipality,
        "country": iso_country,
        "latitude": latitude_deg,
        "longitude": longitude_deg
    }
