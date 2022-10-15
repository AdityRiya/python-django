import imp
from operator import imod
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','app1.settings')
import django
django.setup()
import random
from app1.models import AccessRecord,Topic,Webpage
from faker import Faker
fakegen = Faker()
topics=['Search','Social','Marketplace','News','Games']