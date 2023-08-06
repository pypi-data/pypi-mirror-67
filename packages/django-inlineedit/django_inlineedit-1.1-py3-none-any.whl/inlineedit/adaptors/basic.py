from django.db.models import Model as DjangoModel, Field as DjangoField
from django.forms import Field as DjangoFormField
from django.contrib.auth.models import User, AnonymousUser
from django.utils.html import format_html
from django.conf import settings

from typing import Union, Optional

if 'reversion' in settings.INSTALLED_APPS:
    import reversion
    _reversion_installed = True
    if settings.DEBUG: print(">>> django-Inlineedit -> django-reversion is enabled")
else:
    _reversion_installed = False
    if settings.DEBUG: print(">>> django-Inlineedit -> django-reversion is disabled")


class BasicAdaptor:
    "Simplest adaptor and interface"
    
    def __init__(
            self,
            model_object: DjangoModel,
            field: DjangoField,
            user: Optional[Union[User, AnonymousUser]] = None
    ):
        self._model: DjangoModel = model_object
        self._field = field
        self._user = user

        if _reversion_installed:
            self._reversion_enabled = True
        else:
            self._reversion_enabled = False

    def form_field(self) -> DjangoFormField:
        "Return the DjangoFormField object"
        return self._field.formfield()

    def empty_message(self) -> str:
        "Returns message to show users if field is empty. The default is 'Hover here to edit <name>'"
        return "Hover here to edit {}".format(self._field.verbose_name)

    def db_value(self):
        "Returns the field value as stored in the db"
        return getattr(self._model, self._field.attname)        

    def display_value(self):
        "Returns the field value to be shown to users"
        db = self.db_value()
        
        if self._field.choices: # convert to external representation
            display = dict(self._field.choices).get(db,"--")
        elif db == None:
            display = "N/A"
        elif isinstance(db, bool):
            display = format_html("&check;" if db else "&cross;")
        else:
            display = db
        
        return display

    def save(self, value: str):
        "Save a new field value to the db. The default version supports django-reversions if that is enabled"
        setattr(self._model, self._field.attname, value)
        if self._reversion_enabled:
            with reversion.create_revision():
                self._model.save()
                if self._user:
                    reversion.set_user(self._user)
        else:
            self._model.save()
