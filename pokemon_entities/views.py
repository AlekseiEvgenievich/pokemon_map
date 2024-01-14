import folium
import json
import requests
import datetime
import pytz
import datetime
from django.utils import timezone

from django.http import HttpResponseNotFound
from django.shortcuts import render

from .models import Pokemon,PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)
 

def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request): 
   # with open('pokemon_entities/pokemons.json', encoding='utf-8') as database:
   #     pokemons = json.load(database)['pokemons']
   # pokemons = Pokemon.objects.all()
    moscow_tz = timezone.pytz.timezone('Europe/Moscow')
    current_time = timezone.localtime().astimezone(moscow_tz)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemons_entities = PokemonEntity.objects.filter(appeared_at__lt=current_time, 
        disappeared_at__gt=current_time)
    for pokemon_entity in pokemons_entities:
        add_pokemon(
            folium_map, pokemon_entity.latttude,
            pokemon_entity.longitude,
            request.build_absolute_uri(pokemon_entity.pokemon.photo.url)
        )       

    pokemons = Pokemon.objects.all()
    pokemons_on_page = []
    for pokemon in pokemons:
        if pokemon.photo:
            print(pokemon.photo.url)
            pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url':  request.build_absolute_uri(pokemon.photo.url),
            'title_ru': pokemon.title,
            })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })



def show_pokemon(request, pokemon_id):
#    with open('pokemon_entities/pokemons.json', encoding='utf-8') as database:
#        pokemons = json.load(database)['pokemons']
    requested_pokemon = Pokemon.objects.get(id=pokemon_id)
#    for pokemon in pokemons:
#        if pokemon['pokemon_id'] == int(pokemon_id):
#            requested_pokemon = pokemon
#            break
#    else:
#        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    pokemons_dict = {"2":{"title_ru": "Бульбазавр","img_url": "https://upload.wikimedia.org/wikipedia/ru/c/ca/%D0%91%D1%83%D0%BB%D1%8C%D0%B1%D0%B0%D0%B7%D0%B0%D0%B2%D1%80.png"},
       "3":{"title_ru": "Ивизавр","img_url": "https://vignette.wikia.nocookie.net/pokemon/images/7/73/002Ivysaur.png/revision/latest/scale-to-width-down/200?cb=20150703180624&path-prefix=ru"},
       "4":{ "title_ru": "Венузавр","img_url": "https://vignette.wikia.nocookie.net/pokemon/images/a/ae/003Venusaur.png/revision/latest/scale-to-width-down/200?cb=20150703175822&path-prefix=ru"}
    }
    pokemons_entities = PokemonEntity.objects.filter(pokemon=requested_pokemon)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemons_entities:
        add_pokemon(
            folium_map, pokemon_entity.latttude,
            pokemon_entity.longitude,
            request.build_absolute_uri(pokemons_dict[pokemon_id]["img_url"])
        )
    #if requested_pokemon.photo:
    pokemons_on_page = {
            'pokemon_id': pokemon_id,
            'img_url':  pokemons_dict[pokemon_id]["img_url"],
            'title_ru': pokemons_dict[pokemon_id]["title_ru"],
            'description': requested_pokemon.description,
            'title_en': requested_pokemon.title_en,
            'title_jp': requested_pokemon.title_jp
    }


    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon':pokemons_on_page ,
    })

