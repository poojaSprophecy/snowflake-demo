import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.decorators import task
from airflow.models.param import Param
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from aawqaml_fdxtafbo3lux7a_.tasks import DBT_0
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "AAwQAml_fDxTAFBO3lux7A_", 
    schedule_interval = "0/10 * * * *", 
    default_args = {"owner" : "Prophecy", "ignore_first_depends_on_past" : True, "do_xcom_push" : True, "pool" : "hvPurrET"}, 
    start_date = pendulum.today('UTC'), 
    end_date = pendulum.datetime(2024, 3, 20, tz = "UTC"), 
    catchup = True, 
    tags = []
) as dag:
    DBT_0_op = DBT_0()
