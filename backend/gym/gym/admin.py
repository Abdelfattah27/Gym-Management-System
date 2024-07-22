# Import the necessary modules, and specify constants if not defined earlier in your code.

from django.contrib import admin
from django.urls import reverse
from django.utils.translation import gettext as _
from django.db import models
from django import forms
from django.utils.html import format_html

from django.shortcuts import redirect


class CustomAdminImageWidget(forms.ClearableFileInput):
    def render(self, name, value, attrs=None, renderer=None):
        output = []

        # Render the image if a file is selected
        if value and getattr(value, "url", None):
            output.append(
                f'<div class="image_previewer_wrapper">'
                f'<img class="image_preview" src="{value.url}" alt="{name}" />'
                f'</div>'
            )

        # Render the file input and custom button
        file_button = (
            '<div class="file-input-container">'
            '<div class="clear-image">'
                f'<label class="mr-3" for="{name}-clear_id">Clear</label>'
                f'<input class="inp-clear-image" type="checkbox" name="{name}-clear" id="{name}-clear_id">'
            '</div>'
            '<label class="custom-file-upload">'

            f'<input class="image_upload file-input" type="file" name="{name}" accept="image/*" id="id_{name}" onchange="updateFileName()">'
            
            '<span class="file-button-text" id="fileButtonText">Choose file</span>'
            '<i class="fas fa-upload"></i>' 
            '</label>'
            '</div>'
        )
        output.append(file_button)
        return format_html("".join(output) )
 
 
IS_POPUP_VAR = "_popup"



#############################
# Helper Functions          #
#############################




#################################
# Custom ModelAdmin             #
#################################

class CustomModelAdmin(admin.ModelAdmin) :
    
    formfield_overrides = {
        models.ImageField: {"widget": CustomAdminImageWidget},
        # models.URLField : {"widget" : CustomAdminURLWidget}
    }
    show_full_result_count = False
    def history_view(self, request, object_id, extra_context = None) :
        if request.user.is_superuser :
            return super().history_view(request, object_id, extra_context)
        else : 
            return redirect(reverse("admin:index"))

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': False,
            'show_save_and_continue': True,
            'show_save_and_add_another': False,
            'show_delete': True  ,
            # "show_close" : False
        })
        return super().render_change_form(request, context, add, change, form_url, obj)

    # Register the delete action
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj:
            # Prevent the is_deleted field from being editable for superuser
            readonly_fields += ('is_deleted',)
        return readonly_fields
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)

        fields = [field for field in fields if field != 'is_deleted' and field != "updated_by" and field != "created_by"]
        return fields
    def save_model(self, request, obj, form, change):
        if not change:  # Only set `created_by` when creating a new object
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

    list_per_page = 10  # Set the default number of items per page

    def get_list_per_page(self, request):
        """
        Return the number of items to display per page.
        """
        default_per_page = self.list_per_page
        custom_per_page = request.GET.get('_per_page', default_per_page)

        # Ensure the custom_per_page is an integer
        try:
            custom_per_page = int(custom_per_page)
        except ValueError:
            custom_per_page = default_per_page

        # Limit the number of items per page to a reasonable range
        custom_per_page = max(1, min(100, custom_per_page))

        return custom_per_page

    def changelist_view(self, request, extra_context=None):
        """
        Override the changelist view to handle custom pagination.
        """
        if request.method == 'GET':
            if '_per_page' in request.GET:
                self.list_per_page = self.get_list_per_page(request)

        return super().changelist_view(request, extra_context)  

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if not instance.pk:
                instance.created_by = request.user
            instance.save()
        formset.save_m2m()
        
        for deleted_form in formset.deleted_forms:
            deleted_instance = deleted_form.instance
            deleted_instance.delete()




