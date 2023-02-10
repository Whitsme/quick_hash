import sqlite3

conn = sqlite3.connect('scan_results.db')
c = conn.cursor()
"""connects to database and creates cursor"""

def builder() -> bool:
    try:
        c.execute("CREATE TABLE IF NOT EXISTS sandbox(resource text, sha256 text, category text, sandbox_used text, classification text)")
        c.execute("CREATE TABLE IF NOT EXISTS analysis(resource text, sha256 text, scan text, category text, engine_name text, engine_version text, result text, method text, engine_update text)")
        conn.commit()
        """creates tables if they do not exist"""
        return True
    except:
        return False

def writer(write_this, to_this):
    try:
        if len(write_this) > 5: 
            c.execute("INSERT INTO {} VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)".format(to_this), (write_this[0], write_this[1], write_this[2], write_this[3], write_this[4], write_this[5], write_this[6], write_this[7], write_this[8]))
            """writes analysis results to database"""
        elif len(write_this) == 5:
            c.execute("INSERT INTO {} VALUES(?, ?, ?, ?, ?)".format(to_this), (write_this[0], write_this[1], write_this[2], write_this[3], write_this[4][0]))
            """writes sandbox results to database"""        
        elif len(write_this) < 4:
            """this is for another result not yet implemented"""
            pass
        conn.commit()
        """commits changes to database"""
        return True
    except:
        return False
