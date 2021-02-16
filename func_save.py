from dataclasses import is_dataclass, asdict


def inner_classes(obj):
    return [cls_attribute for cls_attribute in obj.__dict__.values() if 'object' in str(cls_attribute)]


def save(instance, names):
    dic = vars(instance)

    for key, val in dic.items():
        if str(val.__class__.__name__) in names:
            names = inner_classes(val)
            dic[key] = save(val, names)

        elif isinstance(val, dict):
            for k, v in val.items():
                names = inner_classes(v)
                dic[key][k] = save(v, names)

        elif isinstance(val, list):
            for i in range(len(val)):
                try:
                    names = inner_classes(val[i])
                    val[i] = save(val[i], names)
                except: pass

        elif is_dataclass(val):
            dic[key] = asdict(val)
    return dic
