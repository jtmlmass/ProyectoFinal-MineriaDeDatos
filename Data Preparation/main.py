import data_prep as dp
from processing_files import processing
import pandas

root_path = '/home/tomas/Desktop/Mineria de Datos/ProyectoFinal-MineriaDeDatos/noncomm_use_subset'
columns = ['paper_id', 'title', 'abstract', 'body_text']
params = {'root_path': root_path}
processing_ = processing(params)
papers = pandas.DataFrame(processing_.dict_, columns=columns)

for paper in papers:
    print(paper['body_tcext'])
    processed_text = dp.process_text(paper['body_text'])
    print(processed_text)
