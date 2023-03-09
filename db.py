import sqlite3


conn = sqlite3.connect('scan_results.db')

c = conn.cursor()

"""connects to database and creates cursor"""


def builder() -> bool:

    try:

        c.execute("CREATE TABLE IF NOT EXISTS file_sandbox(resource text, sha256 text, category text, sandbox_used text, classification text)")

        c.execute("CREATE TABLE IF NOT EXISTS file_analysis(resource text, sha256 text, scan text, category text, engine_name text, engine_version text, result text, method text, engine_update text)")

        c.execute("CREATE TABLE IF NOT EXISTS url_analysis(resource text, id text, category text, result text, method text, engine_name text)")

        c.execute("CREATE TABLE IF NOT EXISTS crx_report(resource text, csp text, permissions text, total text, last_update text, name text, permission_warnings text, size text, users text, version text)")

        conn.commit()

        """creates tables if they do not exist"""

        return True

    except:

        return False

def existing(ui_type, db_table, ui) -> bool:

    in_db = c.execute("SELECT {} FROM {}".format(ui_type, db_table))

    table_check = in_db.fetchall()

    ui = ('{}'.format(ui),)

    if ui in table_check:

        return True

    else:

        return False


def writer(write_this, to_this):

    # try:

        if len(write_this) > 8 and to_this == 'file_analysis': 
            #if existing("sha256", "file_analysis", write_this[1]) != True:

                c.execute("INSERT INTO {} VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)".format(to_this), (write_this[0], write_this[1], write_this[2], write_this[3], write_this[4], write_this[5], write_this[6], write_this[7], write_this[8]))

                """writes file analysis results to database"""

        elif len(write_this) == 8 and to_this == 'file_analysis':
            #if existing("sha256", "file_analysis", write_this[1]) != True:

                c.execute("INSERT INTO {} VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)".format(to_this), (write_this[0], write_this[1], write_this[2], "none", write_this[3], write_this[4], write_this[5], write_this[6], write_this[7]))

                """writes file analysis results to database"""

        elif to_this == 'url_analysis':
            #if existing("id", "url_analysis", write_this[1]) != True:

                c.execute("INSERT INTO {} VALUES(?, ?, ?, ?, ?, ?)".format(to_this), (write_this[0], write_this[1], write_this[2], write_this[3], write_this[4], write_this[5]))

                """writes url analysis results to database"""

        elif to_this == 'file_sandbox':
            #if existing("sha256", "file_sandbox", write_this[1]) != True:

                c.execute("INSERT INTO {} VALUES(?, ?, ?, ?, ?)".format(to_this), (write_this[0], write_this[1], write_this[2], write_this[3], write_this[4][0]))

                """writes file sandbox results to database"""        

        elif to_this == 'crx_report':
            c.execute("INSERT INTO {} VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)".format(to_this), (write_this[0], write_this[1], write_this[2], write_this[3], write_this[4], write_this[5], write_this[6], write_this[7], write_this[8], write_this[9]))


        conn.commit()

        """commits changes to database"""

        return True

    # except:

    #     return False


def reader(db_table):

    try:

        in_db = c.execute("SELECT * FROM {}".format(db_table))

        return True

    except:

        return False
        