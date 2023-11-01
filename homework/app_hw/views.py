from django.shortcuts import render
from app_hw.models import Character, MainCharacter, GuideGame, Episode, Items

# Create your views here.


def project_concept(request):
    epis = Episode.objects.all()
    char = Character.objects.all()
    main_char = MainCharacter.objects.all()
    guide = GuideGame.objects.all()
    item = Items.objects.all()
    context = {'episodes': epis, 'character': char, 'main_character': main_char, 'guides': guide, 'items': item}

    return render(request, 'index.html', context=context)


# def book_detail_view(request, book_slug):
#     book = Episode.objects.get(slug=book_slug)
#     context = {'books': book}
#
#     return render(request, 'book_detail.html', context=context)


def episode_page(request, pk):
    epis = Episode.objects.get(id=pk)
    episode = Episode.objects.all()
    context = {'episode_list': episode, 'episodes': epis}

    return render(request, 'episodes_index.html', context=context)


def main_character_page(request, pk):
    main_char = MainCharacter.objects.get(id=pk)
    mainchar = MainCharacter.objects.all()
    context = {'mainchar_list': mainchar, 'main_char': main_char}

    return render(request, 'mainCharacter.html', context=context)


def characters(request, pk):
    char = Character.objects.get(id=pk)
    characters = Character.objects.all()
    context = {'character_list': characters, 'chars': char}

    return render(request, 'characters.html', context=context)


def guide_game_page(request, pk):
    guide_gm = GuideGame.objects.get(id=pk)
    guide = GuideGame.objects.all()
    context = {'guide_game_list': guide, 'guides': guide_gm}

    return render(request, 'guides.html', context=context)


def item_page(request, pk):
    item_p = Items.objects.get(id=pk)
    item = Items.objects.all()
    context = {'items_list': item, 'items': item_p}

    return render(request, 'item.html', context=context)

