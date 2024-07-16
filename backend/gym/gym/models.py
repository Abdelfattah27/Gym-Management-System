from django.db import models
from authen.models import User

class DeletedModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
    def all_objects(self):
        return super().get_queryset()
    def delete(self):
        # Instead of deleting the objects, set is_deleted=True for all of them
        self.get_queryset().update(is_deleted=True)

class BaseModel (models.Model) : 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User , on_delete=models.SET_NULL , null=True)
    updated_by = models.ForeignKey(User , on_delete=models.SET_NULL , null= True) 
    is_deleted = models.BooleanField(default=False) 
    objects = DeletedModelManager()
    class Meta:
        abstract = True

    def delete(self):
        self.is_deleted = True
        self.save()
        for related_object in self._meta.related_objects:
            if related_object.on_delete == models.CASCADE:
                if hasattr(self , related_object.get_accessor_name()) :
                    related_manager = getattr(self, related_object.get_accessor_name())
                    try : 
                        for related_item in related_manager.all():
                            related_item.delete()
                    except : 
                        related_manager.delete()

    def undelete(self):
        self.is_deleted = False
        self.save()
