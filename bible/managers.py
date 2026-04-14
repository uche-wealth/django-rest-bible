from django.db import models

class BookManager(models.Manager):
    """
    Book Manager
    """
    # use for related fields
    use_for_related_fields = True

    def get_old_testament(self):
        return self.get_queryset().filter(is_new_testament=False)

    def get_new_testament(self):
        return self.get_queryset().filter(is_new_testament=True)
    
    def get_gospels(self):
        return self.get_queryset().filter(is_new_testament=True, number__gte=40, number__lte=43)
    
    def get_epistles(self):
        return self.get_queryset().filter(is_new_testament=True, number__gt=43)


