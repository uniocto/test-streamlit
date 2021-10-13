import tempfile
import openpyxl
from pathlib import Path
from abc import ABC, abstractclassmethod
import streamlit as st


class Page(ABC):
    name: str

    @abstractclassmethod
    def render(cls):
        pass


class UploadPage(Page):
    name = "Upload"

    @classmethod
    def render(cls, state: dict):
        st.title("Upload")
        uploaded_file = st.file_uploader("Choose your .xlsx files", type="xlsx")

        if uploaded_file is not None:
            # Make temp file path from uploaded file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp_file:
                st.markdown("## Original PDF file")
                fp = Path(tmp_file.name)
                fp.write_bytes(uploaded_file.getvalue())
                st.write(cls._show_excel_data(tmp_file.name))
        form = st.form("my_form")
        data = form.slider("Inside the form")
        submit = form.form_submit_button("Submit")

    def _show_excel_data(self, file_path: str):
        wb = openpyxl.load_workbook(file_path)
        sh = wb["アンケート"]
        return sh["A4"].value


class ProcessPage(Page):
    name = "Process"

    @classmethod
    def render(cls, state: dict):
        st.title("Process")


class AnalysisPage(Page):
    name = "Analysis"

    @classmethod
    def render(cls, state: dict):
        st.title("Analysis")


class Pages:
    pageComponents = (UploadPage, ProcessPage, AnalysisPage)
    page_names = list(i.name for i in pageComponents)
