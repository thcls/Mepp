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
  #menu_string = ""
  for index, row in table.iterrows():
    if not pd.isna(table.iloc[index, 0]):
      categ = table.iloc[index, 0]
      if index != 0:
        print("")
        #menu_string = menu_string + "\n"
      print(categ.replace('\r', ''))
      #menu_string = menu_string + categ.replace('\r', '')
      print('------------------')
      #menu_string = menu_string + '------------------'
    print(table.iloc[index, dia_semana].replace('\r', '\n'))
    #menu_string = menu_string + table.iloc[index, dia_semana].replace('\r', '\n')
    #return menu_string