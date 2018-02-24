from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Application, Owner, Questionnaire, Tag, Rule, TagType
from .forms import ApplicationForm, OwnerForm, QuestionnaireForm, TagForm, RuleForm, TagTypeForm
from profiles.models import Profile
from braces.views import LoginRequiredMixin


class ApplicationListView(ListView):
    model = Application


class ApplicationCreateView(LoginRequiredMixin, CreateView):
    model = Application
    form_class = ApplicationForm

    def form_valid(self, form):
        form.instance.last_user = Profile.objects.get(user=self.request.user)
        return super(ApplicationCreateView, self).form_valid(form)


class ApplicationDetailView(LoginRequiredMixin, DetailView):
    model = Application


class ApplicationUpdateView(LoginRequiredMixin, UpdateView):
    model = Application
    form_class = ApplicationForm

    def form_valid(self, form):
        form.instance.last_user = Profile.objects.get(user=self.request.user)
        return super(ApplicationUpdateView, self).form_valid(form)


class OwnerListView(LoginRequiredMixin, ListView):
    model = Owner


class OwnerCreateView(LoginRequiredMixin, CreateView):
    model = Owner
    form_class = OwnerForm

    def form_valid(self, form):
        form.instance.last_user = Profile.objects.get(user=self.request.user)
        return super(OwnerCreateView, self).form_valid(form)


class OwnerDetailView(LoginRequiredMixin, DetailView):
    model = Owner


class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    model = Owner
    form_class = OwnerForm

    def form_valid(self, form):
        form.instance.last_user = Profile.objects.get(user=self.request.user)
        return super(OwnerUpdateView, self).form_valid(form)


class QuestionnaireListView(LoginRequiredMixin, ListView):
    model = Questionnaire


class QuestionnaireCreateView(LoginRequiredMixin, CreateView):
    model = Questionnaire
    form_class = QuestionnaireForm

    def get_context_data(self, **kwargs):
        context = super(QuestionnaireCreateView, self).get_context_data(**kwargs)
        context['tagtypes'] = TagType.objects.all().order_by('pk')
        return context

    def form_valid(self, form):
        form.instance.last_user = Profile.objects.get(user=self.request.user)
        return super(QuestionnaireCreateView, self).form_valid(form)


class QuestionnaireDetailView(LoginRequiredMixin, DetailView):
    model = Questionnaire


class QuestionnaireUpdateView(LoginRequiredMixin, UpdateView):
    model = Questionnaire
    form_class = QuestionnaireForm

    def form_valid(self, form):
        form.instance.last_user = Profile.objects.get(user=self.request.user)
        return super(QuestionnaireUpdateView, self).form_valid(form)


class TagListView(LoginRequiredMixin, ListView):
    model = Tag


class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    form_class = TagForm

    def form_valid(self, form):
        form.instance.last_user = Profile.objects.get(user=self.request.user)
        return super(TagCreateView, self).form_valid(form)


class TagDetailView(LoginRequiredMixin, DetailView):
    model = Tag


class TagUpdateView(LoginRequiredMixin, UpdateView):
    model = Tag
    form_class = TagForm

    def form_valid(self, form):
        form.instance.last_user = Profile.objects.get(user=self.request.user)
        return super(TagUpdateView, self).form_valid(form)


class RuleListView(LoginRequiredMixin, ListView):
    model = Rule


class RuleCreateView(LoginRequiredMixin, CreateView):
    model = Rule
    form_class = RuleForm

    def form_valid(self, form):
        form.instance.last_user = Profile.objects.get(user=self.request.user)
        return super(RuleCreateView, self).form_valid(form)


class RuleDetailView(LoginRequiredMixin, DetailView):
    model = Rule


class RuleUpdateView(LoginRequiredMixin, UpdateView):
    model = Rule
    form_class = RuleForm

    def form_valid(self, form):
        form.instance.last_user = Profile.objects.get(user=self.request.user)
        return super(RuleUpdateView, self).form_valid(form)


class TagTypeListView(LoginRequiredMixin, ListView):
    model = TagType


class TagTypeCreateView(LoginRequiredMixin, CreateView):
    model = TagType
    form_class = TagTypeForm

    def form_valid(self, form):
        form.instance.last_user = Profile.objects.get(user=self.request.user)
        return super(TagTypeCreateView, self).form_valid(form)


class TagTypeDetailView(LoginRequiredMixin, DetailView):
    model = TagType

    def get_context_data(self, **kwargs):
        context = super(TagTypeDetailView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.filter(type=self.name)
        return context


class TagTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = TagType
    form_class = TagTypeForm

    def form_valid(self, form):
        form.instance.last_user = Profile.objects.get(user=self.request.user)
        return super(TagTypeUpdateView, self).form_valid(form)
