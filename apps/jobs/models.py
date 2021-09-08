from django.db import models
from django.contrib.auth.models import User

JobType = [
    (0, '技术类'),
    (1, '管理类'),
    (2, '运营类'),
    (3, '销售类'),
]

JobCity = [
    (0, '北京'),
    (1, '大连'),
    (2, '上海'),
]

DegreeType = (('本科', '本科'), ('硕士', '硕士'), ('博士', '博士'))

Gender = (('男', '男'), ('女', '女'))


class Job(models.Model):
    job_type = models.SmallIntegerField(choices=JobType, blank=False, verbose_name='职位类别')
    job_name = models.CharField(max_length=200, blank=False, verbose_name='职位名称')
    job_city = models.SmallIntegerField(choices=JobCity, blank=False, verbose_name='工作地点')
    job_duty = models.TextField(max_length=1200, verbose_name='职位职责')
    job_require = models.TextField(max_length=1200, verbose_name='职位要求')
    creator = models.ForeignKey(User, verbose_name='创建人', null=True, on_delete=models.SET_NULL)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    upgrade_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'tb_job'
        verbose_name = '职位信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.job_name


class Resume(models.Model):
    """
    面试者信息
    """
    username = models.CharField(max_length=100, verbose_name='姓名')
    applicant = models.ForeignKey(User, verbose_name="申请人", null=True, on_delete=models.SET_NULL)
    city = models.CharField(max_length=100, verbose_name='城市')
    phone = models.CharField(max_length=100, verbose_name='手机号码')
    email = models.EmailField(max_length=100, blank=True, verbose_name='邮箱')
    # apply_position = models.CharField(max_length=100, blank=True, verbose_name='应聘职位')
    apply_position = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True, verbose_name='应聘职位')
    gender = models.CharField(max_length=100, choices=Gender, blank=True, verbose_name='性别')
    picture = models.ImageField(upload_to='images/', blank=True, verbose_name='个人照片')
    attachment = models.FileField(upload_to='file/', blank=True, verbose_name='简历附件')

    # 学校与学历信息
    school = models.CharField(max_length=100, blank=True, verbose_name='学校')
    major = models.CharField(max_length=100, blank=True, verbose_name='专业')
    degree = models.CharField(max_length=100, choices=DegreeType, blank=True, verbose_name='学历')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    upgrade_date = models.DateTimeField(auto_now=True, verbose_name="更新日期")

    # 候选人自我介绍，工作经历，项目经历
    self_introduction = models.TextField(max_length=1024, blank=True, verbose_name='自我介绍')
    work_experience = models.TextField(max_length=1024, blank=True, verbose_name='工作经历')
    project_experience = models.TextField(max_length=1024, blank=True, verbose_name='项目经历')

    class Meta:
        db_table = 'tb_resume'
        verbose_name = '简历列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
