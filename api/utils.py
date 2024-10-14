from .models import *
# TODO add sex as a category in this function


def get_mne(spit, element, age, sex):

    if sex is None:
        entries = Entry.objects.filter(meta__spit=spit).filter(
            bone=element).filter(meta__age=age)
    else:
        entries = Entry.objects.filter(meta__spit=spit).filter(
            bone=element).filter(meta__age=age).filter(meta__sex=sex)
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


def get_mne_by_age(spit, element, sex=None):
    """ For given spit and element, find the mne for each age group in database

    Calls get_mne() for each age group.
    """
    age_cats = [x for (x, y) in EntryMeta.Age.choices]
    out_dict = {}
    total = 0
    for age in age_cats:
        mne = get_mne(spit, element, age, sex)
        age = age.lower().replace(' ', '_')
        out_dict[age] = mne
        if out_dict[age]:
            total += out_dict[age]["mne"]
    out_dict["total"] = total
    return out_dict


def get_mne_by_sex(spit, element, sex_split):
    """If called for, further split calculations by sex
    """
    if not sex_split:
        return get_mne_by_age(spit, element)
    sex_cats = [x for (x, y) in EntryMeta.Sex.choices]
    out_dict = {}
    total = 0
    for sex in sex_cats:
        mne = get_mne_by_age(spit, element, sex)
        sex = sex.lower().replace(' ', '_')
        out_dict[sex] = mne
        if out_dict[sex]:
            total += out_dict[sex]["total"]
    out_dict["total"] = total
    return out_dict


def get_mne_by_element(spit, sex_split):
    """For given spit, find the mne for each element in database

    Calls get_mne_by_age() for each element
    Elements with multiple parts such as the cranium and foot are treated as one element
    """
    elements = Element.objects.all()
    out_dict = {}
    mni = 0
    for element in elements:
        data = get_mne_by_sex(spit, element, sex_split)
        element = element.name.lower().replace(' ', '_')
        out_dict[element] = data
        if out_dict[element]["total"] > mni:
            mni = out_dict[element]["total"]
    out_dict["mni"] = mni
    return out_dict


def get_mne_by_spit(site, sex_split=False):
    """For a given site, return mne calculations for each spit

    Calls get_mne_by_element()
    """
    spits = Spit.objects.filter(site=site)
    if not spits:
        return {}
    out_dict = {"site_name": site.name}
    site_total = 0
    for spit in spits:
        out_dict[f'context_{spit.number}'] = get_mne_by_element(
            spit, sex_split)
        site_total += out_dict[f'context_{spit.number}']["mni"]
    out_dict["site_mni"] = site_total
    return out_dict
