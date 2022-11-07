import tabula
from zipfile import ZipFile
from glob import glob

lista_tabelas = tabula.read_pdf("https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN541_RN542_RN544_546.pdf",
pages="all",encoding="ISO-8859-1")
print(len(lista_tabelas))

tabela = lista_tabelas

tabelas = sorted(glob("./*.csv"))

i=0
j=0
for table in lista_tabelas:
    i+= 1
    tabela = table.to_csv('tabela_'+str(i)+'_Anexo1.csv', index=False)
    print('Tabela '+str(i)+' convertida para .csv')



print("Compactando arquivos csv em Zipfile...")
with ZipFile("tabelas_Anexo1_compactadas.zip", "w") as zip:
    for tabela in tabelas:
        j+= 1
        zip.write("tabela_"+str(j)+"_Anexo1.csv")
        print("File ",j," compressed")
