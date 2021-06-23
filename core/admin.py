from django.contrib import admin
from .models import user, patient, responder,blogs, comment, reply


admin.site.register(user.User)
admin.site.register(patient.PatientProfile)
admin.site.register(responder.ResponderProfile)
admin.site.register(blogs.Blog)
admin.site.register(comment.Comment)
admin.site.register(reply.Reply)