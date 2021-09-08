from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Job, JobCity, JobType
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import Resume


def job_list(request):
    jobs = Job.objects.order_by('job_type')
    context = {
        'jobs': jobs
    }
    for job in jobs:
        job.job_type = JobType[job.job_type][1]
        job.job_city = JobCity[job.job_city][1]
    return render(request, 'index.html', context=context)


def job_detail(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
        job.job_city = JobCity[job.job_city][1]
        job.job_type = JobType[job.job_type][1]
    except Job.DoesNotExist:
        raise Http404('该职位不存在！')
    return render(request, 'job_detail.html', {'job': job})


class ResumeCreateView(LoginRequiredMixin, CreateView):
    """    简历职位页面  """
    template_name = 'resume_form.html'
    success_url = '/'
    model = Resume
    fields = ["username", "city", "phone",
              "email", "apply_position", "gender",
              "school", "major", "degree", "picture", "attachment",
              "self_introduction", "work_experience", "project_experience"]

    ### 从 URL 请求参数带入默认值
    def get_initial(self):
        initial = {}
        for x in self.request.GET:
            initial[x] = self.request.GET[x]
        return initial

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.applicant = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ResumeDetailView(DetailView):
    """   简历详情页    """
    model = Resume
    template_name = 'resume_detail.html'
