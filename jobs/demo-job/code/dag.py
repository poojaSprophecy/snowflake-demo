import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from poojas_airflowdemo_snowflakedemo_demo_job.tasks import Email_1, Model_0, Python_1
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "poojas_airflowdemo_SnowflakeDemo_demo_job", 
    schedule_interval = "0 0/1 * * *", 
    default_args = {"owner" : "Prophecy", "ignore_first_depends_on_past" : True, "do_xcom_push" : True}, 
    start_date = pendulum.today('UTC'), 
    catchup = False, 
    tags = []
) as dag:
    Email_1_op = Email_1()
    Model_0_op = Model_0()
    Python_1_op = Python_1()
    Email_1_op >> Model_0_op
    Model_0_op >> Python_1_op
