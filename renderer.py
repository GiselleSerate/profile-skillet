# Test jinja2 template rendering
from jinja2 import Environment, PackageLoader, select_autoescape
import empty

env = Environment(
    loader=PackageLoader('empty', '.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('profiles.xml')
print(template.render(profile_name='awoo', action_normal='alert', action_wildfire='alert'))