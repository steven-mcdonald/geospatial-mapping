import json
import os

savepath = '../resources/air'

selected_routes_dict = {
    'London': {
        'London to LA': ['LHR', 'LAX'],
        'London to NYC': ['LHR', 'JFK'],
        'London to Orlando': ['LHR', 'MCO'],
        'London to Vancouver': ['LHR', 'YVR'],
        'London to Gibraltar': ['LHR', 'GIB'],
        'London to Malta': ['LHR', 'MLA'],
        'London to Oslo': ['LHR', 'OSL'],
        'London to Bergen': ['LHR', 'BGO'],
        'London to Dubai': ['LHR', 'DXB'],
        'London to Vietnam': ['LHR', 'SGN'],
        'London to KL': ['LHR', 'KUL'],
        'London to Sao Paulo': ['LHR', 'GRU'],
        'London to Rio': ['LHR', 'GIG'],
        'London to Buenos Aires': ['LHR', 'EZE'],
        'Buenos Aires to Tierra del Fuego': ['EZE', 'USH'],
        'London to Athens': ['LHR', 'ATH'],
        'Athens to Dubai': ['ATH', 'DXB'],
        'Dubai to Bangkok': ['DXB', 'BKK'],
        'Bangkok to Sydney': ['BKK', 'SYD'],
        'Sydney to Auckland': ['SYD', 'AKL'],
        'Auckland to Wellington': ['AKL', 'WLG'],
        'Auckland to Fiji': ['AKL', 'NAN'],
        'Fiji to Cook Islands': ['NAN', 'RAR'],
        'Cook Islands to Tahiti': ['RAR', 'PPT'],
        'Tahiti to Los Angeles': ['PPT', 'LAX'],
        'Los Angeles to Mexico City': ['LAX', 'MEX'],
        },

    'Paris': {
        'Paris to Singapore': ['CDG', 'SIN'],
        'Paris to Saudi Arabia': ['CDG', 'RUH'],
        'Paris to Havana': ['CDG', 'HAV'],
        'Paris to Aruba': ['CDG', 'AUA'],
        'Paris to Cairo': ['CDG', 'CAI'],
        'Paris to Brazzaville': ['CDG', 'BZV'],
        'Paris to Point Noire': ['CDG', 'PNR'],
        'Paris to Accra Ghana': ['CDG', 'ACC'],
        'Paris to Luanda Angola': ['CDG', 'LAD'],
        'Paris to Johannesburg': ['CDG', 'JNB'],
        'Johannesburg to Maputo Mozambique': ['JNB', 'MPM'],
        'Paris to Houston': ['CDG', 'IAH'],
        'Paris to Vancouver': ['CDG', 'YVR'],
        'Los Angeles to Vancouver': ['LAX', 'YVR'],
        'Paris to Montreal': ['LHR', 'YUL'],
        },

    'Singapore': {
        'Singapore to Tokyo': ['SIN', 'HND'],
        'Singapore to Seoul': ['SIN', 'ICN'],
        'Seoul to Busan': ['ICN', 'PUS'],
        'Singapore to Bali': ['SIN', 'DPS'],
        'Bali to Lombok': ['DPS', 'LOP'],
        'Singapore to Manado': ['SIN', 'MDC'],
        'Singapore to Auckland': ['SIN', 'AKL'],
        'Singapore to Bangkok': ['SIN', 'BKK'],
        'Singapore to Yangon Myanmar': ['SIN', 'RGN'],
        'Singapore to Siem Reap Cambodia': ['SIN', 'SIA'],
        'Singapore to Brunei': ['SIN', 'BWN'],
        'Singapore to Borneo': ['SIN', 'BKI'],
        'Singapore to Kota Bharu': ['SIN', 'KBR'],
        'Singapore to Langkawi': ['SIN', 'LGK'],
        'Singapore to Krabi': ['SIN', 'KBV'],
        'Singapore to Beijing': ['SIN', 'PKX'],
        'Beijing to Khabarovsk': ['PKX', 'KHV'],
        'Khabarovsk to Magadan': ['KHV', 'GDX'],
        }
    }

# oslo_routes_dict = {
#     # 'Oslo to Kirkenes': ['OSL', 'KKN'],
#     # 'Oslo to Miami': ['OSL', 'MIA'],
#     # 'Oslo to New York': ['OSL', 'JFK'],
#     # 'Oslo to Houston': ['OSL', 'IAH'],
#     # 'Oslo to Dublin': ['OSL', 'DUB'],
#     'Frankfurt to JFK': ['FRA', 'JFK']
# }

with open(os.path.join(savepath, 'selected_routes.json'), 'w') as f:
    json_dumps_str = json.dumps(selected_routes_dict, indent=4)
    print(json_dumps_str, file=f)

print()
