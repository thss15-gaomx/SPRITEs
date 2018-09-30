from django.db import models


class Page(models.Model):
    header = models.IntegerField(default=0)    # 0: null
    sidebar = models.IntegerField(default=0)
    footer = models.IntegerField(default=0)
    section_num = models.IntegerField(default=0)  # section numbers contained


class Section(models.Model):
    page_id = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    name = models.CharField(max_length=64, default="")


class Block(models.Model):
    pos_x = models.IntegerField(default=0)   # position
    pos_y = models.IntegerField(default=0)
    width = models.IntegerField(default=1)   # size
    height = models.IntegerField(default=1)
    content_type = models.CharField(max_length=64, default="")  # the widget type of the block
    section_id = models.IntegerField(default=0)

    # text features
    text_content = models.TextField(null = True)
    font_size = models.CharField(max_length=64, default="16px")
    font_color = models.CharField(max_length=64, default="black")
    background_color = models.CharField(max_length=64, default="white")

    # pic features
    pic_content = models.ImageField(upload_to='img', null = True)
    name = models.CharField(max_length=100, default="anonymous")

    # pic and text features(unused now)
    pic_text_type = models.IntegerField(default=0)
    # pic and text type(unused now)
    TYPE_BACKGROUND = 1
    TYPE_CARD = 2
    TYPE_COMMENT = 3
