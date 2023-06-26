import json

from requests import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core import serializers
from django.http import JsonResponse

from .models import Aircrafts, Flights

class FlightsView(APIView):
    def get(self, request):
        """
        GET method to find flight's informations. The parameters are not required.
        -from (string): starting airport code
        -from_coordinate [string]: a string pass like list with 2 decima coordinate
        -to (string): arrival airport code
        -to_coordinate [string]: a string pass like list with 2 decima coordinate
        -start_date (string): starting date in the format YYYY-MM-DD
        -end_date (string): arrival date in the format YYYY-MM-DD
        -start_time (string): starting time with the format HH:MM
        -end_time (string): end time with the format HH:MM
        -aircraft_code (string): unique aircraft code

        :return: json with selected flights

        """
        if request.method == 'GET':
            if len(dict(request.GET)) == 0:
                queryset = serializers.serialize("json", Flights.objects.all())
                queryset = json.loads(queryset)
                return JsonResponse({'flights': queryset})
            else:
                queryset = Flights.objects.all()
                if request.GET.get('from'):
                    queryset = queryset.filter(_from=request.GET['from'])
                if request.GET.get('to'):
                    queryset = queryset.filter(to=request.GET['to'])
                from datetime import datetime
                now = datetime.now()
                import datetime
                if request.query_params.get('start_date') is not None or request.query_params.get('start_time') is not None:
                    start_datetime = f"{request.query_params.get('start_date')} {request.query_params.get('start_time')}:00"
                    start_datetime = datetime.datetime.strptime(start_datetime, '%Y-%m-%d %H:%M:%S')
                    if start_datetime < now:
                        return JsonResponse({'ERROR': {"The arrival date is before today": ""}})

                if request.query_params.get('end_date') is not None or request.query_params.get(
                        'end_time') is not None:
                    end_datetime = f"{request.query_params.get('end_date')} {request.query_params.get('end_time')}:00"
                    end_datetime = datetime.datetime.strptime(end_datetime, '%Y-%m-%d %H:%M:%S')
                    if end_datetime < now:
                        return JsonResponse({'ERROR': {"The arrival date is before today": ""}})
                    elif end_datetime < start_datetime:
                        return JsonResponse({'ERROR': {"The arrival dare is before the starting date": ""}})

                if request.GET.get('start_time'):
                    #gte lte is the equivalent of: >=, <=
                    queryset = queryset.filter(starting_datetime__gte=start_datetime)
                if request.GET.get('end_time'):
                    queryset = queryset.filter(end_datetime__lte=end_datetime)
                if request.GET.get('aircraft_code')=='Null' or request.GET.get('aircraft_code')=='Null':
                    queryset = queryset.filter(aircraft_name__isnull=True)#my_field__isnull=True

            my_list = serializers.serialize('json', queryset)
            my_json = json.loads(my_list)
            return JsonResponse({'flights': my_json})

    def post(self, request, format=None):
        """
        POST method to create a new flight. It's possibile to create a flight without aircraft.
        -from (string): starting airport code
        -from_coordinate [string]: a string pass like list with 2 decima coordinate
        -to (string): arrival airport code
        -to_coordinate [string]: a string pass like list with 2 decima coordinate
        -start_date (string): starting date in the format YYYY-MM-DD
        -end_date (string): arrival date in the format YYYY-MM-DD
        -start_time (string): starting time with the format HH:MM
        -end_time (string): end time with the format HH:MM
        -aircraft_code (string): unique aircraft code

        :return: json with flight's id
        """
        try:
            global end_datetime, start_datetime
            if request.method == 'POST':
                from datetime import datetime
                now = datetime.now()
                import datetime
                #inizio controlli sulla correttezza del dato inserito


                #recupero le coordinate delle città inserite
                from_coordinate = get_coordinates(request.query_params.get('from'))
                to_coordinate = get_coordinates(request.query_params.get('to'))


                if request.query_params.get('start_date') is not None or request.query_params.get('start_time') is not None:
                    start_datetime = f"{request.query_params.get('start_date')} {request.query_params.get('start_time')}:00"
                    start_datetime = datetime.datetime.strptime(start_datetime, '%Y-%m-%d %H:%M:%S')
                    if start_datetime < now:
                        return JsonResponse({'ERROR': {"La data di partenza è antecedente ad oggi": ""}})

                if request.query_params.get('end_date') is not None or request.query_params.get(
                        'end_time') is not None:
                    end_datetime = f"{request.query_params.get('end_date')} {request.query_params.get('end_time')}:00"
                    end_datetime = datetime.datetime.strptime(end_datetime, '%Y-%m-%d %H:%M:%S')
                    if end_datetime < now:
                        return JsonResponse({'ERROR': {"The arrival date is prior to the departure date": ""}})

                    if end_datetime < start_datetime:
                        return JsonResponse({'ERROR': {"The departure date is prior to the arrival date": ""}})

                if 'aircraft_code' in request.query_params:
                    aircraft = Aircrafts.objects.filter(name__contains=request.query_params.get('aircraft_code'))
                    if len(aircraft)==0:
                        return JsonResponse({'ERROR': {"the air not exist": ""}})

                    #check if the aircraft is avalaible
                    fligts= Flights.objects.filter(aircraft_name=aircraft.first())
                    fligts= fligts.filter(starting_datetime__gte=start_datetime)
                    fligts= fligts.filter(end_datetime__lte=end_datetime)
                    if len(fligts)>0:
                        return JsonResponse({'ERROR': {f"The air {aircraft.first().name} is busy": ""}})

                    aircraft_name=aircraft.first()

                else:
                    aircraft_name=None

                new_flight = Flights(_from=request.query_params.get('from'), to=request.query_params.get('to'), starting_datetime=start_datetime, end_datetime=end_datetime , aircraft_name=aircraft_name, _from_coordinate=str(from_coordinate), _to_coordinate=str(to_coordinate))
                new_flight.save()
                return JsonResponse({'SUCCESS': {"flight_id":new_flight.id}})
        except:
            return JsonResponse({'ERROR': {"ERROR: correct format": """
            -from (string): starting airport code
            -to (string): arrival airport code
            -start_date (string): starting date in the format YYYY-MM-DD
            -end_date (string): arrival date in the format YYYY-MM-DD
            -start_time (string): starting time with the format HH:MM
            -end_time (string): end time with the format HH:MM
            -aircraft_code (string): unique aircraft code
                """}})

    def put(self, request, format=None):
        """
        PUT method to add an aircraft in the flight. To renew and add aircraft
        -aircraft_code (string): aircraft unique code
        -new_aircraft_code (string): aircraft unique code
        :return: json with flight's id
        """
        #TODO: controlliamo se sta il nome nuovo ed l'ID dell'aereo
        aircraft_name = request.query_params.get('aircraft_code')
        aircraft = Aircrafts.objects.filter(name__contains=request.query_params.get('aircraft_code'))
        if len(aircraft)==0:
            #aggiungiamo un nuovo areo
            new_flight = Aircrafts(name=aircraft_name)
            new_flight.save()
            return JsonResponse({'SUCCESS': {"aereo non presente ed aggiunto alla flotta, aircraft_id": new_flight.id}})

        #TODO: recuperiamo il codice ID
        #request.query_params.get('new_aircraft_code')
        flight = Aircrafts.objects.get(id=aircraft.first().id)
        flight.aircraft_name = request.query_params.get('new_aircraft_code')
        flight.save()

        return JsonResponse({'UPDATE SUCCESS': {"flight_id": flight.id, "new_name": flight.aircraft_name}})


from django.shortcuts import render
from aviation_management_system.city_coordinate import get_coordinates

def mappa(request):
    flights = Flights.objects.all()

    for flight in flights:
        start_coordinate=get_coordinates(flight._from)
        end_coordinate=get_coordinates(flight.to)


    coordinate1 = (start_coordinate)  # Esempio di coordinate 1 (New York)
    coordinate2 = (end_coordinate)   # Esempio di coordinate 2 (Londra)

    context = {
        'coordinate1': coordinate1,
        'coordinate2': coordinate2,
    }

    return render(request, 'aviation_management_system/mappa.html', context)



