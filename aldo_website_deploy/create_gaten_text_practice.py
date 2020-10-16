from openpyxl import load_workbook
workbook=load_workbook(filename="nederlandswoorden.xlsx")

sheet=workbook.active
i=0
for source,target in zip(sheet['A'],sheet['E']):
    try:
        woorden_source=source.value.split(" ")
        woorden_target=target.value.split(" ")
    except(AttributeError):
        i=i+1
        continue
    for each_word_in_source in woorden_source:
        if each_word_in_source in woorden_target:
            woorden_target[woorden_target.index(each_word_in_source)]="..."
        else:
            continue
    sheet["C{}".format(i+1)].value=" ".join(woorden_target)
    i=i+1
workbook.save(filename="hello_world_append.xlsx")