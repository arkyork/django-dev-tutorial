from django import template

register = template.Library()

@register.filter(name='status_to_string')
def convert_status(st,name):
    print(f'name:{name}')
    if st==10:
        return 'good'
    else:
        return 'bad'