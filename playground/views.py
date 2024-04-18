from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product,OrderItem,Order,Customer,Collection
from django.db.models.aggregates import Count,Sum,Avg,Min,Max
from django.db.models import Q,F,Value,Func,Count
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from tags.models import TaggedItem
from django.db import transaction
from django.db import connection
def say_hello(request):
    return render(request, 'index.html', {"name":"leole"})
        