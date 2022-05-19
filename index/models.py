from django.db import models

class Category(models.Model):
    name = models.CharField('分类',max_length=100)
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Audio(models.Model):
    song_name = models.CharField('歌名',max_length=70)
    singer = models.CharField('歌手',max_length=100)
    category = models.ManyToManyField(Category, verbose_name='分类')
    song_image = models.ImageField(upload_to='pic/',verbose_name='歌曲封面')
    song_file = models.FileField(upload_to = 'audio/', verbose_name = '源文件')
    song_lrc = models.FileField(upload_to = 'lrc/', verbose_name = '源文件')
    upload_user = models.CharField('分享用户',max_length=50)
    song_release = models.CharField('发行时间', max_length=20)
    #下面为新增代码
    class Meta:
        verbose_name = '音乐'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.song_name


# 歌曲动态表dynamic
class Dynamic(models.Model):
    song = models.ForeignKey(Audio, on_delete=models.CASCADE, verbose_name='歌名')
    dynamic_plays = models.IntegerField('播放次数')
    dynamic_search = models.IntegerField('搜索次数')
    class Meta:
        # 设置Admin界面的显示内容
        verbose_name = '歌曲动态'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.song.song_name

# 歌曲点评表comment
class Comment(models.Model):
    comment_id = models.AutoField('序号', primary_key=True)
    comment_text = models.CharField('内容', max_length=500)
    comment_user = models.CharField('用户', max_length=20)
    song = models.ForeignKey(Audio, on_delete=models.CASCADE,verbose_name='歌名')
    comment_date = models.CharField('日期', max_length=50)
    class Meta:
        # 设置Admin界面的显示内容
        verbose_name = '歌曲评论'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.comment_id
# Create your models here.
