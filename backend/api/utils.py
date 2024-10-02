from .models import *

# TODO add sex as a category in this function


def get_mne(spit, element, age, secondary=None):
    if not secondary:
        entries = Entry.objects.filter(meta__spit=spit).filter(
            bone=element).filter(meta__age=age)
    else:
        entries = Entry.objects.filter(meta__spit=spit).filter(
            bone__secondary=secondary).filter(meta__age=age)
    if not entries:
        return {}
    landmark_count = {}
    for entry in entries:
        landmarks = entry.landmarks.all()
        for landmark in landmarks:
            if landmark_count.get(landmark.landmark_id) is not None:
                landmark_count[landmark.landmark_id] += 1
            else:
                landmark_count[landmark.landmark_id] = 1
    mne = max(landmark_count.values())
    lm = [key for key, value in landmark_count.items() if value == mne]
    if len(lm) > 1:
        return {"landmarks": lm, "mne": mne}
    else:
        return {"landmark": lm[0], "mne": mne}


def get_mne_by_age(spit, element, secondary=None):
    """ For given spit and element, find the mne for each age group in database

    Calls get_mne() for each age group.
    """
    age_cats = [x for (x, y) in EntryMeta.Age.choices]
    out_dict = {}
    total = 0
    for age in age_cats:
        mne = get_mne(spit, element, age, secondary)
        age = age.lower().replace(' ', '_')
        out_dict[age] = mne
        if out_dict[age]:
            total += out_dict[age]["mne"]
    out_dict["total"] = total
    return out_dict


def get_mne_by_element(spit):
    """For given spit, find the mne for each element in database

    Calls get_mne_by_age for each element
    Elements with multiple parts such as the cranium and foot are treated as one element
    """
    elements = Element.objects.all()
    out_dict = {}
    mni = 0
    for element in elements:
        if element.secondary == "":
            out_dict[element.name] = get_mne_by_age(spit, element)
            if out_dict[element.name]["total"] > mni:
                mni = out_dict[element.name]["total"]
        else:
            if not element.secondary in out_dict:
                out_dict[element.secondary] = get_mne_by_age(
                    spit, element, element.secondary)
                if out_dict[element.secondary]["total"] > mni:
                    mni = out_dict[element.secondary]["total"]
    out_dict["mni"] = mni
    return out_dict
