from django.db import models

# Create your models here.


class Ssrnpaper(models.Model):
    gid = models.IntegerField(unique=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    downloads = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ssrnpaper'

    # def __str__(self):
    #     return self.title

    def __unicode__(self):
        # return self.title
        return self.gid, self.title, self.author, self.link, self.downloads

# search function
