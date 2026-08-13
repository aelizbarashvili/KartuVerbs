#!/home/achiko/anaconda3/bin/python
#
#in .vimrc
#set softtabstop=4
#set tabstop=4
#set shiftwidth=4
#set expandtab
#
# and then in vim - :retab

import pandas as pd
import unicodedata

df = pd.read_csv('f14_fullvnnew.csv',sep=';',dtype=str)

def tr(word, translit_table):
    converted_word = ''
    for char in word:
        transchar = ''
        if char in translit_table:
            transchar = translit_table[char]
        else:
            transchar = char
        converted_word += transchar
    return converted_word

def tense_ka(tense_en):
    if tense_en == "present":
         return "აწმყო"
    if tense_en == "imperfect":
         return "უწყვეტელი"
    if tense_en == "conj-present":
         return "აწმყოს_კავშირებითი"
    if tense_en == "future":
         return "მყოფადი"
    if tense_en == "conditional":
         return "I_ხოლმეობითი"
    if tense_en == "conj-future":
         return "მყოფადის_კავშირებითი"
    if tense_en == "aorist":
         return "წყვეტილი"
    if tense_en == "optative":
         return "ბრძანებითი"
    if tense_en == "perfect":
         return "I_თურმეობითი"
    if tense_en == "pluperfect":
         return "II თურმეობითი"
    if tense_en == "conj-perfect":
         return "III კავშირებითი"

def number_ka(number_en):
    if number_en == 'sg':
        return 'მხ'
    if number_en == 'pl':
        return 'მრ'

def lang_ka(lang_en):
    if lang_en == 'ng':
        return 'ახალი ქართული'
    if lang_en == 'og':
        return 'ძველი/საშუალო ქართული'

def class_morph_type_ka(class_morph_type_en):
    if class_morph_type_en == 'Act':
        return 'მოქმედებითი გვარი'
    if class_morph_type_en == 'MedAct':
        return 'საშუალ-მოქმედებითი გვარი'
    if class_morph_type_en == 'Caus':
        return 'კაუზატიური'
    if class_morph_type_en == 'MedPass':
        return 'საშუალ-ვნებითი გვარი'
    if class_morph_type_en == 'Pass':
        return 'ვნებითი გვარი'
    if class_morph_type_en == 'StatPass':
        return 'სტატიკური ვნებითი გვარი'

def morph_type_ka(morph_type_en):
    if morph_type_en == 'active':
        return 'მოქმედებითი'
    if morph_type_en == 'causative':
        return 'კაუზატიური'
    if morph_type_en == 'stative-passive':
        return 'სტატიკური ვნებითი'
    if morph_type_en == 'passive':
        return 'ვნებითი'

def remove_control_characters(s):
        return ''.join(c for c in s if unicodedata.category(c)[0] != 'C')

ka2en= {'\u10D0': 'a',
        '\u10D1': 'b',
        '\u10D2': 'g',
        '\u10D3': 'd',
        '\u10D4': 'e',
        '\u10D5': 'v',
        '\u10D6': 'z',
        '\u10D7': 'T',
        '\u10D8': 'i',
        '\u10D9': 'k',
        '\u10DA': 'l',
        '\u10DB': 'm',
        '\u10DC': 'n',
        '\u10DD': 'o',
        '\u10DE': 'p',
        '\u10DF': 'J',
        '\u10E0': 'r',
        '\u10E1': 's',
        '\u10E2': 't',
        '\u10E3': 'u',
        '\u10E4': 'f',
        '\u10E5': 'q',
        '\u10E6': 'R',
        '\u10E7': 'y',
        '\u10E8': 'S',
        '\u10E9': 'C',
        '\u10EA': 'c',
        '\u10EB': 'Z',
        '\u10EC': 'w',
        '\u10ED': 'W',
        '\u10EE': 'x',
        '\u10EF': 'j',
        '\u10F0': 'h'
}
# Mireille's transliteration
ka2en = { '\u10D0': 'a', '\u10D1': 'b', '\u10D2': 'g', '\u10D3': 'd', '\u10D4': 'e', '\u10D5': 'v', '\u10D6': 'z', '\u10D7': "t", '\u10D8': 'i', '\u10D9': "k'", '\u10DA': 'l', '\u10DB': 'm', '\u10DC': 'n', '\u10DD': 'o', '\u10DE': "p'", '\u10DF': 'zh', '\u10E0': 'r', '\u10E1': 's', '\u10E2': "t'", '\u10E3': 'u', '\u10E4': "p", '\u10E5': "k", '\u10E6': 'gh', '\u10E7': "q'", '\u10E8': 'sh', '\u10E9': "ch", '\u10EA': "ts", '\u10EB': 'dz', '\u10EC': "ts'", '\u10ED': "ch'", '\u10EE': 'kh', '\u10EF': 'j', '\u10F0': 'h' }
 

# We should use it when direct  transliteration from EN to KA is not good and different terms are needed in EN and in KA
different_terms = ["class_morph_type", "lang", "morph_type", "number", "tense"]

