import json
import sys
import xlsxwriter

class Chatito2Cognigy: 
    def __init__(self, input_path, output_path, intent):
         self._chattete_path = input_path 
         self._cognigy_path = output_path 
         self._intent = intent 
    
    def _write_to_csv(self):
        workbook = xlsxwriter.Workbook(self._cognigy_path) 
        worksheet = workbook.add_worksheet() 
        f = open(self._chattete_path, ) 
        data = json.load(f) 
        intent_name = self._intent 
        row = 0 
        for data in data[intent_name]:
            training_ex = '' 
            for i in data: 
                if i['type'] == 'Slot':
                    i['value'] = '[{0}]'.format(i['value'])
                    training_ex = training_ex + i['value'] 
                    worksheet.write(row, 0, intent_name) 
                    worksheet.write(row, 1, 'exampleSentence') 
                    worksheet.write(row, 2, training_ex) 
                    row = row + 1 
        f.close() 
        workbook.close() 
    def write_intents(self):
        self._write_to_csv() 
def main():
    input_template_path = sys.argv[1] 
    output_path = sys.argv[2] 
    intent = sys.argv[3]
    gen_train = Chatito2Cognigy(input_template_path, output_path, intent) 
    gen_train.write_intents()
    if __name__ == '__main__':
        main()