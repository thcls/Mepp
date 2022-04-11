import tabula
import os
import pandas as pd

def get_day_menu(pdf_filepath, dia_semana, almoco=True):
  # dia_semana
  # 1 - Segunda
  # 2 - Terça
  # 3 - Quarta
  # 4 - Quinta
  # 5 - Sexta

  # almoco = True -> retorna cardapio do almoco
  # almoco = False -> retorna cardapio da janta
  
  tables = tabula.read_pdf(pdf_filepath, pages="all")
  if almoco:
    table = tables[0]
  else:
    table = tables[1]
  #cardapio = table.iloc[:, dia_semana]
  print(table)
  menu_items = []
  for index, row in table.iterrows():
    if not pd.isna(table.iloc[index, 0]):
      categ = table.iloc[index, 0]
      if index != 0:
        #print("")
        menu_items.append("")
      #print(categ.replace('\r', ''))
      menu_items.append(categ.replace('\r', ''))
      #print('------------------')
      menu_items.append('------------------')
    if not pd.isna(table.iloc[index, dia_semana]):
      #print(table.iloc[index, dia_semana].replace('\r', '\n'))
      menu_items.append(table.iloc[index, dia_semana].replace('\r', '\n'))
  return '\n'.join(menu_items)