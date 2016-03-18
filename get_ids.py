from marked_text_pdf import markedExtract

def get_ids():
    m=markedExtract()
    f = open('comment_ids.txt','rb')
    res=[]
    newline=""
    for line in f:
        for note in line:
            if note=="\t":
                res.append(int(newline))
                newline=""
                break
            else:
                newline = newline + note

    m.extract_comments_for_pdf(13876)
    for id in res:
        if m.get_text_by_comment_id(id) == "fail":
            print id
    f.close()

get_ids()