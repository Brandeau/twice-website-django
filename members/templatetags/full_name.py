from django import template

register = template.Library()

@register.filter
def full_name(member, lang):
    first_name = member.__dict__.get(f"first_name_{lang}", "")
    last_name = member.__dict__.get(f"last_name_{lang}", "")

    if first_name is None:
        first_name = ""

    if last_name is None:
        last_name = ""
    
    return f"{last_name}{first_name}"