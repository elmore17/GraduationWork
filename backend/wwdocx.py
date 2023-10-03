from docxtpl import DocxTemplate


context = {}
context['title_text'] = 'Выписка из протокола №1'
context['title_kis'] = 'Заседание кафедры'
doc = DocxTemplate('../example.docx')
doc.render(context)
doc.save("../generated_docx.docx")