# To form "value" - here all property names (subjects) should be listed
subj = ["caus_sf", "class_morph_type", "c-root", "ending", "impr_pv", "lang", "morph_type", "nasal_infix", "number", "obj_pers", "part_pfx", "part_sfx", "passive_sfx", "person", "pf_12_pv", "pf_pv", "postradical", "pre2", "preradical", "preverb", "root", "sf2", "tense", "type_aorist_3sg", "type_optative", "type_pr_st_ext", "type_subj12_sfx", "type_subj3_sfx", "vn2", "vv"]

# To form "obj_property" - here should be liste whose property names which should be converted as "value_name" and transliterated into 2 langueage: EN and KA 
obj_property_en_ka = ["caus_sf", "c-root", "root", "ending", "impr_pv", "nasal_infix", "part_pfx", "part_sfx", "passive_sfx", "pf_12_pv", "pf_pv", "postradical", "pre2", "preradical", "preverb", "sf2", "type_aorist_3sg", "type_optative", "type_pr_st_ext", "type_subj12_sfx", "type_subj3_sfx", "vn2", "vv"]


row,col = df.shape 
illegal_characters = ['{', '}', '|', '\\', '^', '~', '[', ']', '"', ':', '?', '$', '(', ')']

n1=0
n2=0
x=df.columns[0] 
for i in range(row): 
        f_ka=df[x][i]
        f=tr(f_ka,ka2en)
        n1 += 1
        s = "s"+str(n1)
        print(f'<{s}> rdf:type <inflected_verb> .') 
        for j in range(col-1): 
                n2 += 1
                c = df.columns[j+1] 
                r = df[c][i]
                if (c == 'tense'):
                    y_en = f+"_"+r
                    y_ka = f_ka+"_"+tense_ka(r)
                if (c == 'person'):
                    y_en = y_en+"_"+r
                    y_ka = y_ka+"_"+r
                if (c == 'number'):
                    y_en = y_en+r
                    y_ka = y_ka+number_ka(r)
                if (c == 'vn2'):
                    y_en = y_en+"_"+tr(r,ka2en)
                    y_ka = y_ka+"_"+r

                if (c in obj_property_en_ka) and ( r != '-'):
                    r1 = r+'_'+c
                    print(f'<{s}> <{c}> <{tr(r1,ka2en)}> .')
                    print(f'<{tr(r1,ka2en)}> rdfs:label "{r}"@ka .')
                    print(f'<{tr(r1,ka2en)}> rdfs:label "{tr(r,ka2en)}"@en .')
                elif (c in subj) and (r != '-'):
                    print(f'<{s}> <{c}> <{tr(r,ka2en)}> .')
                    if (c in different_terms):
                        if (c == 'tense'):
                            print(f'<{tr(r,ka2en)}> rdfs:label "{tense_ka(r)}"@ka .')
                            print(f'<{tr(r,ka2en)}> rdfs:label "{tr(r,ka2en)}"@en .')
                        elif (c == 'number'):
                            print(f'<{tr(r,ka2en)}> rdfs:label "{number_ka(r)}"@ka .')
                            print(f'<{tr(r,ka2en)}> rdfs:label "{tr(r,ka2en)}"@en .')
                        elif (c == 'lang'):
                            print(f'<{tr(r,ka2en)}> rdfs:label "{lang_ka(r)}"@ka .')
                            print(f'<{tr(r,ka2en)}> rdfs:label "{tr(r,ka2en)}"@en .')
                        elif (c == 'class_morph_type'):
                            print(f'<{tr(r,ka2en)}> rdfs:label "{class_morph_type_ka(r)}"@ka .')
                            print(f'<{tr(r,ka2en)}> rdfs:label "{tr(r,ka2en)}"@en .')
                        elif (c == 'morph_type'):
                            print(f'<{tr(r,ka2en)}> rdfs:label "{morph_type_ka(r)}"@ka .')
                            print(f'<{tr(r,ka2en)}> rdfs:label "{tr(r,ka2en)}"@en .')
                        else:
                            print(f'<{tr(r,ka2en)}> rdfs:label "{r}"@ka .')
                            print(f'<{tr(r,ka2en)}> rdfs:label "{tr(r,ka2en)}"@en .')
                else:
                    print(f'<{s}> <{c}> <{tr(r,ka2en)}> .')
                if (c == 'vn2') and (c != '-'):
#                    print(f'<{tr(r,ka2en)}> rdfs:seeAlso <https://translate.ge/word/#{r}> .')
                    print(f'<{tr(r,ka2en)}_vn2> rdfs:seeAlso <https://beta2.translate.ge/api/translate?from=ka&to=en&str={r}> .')
        print(f'<{s}> rdfs:label "{y_en}"@en .')
        print(f'<{s}> rdfs:label "{y_ka}"@ka .')
        print(f'<{s}> <surface_form> <{f}> .') 
        print(f'<{f}> rdfs:label "{f_ka}"@ka .') 
        print(f'<{f}> rdfs:label "{f}"@en .') 
