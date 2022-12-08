from rest_framework.test import APIClient

from django.test import TestCase
from tasks.models import Task
from tasks.serializers import TaskSerializer
import json


class SimpleTest(TestCase):
    test_data = [
            {'task_title': 'first title'},
            {'task_title': 'second title'},
            {'task_title': 'third title'},
            {'task_title': 'fourth title'},
            {'task_title': 'fifth title'},
        ]


    def setup(self):
        self.client = APIClient()
        

    def test_list_connectivity(self):
        response = self.client.head('/tasks/')
        self.assertEqual(response.status_code,200)


    def test_create(self):
        response = self.client.post('/tasks/', {'task_title': 'first title'}, format='json')
        data = json.loads(response.content)
        self.assertEqual(int(data['order_no']),1)


    def test_retrieve_by_id(self):
        t = Task.objects.create(task_title='First Task')
        result = self.client.get('/tasks/'+str(t.id)+'/', format='json')
        test = json.loads(result.content)
        self.assertEqual(test,{'id':1,'task_title':'First Task','order_no':1})


    def test_update_by_id(self):
        t = Task.objects.create(task_title=self.test_data[0])

        # send a task object to POST 
        data = {'task_title':'updated_task_title'}
        # send a partial update to PUT
        response = self.client.put('/tasks/'+str(t.id)+'/', data, content_type='application/json')
        
        test = Task.objects.filter(id=t.id).first()
        self.assertEqual(test.task_title, 'updated_task_title')


    def test_delete_by_id(self):
        # send a task object to POST 
        response = self.client.post('/tasks/', self.test_data[0], format='json')
        x = json.loads(response.content)
        
        result = self.client.delete('/tasks/'+str(x['id'])+'/')
        self.assertEqual(result.status_code, 204)


    def test_movetask_by_id(self):
        new_order_no=1
        for d in self.test_data:
            t = Task.objects.create(task_title=d['task_title'])

        # move_item(self, request, pk=None, new_order_no=None)
        response = self.client.post('/tasks/1/move/5/')

        task = Task.objects.filter(id=1).first()

        self.assertEqual(task.order_no,5)

       