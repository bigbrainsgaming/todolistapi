from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=300, blank=False, default='')
    order_no = models.IntegerField(null=False, default=0)
    
    class Meta:
        db_table = "task"

    def __get_next_order_no(self):
        next = self.objects.order_by("-order_no").first()
        if next is None:
            return 0
        else:
            return next.order_no

    # get all items within curr_order_no and new_order_no
    # if new_order_no > curr_order_no all items order_no +1
    # if new_order_no < curr_order_no all items order_no -1
    def save(self,*args,**kwargs):
        if self.id is None:
            next_order_no = self.__get_next_order_no()
            self.order_no = int(next_order_no) + 1
        else:
            all_tasks= self.objects
            if int(self.current_order_no) > int(self.new_order_no):
                for task in all_tasks.filter(order_no__gt = self.current_order_no, order_no__lte = self.new_order_no):
                    task.order_no = task.order_no + 1
            elif int(self.current_order_no) < int(new_order_no):
                for task in all_tasks.filter(order_no__gt = self.new_order_no, order_no__lte = self.current_order_no):
                    task.order_no = task.order_no - 1
                self.objects.bulk_update(all_tasks,['order_no'])
                self.order_no = self.new_order_no
        
        super(Task,self).save(*args,**kwargs)
