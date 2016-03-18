instructions for marked_text_pdf.py

before starting: 
open nbsite/settings_credentials.py and change the database name to match the one you use.
(if not working on localhost or port 5432, sqlAdder.py line 8 also needed to be updated)

1.import:
from marked_text_pdf import markedExtract

2.creating an instance:
m = markedExtract()

3.extracting marked text from pdf using source_id of the pdf:
#in order to work, the pdf need to be in folder tmp, and its name is "source_id.pdf"

m.extract_comments_for_pdf(source_id)

4.extracting marked text from pdf by source_id and comment_id:
#function "extract_comments_for_pdf" must be actived with the relavent source_id before using this function, in order to work

m.get_text_by_comment_id(source_id,comment_id)

5.adding pdf's marked text to db:
#function "extract_comments_for_pdf" must be actived with the relavant source_id before using this function, in order to work
#NOTICE - delete indicate if to delete the old lines in the DB for the given source id. default value=True

m.add_pdf_to_db(source_id,db_name,delete=True)