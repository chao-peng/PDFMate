from pypdf import PdfMerger, PdfReader, PdfWriter


def parse_ranges(range_string):
    ranges = str(range_string).split(',')
    result = []

    for item in ranges:
        if '-' in item:
            start, end = item.split('-')
            result.extend(range(int(start), int(end) + 1))
        else:
            result.append(int(item))
    return result


class PDFMate(object):
    @staticmethod
    def merge(*args, o):
        merger = PdfMerger()
        for pdf in args:
            if ":" in pdf:
                page_range = parse_ranges(pdf[pdf.find(":") + 1:])
                pdf = pdf[: pdf.find(":")]
                for page in page_range:
                    merger.append(pdf, pages=(page - 1, page))
            else:
                merger.append(pdf)

        merger.write(o)
        merger.close()

    @staticmethod
    def split(*args, i):
        pdf = PdfReader(i)
        filename = i
        if "/" in i:
            filename = i[i.rfind("/") + 1:]
        basename = filename
        if ".pdf" in filename:
            basename = filename[: filename.rfind(".pdf")]
        for r in args:
            new_filename = f"{basename}_{r}.pdf"
            pages = parse_ranges(r)
            pdf_writer = PdfWriter()
            for page in pages:
                pdf_writer.add_page(pdf.pages[page - 1])
            with open(new_filename, "wb") as out:
                pdf_writer.write(out)
            pdf_writer.close()
