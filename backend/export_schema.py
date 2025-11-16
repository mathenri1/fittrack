import sqlite3
import os
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.resolve()        
DB = BASE_DIR / "instance" / "fittrack.sqlite3"           
OUT = BASE_DIR.parent / "docs" / "dados" / "schema.sql"   

if not DB.exists():
    raise FileNotFoundError(f"Banco não encontrado: {DB}")

OUT.parent.mkdir(parents=True, exist_ok=True)

con = sqlite3.connect(DB)
cur = con.cursor()
cur.execute("""
  SELECT sql
  FROM sqlite_master
  WHERE type IN ('table','index','trigger')
    AND name NOT LIKE 'sqlite_%'
  ORDER BY type, name;
""")
sqls = [row[0] for row in cur.fetchall() if row[0]]

OUT.write_text(";\n\n".join(sqls) + ";\n", encoding="utf-8")
print("Schema exportado para:", OUT)
