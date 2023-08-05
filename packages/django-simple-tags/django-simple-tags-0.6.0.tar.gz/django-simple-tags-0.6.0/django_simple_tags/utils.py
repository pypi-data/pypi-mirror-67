


def get_related_model_field(model, field_name):
    field_names = field_name.split("__")
    root = model
    for field_name in field_names:
        field = root._meta.get_field(field_name)
        model = root
        root = getattr(field, "related_model", None)
    return model, field

