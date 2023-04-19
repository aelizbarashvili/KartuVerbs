# KartuVerbs

Kartu-Verbs database contains information about Georgian inflected verbs and it's characteristics. In a input file (csv) we have information in the following fields:

    form: Inflected form of a Georgian verb
    tense_in_paradigm: Tense for the inflected form
    person: Person for the inflected form (1, 2, 3)
    number: Number for the inflected form (sg, pl)
    preverb: Preverb for the inflected form
    pre2: Preradical for the inflected form
    root: Root for the inflected form
    sf2: Stem formant for the inflected form
    caus_sf: causative Stem formant for the inflected form
    ending: Ending for the inflected form
    tsch_class: Tschkhenkeli Class
    morph_type: morphology type
    id: Id in Clarino database to keep link to the corresponding croot
    sub_id: Id in Clarino database to keep link to the corresponding verb paradigm
    vn2: Verbal Noun for the inflected form

r goal is to train a model which will predict a Verbal Noun based on the following information: form, tense_in_paradigm, person, number, preverb, pre2, root, sf2, caus_sf, ending, tsch_class, orph_type and sub_id
