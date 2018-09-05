from django.db import models


class Page(models.Model):
    header = models.IntegerField(default=0)    # 0 -> null
    sidebar = models.IntegerField(default=0)
    footer = models.IntegerField(default=0)
    section_num = models.IntegerField(default=0)


class Section(models.Model):
    page_id = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    name = models.CharField(max_length=64, default="")


class Block(models.Model):
    pos_x = models.IntegerField(default=0)
    pos_y = models.IntegerField(default=0)
    width = models.IntegerField(default=1)
    height = models.IntegerField(default=1)
    content_type = models.CharField(max_length=64, default="")
    section_id = models.IntegerField(default=0)


class Text(models.Model):
    block = models.OneToOneField(Block, on_delete=models.CASCADE)
    content = models.TextField()
    font_size = models.CharField(max_length=64, default="16px")
    font_color = models.CharField(max_length=64, default="black")
    background_color = models.CharField(max_length=64, default="white")


class Pic(models.Model):
    block = models.OneToOneField(Block, on_delete=models.CASCADE)
    content = models.ImageField(upload_to='img')
    name = models.CharField(max_length=100, default="anonymous")


class TextPic(models.Model):
    block = models.OneToOneField(Block, on_delete=models.CASCADE)
    content = models.TextField()
    font_size = models.CharField(max_length=64, default="16px")
    font_color = models.CharField(max_length=64, default="black")
    background_image = models.ImageField(upload_to='img')
    type = models.IntegerField(default=0)

    TYPE_BACKGROUND = 1
    TYPE_CARD = 2
    TYPE_COMMENT = 3
