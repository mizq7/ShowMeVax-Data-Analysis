"""
    File: generate_smv_report_org
    CreateDate: 2/29/24
    UpdateDate: 11/12/24
    Author: MUINUL ISLAM
    GitHub: kzraryan-mu
    Email: mizq7@umsystem.edu
"""
from pdf_report_generator.pdf_report_generator import PdfReportGenerator
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col, upper, lit, when, concat, iff, coalesce, cast

# Import necessary modules and libraries here

""" user input start """
DATA_VERSION = '2023_FEB'
ROLE = 'NGBMI'
PATH_TEMPLATES = '../assets/html'
TITLE_REPORT = "ShowMeVax Data Quality Report: Assessing Missouri's Immunization Information System"
FILE_HTML = f'../results/html/smv_{DATA_VERSION}_org.html'
FILE_CSS = '../../assets/css/report.css'  # file_css is relative path from the file_html
FILE_PDF = f'../results/pdf/smv_{DATA_VERSION}_org.pdf'
""" user input end """


def get_analysis_data(s: Session):
    dm = s.table('IISDM.ETL.DC_DOMAIN')
    dcc = s.table('IISDM.ETL.DC_COMPONENT').with_column_renamed('DC_DOMAIN_ID', 'X_DC_DOMAIN_ID') \
        .with_column('TABLE_NOTE', coalesce(col('TABLE_NOTE'), lit('')))
    dc = s.table('IISDM.ETL.DC').with_column_renamed('DC_COMPONENT_ID', 'X_DC_COMPONENT_ID')
    data = s.table(f'IISDM.REPORT.IISDM_{DATA_VERSION}') \
        .with_column_renamed('DC_ID', 'X_DC_ID') \
        .filter(col('LEVEL').isNull())

    df_sp = dm.join(dcc, dm['DC_DOMAIN_ID'] == dcc['X_DC_DOMAIN_ID']) \
        .join(dc, dcc['DC_COMPONENT_ID'] == dc['X_DC_COMPONENT_ID']) \
        .join(data, dc['DC_ID'] == data['X_DC_ID']) \
        .filter(dcc['DC_COMPONENT_TYPE'] == 'Table') \
        .with_column('DC_RESULT',
                     when(col('RNG_START').is_null(), '')
                     .when(
                         (col('RNG_START') == 0) & col('PERCENTAGE_DC_PASS').between(col('RNG_START'), col('RNG_PASS')),
                         'PASS')
                     .when((col('RNG_START') == 0) & (col('PERCENTAGE_DC_PASS') > col('RNG_PASS')) & (
                             col('PERCENTAGE_DC_PASS') < col('RNG_INV')), 'INV')
                     .when((col('RNG_START') == 0) & col('PERCENTAGE_DC_PASS').between(col('RNG_INV'), col('RNG_FAIL')),
                           'FAIL')
                     .when((col('RNG_START') == 100) & col('PERCENTAGE_DC_PASS').between(col('RNG_PASS'),
                                                                                         col('RNG_START')),
                           'PASS')
                     .when((col('RNG_START') == 100) & (col('PERCENTAGE_DC_PASS') < col('RNG_PASS')) & (
                             col('PERCENTAGE_DC_PASS') > col('RNG_INV')), 'INV')
                     .when(
                         (col('RNG_START') == 100) & col('PERCENTAGE_DC_PASS').between(col('RNG_FAIL'), col('RNG_INV')),
                         'FAIL')
                     .otherwise('')
                     ) \
        .with_column('DC_TITLE_MOD'
                     , iff(col('ADDITIONAL_TITLE').is_not_null(),
                           concat(col('DC_TITLE'), lit(' '), col('ADDITIONAL_TITLE')),
                           col('DC_TITLE')
                           )
                     ) \
        .with_column(
        'RNG_SIGN'
        , when(col('RNG_START').is_not_null() & col('RNG_START') == 0, concat(lit('<= '), cast(col('RNG_PASS'), 'INT')))
        .when(col('RNG_START').is_not_null() & col('RNG_START') == 100,
              concat(lit('>= '), cast(col('RNG_PASS'), 'INT')))
        .otherwise('')
    ).sort(
        col('DC_DOMAIN_ORDER').asc(),
        col('DC_COMPONENT_ORDER').asc(),
        col('INTERNAL_ORDER').asc(),
        col('DC_ORDER').asc(),
        col('N_RECORDS').desc())
    return df_sp


def main():
    """
        Main function: Entry point of the script.
    """
    session = Session.builder.config('connection_name', 'smv').create()
    session.use_role(ROLE)

    df_glossary = session.table('IISDM.ETL.GLOSSARY').to_pandas()
    df_data = get_analysis_data(session).to_pandas()

    year, month = DATA_VERSION.split('_')
    name_report = f'{month} {year}'

    report = PdfReportGenerator(df_data=df_data,
                                df_glossary=df_glossary,
                                report_name=name_report,
                                report_title=TITLE_REPORT,
                                template_path=PATH_TEMPLATES,
                                css_file=FILE_CSS,
                                output_html_file=FILE_HTML,
                                output_pdf_file=FILE_PDF,
                                image_cache={})
    report.generate_report()


if __name__ == "__main__":
    main()
