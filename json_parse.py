import re
def f_getDevlStatus(in_metaData):
    """extract entity metadata json fields from curricunet

    :param in_metaData: JSON of metaData from curricunet v4
    :return: return list of data
    """
    return_val = []

    return_val.append(in_metaData['entityId'])
    return_val.append(in_metaData['entityTitle'])
    return_val.append(in_metaData['processActionType'])
    return_val.append(in_metaData['proposalType'])
    return_val.append(in_metaData['status'])

    return return_val


def f_getDelSection(in_secData):
    """extract course info and delete data

    :param in_secData: JSON (0) subsection from curricunet v4
    :return: return list of data
    """
    return_val = []
    temp = in_secData[0]['fields']
    return_val.append(temp[0]['lookUpDisplay'])  # prefix
    return_val.append(temp[1]['fieldValue'])  # crsNumb
    return_val.append(temp[2]['fieldValue'])  # title
    return_val.append('')  # shortTitle
    return_val.append('')  # narrative

    return_val.append(in_secData[1]['fields'][0]['lookUpDisplay'])  # term
    return_val.append(in_secData[1]['fields'][1]['fieldValue'])  # year
    return_val.append('')  # crsJustify

    return return_val


def f_getSection(in_secData):
    """extract course info and justification data from curricunet

    :param in_secData: JSON (0) subsection from curricunet v4
    :return: return list of data
    """
    return_val = []
    temp = in_secData[0]['fields']
    return_val.append(temp[1]['lookUpDisplay'])  # prefix
    return_val.append(temp[2]['fieldValue'])  # crsNumb
    return_val.append(temp[3]['fieldValue'])  # title
    return_val.append(temp[4]['fieldValue'])  # shortTitle
    return_val.append(temp[5]['fieldValue'])  # narrative

    temp = in_secData[1]['fields']
    return_val.append(temp[0]['lookUpDisplay'])  # term
    return_val.append(temp[1]['fieldValue'])  # year
    return_val.append(in_secData[2]['fields'][0]['fieldValue'])  # crsJustify

    return return_val


def f_getCrsList(in_secData):
    """extract cross listed data from curricunet

    :param in_secData: JSON (1) subsection from curricunet v4
    :return: return list of data
    """
    return_val = []
    for i in range(0, len(in_secData)):
        # print(in_secData[i]['attributes']['sectionName'])
        return_val.append(in_secData[i]['attributes']['sectionName'])

    return return_val


def f_getUnits(in_secData):
    """extract min and max unit data from curricunet

    :param in_secData: JSON (2) subsection from curricunet v4
    :return: return list of data
    """
    return_val = []

    # var units
    return_val.append(in_secData[0]['fields'][0]['fieldValue'])
    # min units and hrs
    return_val.append(in_secData[1]['fields'][0]['fieldValue'])  # Units
    return_val.append(in_secData[2]['fields'][0]['fieldValue'])  # LecHrs
    return_val.append(in_secData[2]['fields'][1]['fieldValue'])  # ActivityHrs
    return_val.append(in_secData[2]['fields'][2]['fieldValue'])  # WrkExpHrs
    return_val.append(in_secData[2]['fields'][3]['fieldValue'])  # LabHrs
    return_val.append(in_secData[2]['fields'][4]['fieldValue'])  # Homework Hrs
    return_val.append(in_secData[2]['fields'][5]['fieldValue'])  # Additional Homework Hrs
    return_val.append(in_secData[2]['fields'][6]['fieldValue'])  # total Hrs
    # max units and hrs
    return_val.append(in_secData[3]['fields'][0]['fieldValue'])  # Units
    return_val.append(in_secData[4]['fields'][0]['fieldValue'])  # LecHrs
    return_val.append(in_secData[4]['fields'][1]['fieldValue'])  # ActivityHrs
    return_val.append(in_secData[4]['fields'][2]['fieldValue'])  # WrkExpHrs
    return_val.append(in_secData[4]['fields'][3]['fieldValue'])  # LabHrs
    return_val.append(in_secData[4]['fields'][4]['fieldValue'])  # Homework Hrs
    return_val.append(in_secData[4]['fields'][5]['fieldValue'])  # Additional Homework Hrs
    return_val.append(in_secData[4]['fields'][6]['fieldValue'])  # total Hrs

    return return_val


def f_getFieldTrip(in_secData):
    """extract field trip data from curricunet

    :param in_secData: JSON (6) subsection from curricunet v4
    :return: return list of data
    """
    return_val = []

    l_fieldtrips = in_secData[0]['fields']
    return_val.append(l_fieldtrips[0]['fieldValue'])  # required
    return_val.append(l_fieldtrips[1]['fieldValue'])  # type

    return return_val


def f_getGrdMethod(in_secData):
    """extract grading method data from curricunet

    :param in_secData: JSON (7) subsection from curricunet v4
    :return: return list of data
    """
    return_val = []

    return_val.append(in_secData[0]['fields'][0]['lookUpDisplay']) # grdMethod
    return_val.append(in_secData[1]['fields'][0]['lookUpDisplay']) # repeatFreq
    return_val.append(in_secData[2]['fields'][0]['fieldValue']) # maxUnitsAllowed
    return_val.append(in_secData[3]['fields']) # grdMethod3

    return return_val


