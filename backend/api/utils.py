from .models import *

# TODO add sex as a category in this function


def get_mne(spit, element, age):
    entries = Entry.objects.filter(meta__spit=spit).filter(
        bone=element).filter(meta__age=age)
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


def get_mne_by_age(spit, element):
    """ For given spit and element, find the mne for each age group in database

    Calls get_mne() for each age group.
    """
    age_cats = [x for (x, y) in EntryMeta.Age.choices]
    out_dict = {}
    total = 0
    for age in age_cats:
        out_dict[age] = get_mne(spit, element, age)
        if out_dict[age]:
            total += out_dict[age]["mne"]
    out_dict["total"] = total
    return out_dict
