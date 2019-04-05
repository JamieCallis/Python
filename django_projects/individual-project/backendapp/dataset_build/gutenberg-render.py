from gutenberg.acquire import get_metadata_cache
# this file is required to be run before generateData.py can be run
cache = get_metadata_cache()
cache.populate()