def f_getDiscipline(in_secData):
    """extract min qual data from curricunet

    :param in_secData: JSON (8) subsection from curricunet v4
    :return: return list of data
    """
    return_val = []

    l_discipline = in_secData[1]['subsections']
    l_minQual = ''

    if len(l_discipline) > 0:
        for i in range(0, len(l_discipline)):
            # print(l_discipline[i]['fields'][0])
            l_minQual += l_discipline[i]['fields'][0]['lookUpDisplay'] + '\n'

    return_val.append(l_minQual.strip('\n'))

    return return_val


def f_getSLO(in_secData):
    """extract student learning outcome data from curricunet

    :param in_secData: JSON (9) subsection from curricunet v4
    :return: return list of data
    """
    return_val = []
    l_geArea = in_secData[1]['subsections']
    l_geSLO = '<p>After successful completion of this course, students will be able to:</p>'
    l_geSLO += '<ol type="A">'

    if len(l_geArea) > 0:
        for i in range(0, len(l_geArea)):
            curGe = l_geArea[i]["fields"][0]['fieldValue']
            l_geSLO += '<li>' + curGe + '</li>'
    l_geSLO += '</ol>'
    return_val.append(l_geSLO)

    return return_val


def f_getNotes(in_secData):
    """extract course classification and notes data from curricunet

    :param in_secData: JSON (16) subsection from curricunet v4
    :return: return list of data
    """
    return_val = []

    # %%Codes and Notes
    return_val.append(in_secData[0]['fields'][0]['fieldValue'])  ##Course_CAT
    temp = in_secData[1]['fields']
    return_val.append(re.sub('[.]', '', temp[0]['lookUpDisplay'][0:7]))  ## TOP
    return_val.append(temp[1]['lookUpDisplay']) ## CIP

    return_val.append(in_secData[2]['fields'][0]['lookUpDisplay'])  ## SAM
    temp = in_secData[3]['fields']
    return_val.append(temp[0]['lookUpDisplay'])  ## COOP
    return_val.append(temp[1]['lookUpDisplay'])  ## CB21
    return_val.append(temp[2]['lookUpDisplay'])  ## Funding agency
    return_val.append(temp[3]['fieldValue'])  ## Catalog Notes
    return_val.append(temp[4]['fieldValue'])  ## Time Schedule Notes
    return_val.append(temp[5]['fieldValue'])  ## Internal Notes

    return return_val


def f_getAppInfo(in_secData):
    """extract origination and approval date data from curricunet

    :param in_secData: JSON (17) subsection from curricunet v4
    :return: return list of data
    """
    return_val = []

    ## Originator and Approval Date
    l_originator = in_secData[0]['fields']
    return_val.append(l_originator[0]['lookUpDisplay'])  ## origPerson
    return_val.append(l_originator[1]['fieldValue'])  ##origDeptChair
    return_val.append(l_originator[2]['fieldValue'])  ##origDean
    try:
        l_keyDates = in_secData[1]['subsections'][0]['fields']
        return_val.append(l_keyDates[0]['lookUpDisplay'])  ## Approval Text
        return_val.append(l_keyDates[1]['fieldValue'])  ## Approvel Date
    except IndexError:
        return_val.append('')
        return_val.append('')

    return return_val


def f_getCoContrib(in_secData):
    """extract cocontributor name data from curricunet

    :param in_secData: JSON (18) subsection from curricunet v4
    :return: return list of data
    """
    return_val = []

    try:
        l_cocontrib = in_secData[0]['subsections'][0]['fields']
        return_val.append(l_cocontrib[0]['lookUpDisplay'])
    except IndexError:
        return_val.append('');

    return return_val


def f_extract_metaData(in_prog):
    """extract json metadata fields within a specific program

    :param in_prog: program JSON from curricunet v4
    :return: return list of data
    """
    l_metaData = in_prog['entityMetadata']

    return_val = f_getDevlStatus(l_metaData)

    return return_val


def f_extractJsonDel(in_prog):
    """extract json fields within a specific delete program

    :param in_prog: program JSON from curricunet v4
    :return: return list of data
    """
    l_coreData = in_prog['entityFormData']['rootSections']

    return_val = f_getDelSection(l_coreData[0]['subsections'])
    return_val += [''] * 44

    return return_val


def f_extractJsonNewCR(in_prog):
    """extract json fields within a specific new program

    :param in_prog: program JSON from curricunet v4
    :return: return list of data
    """
    # l_attribute = in_prog['attributes']
    l_coreData = in_prog['entityFormData']['rootSections']

    return_val = f_getSection(l_coreData[0]['subsections'])
    return_val += f_getCrsList(l_coreData[1]['subsections'])
    return_val += f_getUnits(l_coreData[2]['subsections'])
    return_val += f_getFieldTrip(l_coreData[6]['subsections'])
    return_val += f_getGrdMethod(l_coreData[7]['subsections'])
    return_val += f_getDiscipline(l_coreData[8]['subsections'])
    return_val += f_getSLO(l_coreData[9]['subsections'])
    return_val += f_getNotes(l_coreData[16]['subsections'])
    return_val += f_getAppInfo(l_coreData[17]['subsections'])
    return_val += f_getCoContrib(l_coreData[18]['subsections'])

    return return_val
