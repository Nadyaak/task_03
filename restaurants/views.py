from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {'my_list': [
    {"restaurant_name":"Anoosh","food_type":"Dessert"},
    {"restaurant_name":"Five guys","food_type":"Fast food"},
    {"restaurant_name":"Pizza hut","food_type":"Pizza"}
    ]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {"my_object" :
     {"restaurant_name":"Anoosh"
    ,"food_type":"Dessert" 
    , "favorite":"it is my favorite restaurant"}


    }
    return render(request, 'detail.html', context)
