from django.db import models
from django.urls import reverse


class MenuInstance(models.Model):
    name = models.CharField(max_length=100)
    init_url = models.CharField(max_length=100, blank=True, null=True, unique=True)
    final_url = models.CharField(max_length=100, blank=True, null=True, unique=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.init_url:
            divided_init_url = str(self.init_url).split()
            url_name = divided_init_url[0]
            rest = divided_init_url[1:]
            rev_div_url = reverse(url_name, args=rest)
            if self.final_url:
                if self.final_url != rev_div_url:
                    raise Exception("Final_url is not the same as init_url!")

            else:
                self.final_url = rev_div_url
        super(MenuInstance, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def children(self):
        return self.menuinstance_set.all()

    def get_children_ids(self):
        if self.parent:
            return self.parent.get_children_ids() + [self.parent.id]
        else:
            return []
