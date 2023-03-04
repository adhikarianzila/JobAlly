from django.contrib import admin
from .models import JobModel, InternshipModel, RegistrationModel, UserModel
from .models import ContactModel

# JobModel


class JobModelAdmin(admin.ModelAdmin):
    list_display = ("Jobtitle", "CompanyURL", "JobLink", "JobDescription")


admin.site.register(JobModel, JobModelAdmin)

# Internshipmodel


class InternshipModelAdmin(admin.ModelAdmin):
    list_display = ("InternTitle", "InternType", "CompanyName", "CompanyURL",
                    "InternArea", "InternLink", "InternDescription", "Skill")


admin.site.register(InternshipModel, InternshipModelAdmin)

# Register model


class RegisterModelAdmin(admin.ModelAdmin):
    list_display = ("Name", "Email", "Password")


admin.site.register(RegistrationModel, RegisterModelAdmin)

# LoginModel


class UserModelAdmin(admin.ModelAdmin):
    list_display = ("Email", "Password")
# Register model


admin.site.register(UserModel, UserModelAdmin)

# ContactModel


class ContactModelAdmin(admin.ModelAdmin):
    list_display = ("Name", "Email", "Message", "Subject")
# Register model


admin.site.register(ContactModel, ContactModelAdmin)
