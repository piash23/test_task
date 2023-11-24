from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Parent, Child
from .serializers import ParentSerializer, ChildSerializer


class ParentTests(APITestCase):
    def test_create_parent(self):
        """
        Ensure we can create a new parent object.
        """
        url = reverse('userapp:parent-list')
        data = {'first_name': 'John', 'last_name': 'Doe', 'street': '123 Main St', 'city': 'Anytown', 'state': 'NY',
                'zip_code': '12345'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Parent.objects.count(), 1)
        self.assertEqual(Parent.objects.get().first_name, 'John')

    def test_get_parent(self):
        """
        Ensure we can get a parent object.
        """
        parent = Parent.objects.create(first_name='John', last_name='Doe', street='123 Main St', city='Anytown',
                                       state='NY', zip_code='12345')
        url = reverse('userapp:parent-detail', kwargs={'pk': parent.pk})
        response = self.client.get(url, format='json')
        serializer = ParentSerializer(parent)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_parent(self):
        """
        Ensure we can update a parent object.
        """
        parent = Parent.objects.create(first_name='John', last_name='Doe', street='123 Main St', city='Anytown',
                                       state='NY', zip_code='12345')
        url = reverse('userapp:parent-update', kwargs={'pk': parent.pk})
        data = {'first_name': 'Jane', 'last_name': 'Doe', 'street': '456 Elm St', 'city': 'Othertown', 'state': 'NY',
                'zip_code': '12345'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        parent.refresh_from_db()
        self.assertEqual(parent.first_name, 'Jane')
        self.assertEqual(parent.street, '456 Elm St')

    def test_delete_parent(self):
        """
        Ensure we can delete a parent object.
        """
        parent = Parent.objects.create(first_name='John', last_name='Doe', street='123 Main St', city='Anytown',
                                       state='NY', zip_code='12345')
        url = reverse('userapp:parent-delete', kwargs={'pk': parent.pk})
        response = self.client.delete(url, format='json', follow=True)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Parent.objects.count(), 0)


class ChildTests(APITestCase):
    def setUp(self):
        self.parent = Parent.objects.create(first_name='John', last_name='Doe', street='123 Main St', city='Anytown',
                                            state='NY', zip_code='12345')
        self.url = reverse('userapp:child-list', args=[self.parent.pk])

    def test_create_child(self):
        """
        Ensure we can create a new child object.
        """
        data = {'first_name': 'John', 'last_name': 'Doe'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Child.objects.count(), 1)
        self.assertEqual(Child.objects.get().first_name, 'John')

    def test_get_child(self):
        """
        Ensure we can get a child object.
        """
        child = Child.objects.create(first_name='John', last_name='Doe', parent=self.parent)
        url = reverse('userapp:child-detail', kwargs={'pk': child.pk})
        response = self.client.get(url, format='json')
        serializer = ChildSerializer(child)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_child(self):
        """
        Ensure we can update a child object.
        """
        child = Child.objects.create(first_name='John', last_name='Doe', parent=self.parent)
        url = reverse('userapp:child-update', kwargs={'pk': child.pk})
        data = {'first_name': 'Jane', 'last_name': 'Doe', 'parent': self.parent.pk}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        child.refresh_from_db()
        self.assertEqual(child.first_name, 'Jane')

    def test_delete_child(self):
        """
        Ensure we can delete a child object.
        """
        child = Child.objects.create(first_name='John', last_name='Doe', parent=self.parent)
        url = reverse('userapp:child-delete', kwargs={'pk': child.pk})
        response = self.client.delete(url, format='json', follow=True)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Child.objects.count(), 0)
