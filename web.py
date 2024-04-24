import csv
import json
import pandas as pd
import streamlit as st
import urllib3
from f_print_time import f_print_time
import json_parse

# url paths
gen_URL_path = r'https://secure.curricunet.com/scripts/webservices/generic_meta/clients/versions/v4/ccsf.cfc?'
gen_rep_type = r'method=getCourses'
gen_req = ''
gen_retFormat = r'&returnformat=json'
http = urllib3.PoolManager()

def main():
    l_csv = None
    l_finFile = None
    l_numRec = 0
    st.set_page_config(page_title= "This is CCSF Curricunet App")
    st.title("CCSF Curricunet process")
    l_cur_time = f_print_time()

    # menu = ['Home', 'Dataset', 'About']
    # choice = st.sidebar.selectbox("Menu", menu)
    # st.sidebar.success("Select any page from Here")
    st.write(f"The current time is %s" % l_cur_time)
    st.subheader("Home")

    l_csv = st.file_uploader("Choose a CSV file", type=['csv'])

    l_dispTitle = st.checkbox('Display Title')
    if st.button("Process"):
        if l_csv is not None:
            l_fileDetail = {
                "Filename": l_csv.name,
                "FileType": l_csv.type,
                "FileSize": l_csv.size
            }
            st.write(l_fileDetail)


            crsFile = pd.read_csv(l_csv)
            # st.dataframe(crsFile)


            # create dataframe headers
            enty_header = ['DEPT_CODE', 'COLL_CODE', 'EID', 'Title',
                           'procActionType',
                           'propType',
                           'propStatus', 'prefix', 'crsNumb', 'title',
                           'shrtTitle', 'ctlgDesc', 'Semester', 'Year',
                           'crsJustification',
                           'crossList1', 'crossList2', 'crossList3', 'varUnits',
                           'minUnits',
                           'minLecHrs', 'minActHrs', 'minWrkExpHrs', 'minLabHrs',
                           'min_hwHrs',
                           'min_addHwHrs', 'min_totHrs', 'maxUnits',
                           'maxLecHrs', 'maxActHrs', 'maxWrkExpHrs', 'maxLabHrs',
                           'max_hwHrs',
                           'max_addHwHrs', 'max_totHrs', 'reqFieldTrip',
                           'typeFieldTrip',
                           'grdMethod', 'repeatFreq', 'maxUnitsAllowed',
                           'grdMethod3',
                           'discipline', 'crsSLO', 'crsCat', 'crsTOP', 'crsCIP',
                           'crsSAM',
                           'crsCOOP', 'crsCB21', 'fundAgency', 'catalogNotes',
                           'timeSchedNotes',
                           'internalNotes', 'origPerson', 'origDeptChair',
                           'origDean', 'origDateType',
                           'origDate', 'coContrib', 'action'
                           ]
            cqEntydf = pd.DataFrame(columns=enty_header)

            # %% STEP 2 for each record create entity record
            st.write('Start: ' + f_print_time())
            for index, row in crsFile.iterrows():
                # get entity_id
                l_numRec += 1
                gen_req = r'&courseId=' + str(row.entity_id)

                # load json from URL
                cur_url = gen_URL_path + gen_rep_type + gen_req + gen_retFormat
                data = json.loads(http.request('GET', cur_url).data)

                # extract program data
                cur_prog = data['entityInstances'][0]
                cqEnty_rec = [row.DEPT_CODE, row.COLL_CODE]
                cqEnty_rec += json_parse.f_extract_metaData(cur_prog)
                if l_dispTitle:
                    st.write(cqEnty_rec[3])

                if (cqEnty_rec[4] == 'Deactivate'):
                    cqEnty_rec += json_parse.f_extractJsonDel(cur_prog);
                else:
                    cqEnty_rec += json_parse.f_extractJsonNewCR(cur_prog);

                cqEnty_rec = pd.DataFrame(cqEnty_rec).transpose()
                cqEnty_rec['type'] = row.propType
                cqEnty_rec.columns = enty_header
                cqEntydf = pd.concat([cqEntydf, cqEnty_rec],
                                     ignore_index=True)

            st.write(f'Number of records Processed: %i ' %l_numRec)
            st.write('End: ' + f_print_time())
            # st.dataframe(cqEntydf)
            l_finFile = cqEntydf.to_csv(quoting=csv.QUOTE_ALL, index=False,
                                        encoding='utf-8')
    if l_finFile is not None:
        st.download_button(
            label="Press to Download",
            data=l_finFile,
            file_name="stream_temp.csv",
            mime="text/csv",
        )

if __name__ == '__main__':
    main()