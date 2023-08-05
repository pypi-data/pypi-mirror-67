# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytse_client', 'pytse_client.data', 'pytse_client.examples']

package_data = \
{'': ['*']}

install_requires = \
['pandas', 'requests>=2.23.0,<3.0.0']

setup_kwargs = {
    'name': 'pytse-client',
    'version': '0.1.1',
    'description': 'tehran stock exchange(TSE) client in python',
    'long_description': '# pyTSEClient (python tse client)\n&rlm;\nبا استفاده از این پکیج میتونید به دیتای بازار بورس تهران در پایتون دسترسی داشته باشید.\n&rlm;\n\n&rlm;\nهدف حل مشکلات گرفتن اطلاعات بروز از سایت بازار بورس تهران هست.\n&rlm;\n\n## قابلیت ها\n * دریافت اطلاعات روز های معاملاتی هر سهم و قابلیت ذخیره سازی\n * قابلیت گرفتن اطلاعات یک سهام\n\n## نصب \n```bash\npip install pytse-client \n```\n\n## نحوه استفاده\n### دانلود سابقه سهم ها\nبا استفاده از این تابع میتوان سابقه سهام هارو دریافت کرد و هم اون رو ذخیره و هم توی کد استفاده کرد\n```python\nimport pytse_client as tse\ntickers = tse.download(symbols="all", write_to_csv=True)\ntickers["ولملت"] # history\n\n            date     open     high  ...     volume  count    close\n0     2009-02-18   1050.0   1050.0  ...  330851245    800   1050.0\n1     2009-02-21   1051.0   1076.0  ...  335334212   6457   1057.0\n2     2009-02-22   1065.0   1074.0  ...    8435464    603   1055.0\n3     2009-02-23   1066.0   1067.0  ...    8570222    937   1060.0\n4     2009-02-25   1061.0   1064.0  ...    7434309    616   1060.0\n...          ...      ...      ...  ...        ...    ...      ...\n2323  2020-04-14   9322.0   9551.0  ...  105551315  13536   9400.0\n2324  2020-04-15   9410.0   9815.0  ...  201457026  11322   9815.0\n2325  2020-04-18  10283.0  10283.0  ...  142377245   8929  10283.0\n2326  2020-04-19  10797.0  10797.0  ...  292985635  22208  10380.0\n2327  2020-04-20  10600.0  11268.0  ...  295590437  16313  11268.0\n```\nسابقه سهم توی فایلی با اسم سهم نوشته میشه `write_to_csv=True` همچنین با گذاشتن\n\nاست `Dataframe` سابقه سهم در قالب\n\n\nبرای دانلود سابقه یک یا چند سهم کافی هست اسم اون ها به تابع داده بشه:\n```python\nimport pytse_client as tse\ntse.download(symbols="وبملت", write_to_csv=True)\ntse.download(symbols=["وبملت", "ولملت"], write_to_csv=True)\n```\n\n### Ticker ماژول\n&rlm;\nاین ماژول به شما اجازه میده در پایتون به اطلاعات سهام دسترسی داشته باشید.\nبرای مثال:\n&rlm;\n```python\nimport pytse_client as tse\n\ntse.download(symbols="وبملت", write_to_csv=True)  # optional\nticker = tse.Ticker("وبملت")\n\n# سابقه\nticker.history\n\n# آدرس سهم\nticker.url\n\n# آیدی سهم در سایت\nticker.index\n\n```\nبرای استفاده لازم نیست حتما تابع دانلود صدا زده بشه.\nاگر این کد رو بدون دانلود کردن سهم  استفاده کنید خودش اطلاعات سهم رو از سایت میگیره،\nاما اگر قبل از اون از دانلود استفاده کرده باشید\nبه جای گرفتن از اینترنت اطلاعات رو از روی فایل میخونه که سریع تر هست\n\n##### نکته\n&rlm;\nطبق تجربه\u200c ای که داشتم چون گاهی اوقات سایت بورس مدت زیادی طول میکشه تا اطلاعات رو بفرسته یا بعضی مواقع نمیفرسته بهتر هست که اول تابع دانلود رو استفاده کنید برای سهم هایی که لازم هست و بعد با دیتای اون ها کار کنید.\n&rlm;\n#### &rlm; پکیج های مورد نیاز: &rlm; \n* [Pandas](https://github.com/pydata/pandas)\n* [Requests](http://docs.python-requests.org/en/master/)\n#### &rlm; الهام گرفته از: &rlm; \n* tehran_stocks: https://github.com/ghodsizadeh/tehran-stocks\n* yfinance: https://github.com/ranaroussi/yfinance',
    'author': 'glyphack',
    'author_email': 'sh.hooshyari@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
