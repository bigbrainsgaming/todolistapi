from django.db import models

# Create your models here.
class Task(models.Model):
    task_title = models.CharField(max_length=300, blank=False, default='')
    order_no = models.IntegerField(null=False, default=0)
    
    class Meta:
        db_table = "task"


    def save(self, *args, **kwargs):
        if self._state.adding == False:
            
            instance = self.__class__.objects.filter(id=self.id).first()
            if instance is not None:
                instance.task_title = self.task_title
        
        elif self._state.adding == True:
            latest = self.__class__.objects.order_by('-order_no').first()
        
            if latest is not None:
                self.order_no = int(latest.order_no) + 1
            else:
                self.order_no = 1
                
        super(Task,self).save()

    def move(self,new_order_no, *args, **kwargs):
        latest = self.__class__.objects.order_by('-order_no').first()
        lowest = self.__class__.objects.order_by('order_no').first()
        current_order_no = int(self.order_no)
    
        if int(new_order_no) == int(latest.order_no):
            all_tasks = self.__class__.objects.filter(order_no__lte=latest.order_no)
            for task in all_tasks:
                task.order_no = int(task.order_no) - 1
        elif int(new_order_no) == int(lowest.order_no):
            all_tasks = self.__class__.objects.filter(order_no__gte=lowest.order_no)
            for task in all_tasks:
                task.order_no = int(task.order_no) + 1
        # current_order_no    9
        # new_order_no        3                
        elif int(current_order_no) > int(new_order_no):
            all_tasks = self.__class__.objects.filter(order_no__gte=new_order_no,order_no__lt=current_order_no)
            for task in all_tasks:
                task.order_no = int(task.order_no) + 1
        # current_order_no    3
        # new_order_no        9                
        elif int(current_order_no) < int(new_order_no):
            all_tasks = self.__class__.objects.filter(order_no__gt=current_order_no,order_no__lte=new_order_no)
            for task in all_tasks:
                task.order_no = int(task.order_no) - 1
       

        self.__class__.objects.bulk_update(all_tasks,['order_no'])
        
        self.order_no = new_order_no
        result = self.save(update_fields=['order_no'])
        print(result)
        return

    def delete(self,*args,**kwargs):
        max_task = self.__class__.objects.order_by("-order_no").first()
        if int(max_task.order_no) > int(self.order_no):
            all_tasks = self.__class__.objects.filter(order_no__gte=self.order_no,order_no__lte=int(max_task.order_no))
            for task in all_tasks:
                task.order_no = int(task.order_no) - 1

            self.__class__.objects.bulk_update(all_tasks, ['order_no'])    

        super(Task,self).delete(*args, **kwargs)