import folium
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Pokemon, PokemonEntity

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


def get_current_time(zone='Europe/Moscow'):
    tz = timezone.pytz.timezone(zone)
    current_time = timezone.localtime().astimezone(tz)
    return current_time    


def show_all_pokemons(request): 
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemons_entities = PokemonEntity.objects.filter(appeared_at__lt=get_current_time(), 
        disappeared_at__gt=get_current_time())
    for pokemon_entity in pokemons_entities:
        add_pokemon(
            folium_map, pokemon_entity.latttude,
            pokemon_entity.longitude,
            request.build_absolute_uri(pokemon_entity.pokemon.photo.url)
        )       

    pokemons = Pokemon.objects.all()
    pokemons_on_page = []
    for pokemon in pokemons:
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
    requested_pokemon = get_object_or_404(Pokemon,id=pokemon_id)
   
    pokemons_entities = PokemonEntity.objects.filter(pokemon=requested_pokemon,appeared_at__lt=get_current_time(), 
        disappeared_at__gt=get_current_time())
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemons_entities:
        add_pokemon(
            folium_map, pokemon_entity.latttude,
            pokemon_entity.longitude,
            request.build_absolute_uri(requested_pokemon.photo.url)
        )

    if requested_pokemon.previous_evolution:
        previous_evolution = {
            'title_ru': requested_pokemon.previous_evolution.title,
            'pokemon_id': requested_pokemon.previous_evolution.id,
            'img_url': request.build_absolute_uri(requested_pokemon.previous_evolution.photo.url)
        }
    else:
        previous_evolution = None

    if requested_pokemon.next_evolution.first():
        next_evolution = {
            'title_ru': requested_pokemon.next_evolution.first().title,
            'pokemon_id': requested_pokemon.next_evolution.first().id,
            'img_url': request.build_absolute_uri(requested_pokemon.next_evolution.first().photo.url)
        }
    else:
        next_evolution = None

    pokemons_on_page = {
            'pokemon_id': pokemon_id,
            'img_url':  request.build_absolute_uri(requested_pokemon.photo.url),
            'title_ru': requested_pokemon.title,
            'description': requested_pokemon.description,
            'title_en': requested_pokemon.title_en,
            'title_jp': requested_pokemon.title_jp,
            'previous_evolution': previous_evolution,
            'next_evolution': next_evolution
    }


    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemons_on_page,
    })

