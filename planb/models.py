from django.db import models


class Page(models.Model):
    header = models.IntegerField(default=0)    # 0: null
    sidebar = models.IntegerField(default=0)
    footer = models.IntegerField(default=0)
    section_num = models.IntegerField(default=0)


class Section(models.Model):
    page_id = models.IntegerField(default=0)
    style = models.CharField(max_length=64, default="")  # 10 styles
    name = models.CharField(max_length=64, default="")
    level = models.IntegerField(default=0)


class Block(models.Model):
    content_type = models.CharField(max_length=64, default="")  # the widget type of the block
    section_id = models.IntegerField(default=0)
    column = models.IntegerField(default=0)   # column number in the section

    # layout settings
    padding = models.CharField(max_length=64, default="")
    margin = models.CharField(max_length=64, default="")

    # text features
    text_content = models.TextField(null = True)
    font_size = models.CharField(max_length=64, default="16px")
    font_color = models.CharField(max_length=64, default="black")
    background_color = models.CharField(max_length=64, default="white")

    # pic features
    pic_content = models.ImageField(upload_to='img', null = True)
    name = models.CharField(max_length=100, default="anonymous")
