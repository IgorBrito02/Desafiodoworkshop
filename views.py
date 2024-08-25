from django.views.generic.edit import CreateView
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from .forms import CountryForm
from .models import Country
import requests
import json

# Dicionário de tradução das capitais
capital_translations = {
    "King Edward Point": "Cabo Rei Eduardo",
    "St. George's": "São Jorge",
    "Bern": "Berna",
    "Freetown": "Cidade Livre",
    "Budapest": "Budapeste",
    "Taipei": "Taipé",
    "Mata-Utu": "Mata-Utu",
    "Bridgetown": "Cidade da Ponte",
    "Adamstown": "Cidade de Adam",
    "Yamoussoukro": "Iamussucro",
    "Tunis": "Túnis",
    "Rome": "Roma",
    "Porto-Novo": "Porto-Novo",
    "Jakarta": "Jacarta",
    "Praia": "Praia",
    "Basseterre": "Basse-Terre",
    "Vientiane": "Vientiane",
    "Kralendijk": "Kralendijk",
    "Kampala": "Campala",
    "Andorra la Vella": "Andorra-a-Velha",
    "Gitega": "Gitega",
    "Pretoria": "Pretória",
    "Bloemfontein": "Bloemfontein",
    "Cape Town": "Cidade do Cabo",
    "Paris": "Paris",
    "Tripoli": "Trípoli",
    "Mexico City": "Cidade do México",
    "Libreville": "Libreville",
    "Saipan": "Saipã",
    "Skopje": "Escópia",
    "Beijing": "Pequim",
    "Sana'a": "Saná",
    "Gustavia": "Gustávia",
    "St. Peter Port": "Porto de São Pedro",
    "Honiara": "Honiara",
    "Longyearbyen": "Longyearbyen",
    "Tórshavn": "Tórshavn",
    "Tashkent": "Tashkent",
    "Cairo": "Cairo",
    "Dakar": "Dacar",
    "Sri Jayawardenepura Kotte": "Sri Jayawardenepura Kotte",
    "Ramallah": "Ramallah",
    "Jerusalem": "Jerusalém",
    "Dhaka": "Daca",
    "Lima": "Lima",
    "Singapore": "Singapura",
    "Ankara": "Ancara",
    "Kabul": "Cabul",
    "Oranjestad": "Oranjestad",
    "Avarua": "Avarua",
    "London": "Londres",
    "Lusaka": "Lusaca",
    "Helsinki": "Helsinque",
    "Niamey": "Niamei",
    "Flying Fish Cove": "Enseada do Peixe-Voado",
    "Fakaofo": "Fakaofo",
    "Bissau": "Bissau",
    "Baku": "Baku",
    "Saint-Denis": "Saint-Denis",
    "Djibouti": "Djibuti",
    "Pyongyang": "Pyongyang",
    "Port Louis": "Porto Luís",
    "Plymouth": "Plymouth",
    "Charlotte Amalie": "Charlotte Amalie",
    "Bogotá": "Bogotá",
    "Athens": "Atenas",
    "Zagreb": "Zagreb",
    "Rabat": "Rabat",
    "Algiers": "Argel",
    "Antarctica": "Antártica",
    "Amsterdam": "Amsterdã",
    "Khartoum": "Cartum",
    "Suva": "Suva",
    "Vaduz": "Vaduz",
    "Kathmandu": "Catmandu",
    "San Juan": "San Juan",
    "Tbilisi": "Tbilisi",
    "Islamabad": "Islamabad",
    "Monaco": "Mônaco",
    "Gaborone": "Gaborone",
    "Beirut": "Beirute",
    "Port Moresby": "Port Moresby",
    "Mamoudzou": "Mamoudzou",
    "Santo Domingo": "Santo Domingo",
    "Kingston": "Kingston",
    "Bouvet Island": "Ilha Bouvet",
    "Doha": "Doha",
    "Antananarivo": "Antananarivo",
    "New Delhi": "Nova Délhi",
    "Damascus": "Damasco",
    "Podgorica": "Podgorica",
    "Mbabane": "Mbabane",
    "Asunción": "Assunção",
    "San Salvador": "San Salvador",
    "Kyiv": "Kiev",
    "Douglas": "Douglas",
    "Windhoek": "Windhoek",
    "Abu Dhabi": "Abu Dhabi",
    "Sofia": "Sófia",
    "Nuuk": "Nuuk",
    "Berlin": "Berlim",
    "Phnom Penh": "Phnom Penh",
    "Baghdad": "Bagdá",
    "Port-aux-Français": "Port-aux-Français",
    "Stockholm": "Estocolmo",
    "Havana": "Havana",
    "Bishkek": "Biskek",
    "Moscow": "Moscovo",
    "Kuala Lumpur": "Kuala Lumpur",
    "São Tomé": "São Tomé",
    "Nicosia": "Nicósia",
    "Ottawa": "Ottawa",
    "Lilongwe": "Lilongwe",
    "Riyadh": "Riad",
    "Sarajevo": "Sarajevo",
    "Addis Ababa": "Addis Abeba",
    "Madrid": "Madri",
    "Ljubljana": "Liubliana",
    "Muscat": "Mascate",
    "Saint-Pierre": "Saint-Pierre",
    "Macau": "Macau",
    "City of San Marino": "Cidade de San Marino",
    "Maseru": "Maseru",
    "Majuro": "Majuro",
    "Philipsburg": "Philipsburg",
    "Reykjavik": "Reykjavik",
    "Luxembourg": "Luxemburgo",
    "Buenos Aires": "Buenos Aires",
    "Cockburn Town": "Cockburn Town",
    "Yaren": "Yaren",
    "West Island": "West Island",
    "El Aaiún": "El Aaiún",
    "Roseau": "Roseau",
    "San José": "San José",
    "Canberra": "Canberra",
    "Bangkok": "Bangkok",
    "Port-au-Prince": "Port-au-Prince",
    "Funafuti": "Funafuti",
    "Tegucigalpa": "Tegucigalpa",
    "Malabo": "Malabo",
    "Castries": "Castries",
    "Papeetē": "Papeetē",
    "Minsk": "Minsk",
    "Riga": "Riga",
    "Ngerulmud": "Ngerulmud",
    "Basse-Terre": "Basse-Terre",
    "Manila": "Manila",
    "Gibraltar": "Gibraltar",
    "Copenhagen": "Copenhague",
    "Yaoundé": "Yaoundé",
    "Conakry": "Conacri",
    "Manama": "Manama",
    "Paramaribo": "Paramaribo",
    "Kinshasa": "Kinshasa",
    "Mogadishu": "Mogadíscio",
    "Prague": "Praga",
    "Nouméa": "Nouméa",
    "Port Vila": "Port Vila",
    "Jamestown": "Jamestown",
    "Lomé": "Lomé",
    "Road Town": "Road Town",
    "Nairobi": "Nairóbi",
    "Alofi": "Alofi",
    "Heard Island and McDonald Islands": "Ilha Heard e Ilhas McDonald",
    "Kigali": "Quigali",
    "Tallinn": "Tallin",
    "Bucharest": "Bucareste",
    "Port of Spain": "Porto Espanha",
    "Georgetown": "Georgetown",
    "Dili": "Díli",
    "Hanoi": "Hanói",
    "Montevideo": "Montevidéu",
    "Vatican City": "Cidade do Vaticano",
    "City of Victoria": "Cidade de Vitória",
    "Vienna": "Viena",
    "Saint John's": "Saint John's",
    "Ashgabat": "Ashgabat",
    "Maputo": "Maputo",
    "Panama City": "Cidade do Panamá",
    "Palikir": "Palikir",
    "Dublin": "Dublin",
    "Willemstad": "Willemstad",
    "Cayenne": "Caiena",
    "Victoria": "Victoria",
    "Diego Garcia": "Diego Garcia",
    "Guatemala City": "Cidade da Guatemala",
    "Quito": "Quito",
    "Fort-de-France": "Fort-de-France",
    "Dushanbe": "Duchambé",
    "Valletta": "Valeta",
    "Banjul": "Banjul",
    "Abuja": "Abuja",
    "Nassau": "Nassau",
    "Pristina": "Pristina",
    "Kuwait City": "Cidade do Kuwait",
    "Malé": "Malé",
    "Juba": "Juba",
    "Tehran": "Teerã",
    "Tirana": "Tirana",
    "Brasília": "Brasília",
    "Belgrade": "Belgrado",
    "Belmopan": "Belmopan",
    "Naypyidaw": "Naypyidaw",
    "Thimphu": "Thimphu",
    "Caracas": "Caracas",
    "Monrovia": "Monróvia",
    "Kingston": "Kingston",
    "Warsaw": "Varsóvia",
    "George Town": "George Town",
    "Bandar Seri Begawan": "Bandar Seri Begawan",
    "Moroni": "Moroni",
    "Hagåtña": "Hagåtña",
    "Nuku'alofa": "Nuku'alofa",
    "South Tarawa": "South Tarawa",
    "Accra": "Acra",
    "N'Djamena": "N'Djamena",
    "Harare": "Harare",
    "Marigot": "Marigot",
    "Ulan Bator": "Ulaanbaatar",
    "Lisbon": "Lisboa",
    "Pago Pago": "Pago Pago",
    "Brazzaville": "Brazzaville",
     "Brussels": "Bruxelas",
    "Jerusalem": "Jerusalém",
    "Wellington": "Wellington",
     "Managua": "Manágua",
    "The Valley": "The Valley",
    "Chișinău": "Chisinau",
    "Bamako": "Bamaco",
    "Stanley": "Stanley",
    "Yerevan": "Erevã",
    "Apia": "Apia",
    "Saint Helier": "Saint Helier",
    "Tokyo": "Tóquio",
    "Sucre": "Sucre",
    "Santiago": "Santiago",
    "Washington, D.C.": "Washington, D.C.",
    "Kingstown": "Kingstown",
    "Hamilton": "Hamilton",
    "Victoria": "Victoria",
    "Diego Garcia": "Diego Garcia",
    "Guatemala City": "Cidade da Guatemala",
    "Quito": "Quito",
    "Fort-de-France": "Fort-de-France",
    "Dushanbe": "Duchambé",
    "Valletta": "Valeta",
    "Banjul": "Banjul",
    "Abuja": "Abuja",
    "Nassau": "Nassau",
    "Pristina": "Pristina",
    "Kuwait City": "Cidade do Kuwait",
    "Malé": "Malé",
    "Juba": "Juba",
    "Tehran": "Teerã",
    "Tirana": "Tirana",
    "Brasília": "Brasília",
    "Belgrade": "Belgrado",
    "Belmopan": "Belmopan",
    "Naypyidaw": "Naypyidaw",
    "Thimphu": "Thimphu",
    "Caracas": "Caracas",
    "Monrovia": "Monróvia",
    "Kingston": "Kingston",
    "Warsaw": "Varsóvia",
    "George Town": "George Town",
    "Bandar Seri Begawan": "Bandar Seri Begawan",
    "Moroni": "Moroni",
    "Hagåtña": "Hagåtña",
    "Nuku'alofa": "Nuku'alofa",
    "South Tarawa": "Tarawa do Sul",
    "Accra": "Acra",
    "N'Djamena": "N'Djamena",
    "Harare": "Harare",
    "Marigot": "Marigot",
    "Ulaanbaatar": "Ulan Bator",
    "Lisbon": "Lisboa",
    "Pago Pago": "Pago Pago",
    "Brazzaville": "Brazzaville",
    "Brussels": "Bruxelas",
    "Jerusalem": "Jerusalém",
    "Wellington": "Wellington",
    "Managua": "Manágua",
    "The Valley": "The Valley"
    # Adicione outras capitais conforme necessário
}

