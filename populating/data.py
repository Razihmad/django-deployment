import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','populating.settings')

import django
django.setup()


# faker pop up

import random
from myapp.models  import AccessRecord,Webpage,Topic

from faker import Faker

fake = Faker()

topics = ['Search','Social','Marketplace','Game','News']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()

    return t

def populte(N=5):

    for entry in range(N):

        top = add_topic()

        fake_url = fake.url()
        fake_date = fake.date()
        fake_name = fake.company()
        # create the new webpage entry
        w = Webpage.objects.get_or_create(topic= top,name=fake_name,url=fake_url)[0]

        # create a fake ACCESSRECORS

        acc = AccessRecord.objects.get_or_create(name=w,date=fake_date)[0]


if __name__ == "__main__":
    print("populating")
    populte(20)
    print("populating complete")
    

