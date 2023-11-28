# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter.adapter import ItemAdapter
import sqlite3
class AmazonPipeline:
    def __init__(self) -> None:
         self.create_connection()
         self.create_table()
    
    def create_connection(self):
        self.conn=sqlite3.connect("mydata.db")
        self.curr=self.conn.cursor()
    def create_table(self):
        self.curr.execute('''Drop TABLE IF  EXISTS data_tb''')
        self.curr.execute('''CREATE TABLE data_tb (product_name TEXT , product_author TEXT,product_price TEXT,product_imagelink TEXT)''')


    def process_item(self, item, spider):
        self.store_db(item)
        return item
    def store_db(self,item):
        self.curr.execute("INSERT INTO data_tb VALUES(?,?,?,?)",(item['product_name'][0],item['product_author'][0],item['product_price'][0],item['product_imagelink'][0]))
        self.conn.commit()
  
