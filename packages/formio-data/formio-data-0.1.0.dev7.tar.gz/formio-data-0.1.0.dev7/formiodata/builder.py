# Copyright Nova Code (http://www.novacode.nl)
# See LICENSE file for full licensing details.

import json
import logging

from copy import deepcopy

from formiodata import components


class Builder:

    def __init__(self, schema_json, language='en', **kwargs):
        """
        @param schema_json
        @param lang
        """
        self.schema = json.loads(schema_json)
        self.language = language
        # i18n (translations)
        self.i18n = kwargs.get('i18n', {})

        # Components
        ## Raw components from the schema
        self.raw_components = []
        ## Raw components enriched with Component(object) API.
        self.components = []
        ## Key/value dictionay of Form components for instant access.
        self.form_components = {}
        ## Set/load component attrs intialized above.
        self.load_components()

        # TODO kwargs['component_cls']
        # Custom component classes
        self._component_cls = []

    def load_components(self):
        self.raw_components = self.schema.get('components')
        self.components = deepcopy(self.schema.get('components'))
        self._load_components(self.components)

    def _load_components(self, components):
        """
        @param components
        """
        for component in components:
            component_obj = self.get_component_object(component)
            component['_object'] = component_obj
            if component.get('key'):
                self.form_components[component.get('key')] = component_obj

            # Nested components in e.g. columns, panels
            if component.get('components'):
                self._load_components(component.get('components'))
            for k, vals in component.copy().items():
                if isinstance(vals, list):
                    for v in vals:
                        if v.get('components'):
                            self._load_components(v.get('components'))

    def get_component_object(self, component):
        """
        @param component
        """
        component_type = component.get('type')
        if component_type:
            try:
                cls_name = '%sComponent' % component_type
                cls = getattr(components, cls_name)
                return cls(component, self.language, i18n=self.i18n)
            except AttributeError as e:
                # TODO try to find/load first from self._component_cls else
                # re-raise exception or silence (log error and return False)
                logging.error(e)
                return components.Component(component)
        else:
            return False
