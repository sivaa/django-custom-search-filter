from django.contrib import admin
from app.models import Person, OtherName

class PersonAdmin(admin.ModelAdmin):
    search_fields = ['name',]
    list_filter = ['type',]
    
    def queryset(self, request):
        """
        Returns a QuerySet of all model instances that can be edited by the
        admin site. This is used by changelist_view.
        """
        qs = self.model._default_manager.get_query_set()
        # TODO: this should be handled by some parameter to the ChangeList.
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
            
        #Custom Search
        # 1. Get the query value and clear it from the request
        q=''
        try:
            q = request.GET['q']
            copy = request.GET.__copy__()
            copy.__delitem__('q')
            request.GET = copy
            
        except:
            pass
        
        result_list = []    
            
        # Search on main model (Person)
        person_obj_list = Person.objects.filter(name__contains = q)        
        for person in person_obj_list:
            result_list.append(person.pk)
        
        # Search on the other related model (Other Name)
        other_names_obj_list = OtherName.objects.filter(name__contains = q)        
        for other_name in other_names_obj_list:
            result_list.append(other_name.person.pk)            
        return qs.filter(pk__in = result_list) # apply the filter

class OtherNameAdmin(admin.ModelAdmin):
    pass

admin.site.register(Person, PersonAdmin)
admin.site.register(OtherName, OtherNameAdmin)