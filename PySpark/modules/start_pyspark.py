import os

## notebook def
#%env PYTHONHASHSEED=1234
#%env JAVA_HOME=/usr/lib/jvm/java-17-openjdk-17.0.3.0.7-2.fc36.x86_64
#%env SPARK_HOME=/home/derpo/apps/spark/spark-3.3.0-bin-hadoop3

os.environ["PYTHONHASHSEED"] = "1234"
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-17-openjdk-17.0.5.0.8-3.fc36.x86_64"  ## folder and files local
os.environ["SPARK_HOME"] = "/home/derpo/apps/spark/spark-3.3.0-bin-hadoop3"

import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql import Window
from pyspark.sql.types import *
from pyspark.sql.functions import *

appName = 'Leitura de dados estruturados'
master = 'local'

spark = SparkSession.builder     \
    .master(master) \
    .appName(appName) \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")