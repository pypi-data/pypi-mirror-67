from recipe_caching.mappers import FromCache

from recipe import SETTINGS
from recipe.dynamic_extensions import DynamicExtensionBase


class CachingQueryHook(DynamicExtensionBase):
    """A stevedore based DynamicExtension that sets the proper options for a
    cached query
    """

    def __init__(self, recipe_parts):
        """Initializes a new CachingQueryHook
        :param recipe_parts: the components of a recipe
        :type key: dict
        """
        super(CachingQueryHook, self).__init__(recipe_parts)

    def execute(self):
        """Adds the FromCache option to the query

        :return: all the recipe components in recipe_parts format
        :rtype: dict
        """
        # If there is a recipe, use it to configure cache details
        cache_region = self.recipe_parts.get(
            'cache_region', getattr(SETTINGS, 'CACHE_REGION', 'default')
        )
        cache_prefix = self.recipe_parts.get(
            'cache_prefix', getattr(SETTINGS, 'CACHE_PREFIX', 'default')
        )
        self.recipe_parts['query'] = self.recipe_parts['query'].options(
            FromCache(cache_region, cache_prefix=cache_prefix)
        )
        return self.recipe_parts
