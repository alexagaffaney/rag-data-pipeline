from langchain_community.document_loaders import PyPDFLoader


def load_pdf_file(file) -> list:
    print("Loading file: {}".format(file))

    # load pdf file and split into pages
    loader = PyPDFLoader(file)
    pages = loader.load_and_split()

    return pages
