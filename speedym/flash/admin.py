from django.contrib import admin

from .models import Factoid, BinaryFact, QuestionSet, Bout, User, ResponseTiming

admin.site.register(Factoid)
admin.site.register(BinaryFact)
admin.site.register(QuestionSet)
admin.site.register(Bout)
admin.site.register(User)
admin.site.register(ResponseTiming)
# Register your models here.
