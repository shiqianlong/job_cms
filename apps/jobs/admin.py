from datetime import datetime

from django.contrib import admin, messages
from .models import Job, Resume
from ..interview.models import Candidate
from django.utils.html import format_html


class JobAdmin(admin.ModelAdmin):
    list_display = ('job_name', 'job_type', 'job_city', 'create_time')


def enter_interview_process(modeladmin, request, queryset):
    candidate_names = ""
    for resume in queryset:
        candidate = Candidate()
        # 把 obj 对象中的所有属性拷贝到 candidate 对象中:
        candidate.__dict__.update(resume.__dict__)
        candidate.created_date = datetime.now()
        candidate.upgrade_date = datetime.now()
        candidate_names = candidate.username + "," + candidate_names
        candidate.creator = request.user.username
        candidate.save()
    messages.add_message(request, messages.INFO, '候选人: %s 已成功进入面试流程' % (candidate_names))


enter_interview_process.short_description = u"进入面试流程"


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('username', 'gender', 'image_tag', 'apply_position', 'email')
    fieldsets = (
        (None, {'fields': (
            'applicant', ('username', 'city', 'phone'),
            ('picture', 'attachment'),
            ('email', 'apply_position', 'gender'),
            ('school', 'major', 'degree'),
            ('self_introduction', 'work_experience', 'project_experience')
        )}),
    )

    actions = (enter_interview_process,)

    def image_tag(self, obj):
        if obj.picture:
            return format_html('<img src="{}" style="width:100px;height:80px;"/>'.format(obj.picture.url))
        return ""

    image_tag.allow_tags = True
    image_tag.short_description = '照片'


admin.site.register(Job, JobAdmin)
admin.site.register(Resume, ResumeAdmin)
admin.site.site_header = '面试人员管理系统'
