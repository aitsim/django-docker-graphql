import pytest
import json
from django.urls import reverse
from django.test import Client

@pytest.mark.django_db
def test_create_user():


   mutation = """
        mutation {
         createActor(input: {name: "med"} ) {
         ok
         actor {
               id
               name
                }
                }
        }
                """
   response = Client().post(reverse('graphql_api'), data={'query': mutation})






   assert response.status_code == 200
   # ?\assert response.json()['data']['createUser']['user']['id']
   #  # assert response.json()['data']['createUser']['token']
   # assert User.objects.filter(email=email).exists()