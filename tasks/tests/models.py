from django.test import TestCase
from tasks.models import Task


class TaskTestCase(TestCase):

    def setUp(self):
        pass


    def tearDown(self):
        pass


    # test to check if the order_no increments by 1 after creating another task.
    def test_create(self):
        t1 = Task.objects.create(task_title='first task')
        t2 = Task.objects.create(task_title='second task')
        t3 = Task.objects.create(task_title='third task')

        self.assertEqual(int(t1.order_no),1)
        self.assertEqual(t1.task_title,'first task')
        self.assertEqual(int(t2.order_no),2)
        self.assertEqual(t2.task_title,'second task')
        self.assertEqual(int(t3.order_no),3)
        self.assertEqual(t3.task_title,'third task')

    # test to check if updating order_no or simply changing task title works
    def test_update(self):
        t1 = Task.objects.create(task_title='a')
        t2 = Task.objects.create(task_title='b')
        t3 = Task.objects.create(task_title='c')

        t1.task_title='a'
        t1.save()
        t1 = Task.objects.filter(order_no=1).first()
        self.assertEqual(t1.task_title,'a')

        t1.move(new_order_no=3)
        
        t4 = Task.objects.filter(task_title='a').first()
        self.assertEqual(int(t4.order_no),3)

        st = Task.objects.filter(task_title='b').first()
        self.assertEqual(int(st.order_no),1)

        tt = Task.objects.filter(task_title='c').first()
        self.assertEqual(int(tt.order_no),2)

    # test to check if order-no is being updated as we try to delete a task anywhere.
    def test_delete(self):
        t1 = Task.objects.create(task_title='a')
        t2 = Task.objects.create(task_title='b')
        t3 = Task.objects.create(task_title='c')

        deleted_id = t1.id
        t1.delete()

        deleted = Task.objects.filter(id=deleted_id).first()
        self.assertEqual(deleted, None)

        t2 = Task.objects.filter(task_title='b').first()
        t3 = Task.objects.filter(task_title='c').first()

        self.assertEqual(t2.order_no,1)
        self.assertEqual(t3.order_no,2)