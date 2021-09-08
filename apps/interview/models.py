from django.db import models
from django.contrib.auth.models import User

from apps.jobs.models import DegreeType

# 第一轮面试结果
FIRST_INTERVIEW_RESULT_TYPE = ((u'建议复试', u'建议复试'), (u'待定', u'待定'), (u'放弃', u'放弃'))

# 复试面试建议
INTERVIEW_RESULT_TYPE = ((u'建议录用', u'建议录用'), (u'待定', u'待定'), (u'放弃', u'放弃'))

# HR终面结论
HR_SCORE_TYPE = (('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C'))

# 性别
GENDER = (('男', '男'), ('女', '女'))


class Candidate(models.Model):
    # 面试者情况
    username = models.CharField(max_length=135, verbose_name=u'姓名')
    city = models.CharField(max_length=135, verbose_name=u'城市')
    phone = models.CharField(max_length=135, verbose_name=u'手机号码')
    email = models.EmailField(max_length=135, blank=True, verbose_name=u'邮箱')
    apply_position = models.ForeignKey('jobs.Job', on_delete=models.SET_NULL, null=True, verbose_name='应聘职位')
    school = models.CharField(max_length=135, blank=True, verbose_name='学校')
    gender = models.CharField(choices=GENDER, max_length=135, blank=True, verbose_name=u'性别')

    # 学校与学历信息
    major = models.CharField(max_length=135, blank=True, verbose_name=u'专业')
    degree = models.CharField(max_length=135, choices=DegreeType, blank=True, verbose_name=u'学历')

    paper_score = models.DecimalField(decimal_places=1, null=True, max_digits=3, blank=True, verbose_name=u'笔试成绩')

    # 第一轮面试记录
    first_score = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True, verbose_name=u'初试分',
                                      help_text=u'1-5分，极优秀: >=4.5，优秀: 4-4.4，良好: 3.5-3.9，一般: 3-3.4，较差: <3分')
    first_learning_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                 verbose_name=u'学习能力得分')
    first_professional_competency = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                        verbose_name=u'专业能力得分')
    first_advantage = models.TextField(max_length=1024, blank=True, verbose_name=u'优势')
    first_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name=u'顾虑和不足')
    first_result = models.CharField(max_length=256, choices=FIRST_INTERVIEW_RESULT_TYPE, blank=True,
                                    verbose_name=u'初试结果')
    first_interviewer_user = models.ForeignKey(User, related_name='first_interviewer_user', blank=True, null=True,
                                               on_delete=models.CASCADE, verbose_name=u'一面官')

    first_remark = models.CharField(max_length=135, blank=True, verbose_name=u'初试备注')

    # 第二轮面试记录
    second_score = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True, verbose_name=u'专业复试得分',
                                       help_text=u'1-5分，极优秀: >=4.5，优秀: 4-4.4，良好: 3.5-3.9，一般: 3-3.4，较差: <3分')
    second_professional_competency = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                         verbose_name=u'专业能力得分')
    second_advantage = models.TextField(max_length=1024, blank=True, verbose_name=u'优势')
    second_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name=u'顾虑和不足')
    second_result = models.CharField(max_length=256, choices=INTERVIEW_RESULT_TYPE, blank=True, verbose_name=u'专业复试结果')
    second_interviewer_user = models.ForeignKey(User, related_name='second_interviewer_user', blank=True, null=True,
                                                on_delete=models.CASCADE, verbose_name=u'二面官')
    second_remark = models.CharField(max_length=135, blank=True, verbose_name=u'专业复试备注')

    # HR终面
    hr_score = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name=u'HR复试综合等级')

    hr_result = models.CharField(max_length=256, choices=INTERVIEW_RESULT_TYPE, blank=True, verbose_name=u'HR复试结果')
    hr_interviewer_user = models.ForeignKey(User, related_name='hr_interviewer_user', blank=True, null=True,
                                            on_delete=models.CASCADE, verbose_name=u'HR面试官')
    hr_remark = models.CharField(max_length=256, blank=True, verbose_name=u'HR复试备注')

    creator = models.CharField(max_length=256, blank=True, verbose_name=u'候选人数据的创建人')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    upgrade_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=u'更新时间')
    last_editor = models.CharField(max_length=256, blank=True, verbose_name=u'最后编辑者')

    class Meta:
        db_table = u'candidate'
        verbose_name = u'应聘者'
        verbose_name_plural = u'应聘者'
        permissions = [
            ("export", "Can export candidate list"),
            ("notify", "notify interviewer for candidate review"),
        ]

    def __str__(self):
        return self.username
