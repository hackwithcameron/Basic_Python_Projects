import sqlite3


fileList = ('information.docx', 'Hello.txt', 'myImage.png',
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')


def find_txt(fileList):
    lst_1 = []
    for i in fileList:
        if i[-1:-4:-1] == "txt":
            lst_1.append(i)
    return lst_1


txt_lst = find_txt(fileList)


def database():
    conn = sqlite3.connect("doc.db")

    with conn:  # Create db if not already created
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_txt_doc( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            file_names TEXT)")
        conn.commit()
    conn.close()


def enter_data(txt_lst):  # Enter data into tables using a for loop
    conn = sqlite3.connect("doc.db")

    with conn:
        cur = conn.cursor()
        for i in range(len(txt_lst)):
            cur.execute("INSERT INTO tbl_txt_doc(file_names) VALUES (?)", (txt_lst[i],))
        conn.commit()
    conn.close()


def get_txt():
    conn = sqlite3.connect("doc.db")

    with conn:  # Getting values from db
        cur = conn.cursor()
        cur.execute("SELECT * FROM tbl_txt_doc")
        var = cur.fetchall()
        for i in (range(len(var))):
            msg = "Text file: {}".format(txt_lst[i])
            print(msg)
    conn.close()


if __name__ == "__main__":
    database()
    enter_data(txt_lst)
    get_txt()
