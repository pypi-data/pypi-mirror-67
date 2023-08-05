from django.contrib.admin.options import get_content_type_for_model
from django.db import models

from . import exceptions
from ..filters import FilterMixin
from .mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    UpdateModelMixin,
)
from .abc import Resolver


class GenericModelResolver(Resolver):
    """
    Model based resolver based off of DRF model views.
    """

    queryset = None
    lookup_arg = None
    lookup_field = "pk"

    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method." % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, models.query.QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()
        if self.config.get("nested", False):
            queryset = self.filter_nested_queryset(queryset)
        return queryset

    def filter_nested_queryset(self, queryset):
        # see if we can just use the info context and the name of the resolver field
        # to reverse the relation, fallback on parent_name
        try:
            return getattr(self.parent, self.info.field_name)
        except AttributeError:
            params = {}
            if self.config.get("parent_name", None) == "object_id":
                params["object_id"] = self.parent.id
                params["content_type"] = get_content_type_for_model(self.parent._meta.model)
            elif self.config.get("parent_name", None):
                params[self.config.get("parent_name")] = self.parent.id

            return queryset.filter(**params)

    def get_object(self):
        """
        Returns the object the resolver is displaying.

        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        queryset = self.get_queryset()

        # Perform the lookup filtering.
        lookup_arg = self.lookup_arg or self.lookup_field

        assert lookup_arg in self.operation_kwargs, (
            "Expected resolver %s to be called with an argument "
            'named "%s". Fix your query arguments, or set the `.lookup_field` '
            "attribute on the resolver correctly." % (self.__class__.__name__, lookup_arg)
        )

        filter_kwargs = {self.lookup_field: self.operation_kwargs[lookup_arg]}
        obj = queryset.get(**filter_kwargs)
        # return null?
        # obj = get_object_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        if obj:
            self.check_object_permissions(self.info, obj)

        return obj

    # TODO: move out into its own mixin?
    def retrieve(self, parent, **kwargs):
        return self.get_object()


class ModelResolver(CreateModelMixin, UpdateModelMixin, DestroyModelMixin, FilterMixin, GenericModelResolver):
    pass


class ListModelResolver(ListModelMixin, GenericModelResolver):
    pass
