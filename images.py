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
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2015-04-02_1.jpg?sp=r&st=2022-07-29T14:33:00Z&se=2022-08-03T14:33:00Z&spr=https&sv=2021-06-08&sig=IaedEDCNF0Try4VMoDfaVzNShb3l%2Bu16w0imoByCXiA%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2015-06-13_1.jpg?sp=r&st=2022-07-30T14:34:52Z&se=2022-08-03T14:34:00Z&spr=https&sv=2021-06-08&sig=B7mrXrFnKlrEtHRxjnejYZ9Wkjn%2F9xVirQP4uzMenks%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2015-06-13_2.jpg?sp=r&st=2022-07-30T14:35:23Z&se=2022-07-31T14:35:23Z&spr=https&sv=2021-06-08&sig=g9nuu1Uo7bB88FO1i0N789CdOtxrVk4EYdM%2BEBQ0ug4%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2015-06-16_1.jpg?sp=r&st=2022-07-30T14:36:05Z&se=2022-08-03T14:36:00Z&spr=https&sv=2021-06-08&sig=QeXAHaQ%2Bin7ZhDpArYW%2B7KfdIvwyiOwZgbzQumpi7aw%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/I2019-10-06_1.jpg?sp=r&st=2022-07-30T15:34:03Z&se=2022-08-03T15:34:00Z&spr=https&sv=2021-06-08&sig=0x5MBGO%2B43GN4HpldoLCkHVwn6RHK23VfR7lgkaytqo%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2022-03-25_1.jpg?sp=r&st=2022-07-30T15:34:46Z&se=2022-08-03T15:34:00Z&spr=https&sv=2021-06-08&sig=SIIHOERGNEJMGzj4O4YLIQZlv5cTwaXh4Azh1c%2Bw5EU%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2021-11-07_1.jpg?sp=r&st=2022-07-30T15:35:21Z&se=2022-08-03T15:35:00Z&spr=https&sv=2021-06-08&sig=g56lqzk3E6P3kaevte5WTFMo9LaP9IGBzKJ%2F8VP2MBs%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2021-09-11_1.jpg?sp=r&st=2022-07-30T15:35:45Z&se=2022-07-31T15:35:45Z&spr=https&sv=2021-06-08&sig=UhBi%2BqPU8UXgjYOrzNQfomSLBqTrgjJwlM8LBjxdpqY%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2021-08-15_1.jpg?sp=r&st=2022-07-30T15:36:04Z&se=2022-08-03T15:36:00Z&spr=https&sv=2021-06-08&sig=u3HqiM9DzfjppT%2FsXhhHrXwDZBGY2HdYUlOBOUmWRpU%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2021-08-01_2.jpg?sp=r&st=2022-07-30T15:36:21Z&se=2022-08-03T15:36:00Z&spr=https&sv=2021-06-08&sig=guhanL2NpbtqL4qovj0BA%2FxTUOKuwDZc5NDLw63Jhx4%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2021-08-01_1.jpg?sp=r&st=2022-07-30T15:36:39Z&se=2022-07-31T15:36:39Z&spr=https&sv=2021-06-08&sig=4GGWv9AwfRW3EupWgiCDMusMZVHk%2BG5fTzWu7Od1LX4%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2020-12-27_1.jpg?sp=r&st=2022-07-30T15:36:52Z&se=2022-08-03T15:36:00Z&spr=https&sv=2021-06-08&sig=t7GSOJbVsUmvDvMWW6Akemi8%2FcUz%2Fc2rSHkDQoniX2g%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2020-11-30_2.jpg?sp=r&st=2022-07-30T15:38:31Z&se=2022-08-03T15:38:00Z&spr=https&sv=2021-06-08&sig=4J3L%2BZGz1lQfOZdvJDPfFjyq6j5qPE0zWMi7lEWwHEc%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2020-11-30_1.jpg?sp=r&st=2022-07-30T15:38:54Z&se=2022-08-03T15:38:00Z&spr=https&sv=2021-06-08&sig=Lkj0K5HgMyHBiSrdF9NU100M%2Fkt4TOUbhKxQcOTl8gs%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2020-08-30_1.jpg?sp=r&st=2022-07-30T15:39:17Z&se=2022-07-31T15:39:17Z&spr=https&sv=2021-06-08&sig=KsZUca2OkqPuD5wwkFPSlYQAtAIhw3Vp2tXS9Rt07vI%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2020-08-01_1.jpg?sp=r&st=2022-07-30T15:39:38Z&se=2022-07-31T15:39:38Z&spr=https&sv=2021-06-08&sig=w9RbsEE464oM%2B6J78F%2FEYqi3TbmaQ81sjXBDUH2vyhA%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2020-07-05_1.jpg?sp=r&st=2022-07-30T15:39:58Z&se=2022-07-31T15:39:58Z&spr=https&sv=2021-06-08&sig=D5SpGcBnyKPOYBIm%2FBcCopPjlJb%2B38ycABHIQj0POS0%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2020-05-16_1.jpg?sp=r&st=2022-07-30T15:40:13Z&se=2022-07-31T15:40:13Z&spr=https&sv=2021-06-08&sig=WUSjNx4wI14f4zdg1No8gTt3CXGMBum87PmEtUZMQuc%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2020-05-01_2.jpg?sp=r&st=2022-07-30T15:40:34Z&se=2022-08-03T15:40:00Z&spr=https&sv=2021-06-08&sig=mx1O%2BOA7DXnZD%2BQTWkSQeNZO%2FNh0vfEhWSreT52sI5M%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2020-05-01_1.jpg?sp=r&st=2022-07-30T15:40:55Z&se=2022-08-03T15:40:00Z&spr=https&sv=2021-06-08&sig=yEs8htwvf5VWowODKXRMwKzNZllqjPRmXR6c%2FBtcmgY%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2020-04-15_1.JPG?sp=r&st=2022-07-30T15:41:13Z&se=2022-07-31T15:41:13Z&spr=https&sv=2021-06-08&sig=zzDqpE2uoTK32%2Fk7cmU%2F%2BGoZSIphST%2FBEPRwg3C7Dj0%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2020-03-11_2.jpg?sp=r&st=2022-07-30T15:41:34Z&se=2022-08-03T15:41:00Z&spr=https&sv=2021-06-08&sig=Y5ibD7M4omuqj8GUseNbTgpCs8wyMnfWWSf1YZABQuo%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2019-11-30_2.jpg?sp=r&st=2022-07-30T15:45:04Z&se=2022-08-03T15:45:00Z&spr=https&sv=2021-06-08&sig=TG0VdX2FF4bSnWi6PZIHTyVuVJ%2BJi%2BdT9TVuaBmGdTc%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2019-11-30_1.jpg?sp=r&st=2022-07-30T15:45:23Z&se=2022-07-31T15:45:23Z&spr=https&sv=2021-06-08&sig=D%2FsZsTbD80ibvY822gMlL9yHnoP6uNpgPozb95IoWGs%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2019-11-29_1.jpg?sp=r&st=2022-07-30T15:45:43Z&se=2022-08-03T15:45:00Z&spr=https&sv=2021-06-08&sig=0Tbv7Cd5nSIWnydH1JWiJ9mSIOFEZkGj6HCq%2BcLgSw8%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2019-11-27_1.jpg?sp=r&st=2022-07-30T15:46:00Z&se=2022-07-31T15:46:00Z&spr=https&sv=2021-06-08&sig=ozBRfmmZm9xF4OyTN5bXhxqI2i9MrR8Yqe68O100JNs%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2019-10-20_1.jpg?sp=r&st=2022-07-30T15:46:12Z&se=2022-08-03T15:46:00Z&spr=https&sv=2021-06-08&sig=EJ5%2BSSEB9%2BVk%2FY70uNgm9N46MKk6ggLdkWJNVgEdQPM%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2019-08-03_2.jpg?sp=r&st=2022-07-30T15:46:29Z&se=2022-08-03T15:46:00Z&spr=https&sv=2021-06-08&sig=bxj1cpGrBk4Ei2xlazPdpLADZlk9cuxQy1d5OxD61fo%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2019-06-23_1.jpg?sp=r&st=2022-07-30T15:46:45Z&se=2022-08-03T15:46:00Z&spr=https&sv=2021-06-08&sig=XYty25j1jcgvbvk9jbuTaRly3A7z8XmXbHu62wAGm%2FY%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2019-02-08_2.jpg?sp=r&st=2022-07-30T15:47:06Z&se=2022-07-31T15:47:06Z&spr=https&sv=2021-06-08&sig=IlFZXigjFnArUE2M4r1eBCQnesILMYiCbq%2Ff2jH7Vk0%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2018-09-08_1.jpg?sp=r&st=2022-07-30T15:47:22Z&se=2022-07-31T15:47:22Z&spr=https&sv=2021-06-08&sig=nGIFtpsCl3jMPrsoqe3rWnSYqObnnp8h3XZhl%2FzpAd0%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2018-03-11_1.jpg?sp=r&st=2022-07-30T15:47:37Z&se=2022-08-03T15:47:00Z&spr=https&sv=2021-06-08&sig=9dJmApq86Syxj84qbaYoKx%2FoqdoNJkz9Q2K5ygxkJpo%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2018-01-03_1.jpg?sp=r&st=2022-07-30T15:47:54Z&se=2022-08-03T15:47:00Z&spr=https&sv=2021-06-08&sig=Xx9Ne%2B2C1SDihiojQOaqkF4jy0XLtoGCv2gvW9bskFY%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2017-12-31_1.jpg?sp=r&st=2022-07-30T15:48:09Z&se=2022-07-31T15:48:09Z&spr=https&sv=2021-06-08&sig=VBDKy%2FjCiry1ywJNO3YF773b9zVMuAZH5FSoNIzPOeU%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2017-12-09_1.jpg?sp=r&st=2022-07-30T15:48:25Z&se=2022-08-03T15:48:00Z&spr=https&sv=2021-06-08&sig=M7bbAcJGMtovdg6rvM5Ckwapob54MXaXXCcZuTRtuc0%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2017-09-28_1.JPG?sp=r&st=2022-07-30T15:48:45Z&se=2022-08-03T15:48:00Z&spr=https&sv=2021-06-08&sig=1IEOZP2vU2MMSq8frFpNuLy4K6RLWfUpiCcqNAtRl4M%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2017-03-04_1.JPG?sp=r&st=2022-07-30T15:49:01Z&se=2022-08-03T15:49:00Z&spr=https&sv=2021-06-08&sig=hN%2BI4agbfBZFCkJ27ks0jzWu8%2FSZ4isS19NunVZfLEA%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2016-05-25_01.jpg?sp=r&st=2022-07-30T15:49:18Z&se=2022-08-03T15:49:00Z&spr=https&sv=2021-06-08&sig=%2BabBN3eRVR0vyV79Rl%2F5nkb724Zu3SgJ5XE1rGC4otE%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2016-04-09_1.JPG?sp=r&st=2022-07-30T15:49:34Z&se=2022-08-03T15:49:00Z&spr=https&sv=2021-06-08&sig=UlniHRn7Hio2isMoZcH3bCn2tD4JW9sEaXBG7lDkBbI%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2015-10-21_1.jpg?sp=r&st=2022-07-30T15:49:54Z&se=2022-08-03T15:49:00Z&spr=https&sv=2021-06-08&sig=V6JVpPf7LMzYCxXYF5PxLTKnsphSSoNgodtjsDfXh%2Bs%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2015-09-26_1.JPG?sp=r&st=2022-07-30T15:50:08Z&se=2022-08-03T15:50:00Z&spr=https&sv=2021-06-08&sig=%2FOwYkpuevtFCnnkolczmRnBA0kanVm0GSLnrp0NHBoA%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2015-09-05_1.JPG?sp=r&st=2022-07-30T15:50:23Z&se=2022-08-03T15:50:00Z&spr=https&sv=2021-06-08&sig=fkFUdrCiejI7fw9FnrFIIPwgLlcLjQtax8OvW13%2FB%2Fg%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2015-07-09_1.JPG?sp=r&st=2022-07-30T15:50:36Z&se=2022-08-03T15:50:00Z&spr=https&sv=2021-06-08&sig=2LLns7jtK%2BaPXAMyvTGMWEAk%2FeXjV5f8Njm0bd%2BsMOw%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2015-06-16_1.jpg?sp=r&st=2022-07-30T15:50:51Z&se=2022-08-03T15:50:00Z&spr=https&sv=2021-06-08&sig=i2Q6EiSS5u5Ugw6eVIRoAM274BsynB7%2BJpaXUy3Ag1A%3D&sr=f",
    "https://dltest6304079929.file.core.windows.net/azureml-filestore-4d8a3602-bbfa-4b3d-892f-2da596c8daa7/2015-06-13_2.jpg?sp=r&st=2022-07-30T15:51:08Z&se=2022-08-03T15:51:00Z&spr=https&sv=2021-06-08&sig=ERQVTH1TW79n%2BwGzCMBIZij9elx6K%2FbACCCfszoDudY%3D&sr=f",
]
images_df = pd.DataFrame(images_src, columns=['url'])
images_df.loc[:, "filename"] = images_df.url.apply(get_file_name)
images_df.loc[:, "filedate"] = images_df.filename.apply(get_file_date)
images_df = images_df.sort_values(by="filedate", ascending=True)