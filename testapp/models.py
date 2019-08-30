from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=250)
    USER_MAN, USER_WOMAN = 'M', 'N'
    USER_TYPE = (
        (USER_MAN, '남성'),
        (USER_WOMAN, '여성'),
    )
    sex = models.CharField(max_length=1, choices=USER_TYPE)
