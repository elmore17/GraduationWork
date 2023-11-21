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

# Вставка данных в шаблон
def create_draft(json_file_path):
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
    context['predgos'] = 'Баранчиков Алексей Иванович'
    context['score'] = 'отлично'
    if (context['score'] == 'удовлетворительно'):
        context['haracteransver1'] = 'Студент показал достаточный уровень подготовки. Недостаточно глубоко изучил и' 
        context['haracteransver2'] = 'проанализировал предметную область. При защите ВКР студент проявил неуверенность,'
        context['haracteransver3'] = 'показал слабое знание вопросов темы, не дал полного аргументированного ответа на'
        context['haracteransver4'] = 'заданные вопросы.'
    elif (context['score'] == 'отлично'):
        context['haracteransver1'] = 'Студент показал высокий уровень подготовки и глубокие системные знания,' 
        context['haracteransver2'] = 'свободно оперирует данными исследования, дал развернутые и полные ответы на'
        context['haracteransver3'] = 'поставленные вопросы'
    elif (context['score'] == 'хорошо'):
        context['haracteransver1'] = 'Студент показал высокий уровень подготовки и глубокие системные знания,' 
        context['haracteransver2'] = 'но на дополнительные вопросы комиссии были даны неполные ответы.'
    context['ekzscore'] = 'не предусмотрен учебным планом'
    context['nodata'] = '–'
    context['data'] = '14.06.2023'
    context['scorediplom'] = 'без отличия'
    context['predgossokr'] = 'Баранчиков А.И.'
    context['sekretgossokr'] = 'Трохаченкова Н.Н.'
    doc = DocxTemplate('shablon.docx')
    doc.render(context)
    doc.save("generated_docx.docx")