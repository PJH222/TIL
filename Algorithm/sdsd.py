import random

def lunch(request):
    menu_numbers = random.sample(range(1, 8), 1)
    lunch_menu = ['김치찌개', '된장찌개', '마라탕', '콜라', '떡볶이', '자장면', '돈까스']
    print(menu_numbers)
    menu_recommand = lunch_menu[menu_numbers[0]]

    return render(request, 'lunch.html', {
        'menu_recommand': menu_recommand,
    })

lunch(1)