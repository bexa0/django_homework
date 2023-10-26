from django.shortcuts import render
from app_hw.models import Character, MainCharacter, GuideGame, Episode, Items

# Create your views here.


def project_concept(request):
    return render(request, 'index.html')


def episode_page(request):
    episode = Episode.objects.all()
    context = {'episode_list': episode}

    return render(request, 'episodes_index.html', context=context)


def main_character_page(request):
    mainchar = MainCharacter.objects.all()
    context = {'mainchar_list': mainchar}

    return render(request, 'mainCharacter.html', context=context)


def characters(request):
    characters = Character.objects.all()
    context = {'character_list': characters}

    return render(request, 'characters.html', context=context)


def guide_game_page(request):
    guide = GuideGame.objects.all()
    context = {'guide_game_list': guide}

    return render(request, 'guides.html', context=context)


def item_page(request):
    item = Items.objects.all()
    context = {'items_list': item}

    return render(request, 'item.html', context=context)

