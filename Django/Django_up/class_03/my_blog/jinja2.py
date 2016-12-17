from jinja2 import Environment
from polls.templatetags.poll_filter import lower

def environment(**options):
    env = Environment(**options)
    env.filters['allen_lower'] = lower
    return env