from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


def make_black_listed(model_admin, request, queryset):
    queryset.update(our_note="Не доставляйте пиццу этому пользователю.")
make_black_listed.short_description = 'Делает заметку в черном списке для пользователя'


class CustomAdminModel(UserAdmin):
    # fieldsets = UserAdmin.fieldsets + (
    #     ('Pizza', {'fields': (
    #             'favourite_pizza',
    #             'our_note',
    #     )})
    # ),
    list_display = (
        'username',
        'first_name',
        'last_name',
        'favourite_pizza',
        'our_note',
    )
    list_editable = (
        'favourite_pizza', 'our_note'
    )
    list_filter = (
        'favourite_pizza__name',
    )
    # list_select_related = ('favourite_pizza', )
    search_fields = (
        'first_name',
        'last_name',
        'favourite_pizza__name',
        'our_note',
    )
    actions = (make_black_listed, )

admin.site.register(CustomUser, CustomAdminModel)
