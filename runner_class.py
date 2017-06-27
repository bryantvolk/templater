import glob
from workbook_handler import *
class Runner:

    def __init__(self,as_recieved,template):
        self.as_recieved = as_recieved
        self.template = template

    def work(self,ui):
        handler = Workbook_handler(self.as_recieved, self.template)
        self.completed = 0
        self.progress = ui.progressBar
        print 'writing to file: %s using template: %s' %(
                self.template, self.as_recieved)
        for sheet in handler.recieved.worksheets:
            if sheet.title and not sheet.title[0].isalpha():
                print sheet.title
                self.completed += 10
                self.progress.setValue(self.completed)
                handler.copy_template(sheet.title)
                handler.copy_headers(sheet.title)
                handler.save_sheet(self.template)
        self.progress.setValue(100)
