from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from jobs.models import Job, Company, Department

class JobListView(ListView):
	queryset = Job.objects.filter(is_active=True)
	template_name = "app/pages/job_list.html"

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['new_link'] = reverse_lazy('jobs:job_new')
		return context


class JobDetailView(DetailView):
	queryset = Job.objects.filter(is_active=True)
	template_name = "app/common/object_detail.html"


class JobCreateView(CreateView):
	model = Job
	template_name = "app/common/object_form.html"
	fields = "__all__"


class JobUpdateView(UpdateView):
	model = Job
	template_name = "app/common/object_form.html"
	fields = "__all__"


class JobDeleteView(DeleteView):
	model = Job
	template_name = 'app/common/confirm_delete.html'
	success_url = reverse_lazy('services:job_list')


class CompanyListView(ListView):
	queryset = Company.objects.filter(is_active=True)
	template_name = "app/pages/company_list.html"

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['new_link'] = reverse_lazy('jobs:company_new')
		return context


class CompanyDetailView(DetailView):
	queryset = Company.objects.filter(is_active=True)
	template_name = "app/common/object_detail.html"


class CompanyCreateView(CreateView):
	model = Company
	template_name = "app/common/object_form.html"
	fields = "__all__"


class CompanyUpdateView(UpdateView):
	model = Company
	template_name = "app/common/object_form.html"
	fields = "__all__"


class CompanyDeleteView(DeleteView):
	model = Company
	template_name = 'app/common/confirm_delete.html'
	success_url = reverse_lazy('jobs:company_list')


class DepartmentListView(ListView):
	queryset = Department.objects.filter(is_active=True)
	template_name = "app/pages/department_list.html"

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['new_link'] = reverse_lazy('jobs:department_new')
		return context


class DepartmentDetailView(DetailView):
	queryset = Department.objects.filter(is_active=True)
	template_name = "app/common/object_detail.html"


class DepartmentCreateView(CreateView):
	model = Department
	template_name = "app/common/object_form.html"
	fields = "__all__"


class DepartmentUpdateView(UpdateView):
	model = Department
	template_name = "app/common/object_form.html"
	fields = "__all__"


class DepartmentDeleteView(DeleteView):
	model = Department
	template_name = 'app/common/confirm_delete.html'
	success_url = reverse_lazy('jobs:department_list')
