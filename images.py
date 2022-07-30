import pandas as pd
from urllib.parse import urlparse
import datetime as dt
from pathlib import Path

def get_file_name(url: str) -> str:
    try:
        path = urlparse(url).path
        return path.split("/")[-1]
    except Exception as e:
        print(e)
        return None

def get_file_date(filename: str, format: str="%Y-%m-%d"):
    P = Path(filename)
    filedate = P.stem.split("_")[0]
    try:
        return dt.datetime.strptime(filedate, format)
    except Exception as e:
        print(e)
        return None

images_src = [
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2015-05-15_1.JPG?sp=r&st=2022-07-30T10:21:18Z&se=2022-07-31T10:21:18Z&spr=https&sv=2021-06-08&sig=Dj7mfkkVw1S%2BeZ0a4RN6hNSEADtLcKERu0rdv0XMYNo%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2015-05-15_2.JPG?sp=r&st=2022-07-30T11:13:14Z&se=2022-07-31T11:13:14Z&spr=https&sv=2021-06-08&sig=QMDqlcpflztpiVAr21cP605kNPjW0zHDHjHJNsAbnek%3D&sr=f",
]
images_df = pd.DataFrame(images_src, columns=['url'])
images_df.loc[:, "filename"] = images_df.url.apply(get_file_name)
images_df.loc[:, "filedate"] = images_df.filename.apply(get_file_date)