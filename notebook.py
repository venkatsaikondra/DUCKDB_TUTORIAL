# %%
import pandas as pd
import glob
import time
import duckdb

# %%
conn = duckdb.connect()


# %%
cur_time=time.time()
df=pd.concat([pd.read_csv(f) for f in glob.glob('dataset/*.csv')])
print(f"time:{(time.time()-cur_time)}")
print(df.head())
# %%
cur_time=time.time()
conn.execute(""" 
             SELECT *
             FROM "dataset/*.csv"
             LIMIT 10
""")
# %%
