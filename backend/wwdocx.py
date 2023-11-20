import json
from docx import Document
from docxtpl import DocxTemplate

def read_docx(docx_path, output_json_path):
    doc = Document(docx_path)
    unique_text_list = []

    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                text = cell.text.strip()
                if text and text not in unique_text_list:
                    unique_text_list.append(text)

    unique_text_tuple = tuple(unique_text_list)
    
    # Выбранные данные для вставки
    data = {
        'napravlen': unique_text_tuple[2],
        'studentA': unique_text_tuple[16],
        'title': unique_text_tuple[19],
        'nauchruk': unique_text_tuple[26],
        'rang': unique_text_tuple[28],
        'student': unique_text_tuple[35],
        'studentU': unique_text_tuple[48],
        'kval': unique_text_tuple[51],
        'spec': unique_text_tuple[54]
    }

    # Сохранение в JSON файл
    with open(output_json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)

docx_path = 'exprot.docx'
output_json_path = 'output.json'
read_docx(docx_path, output_json_path)

# Вставка данных в шаблон
json_file_path = 'output.json'
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    dataConst = json.load(json_file)
context = {}
context['napravlenie'] = dataConst['napravlen']
context['studentA'] = dataConst['studentA']
context['title'] = dataConst['title']
context['nauchruc'] = dataConst['nauchruk']
context['rang'] = dataConst['rang']
context['student'] = dataConst['student']
context['studentU'] = dataConst['studentU']
context['kval'] = dataConst['kval']
context['spec'] = dataConst['spec']
doc = DocxTemplate('shablon.docx')
doc.render(context)
doc.save("generated_docx.docx")