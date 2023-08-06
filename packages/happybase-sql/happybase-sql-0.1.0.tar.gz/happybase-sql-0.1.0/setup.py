# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['happybase_sql']

package_data = \
{'': ['*']}

install_requires = \
['psycopg2>=2.8,<3.0', 'sqlalchemy>=1.3,<2.0']

setup_kwargs = {
    'name': 'happybase-sql',
    'version': '0.1.0',
    'description': 'A drop-in replacement for happybase that uses an SQL backend instead of HBase.',
    'long_description': '# happybase-sql #\n\nA (mostly) drop-in replacement for (happybase)[https://happybase.readthedocs.io/en/latest/] that uses an SQL backend instead of HBase.\n\n** Why would I want to use this? **\n\nThis project came about when I was working on a legacy project that used a HBase datastore. The HBase cluster became problematic, suffering from performance issues and was expensive to run. After wrestling with HBase for too long, I decided to migrate the data to SQL and wrote this replacement for the happybase library. It\'s mostly API compatible, so only needed a few minor changes to the code base to swap it in for happybase and thus avoid a lot of time-consuming refactoring. Depending how capital-B *Big Data* your requirements are, you might find (like I did) that the scale of HBase actually wasn\'t required, and an SQL DB was plenty big enough, much simpler to administer and a lot cheaper.\n\n## Getting started ##\n\nYou\'ll need to create a table in your SQL database for each of your HBase tables.\n\n*Note: currently only Postgres is supported*\n\nHere\'s an example table definition, just replace `my_table_name` with the name of your table. Note the two indices, one for key uniqueness (which is the equivalent of the HBase row key), and the `varchar_pattern_ops` index. This is required to allow efficient prefix queries, a feature of HBase key lookups and scans. The data is stored in a JSONB column, where the keys of that JSON data are the HBase column names (e.g. \'cf:col\').\n\n```sql\nCREATE TABLE public."my_table_name" (\n\t"key" varchar NOT NULL,\n\t"data" jsonb NOT NULL\n);\nCREATE UNIQUE INDEX my_table_name_key_idx ON public.my_table_name USING btree (key);\nCREATE INDEX my_table_name_key_ops_idx ON public.my_table_name USING btree (key varchar_pattern_ops);\n```\n\nInstall the happybase-sql package into your project:\n\n```bash\npip install happybase-sql\n```\n\nCreate a `Connection` or `ConnectionPool`. Note that the `host` argument is slightly different to `happybase`, it now refers to the *full* SQL database URL (including port). The port argument is ignored.\n\n```python\nfrom happybase_sql import ConnectionPool\n\n\nconnection_pool = ConnectionPool(size=3, host=\'postgresql://localhost:5432/hbase\')\n\nwith connection_pool.connection() as connection:\n    table = connection.table(\'my_table_name\')\n    table.put(\n        row=\'abcd\',\n        data={\n            \'cf:col1\': \'some data\',\n            \'cf:col2\': \'some more data\',\n        },\n    )\n    row = table.row(\'abcd\')\n    print(row)\n```\n',
    'author': 'Jonathon Waterhouse',
    'author_email': 'jonathon.waterhouse@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jwaterhouse/happybase-sql',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
}


setup(**setup_kwargs)