# Função para detalhes de um país
def country_detail(request):
    if request.method == 'GET':
        # Faz uma solicitação para obter os dados do país
        response = requests.get(f'https://restcountries.com/v3.1/all/')

        # Verifica se a solicitação foi bem-sucedida
        if response.status_code == 200:
            country_data = response.json()
            # Renderiza um template com os dados do país
            return render(request, 'country_detail.html', {'country': country_data})
        else:
            # Em caso de erro, redireciona para a lista de países com uma mensagem de erro
            return redirect('country_list')  # Ou você pode redirecionar para uma página de erro específica
    else:
        # Caso o método não seja GET, redireciona para a lista de países
        return redirect('country_list')

# Função para criar um país
@csrf_exempt
@require_http_methods(["POST", "GET"])
def country_create(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            # Salva o país no banco de dados
            form.save()
            # Redireciona para a lista de países após a criação
            return redirect('country_list')
    else:
        # Se o método for GET, exibe o formulário de criação
        form = CountryForm()
    
    # Renderiza o template com o formulário
    return render(request, 'country_form.html', {'form': form})

# Função para listar todos os países
def country_list(request):
    countries = Country.objects.all()
    return render(request, 'country_list.html', {'countries': countries})

# Função para atualizar um país existente
@csrf_exempt
@require_http_methods(["POST", "GET"])
def country_update(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == 'POST':
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            return redirect('country_list')  # Redireciona para a lista de países após a atualização
    else:
        form = CountryForm(instance=country)
    return render(request, 'country_form.html', {'form': form})

# Função para deletar um país
@csrf_exempt
@require_http_methods(["POST", "GET"])
def country_delete(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == 'POST':
        country.delete()
        return redirect('country_list')  # Redireciona para a lista de países após a deleção
    return render(request, 'country_confirm_delete.html', {'country': country})

# Função para renderizar a primeira página
def first(request):
    return render(request, "countries_data.html")

# Função para renderizar a página 'about'
def about(request):
    return HttpResponse("<h1 style='color:red;'>THIS IS ANOTHER DJANGO VIEW</h1>")

# Função para renderizar a página 'index'
def index(request):
    string = "I am from views file"
    data = ["red", "green", "blue", "magenta", "black"]
    context = {"colors": data, "string": string}
    return render(request, "index.html", context)

# Função para listar todos os países da API externa e traduzir as capitais
def countries(request):
    response = requests.get('https://restcountries.com/v3.1/all')
    data = response.json()

    # Traduzir capitais para português
    for country in data:
        if country.get('capital') and country['capital'][0] in capital_translations:
            country['capital'][0] = capital_translations[country['capital'][0]]

    context = {
        'title': 'All Countries',
        'data': data
    }
    return render(request, 'countries_data.html', context)