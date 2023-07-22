import import_ipynb
from NLP_preprocessing import new_line_tabs
from NLP_preprocessing import remove_HTML_Tags
from NLP_preprocessing import remove_links
from NLP_preprocessing import remove_whitespaces
from NLP_preprocessing import remove_accented_Word
from NLP_preprocessing import case_conversion
from NLP_preprocessing import reduce_repeated_characters
from NLP_preprocessing import expand_contraction_words
from NLP_preprocessing import remove_special_characters
from NLP_preprocessing import remove_stopwords
from NLP_preprocessing import spell_correction
from NLP_preprocessing import lemmatization
import streamlit as st
import base64
import pandas as pd


def main():
    @st.cache_data
    def load_css(file_path):
        with open(file_path) as f:
            return f"<style>{f.read()}</style>"

    # Load the custom CSS
    custom_css = load_css("custom.css")
    st.markdown(custom_css, unsafe_allow_html=True)


    st.title("NLP Preprocessing Application")
    st.write("Upload CSV as input for preprocessing of text")
    upload = st.file_uploader("Upload CSV")
    if upload is not None:
        df = pd.read_csv(upload)
        df = pd.DataFrame(df)
        st.table(df.head())
        st.write("For which column do you want to apply preprocessing")
        selected_column = st.radio("Select a column", df.columns)
        selected_value = df[selected_column]
# Create checkboxes
        st.markdown(
            """
        <style>
    .   checkbox-container > * {
        display: inline-block;
        margin-right: 10px;
        }
        </style>
        """,
            unsafe_allow_html=True
        )

        # col1, col2, col3 = st.columns(3)
        # with col1:
        #     checkbox1 = st.checkbox("Remove Newline & Tabs")
        # with col2:
        #     checkbox2 = st.checkbox("Remove HTML Tags")
        # with col3:
        #     checkbox3 = st.checkbox("Remove Links")

        # col4, col5, col6 = st.columns(3)
        # with col4:
        #     checkbox4 = st.checkbox("Remove WhiteSpaces")
        # with col5:
        #     checkbox5 = st.checkbox("Remove Accented Words")
        # with col6:
        #     checkbox6 = st.checkbox("Case Conversion")

        # col7, col8, col9 = st.columns(3)
        # with col4:
        #     checkbox7 = st.checkbox("Remove Repitation")
        # with col5:
        #     checkbox8 = st.checkbox("Expand Contraction words")
        # with col6:
        #     checkbox9 = st.checkbox("Remove Special characters")
        # col10, col11, col12 = st.columns(3)

        # with col4:
        #     checkbox10 = st.checkbox("Remove Stop Words")
        # with col5:
        #     checkbox11 = st.checkbox("Spelling Corrections")
        # with col6:
        #     checkbox12 = st.checkbox("Lemmatization")

        # def apply_functions(d, selected_functions):
        #     result_column = df[selected_column].copy()  # Replace 'YourColumn' with the actual column name

        #     for function in selected_functions:
        #         if function == 'Remove Newline & Tabs':
        #             result_column = new_line_tabs(result_column)
        #             return result_column
        #     for function in selected_functions:
        #         if function == 'Remove HTML Tags':
        #             result_column = remove_HTML_Tags(result_column)
        #             return result_column
        #     for function in selected_functions:
        #         if function == 'Remove Links':
        #             result_column = remove_links(result_column)
        #             return result_column
        #     for function in selected_functions:
        #         if function == 'Remove WhiteSpaces':
        #             result_column = remove_whitespaces(result_column)
        #             return result_column
        #     for function in selected_functions:
        #         if function == 'Remove Accented Words':
        #             result_column = remove_accented_Word(result_column)
        #             return result_column
        #     for function in selected_functions:
        #         if function == 'Case Conversion':
        #             result_column = case_conversion(result_column)
        #             return result_column
        #     for function in selected_functions:
        #         if function == 'Remove Repitation':
        #             result_column = reduce_repeated_characters(result_column)
        #             return result_column
        #     for function in selected_functions:
        #         if function == 'Expand Contraction words':
        #             result_column = expand_contraction_words(result_column)
        #             return result_column
        #     for function in selected_functions:
        #         if function == 'Remove Special characters':
        #             result_column = remove_special_characters(result_column)
        #             return result_column
        #     for function in selected_functions:
        #         if function == 'Remove Stop Words':
        #             result_column = remove_stopwords(result_column)
        #             return result_column
        #     for function in selected_functions:
        #         if function == 'Spelling Corrections':
        #             result_column = spell_correction(result_column)
        #             return result_column
        #     for function in selected_functions:
        #         if function == 'Lemmatization':
        #             result_column = lemmatization(result_column)
        #             return result_column
        st.write("Which functions do you want to apply")
        functions = ['Remove Newline & Tabs', 'Remove HTML Tags', 'Remove Links', 'Remove WhiteSpaces', 'Remove Accented Words',
                       'Case Conversion', 'Remove Repitation', 'Expand Contraction words', 'Remove Special characters',
                       'Remove Stop Words', 'Spelling Corrections', 'Lemmatization']
          # selected_functions = [st.checkbox(function) for function in functions]
        col1, col2, col3 = st.columns(3)
        with col1:
            checkbox1 = st.checkbox("Remove Newline & Tabs")
        with col2:
            checkbox2 = st.checkbox("Remove HTML Tags")
        with col3:
            checkbox3 = st.checkbox("Remove Links")

        col4, col5, col6 = st.columns(3)
        with col4:
            checkbox4 = st.checkbox("Remove WhiteSpaces")
        with col5:
            checkbox5 = st.checkbox("Remove Accented Words")
        with col6:
            checkbox6 = st.checkbox("Case Conversion")

        col7, col8, col9 = st.columns(3)
        with col4:
            checkbox7 = st.checkbox("Remove Repitation")
        with col5:
            checkbox8 = st.checkbox("Expand Contraction words")
        with col6:
            checkbox9 = st.checkbox("Remove Special characters")
        col10, col11, col12 = st.columns(3)

        with col4:
            checkbox10 = st.checkbox("Remove Stop Words")
        with col5:
            checkbox11 = st.checkbox("Spelling Corrections")
        with col6:
            checkbox12 = st.checkbox("Lemmatization")
        result_column = df[selected_column].copy()
            # result = apply_functions(df, selected_functions)

            # if st.button("Apply Functions"):
        if checkbox1:
            result_column = new_line_tabs(result_column)
        if checkbox2:
            result_column = result_column.apply(remove_HTML_Tags)
        if checkbox3:
            result_column = result_column.apply(remove_links)
        if checkbox4:
            result_column = result_column.apply(remove_whitespaces)
        if checkbox5:
            result_column = result_column.apply(remove_accented_Word)
        if checkbox6:
            result_column = result_column.apply(case_conversion)
        if checkbox7:
            result_column = result_column.apply(reduce_repeated_characters)
        if checkbox8:
            result_column = result_column.apply(expand_contraction_words)
        if checkbox9:
            result_column = result_column.apply(remove_special_characters)
        if checkbox10:
            result_column = result_column.apply(remove_stopwords)
        if checkbox11:
            result_column = result_column.apply(spell_correction)
        if checkbox12:
            result_column = result_column.apply(lemmatization)
        
        df['Output'] = result_column
            # st.write(selected_functions)
        if st.button('Apply'):
            st.write(df.head())
        if st.button('Download CSV'):
            csv = df.to_csv()
                    # Convert DataFrame to CSV string
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="data.csv">Download CSV File</a>'
            st.markdown(href, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
